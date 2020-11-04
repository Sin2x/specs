Name: libantlr4
Version: 4.8
Release: alt1

Summary: ANTLR C++ runtime
License: BSD
Group: System/Libraries

Url: https://github.com/antlr/antlr4

Packager: Vitaly Lipatov <lav@altlinux.ru>

# Source-url: https://github.com/antlr/antlr4/archive/%version.tar.gz
Source: %name-%version.tar

BuildRequires(pre): rpm-macros-cmake
BuildRequires: cmake gcc-c++
BuildRequires: libuuid-devel

%description
ANTLR (ANother Tool for Language Recognition) is a powerful parser generator
for reading, processing, executing, or translating structured text or binary files.
It's widely used to build languages, tools, and frameworks.
From a grammar, ANTLR generates a parser that can build parse trees and also generates
a listener interface (or visitor) that makes it easy to respond to the recognition of phrases of interest.

%package devel
Summary: Header files for %name
Group: Development/C++
Requires: %name = %version-%release

%description devel
Header files for %name.

%prep
%setup
# build only cpp runtime
rm -f *.* && mv runtime runtime-t && mv runtime-t/Cpp/* .
# TODO: fix in upstream
%__subst "s|DESTINATION lib|DESTINATION %_lib|" runtime/CMakeLists.txt

%build
%cmake_insource -DANTLR4_INSTALL=ON -DWITH_DEMO=False -DCMAKE_BUILD_TYPE=Release
%make_build

%install
%makeinstall_std
rm -fv %buildroot%_libdir/libantlr4-runtime.a
rm -fv %buildroot%_docdir/%name/README.md

%files
%_libdir/libantlr4-runtime.so.%version

%files devel
%_docdir/%name/
%_libdir/libantlr4-runtime.so
%_includedir/antlr4-runtime/
%_libdir/cmake/antlr4/

%changelog
* Wed Nov 04 2020 Vitaly Lipatov <lav@altlinux.ru> 4.8-alt1
- initial build for ALT Sisyphus

