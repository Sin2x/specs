# SPDX-License-Identifier: GPL-2.0-only
%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1

Name:		rr
Version:	5.4.0
Release:	alt2
Summary:	Record and Replay Framework
Group:		Development/Debuggers
License:	MIT and BSD and Apache-2.0
URL:		https://rr-project.org/
Vcs:		https://github.com/mozilla/rr.git
# Upstream issue tracker: https://github.com/mozilla/rr/issues/

Provides:	rr-project = %EVR
Obsoletes:	rr-project <= 5.3.0-alt1

Source:		%name-%version.tar
ExclusiveArch:	x86_64
Requires:	gdb

BuildRequires(pre): rpm-macros-cmake
BuildRequires(pre): rpm-build-python3
BuildRequires:	cmake
BuildRequires:	make
BuildRequires:	gcc-c++
BuildRequires:	capnproto-devel

%description
rr is a lightweight tool for recording, replaying and debugging execution of
applications (trees of processes and threads). Debugging extends gdb with very
efficient reverse-execution, which in combination with standard gdb/x86
features like hardware data watchpoints, makes debugging much more fun.

Supported microarchitectures are Intel Nehalem (2010) or later.

%prep
%setup -q
subst "s!/bin/!/lib/rr/!" src/replay_syscall.cc
subst "s!/bin/rr_page_!lib/rr/rr_page_!" src/AddressSpace.cc

%build
%add_optflags -Wno-error=class-memaccess
%cmake -Ddisable32bit=ON -DBUILD_TESTS=OFF
%cmake_build

%install
%cmake_install install DESTDIR=%buildroot
mv %buildroot/%_bindir/rr_* %buildroot%_libdir/rr/
subst '1s:/usr/bin/bash:/bin/bash:' %buildroot%_bindir/signal-rr-recording.sh
rm -f %buildroot%_bindir/rr_page*

%files
%doc LICENSE README.md
%_bindir/rr
%_bindir/signal-rr-recording.sh
%_bindir/rr-collect-symbols.py
%_datadir/rr
%_datadir/bash-completion/completions/rr
%_libdir/rr

%changelog
* Sun Dec 27 2020 Vitaly Chikunov <vt@altlinux.org> 5.4.0-alt2
- spec: Temporary disable '-Werror=class-memaccess'.
- spec: Update licenses.

* Thu Oct 29 2020 Vitaly Chikunov <vt@altlinux.org> 5.4.0-alt1
- Update to 5.4.0 (2020-10-29).
- spec: Rename from rr-project to rr.

* Fri Mar 27 2020 Vitaly Chikunov <vt@altlinux.org> 5.3.0-alt1
- Update to 5.3.0.

* Sat Nov 30 2019 Vitaly Chikunov <vt@altlinux.org> 5.2.0.0.253.g4c734005-alt1
- Update to 5.2.0-253-g4c734005.

* Thu Jun 14 2018 Vitaly Chikunov <vt@altlinux.ru> 5.2.0-alt1
- First build of rr for ALT.

