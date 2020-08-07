%define _unpackaged_files_terminate_build 1

Name: tbb
Version: 2020.3
Release: alt1
Summary: Threading Building Blocks
License: Apache-2.0
Group: Development/Tools
Url: https://www.threadingbuildingblocks.org/

# https://github.com/intel/tbb.git
Source: %name-%version.tar

# These are downstream sources. (from mageia spec file)
Source6: tbb.pc
Source7: tbbmalloc.pc
Source8: tbbmalloc_proxy.pc

# Fedora patches

# Don't snip -Wall from C++ flags.  Add -fno-strict-aliasing, as that
# uncovers some static-aliasing warnings.
# Related: https://bugzilla.redhat.com/show_bug.cgi?id=1037347
Patch1: tbb-2019-dont-snip-Wall.patch

# Fix test-thread-monitor, which had multiple bugs that could (and did, on
# ppc64le) result in a hang.
Patch2: tbb-2019-test-thread-monitor.patch

# Fix a test that builds a 4-thread barrier, but cannot guarantee that more
# than 2 threads will be available to use it.
Patch3: tbb-2019-test-task-scheduler-init.patch

# Fix compilation on aarch64 and s390x.  See
# https://github.com/intel/tbb/issues/186
Patch4: tbb-2019-fetchadd4.patch

Requires: lib%name = %EVR

BuildRequires(pre): rpm-build-python3
BuildRequires: gcc-c++
BuildRequires: python3-devel
BuildRequires: swig

%description
Threading Building Blocks offers a rich and complete approach to
expressing parallelism in a C++ program. It is a library that helps you
leverage multi-core processors for performance and scalability without
having to be a threading expert.

%package -n lib%name
Summary: Shared libraries of Threading Building Blocks
Group: Development/C++

%description -n lib%name
Threading Building Blocks offers a rich and complete approach to
expressing parallelism in a C++ program. It is a library that helps you
leverage multi-core processors for performance and scalability without
having to be a threading expert.

This package contains shared libraries of Threading Building Blocks.

%package devel
Summary: Development libraries and headers of Threading Building Blocks
Group: Development/C++
Requires: lib%name = %version-%release
Requires: %name-headers = %version-%release
Provides: lib%name-devel = %EVR
Conflicts: lib%name-devel < %EVR
Obsoletes: lib%name-devel
Provides: %name-headers = %EVR
Conflicts: %name-headers < %EVR
Obsoletes: %name-headers

%description devel
Threading Building Blocks offers a rich and complete approach to
expressing parallelism in a C++ program. It is a library that helps you
leverage multi-core processors for performance and scalability without
having to be a threading expert.

This package contains development libraries for Threading Building
Blocks.

%package docs
Summary: Documentation for Threading Building Blocks
Group: Development/Documentation
BuildArch: noarch

%description docs
Threading Building Blocks offers a rich and complete approach to
expressing parallelism in a C++ program. It is a library that helps you
leverage multi-core processors for performance and scalability without
having to be a threading expert.

This package contains development documentation for Threading Building
Blocks.

%package examples
Summary: Examples for Threading Building Blocks
Group: Development/Documentation
Requires: lib%name = %EVR
BuildArch: noarch

%description examples
Threading Building Blocks offers a rich and complete approach to
expressing parallelism in a C++ program. It is a library that helps you
leverage multi-core processors for performance and scalability without
having to be a threading expert.

This package contains examples for Threading Building Blocks.

%package -n python3-module-%name
Summary: Python 3 Threading Building Blocks module
Group: Development/Python3

%description -n python3-module-%name
Threading Building Blocks offers a rich and complete approach to
expressing parallelism in a C++ program. It is a library that helps you
leverage multi-core processors for performance and scalability without
having to be a threading expert.

This package contains python3 module for Threading Building Blocks.

%prep
%setup
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1

%build
export CFLAGS="${CFLAGS:-%optflags} -DDO_ITT_NOTIFY -DUSE_PTHREAD"
export CXXFLAGS="${CXXFLAGS:-%optflags} -DDO_ITT_NOTIFY -DUSE_PTHREAD"
export CPLUS_FLAGS="%{optflags} -DDO_ITT_NOTIFY -DUSE_PTHREAD"
export LDFLAGS="${LDFLAGS:-} -lpthread"
export RPM_LD_FLAGS="${RPM_LD_FLAGS:-} -lpthread"
%ifarch riscv64
export LDFLAGS="${LDFLAGS:-} -latomic"
export RPM_LD_FLAGS="${RPM_LD_FLAGS:-} -latomic"
%endif

%make_build stdver=c++14

for file in %{SOURCE6} %{SOURCE7} %{SOURCE8}; do
    base=$(basename ${file})
    sed 's/_FEDORA_VERSION/%{version}/' ${file} > ${base}
    touch -r ${file} ${base}
done

. build/linux*release/tbbvars.sh
pushd python
%make_build -C rml stdver=c++14 \
  CPLUS_FLAGS="%{optflags} -DDO_ITT_NOTIFY -DUSE_PTHREAD" \
  PIC_KEY="-fPIC -Wl,--as-needed" \
  LDFLAGS="$RPM_LD_FLAGS"
