%def_disable qt4
%define oname eigen
Name: %{oname}3
Version: 3.3.8
Release: alt3

Summary: C++ template library for linear algebra
License: LGPLv3+ or GPLv2+
Group: Development/C++

Url: http://eigen.tuxfamily.org/
Source: %name-%version.tar
Packager: Andrey Cherepanov <cas@altlinux.org>

# Install FindEigen3.cmake
# Fix pkg-config file
Patch1:         eigen_pkgconfig.patch
# Fix the include paths in the new Eigen3Config.cmake file
Patch2:         eigen3-3.3.1-fixcmake.patch
# Avoid SSE4.2/AVX on e2k
Patch3:		eigen3-3.3.7-alt-e2k.patch
# https://gitlab.com/libeigen/eigen/-/issues/2011
Patch4: eigen3-3.3.8-upstream-build.patch

BuildRequires(pre): cmake
BuildRequires(pre): rpm-build-ninja
%ifnarch %e2k
BuildRequires: libsuitesparse-devel libscotch-devel libgoogle-sparsehash
%endif
BuildRequires: gcc-c++ doxygen
%if_enabled qt4
BuildRequires: libqt4-devel
%endif
BuildRequires: libsuperlu-devel libmpfr-devel libgmp-devel
BuildRequires: libfftw3-devel libGLU-devel libgsl-devel gcc-fortran
BuildRequires: liblapack-devel libglew-devel libGLUT-devel libXi-devel
BuildRequires: libXmu-devel libmetis-devel phonon-devel libXres-devel
BuildRequires: libXcomposite-devel libXdamage-devel libXdmcp-devel
BuildRequires: libXft-devel libxkbfile-devel libXpm-devel
BuildRequires: libXScrnSaver-devel libXxf86misc-devel libXxf86vm-devel
BuildRequires: boost-devel

# TODO: add devel subpackage and move stuff
Provides: %{name}-devel = %EVR
Provides: %{oname}-devel = %EVR

%description
Eigen is a C++ template library for linear algebra: matrices, vectors,
numerical solvers, and related algorithms.

%package docs
Summary: Documentation for Eigen3
Group: Development/Documentation
BuildArch: noarch
#BuildArch: noarch

%description docs
Eigen is a C++ template library for linear algebra: matrices, vectors,
numerical solvers, and related algorithms.

This package contains development documentation for Eigen.

%package examples
Summary: Examples for Eigen3
Group: Development/Documentation

%description examples
Eigen is a C++ template library for linear algebra: matrices, vectors,
numerical solvers, and related algorithms.

This package contains examples for Eigen.

%prep
%setup
%patch1 -p1
%patch2 -p0 -b .fixcmake
%ifarch %e2k
%patch3 -p2 -b .e2k
%endif
%patch4 -p1

%build
export PATH=$PATH:%_libdir/pastix/bin

%cmake -GNinja \
	-Wno-dev \
	-DINCLUDE_INSTALL_DIR=include/%name \
	-DPKGCONFIG_INSTALL_DIR=%_lib/pkgconfig \
	-DCMAKEPACKAGE_INSTALL_DIR=%_lib/cmake/%name \
	-DOpenGL_GL_PREFERENCE=GLVND \
%ifarch %e2k
	-DEIGEN_TEST_AVX512=OFF \
	-DEIGEN_TEST_AVX=OFF \
	-DEIGEN_TEST_SSE4_2=OFF \
%else
	-DCHOLMOD_INCLUDES=%_includedir/suitesparse \
	-DUMFPACK_INCLUDES=%_includedir/suitesparse \
%endif
%if_disabled qt4
	-DEIGEN_TEST_NOQT=ON \
%endif
	-DSUPERLU_LIBRARIES=-lsuperlu_4.0 \
	-DCMAKE_STRIP="/bin/echo" \
	-DGOOGLEHASH_INCLUDES="%_includedir/google" \
	-DGOOGLEHASH_COMPILE="g++ %optflags" \
	-DMETIS_INCLUDE_DIRS=%_includedir/metis

%ninja_build -C BUILD
%ifnarch %e2k
%ninja_build -C BUILD doc
%endif

%install
%ninja_install -C BUILD

install -d %buildroot%_bindir
%ifnarch %e2k
rm -fR BUILD/doc/examples/CMakeFiles BUILD/doc/examples/*.out \
	BUILD/doc/examples/*.cmake
install -m755 BUILD/doc/examples/* %buildroot%_bindir
%endif

%files
%_includedir/*
%_pkgconfigdir/*
%_libdir/cmake/%name

%ifnarch %e2k
%files examples
%_bindir/*
%doc doc/examples/*

%files docs
%doc BUILD/doc/html/*
%endif

%changelog
* Thu Oct 22 2020 Andrey Cherepanov <cas@altlinux.org> 3.3.8-alt3
- Move cmake files to %_libdir/cmake/eigen3 (ALT #39109).
- Spec cleanup.

* Fri Oct 16 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 3.3.8-alt2
- Applied upstream fix for eigen.

* Sun Oct 11 2020 Andrey Cherepanov <cas@altlinux.org> 3.3.8-alt1
- New version.
- Use ninja for build.

* Fri Jun 26 2020 Michael Shigorin <mike@altlinux.org> 3.3.7-alt5
- E2K: lcc 1.24 workaround

* Thu Aug 29 2019 Sergey V Turchin <zerg@altlinux.org> 3.3.7-alt4
- build without Qt4

* Sat Feb 02 2019 Michael Shigorin <mike@altlinux.org> 3.3.7-alt3
- E2K: avoid SSE4.2/AVX in installed headers too.

* Fri Feb 01 2019 Michael Shigorin <mike@altlinux.org> 3.3.7-alt2
- E2K: avoid building too much for now.

* Fri Dec 14 2018 Andrey Cherepanov <cas@altlinux.org> 3.3.7-alt1
- New version.

* Mon Oct 22 2018 Andrey Cherepanov <cas@altlinux.org> 3.3.5-alt2
- Fix prototype (see https://bugs.debian.org/cgi-bin/bugreport.cgi?bug=908336) (ALT #35537).

* Sun Oct 14 2018 Igor Vlasenko <viy@altlinux.ru> 3.3.5-alt1.qa1
- NMU: applied repocop patch

* Thu Aug 23 2018 Andrey Cherepanov <cas@altlinux.org> 3.3.5-alt1
- New version.

* Wed Jan 31 2018 Igor Vlasenko <viy@altlinux.ru> 3.3.4-alt4
- NMU: fixed FindEigen3.cmake (added fedora patches)
- added -devel provides (TODO: eigen3 should be renamed to eigen3-devel)

* Fri Nov 17 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 3.3.4-alt3
- Updated build dependencies.

* Tue Oct 03 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 3.3.4-alt2
- Rebuilt without libadolc.

* Mon Jun 26 2017 Andrey Cherepanov <cas@altlinux.org> 3.3.4-alt1
- Version 3.3.4

* Mon Mar 20 2017 Andrey Cherepanov <cas@altlinux.org> 3.3.3-alt1
- Version 3.3.3

* Fri Mar 18 2016 Sergey V Turchin <zerg@altlinux.org> 3.2.8-alt1
- new version

* Wed May 28 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.2.1-alt1
- Version 3.2.1

* Tue Nov 12 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.2.0-alt1
- Version 3.2.0

* Wed Jun 19 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.1.3-alt1
- Version 3.1.3

* Mon Feb 04 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.1.2-alt1
- Version 3.1.2

* Wed Sep 12 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.1.1-alt1
- Version 3.1.1

* Tue Mar 06 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.0.5-alt1
- Initial build for Sisyphus

