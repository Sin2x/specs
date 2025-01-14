%define winemonodir %_datadir/wine/mono

Name: wine-mono
Version: 7.4.0
Release: alt1

Summary: Windows build of Mono to run .NET applications via Wine

License: GPL, LGPL2.1, MPL-2.0
Group: Office
Url: http://wiki.winehq.org/Mono

Packager: Vitaly Lipatov <lav@altlinux.ru>

# Source-url: https://dl.winehq.org/wine/wine-mono/%version/wine-mono-%version-x86.tar.xz
Source: %name-%version.tar

BuildArch: noarch

AutoReq: no
AutoProv: no

%description
Mono is an open-source and cross-platform implementation of the .NET
Framework. Wine can use a Windows build of Mono to run .NET applications.
For Wine releases 1.5.3 and later, the Wine Mono package is recommended.

%prep
%setup
# fix python2 print
%__subst 's|^print \(.*\)|print (\1)|' lib/mono/lldb/mono.py

%install
mkdir -p %buildroot%winemonodir/%name-%version/
cp -a * %buildroot%winemonodir/%name-%version/

%files
%dir %_datadir/wine/
%dir %winemonodir/
%winemonodir/%name-%version/

%changelog
* Sun Nov 06 2022 Vitaly Lipatov <lav@altlinux.ru> 7.4.0-alt1
- new version 7.4.0 (with rpmrb script)

* Fri Jun 24 2022 Vitaly Lipatov <lav@altlinux.ru> 7.3.0-alt1
- new version 7.3.0 (with rpmrb script)

* Tue Apr 19 2022 Vitaly Lipatov <lav@altlinux.ru> 7.2.0-alt2
- fix python2 issue

* Mon Apr 11 2022 Vitaly Lipatov <lav@altlinux.ru> 7.2.0-alt1
- new version 7.2.0 (with rpmrb script)

* Fri Apr 01 2022 Vitaly Lipatov <lav@altlinux.ru> 7.1.1-alt1
- new version 7.1.1 (with rpmrb script)

* Sat Nov 20 2021 Vitaly Lipatov <lav@altlinux.ru> 7.0.0-alt1
- new version 7.0.0 (with rpmrb script)

* Fri Jul 30 2021 Vitaly Lipatov <lav@altlinux.ru> 6.3.0-alt1
- new version 6.3.0 (with rpmrb script)

* Mon Jun 21 2021 Vitaly Lipatov <lav@altlinux.ru> 6.2.0-alt1
- new version 6.2.0 (with rpmrb script)

* Fri Apr 16 2021 Vitaly Lipatov <lav@altlinux.ru> 6.1.1-alt1
- new version 6.1.1 (with rpmrb script)

* Thu Feb 18 2021 Vitaly Lipatov <lav@altlinux.ru> 6.0.0-alt1
- new version 6.0.0 (with rpmrb script)

* Sat Oct 10 2020 Vitaly Lipatov <lav@altlinux.ru> 5.1.1-alt1
- new version 5.1.1 (with rpmrb script)

* Sat Jul 04 2020 Vitaly Lipatov <lav@altlinux.ru> 5.1.0-alt1
- new version 5.1.0 (with rpmrb script)

* Tue May 05 2020 Vitaly Lipatov <lav@altlinux.ru> 5.0.0-alt1
- new version 5.0.0 (with rpmrb script)

* Tue Jan 28 2020 Vitaly Lipatov <lav@altlinux.ru> 4.9.4-alt2
- switch to unpacked mono files in /usr/share/wine/mono

* Sun Nov 17 2019 Vitaly Lipatov <lav@altlinux.ru> 4.9.4-alt1
- new version (4.9.4) with rpmgs script

* Sat Sep 28 2019 Vitaly Lipatov <lav@altlinux.ru> 4.9.3-alt1
- new version 4.9.3 (with rpmrb script)

* Sat Jun 22 2019 Vitaly Lipatov <lav@altlinux.ru> 4.9.0-alt1
- new version 4.9.0 (with rpmrb script)

* Sun May 26 2019 Vitaly Lipatov <lav@altlinux.ru> 4.8.3-alt1
- new version 4.8.3 (with rpmrb script)

* Fri Apr 19 2019 Vitaly Lipatov <lav@altlinux.ru> 4.8.1-alt1
- new version 4.8.1 (with rpmrb script)

* Tue Mar 05 2019 Vitaly Lipatov <lav@altlinux.ru> 4.8.0-alt1
- new version 4.8.0 (with rpmrb script)

* Tue Feb 12 2019 Vitaly Lipatov <lav@altlinux.ru> 4.7.5-alt1
- new version 4.7.5 (with rpmrb script)

* Sat Jul 21 2018 Vitaly Lipatov <lav@altlinux.ru> 4.7.3-alt1
- new version (4.7.3) with rpmgs script

* Fri Aug 04 2017 Vitaly Lipatov <lav@altlinux.ru> 4.7.1-alt1
- new version 4.7.1

* Sat Mar 18 2017 Vitaly Lipatov <lav@altlinux.ru> 4.7.0-alt1
- new version (4.7.0) (ALT bug #33252)

* Tue Jan 31 2017 Vitaly Lipatov <lav@altlinux.ru> 4.6.4-alt1
- new version (4.6.4) (ALT bug #33065)

* Thu Jun 16 2016 Vitaly Lipatov <lav@altlinux.ru> 4.6.3-alt1
- new version (4.6.3) with rpmgs script

* Fri Apr 22 2016 Vitaly Lipatov <lav@altlinux.ru> 4.6.2-alt1
- update to 4.6.2

* Mon Mar 09 2015 Vitaly Lipatov <lav@altlinux.ru> 4.5.6-alt1
- update to 4.5.6

* Fri Dec 12 2014 Vitaly Lipatov <lav@altlinux.ru> 4.5.4-alt1
- update to 4.5.4

* Thu Sep 25 2014 Vitaly Lipatov <lav@altlinux.ru> 4.5.2-alt1
- update to 4.5.2

* Sat Dec 22 2012 Vitaly Lipatov <lav@altlinux.ru> 0.0.8-alt1
- update to 0.0.8

* Sat Jul 14 2012 Vitaly Lipatov <lav@altlinux.ru> 0.0.4-alt1
- initial build for ALT Linux Sisyphus (0.0.4 use since wine 1.5.6)

