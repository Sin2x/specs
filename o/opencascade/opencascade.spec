Name: opencascade
Version: 7.5.0
Release: alt2
Summary: SDK intended for development of applications dealing with 3D CAD data
License: LGPL-2.1-only-with-OCCT-exception-1.0
Group: Development/Tools
Url: http://www.opencascade.org

# Upstream requires a login to download sources. 
# https://www.opencascade.com/content/latest-release
# The following URL (after expansion) will work using links from the command line.
# https://www.opencascade.com/sites/default/files/private/occt/OCC_%%{version}_release/%%{name}-%%{version}.tgz
Source: %name-%version.tar
Patch1: opencascade-cmake.patch
Patch2: opencascade-alt-arm-build.patch

Requires: lib%name = %version-%release
Requires: %name-data = %version-%release

BuildRequires(pre): cmake
BuildRequires(pre): rpm-build-ninja
BuildRequires: gcc-c++ libX11-devel libGL-devel libGLU-devel
BuildRequires: tcl-devel tcl-tix libfltk-devel tk-devel libXmu-devel
BuildRequires: java-devel-default libcoin3d-devel libfreetype-devel
BuildRequires: libftgl-devel fontconfig-devel libXi-devel
BuildRequires: libgl2ps-devel zlib-devel libfreeimage-devel
BuildRequires: libXext-devel libvtk-devel doxygen graphviz

%description
Open CASCADE Technology (OCCT) is a suite for 3D surface and solid
modeling, visualization, data exchange and rapid application development. It
is an excellent platform for development of numerical simulation software
including CAD/CAM/CAE, AEC and GIS, as well as PDM applications.

%package -n lib%name
Summary: Shared libraries of Open CASCADE
Group: System/Libraries

%description -n lib%name
Shared libraries of Open CASCADE, development platform for 3D modeling and
numerical simulation applications.

%package devel
Summary: Development files for Open CASCADE Technology
Group: Development/C++
Requires: lib%name = %version-%release
Provides: OCE-devel = %EVR
Obsoletes: OCE-devel < %EVR

%description devel
Development files for Open CASCADE Technology, development platform for 3D
modeling and numerical simulation applications.

%package data
Summary: Data for Open CASCADE
Group: Development/Tools
BuildArch: noarch

%description data
This package contains data and resources for Open CASCADE.

%package samples
Summary: Samples for Open CASCADE
Group: Development/Documentation
BuildArch: noarch

%description samples
This package contains samples for Open CASCADE.

%package doc
Summary: Documentation for Open CASCADE
Group: Development/Documentation
BuildArch: noarch

%description doc
This package contains documentation for Open CASCADE.

%prep
%setup
%patch1 -p1
%ifarch %arm
%patch2 -p2
%endif

# Remove executable bit from sources and documentation files
find src doc -type f -exec chmod -x {} \;
chmod 0644 *.txt

%build
# opencascade does some manual install trickery that does not respect DESTDIR.
# Make DESTDIR and environment variable that can be passed into the CMake config.
export DESTDIR="%buildroot"
%cmake_insource -GNinja \
       -DCMAKE_BUILD_TYPE=RelWithDebInfo \
       -DUSE_TBB=False \
       -DUSE_VTK=True \
       -D3RDPARTY_VTK_INCLUDE_DIR=%_includedir/vtk-9.0 \
       -DINSTALL_DIR_LIB=%_lib \
       -DINSTALL_DIR_CMAKE=%_lib/cmake/%name
%ninja_build

%install
%ninja_install
mv %buildroot%_bindir/DRAWEXE-%version %buildroot%_bindir/DRAWEXE

# Install precompiled documentation
cp -a doc/* %buildroot%_datadir/doc/%name/

%files
%doc LICENSE_LGPL_21.txt OCCT_LGPL_EXCEPTION.txt README.txt
%_bindir/DRAWEXE

%files -n lib%name
%_libdir/*.so.*

%files devel
%_bindir/*.sh
%_libdir/*.so
%_includedir/*
%_libdir/cmake/%name

%files data
%_datadir/%name
%exclude %_datadir/%name/samples

%files samples
%_datadir/%name/samples

%files doc
%_datadir/doc/%name

%changelog
* Wed May 12 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 7.5.0-alt2
- Rebuilt with VTK-9.0.1.

* Mon Nov 30 2020 Andrey Cherepanov <cas@altlinux.org> 7.5.0-alt1
- New version.

* Mon Jun 01 2020 Andrey Cherepanov <cas@altlinux.org> 7.4.0-alt1
- New version.
- Build all data and documentation packages from one source package.
- Obsoletes OCE package.

* Thu Jan 25 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 6.8.0-alt2
- Fixed build with new glibc.

* Fri Mar 24 2017 Vladimir D. Seleznev <vseleznv@altlinux.org> 6.8.0-alt1.qa1
- Rebuilt against Tcl/Tk 8.6

* Fri Mar 27 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 6.8.0-alt1
- Version 6.8.0

* Wed May 21 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 6.7.1-alt1
- Version 6.7.1

* Fri Sep 13 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 6.6.0-alt1
- Version 6.6.0

* Thu Feb 07 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 6.5.4-alt1
- Version 6.5.4

* Tue Oct 02 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 6.5.3-alt2
- Fixed build with gcc 4.7

* Tue Aug 21 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 6.5.3-alt1
- Version 6.5.3

* Wed Jun 06 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 6.5.2-alt3
- Fixed build

* Sun Mar 11 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 6.5.2-alt2
- Fixed build with TBB 40_297

* Wed Feb 29 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 6.5.2-alt1
- Version 6.5.2

* Thu Sep 15 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 6.5.1-alt1
- Version 6.5.1

* Thu Apr 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 6.5.0-alt1
- Version 6.5.0

* Tue Mar 01 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 6.3.0-alt10
- Rebuilt for debuginfo

* Tue Nov 02 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 6.3.0-alt9
- Rebuilt for soname set-versions

* Sat Oct 16 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 6.3.0-alt8
- Fixed underlinking of libraries

* Tue Aug 31 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 6.3.0-alt7
- Fixed for checkbashisms

* Mon Mar 08 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 6.3.0-alt6
- Reduced optimization level: -O2 -> -O1
- Rebuilt with java

* Tue Dec 22 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 6.3.0-alt5
- Set opencascade-commom as noarch

* Tue Dec 22 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 6.3.0-alt4
- Rebuilt without java

* Tue Sep 08 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 6.3.0-alt3
- Changed owner of %_datadir/%name: %name -> %name-common
- Rebuild with gcc4.4

* Wed May 06 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 6.3.0-alt2
- Removed %name directory from /usr/lib
- Fixed channel permission

* Sat May 02 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 6.3.0-alt1
- Initial build for Sisyphus