cp -p rml/libirml.so* .
%python3_build_debug
popd

%install
install -d %buildroot%_libdir
install -m644 build/linux*release/*.so.* \
	%buildroot%_libdir
pushd %buildroot%_libdir
for i in *.so.*
do
	devlib=$(echo $i|sed 's|\.1||')
	devlib=$(echo $devlib|sed 's|\.2||')
	ln -s $i $devlib
done
popd

install -d %buildroot%_includedir
cp -fR include/%name %buildroot%_includedir/

install -d %buildroot%_datadir/%name
cp -fR examples %buildroot%_datadir/%name/

for i in $(find ./ -name '*.html'); do
	install -Dm644 $i %buildroot%_docdir/%name/$i
done

pushd %buildroot%_docdir/%name
	rm -fr examples
	rm -fr python
popd

install -p -m644 CHANGES LICENSE README* %buildroot%_docdir/%name

for file in %{SOURCE6} %{SOURCE7} %{SOURCE8}; do
    install -p -D -m 644 $(basename ${file}) \
        $RPM_BUILD_ROOT/%{_libdir}/pkgconfig/$(basename ${file})
done

# Install the rml headers
mkdir -p $RPM_BUILD_ROOT%{_includedir}/rml
cp -p src/rml/include/*.h $RPM_BUILD_ROOT%{_includedir}/rml

. build/linux*release/tbbvars.sh
pushd python
%python3_install
cp -p libirml.so.1 $RPM_BUILD_ROOT%{_libdir}
ln -s libirml.so.1 $RPM_BUILD_ROOT%{_libdir}/libirml.so
popd

# Install the cmake files
mkdir -p $RPM_BUILD_ROOT%{_libdir}/cmake
cp -a cmake $RPM_BUILD_ROOT%{_libdir}/cmake/%{name}
rm $RPM_BUILD_ROOT%{_libdir}/cmake/%{name}/README.rst

%files -n lib%name
%_libdir/*.so.*

%files devel
%_includedir/rml
%_includedir/tbb
%_libdir/cmake/tbb
%_libdir/lib*.so
%_pkgconfigdir/*.pc

%files docs
%_docdir/%name

%files examples
%_datadir/%name/

%files -n python3-module-%name
%doc python/index.html
%python3_sitelibdir/TBB*
%python3_sitelibdir/tbb
%python3_sitelibdir/__pycache__/*

%changelog
* Fri Aug 07 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 2020.3-alt1
- Updated to upstream version 2020.3.

* Wed Apr 08 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 2020.2-alt1
- Updated to upstream version 2020.2.

* Sun Mar 22 2020 Nikita Ermakov <arei@altlinux.org> 2019-alt1.u8.1
- Add -latomic for riscv64.

* Wed Jul 24 2019 Aleksei Nikiforov <darktemplar@altlinux.org> 2019-alt1.u8
- Updated to upstream version 2019.U8.

* Wed Feb 13 2019 Igor Vlasenko <viy@altlinux.ru> 2019-alt1.u2
- NMU: new version
- packed cmake
- added and packed pkgconfig

* Sun Oct 14 2018 Igor Vlasenko <viy@altlinux.ru> 2018-alt1.u1.1.qa1
- NMU: applied repocop patch

* Thu Mar 22 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 2018-alt1.u1.1
- (NMU) Rebuilt with python-3.6.4.

* Tue Oct 03 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 2018-alt1.u1
- Updated to upstream version 2018.U1.

* Fri Apr 08 2016 Gleb F-Malinovskiy (qa) <qa_glebfm@altlinux.org> 42_20140601-alt1.qa1
- Rebuilt for gcc5 C++11 ABI.

* Thu Jul 10 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 42_20140601-alt1
- Version 42_20140601

* Mon Jun 09 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 42_20140416-alt1
- Version 42_20140416

* Tue Nov 19 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 42_20131003-alt1
- Version 42_20131003

* Fri Jul 26 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 41_20130613-alt1
- Version 41_20130613

* Mon Feb 11 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 41_20130116-alt1
- Version 41_20130116

* Fri Aug 31 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 40_20120613-alt1
- Version 40_20120613

* Mon May 21 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 40_20120408-alt1
- Version 40_20120408

* Wed Mar 07 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 40_297-alt1
- Version 40_297

* Sun Dec 18 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 40_233-alt1
- Version 40_233

* Sun May 08 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 30_20110315-alt1
- Version 30_20110315
- Disabled debug packages (we have debuginfo packages now)

* Tue Mar 22 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 30_20100310-alt6
- Added -g into compiler flags

* Fri Feb 11 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 30_20100310-alt5
- Rebuilt for debuginfo

* Wed Jan 26 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 30_20100310-alt4
- Added debug subpackages

* Fri Oct 15 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 30_20100310-alt3
- Fixed overlinking of libraries

* Wed Mar 31 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 30_20100310-alt2
- Disabled broken test

* Tue Mar 23 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 30_20100310-alt1
- Version 30_20100310 (ALT #23196)

* Fri Dec 18 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 20.014-alt1
- Initial build for Sisyphus

