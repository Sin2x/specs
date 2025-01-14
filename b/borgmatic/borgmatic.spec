Name: borgmatic
Version: 1.6.4
Release: alt1.1

Summary: borgmatic (formerly atticmatic) is a simple Python wrapper script for the Borg

License: GPL-3
Group: File tools
Url: https://github.com/witten/borgmatic

BuildArch: noarch

Packager: Pavel Vainerman <pv@altlinux.ru>

# Source-url: https://github.com/witten/borgmatic/archive/%version.tar.gz
Source: %name-%version.tar

Requires: python3-module-pykwalify >= 1:1.6.1-alt1

BuildRequires(pre): rpm-build-python3 rpm-build-intro

BuildRequires: python3-dev python3-module-setuptools

# according to setup.py
%py3_use pykwalify < 14.06
%py3_use pykwalify > 1.6.0
%py3_use ruamel-yaml > 0.15.0
%py3_use ruamel-yaml < 0.18.0


%description
borgmatic (formerly atticmatic) is a simple Python wrapper script for the Borg backup software 
that initiates a backup, prunes any old backups according to a retention policy, 
and validates backups for consistency. 
The script supports specifying your settings in a declarative configuration file 
rather than having to put them all on the command-line, and handles common errors.

%prep
%setup

%build
%python3_build

%install
%python3_install

%files
%doc LICENSE AUTHORS README.md
%_bindir/*
%python3_sitelibdir_noarch/*

%changelog
* Thu Jul 21 2022 Grigory Ustinov <grenka@altlinux.org> 1.6.4-alt1.1
- NMU: fixed requires according to setup.py

* Sat Jun 25 2022 Pavel Vainerman <pv@altlinux.ru> 1.6.4-alt1
- new version (1.6.4) with rpmgs script

* Mon Nov 29 2021 Pavel Vainerman <pv@altlinux.ru> 1.5.21-alt1
- new version (1.5.21) with rpmgs script

* Tue Oct 12 2021 Pavel Vainerman <pv@altlinux.ru> 1.5.20-alt1
- new version (1.5.20) with rpmgs script

* Sat Jun 19 2021 Pavel Vainerman <pv@altlinux.ru> 1.5.15-alt1
- new version (1.5.15) with rpmgs script

* Sat Jan 02 2021 Pavel Vainerman <pv@altlinux.ru> 1.5.12-alt1
- new version (1.5.12) with rpmgs script

* Sat Aug 22 2020 Pavel Vainerman <pv@altlinux.ru> 1.5.10-alt1
- new version (1.5.10) with rpmgs script

* Tue Jun 23 2020 Pavel Vainerman <pv@altlinux.ru> 1.5.7-alt1
- new version (1.5.7) with rpmgs script

* Tue Jun 09 2020 Pavel Vainerman <pv@altlinux.ru> 1.5.6-alt1
- new version (1.5.6) with rpmgs script

* Wed May 27 2020 Pavel Vainerman <pv@altlinux.ru> 1.5.5-alt1
- new version (1.5.5) with rpmgs script

* Sat May 16 2020 Pavel Vainerman <pv@altlinux.ru> 1.5.4-alt1
- new version (1.5.4) with rpmgs script

* Wed May 13 2020 Pavel Vainerman <pv@altlinux.ru> 1.5.3-alt1
- new version (1.5.3) with rpmgs script

* Wed Jan 15 2020 Nikolai Kostrigin <nickel@altlinux.org> 1.4.21-alt2
- NMU: switch BR: python-module-pykwalify -> python3-module-pykwalify
- fix license

* Sun Dec 22 2019 Pavel Vainerman <pv@altlinux.ru> 1.4.21-alt1
- new version (1.4.21) with rpmgs script

* Mon Dec 02 2019 Pavel Vainerman <pv@altlinux.ru> 1.4.16-alt1
- new version (1.4.16) with rpmgs script

* Fri Nov 08 2019 Pavel Vainerman <pv@altlinux.ru> 1.4.8-alt1
- new version (1.4.8) with rpmgs script

* Fri Nov 01 2019 Pavel Vainerman <pv@altlinux.ru> 1.4.1-alt1
- new version (1.4.1) with rpmgs script

* Sun Oct 20 2019 Pavel Vainerman <pv@altlinux.ru> 1.3.26-alt1
- new version (1.3.26) with rpmgs script

* Sun Sep 29 2019 Pavel Vainerman <pv@altlinux.ru> 1.3.21-alt1
- new version (1.3.21) with rpmgs script

* Mon Sep 23 2019 Pavel Vainerman <pv@altlinux.ru> 1.3.18-alt1
- new version (1.3.18) with rpmgs script

* Thu Sep 19 2019 Pavel Vainerman <pv@altlinux.ru> 1.3.16-alt1
- new version (1.3.16) with rpmgs script

* Fri Sep 13 2019 Pavel Vainerman <pv@altlinux.ru> 1.3.15-alt1
- new version (1.3.15) with rpmgs script

* Tue Jun 18 2019 Pavel Vainerman <pv@altlinux.ru> 1.3.7-alt1
- new version (1.3.7) with rpmgs script

* Fri Jun 14 2019 Pavel Vainerman <pv@altlinux.ru> 1.3.6-alt1
- new version (1.3.6) with rpmgs script

* Sun May 12 2019 Pavel Vainerman <pv@altlinux.ru> 1.3.3-alt1
- new version (1.3.3) with rpmgs script

* Tue Apr 30 2019 Vitaly Lipatov <lav@altlinux.ru> 1.3.1-alt1
- new version 1.3.1 (with rpmrb script)

* Tue Apr 30 2019 Vitaly Lipatov <lav@altlinux.ru> 1.2.17-alt2
- fix (build)requires

* Sun Feb 24 2019 Pavel Vainerman <pv@altlinux.ru> 1.2.17-alt1
- new version (1.2.17) with rpmgs script

* Tue Dec 11 2018 Pavel Vainerman <pv@altlinux.ru> 1.2.12-alt1
- new version (1.2.12) with rpmgs script

* Sun Nov 25 2018 Pavel Vainerman <pv@altlinux.ru> 1.2.11-alt1
- new version (1.2.11) with rpmgs script

* Sun Oct 14 2018 Pavel Vainerman <pv@altlinux.ru> 1.2.8-alt1
- new version (1.2.8) with rpmgs script

* Fri Aug 17 2018 Pavel Vainerman <pv@altlinux.ru> 1.2.2-alt2
- update requires

* Fri Aug 17 2018 Pavel Vainerman <pv@altlinux.ru> 1.2.2-alt1
- update build requires

* Thu Aug 16 2018 Pavel Vainerman <pv@altlinux.ru> 1.2.2-alt0.1
- new version (1.2.2) with rpmgs script
