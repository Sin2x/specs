%define _unpackaged_files_terminate_build 1

%define origname yaml-cpp
%define soversion 0

Name: lib%origname%soversion
Version: 0.6.3
Release: alt2

Summary: A YAML parser and emitter for C++
License: MIT
Group: System/Legacy libraries

Url: https://github.com/jbeder/yaml-cpp

# https://github.com/jbeder/yaml-cpp.git
Source: %name-%version.tar

Patch1: CVE-2017-5950.patch

BuildRequires(pre): rpm-macros-cmake
BuildRequires: boost-devel-headers cmake gcc-c++

Provides: %name = %EVR

%description
A YAML parser and emitter for C++

%prep
%setup
%patch1 -p1

%build
%cmake \
	-DYAML_BUILD_SHARED_LIBS:BOOL=ON \
	-DYAML_CPP_BUILD_TOOLS:BOOL=OFF \
	-DYAML_CPP_BUILD_TESTS:BOOL=OFF \
	%nil

%cmake_build

%install
%cmakeinstall_std

%__rm -rf %buildroot%_includedir/%origname
%__rm -rf %buildroot%_libdir/cmake/%origname
%__rm -rf %buildroot%_libdir/lib%origname.so
%__rm -rf %buildroot%_pkgconfigdir/%origname.pc

%files
%doc LICENSE *.md
%_libdir/*.so.*

%changelog
* Fri Nov 05 2021 Nazarov Denis <nenderus@altlinux.org> 0.6.3-alt2
- Build as legacy library

* Tue Apr 14 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 0.6.3-alt1
- Updated to upstream version 0.6.3.

* Mon Oct 22 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 0.6.2-alt2
- Applied patches from Fedora (Fixes: CVE-2017-5950)

* Tue Sep 11 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 0.6.2-alt1
- Updated to upstream version 0.6.2.

* Tue Dec 1 2015 Vladimir Didenko <cow@altlinux.ru> 0.5.1-alt4
- Rebuild with gcc5

* Tue Mar 24 2015 Vladimir Didenko <cow@altlinux.ru> 0.5.1-alt3
- spec cleanup
- add dependency on corresponding library to devel package

* Sat Jun 7 2014 Andrew Clark <andyc@altlinux.ru> 0.5.1-alt2
- spec file has been changed

* Thu May 29 2014 Andrew Clark <andyc@altlinux.ru> 0.5.1-alt1
- initial build for ALT Linux
