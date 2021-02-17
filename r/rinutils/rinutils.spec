%define _unpackaged_files_terminate_build 1

Name: rinutils
Version: 0.2.0
Release: alt1

Summary: Shlomi Fish's gnu11 C Library of Random headers
Group: System/Libraries
License: MIT
Url: https://github.com/shlomif/rinutils

Source: %name-%version.tar

BuildRequires: cmake >= 3.5 gcc-c++ shlomif-cmake-modules

%description
This is a set of C headers containing macros and static functions
that are expected to work on Unix-like systems and MS Windows
that have been extracted from Shlomi Fishs projects.

%prep
%setup

%build
%cmake -DWITH_TEST_SUITE=OFF

%cmake_build

%install
%cmakeinstall_std 

%files
%_includedir/%name/
%_libdir/Rinutils/
%_pkgconfigdir/librinutils.pc
%doc README.asciidoc NEWS.asciidoc LICENSE

%changelog
* Mon Feb 10 2020 Konstantin Rybakov <kastet@altlinux.org> 0.2.0-alt1
- Initial build for ALT.

