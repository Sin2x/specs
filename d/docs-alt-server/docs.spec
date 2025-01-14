%define variant alt-server
%define Variant ALT Server

%define _documentationdir %_defaultdocdir/documentation
%define _docsinstalldir %_defaultdocdir/%variant

%define variants docs-office-server docs-backup-server docs-desktop docs-school-master docs-school-junior docs-school-lite docs-school-server docs-kdesktop docs-school-terminal docs-school-newlite docs-centaurus docs-simply-linux docs-lxdesktop docs-lxdesktop-lite docs-school-teacher docs-alt-education docs-alt-kworkstation docs-alt-server docs-alt-workstation docs-alt-kworkstation docs-alt-spworkstation docs-alt-server-v

Name: docs-%variant
Version: 10.1
Release: alt6

Summary: %Variant documentation
License: %fdl
Group: Documentation

Packager: ALT Docs Team <docs@packages.altlinux.org>
BuildArch: noarch

Source: %name-%version-%release.tar

Obsoletes: docs-basealt-desktop <= 8.0-alt2
Conflicts: %(for n in %variants ; do [ "$n" = %name ] || echo -n "$n "; done)

BuildRequires(pre):rpm-build-licenses
BuildRequires: publican
BuildRequires: perl-podlators
BuildRequires: libwebp-tools

%description
%Variant documentation.

%prep
%setup -n %name-%version-%release

%build
%make_build

%install
%make_install DESTDIR=%buildroot docdir=%_docsinstalldir install
ln -s $(relative %_docsinstalldir %_documentationdir) %buildroot%_documentationdir
sed -i 's/src="images\/\(.*\).png"/src="images\/\1.webp"/g' %buildroot%_docsinstalldir/ru-RU/index.html
for file in %buildroot%_docsinstalldir/ru-RU/images/*.png; do cwebp $file -o %buildroot%_docsinstalldir/ru-RU/images/$(basename $file .png).webp -quiet && rm $file; done

%files
%_docsinstalldir
%_documentationdir

%changelog
* Tue Nov 15 2022 Elena Mishina <lepata@altlinux.org> 10.1-alt6
- update to ALT Server 10.1
- fix OpenUDS HA (closes: #43979, #43977)

* Fri Sep 16 2022 Elena Mishina <lepata@altlinux.org> 10.1-alt5
- update to ALT Server 10.1rc
- fix typo (closes: #43710)

* Fri Aug 19 2022 Elena Mishina <lepata@altlinux.org> 10.1-alt4
- add OpenUDS HA
- add OpenUDS tunnel

* Mon Jul 18 2022 Elena Mishina <lepata@altlinux.org> 10.1-alt3
- update to ALT Server 10.1Beta4

* Tue Jul 12 2022 Elena Mishina <lepata@altlinux.org> 10.1-alt2
- fix typo (closes: #43146, #43079, #43073)
- fix pbs (closes: #43131, #43132, #43133)

* Mon Jun 20 2022 Elena Mishina <lepata@altlinux.org> 10.1-alt1
- update to ALT Server 10.1Beta
- add proxmox backup server

* Wed Apr 06 2022 Elena Mishina <lepata@altlinux.org> 10.0-alt3
- fix some typos
- add UrBackup, delete bacula
- update documentation

* Tue Nov 30 2021 Elena Mishina <lepata@altlinux.org> 10.0-alt2
- update to ALT Server 10.0rc
- reduce package size

* Tue Nov 09 2021 Elena Mishina <lepata@altlinux.org> 10.0-alt1
- update to ALT Server 10.0Beta

* Wed Jul 09 2021 Elena Mishina <lepata@altlinux.org> 9.2-alt1
- update to ALT Server 9.2
- add OpenUDS

* Mon Mar 15 2021 Elena Mishina <lepata@altlinux.org> 9.1-alt5
- install-packages-advanced: add epm
- admin: pacemaker, group policy
- fix typo

* Mon Nov 30 2020 Elena Mishina <lepata@altlinux.org> 9.1-alt4
- update Zabbix documentation for 5.0

* Mon Nov 16 2020 Elena Mishina <lepata@altlinux.org> 9.1-alt3
- add ALT Media Writer
- add configured new hosts in Zabbix
- update documentation

* Tue Jul 14 2020 Elena Mishina <lepata@altlinux.org> 9.1-alt1
- update to latest public distr of ALT Server 9.1

* Fri Oct 04 2019 Elena Mishina <lepata@altlinux.org> 9.0-alt1
- update to latest public distr

* Mon Jul 29 2019 Elena Mishina <lepata@altlinux.org> 8.90-alt1
- update to beta verson of ALT Server 9.0

* Wed Oct 17 2018 Elena Mishina <lepata@altlinux.org> 8.2-alt4
- fix typo
- update documentation

* Fri Mar 16 2018 Elena Mishina <lepata@altlinux.org> 8.2-alt3
- update documentation

* Thu Dec 11 2017 Elena Mishina <lepata@altlinux.org> 8.2-alt2
- fix conflict package

* Thu Nov 30 2017 Elena Mishina <lepata@altlinux.org> 8.2-alt1
- updated to latest public distr
- fix typo

* Wed May 24 2017 Elena Mishina <lepata@altlinux.org> 8.0-alt6
- update documentation
- fix typo

* Thu Mar 20 2017 Elena Mishina <lepata@altlinux.org> 8.0-alt5
- update documentation
- fix typo

* Thu Feb 09 2017 Elena Mishina <lepata@altlinux.org> 8.0-alt4
- update Conflicts list
- update documentation

* Thu Jan 19 2017 Artem Zolochevskiy <azol@altlinux.ru> 8.0-alt3
- updated to latest public distr

* Fri Jan 13 2017 Artem Zolochevskiy <azol@altlinux.org> 8.0-alt2
- update doc

* Fri Jan 13 2017 Artem Zolochevskiy <azol@altlinux.org> 8.0-alt1
- initial build
