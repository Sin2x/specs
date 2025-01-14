# SPDX-License-Identifier: GPL-2.0-only
%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%set_verify_elf_method strict

Name: sslscan
Version: 2.0.15
Release: alt1
Summary: sslscan tests SSL/TLS enabled services to discover supported cipher suites
License: GPL-3.0-or-later
Group: Networking/Other
Url: https://github.com/rbsec/sslscan

Source: %name-%version.tar
BuildRequires: libssl-devel
%{?!_without_check:%{?!_disable_check:BuildRequires: openssl}}

%description
%summary

%prep
%setup

%build
%add_optflags %(getconf LFS_CFLAGS) -U_FORTIFY_SOURCE -D_FORTIFY_SOURCE=3 -fanalyzer -Werror
%make_build CFLAGS="%optflags" DEFINES=-DVERSION='\"%version-%release\"'

%install
%makeinstall_std

%check
%buildroot%_bindir/sslscan --version
openssl req -x509 -newkey rsa -keyout server.pem -out server.pem -days 1 -nodes -subj /CN=qwerty
openssl s_server &>/dev/null </dev/zero &
trap "kill $!" EXIT
sleep 1
%buildroot%_bindir/sslscan --no-colour --xml=a.xml 127.1:4433
grep -q -v error a.xml
grep -q accepted a.xml
grep -q qwerty   a.xml

%files
%doc LICENSE README.md
%_bindir/sslscan
%_man1dir/sslscan.1.xz

%changelog
* Wed Jul 13 2022 Vitaly Chikunov <vt@altlinux.org> 2.0.15-alt1
- Update to 2.0.15 (2022-07-03).

* Tue Jun 28 2022 Vitaly Chikunov <vt@altlinux.org> 2.0.14-alt1
- Update to 2.0.14 (2022-06-23).
- spec: Add %%check section.

* Sat Mar 26 2022 Vitaly Chikunov <vt@altlinux.org> 2.0.12-alt1
- Update to 2.0.12 (2022-02-23).

* Wed Jun 02 2021 Vitaly Chikunov <vt@altlinux.org> 2.0.10-alt1
- First import of 2.0.10-4-g5224502 (2021-05-29).
