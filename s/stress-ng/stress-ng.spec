# SPDX-License-Identifier: GPL-2.0-only
%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1

Name: stress-ng
Version: 0.11.23
Release: alt1
Summary: Stress test a computer system in various selectable ways
Group: System/Kernel and hardware
License: GPL-2.0-only
Url: http://kernel.ubuntu.com/~cking/stress-ng/
Vcs: git://kernel.ubuntu.com/cking/stress-ng.git
# Mirror Vcs: https://github.com/ColinIanKing/stress-ng

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-make
BuildRequires: banner
BuildRequires: libaio-devel
BuildRequires: libattr-devel
BuildRequires: libbsd-devel
BuildRequires: libcap-devel
BuildRequires: libgcrypt-devel
BuildRequires: libkeyutils-devel
BuildRequires: liblksctp-devel
BuildRequires: libseccomp-devel
BuildRequires: zlib-devel

%description
Stress-ng will stress test a computer system in various selectable ways. It was
designed to exercise various physical subsystems of a computer as well as the
various operating system kernel interfaces. Stress-ng features:

* over 240 stress tests;
* 78 CPU specific stress tests that exercise floating point, integer,
  bit manipulation and control flow;
* over 20 virtual memory stress tests;
* portable: builds on Linux, etc.

%prep
%setup
%ifarch %e2k
# lcc 1.23 can't do string attribute form (1.24.03 will; mcst#4061)
sed -ri 's,"-O([0123])",\1,' stress-ng.h
%endif

%build
%make_build_ext

%install
%makeinstall_std

%check
# getrandom test does not work in sborotschnitza:
#   getrandom using flags GRND_INSECURE failed, errno=22 (Invalid argument)
sed -i '/STRESSORS/s/getrandom //g' debian/tests/lite-test

banner lite-test
time make lite-test
banner done

%files
%doc COPYING
%doc README
%_bindir/stress-ng
%_datadir/bash-completion/completions/stress-ng
%_datadir/stress-ng/
%_mandir/man1/stress-ng.1.*

%changelog
* Thu Nov 12 2020 Vitaly Chikunov <vt@altlinux.org> 0.11.23-alt1
- Update to V0.11.23 (2020-10-30).
- spec: Add %%check section.

* Sat Jul 13 2019 Michael Shigorin <mike@altlinux.org> 0.09.60-alt2
- E2K: fix build with lcc 1.23

* Mon Jul 01 2019 Nikolai Kostrigin <nickel@altlinux.org> 0.09.60-alt1
- New version
- Spec: cleanup

* Sat Aug 11 2018 Vitaly Chikunov <vt@altlinux.org> 0.09.36-alt2
- First package for ALT
