Name: winetricks
Version: 20220617
Release: alt1

Summary: Work around common problems in Wine

License: LGPLv2+
Group: File tools
Url: https://github.com/Winetricks/winetricks

Packager: Vitaly Lipatov <lav@altlinux.ru>

# Source-url: https://github.com/Winetricks/winetricks/archive/refs/heads/master.zip
#Source-url: %url/archive/%version/%name-%version.tar.gz
Source: %name-%version.tar

Patch1: 0001-fix-detection-for-gui-without-args.patch
Patch2: 0001-winetricks-try-use-xvt-as-terminal.patch

BuildArch: noarch

ExclusiveArch: %ix86 x86_64 %arm aarch64

#BuildRequires: wine-common
BuildRequires: desktop-file-utils

# runtime dependencies
#Requires: /usr/bin/wine
Requires: cabextract gzip unzip wget which

#Requires: hicolor-icon-theme
Conflicts: wine-vanilla < 3.18
Conflicts: wine < 3.18
Conflicts: wine-etersoft < 4.0

%description
Winetricks is an easy way to work around common problems in Wine.

It has a menu of supported games/apps for which it can do all the
workarounds automatically. It also lets you install missing DLLs
or tweak various Wine settings individually.
 
%prep
%setup
%patch1 -p1
%patch2 -p1

# fix req. Disable autoreq at all?
%__subst 's|fusermount|a= fusermount|' src/winetricks

sed -i -e "s:steam::" -e "s:flash::" tests/*

%build
# not needed
#subst 's|WINETRICKS_VERSION=.*|WINETRICKS_VERSION=%version|' src/winetricks
# disable version checking
subst 's|winetricks_latest_version_check$||' src/winetricks

%install
%makeinstall_std
# some tarballs do not install appdata
install -m0644 -D -t %buildroot%_datadir/metainfo src/%name.appdata.xml
# hack for empty output to console
subst 's|Terminal=false|Terminal=true|' %buildroot%_desktopdir/%name.desktop

%check
desktop-file-validate %buildroot%_desktopdir/%name.desktop

%files
%doc COPYING debian/copyright
%doc README.md
%_bindir/%name
%_man1dir/%name.1*
%_iconsdir/hicolor/scalable/apps/%name.svg
%_desktopdir/%name.desktop
%_datadir/metainfo/%name.appdata.xml
%_datadir/bash-completion/completions/winetricks
#exclude %_datadir/appdata/%name.appdata.xml

%changelog
* Sat Jun 18 2022 Vitaly Lipatov <lav@altlinux.ru> 20220617-alt1
- new version (20220617) with rpmgs script
- try use xvt as terminal (ALT bug 43003)

* Wed Jun 15 2022 Vitaly Lipatov <lav@altlinux.ru> 20220411-alt3
- fix kdialog detection again
- run from menu with terminal enabled
- disable version checking

* Mon May 23 2022 Vitaly Lipatov <lav@altlinux.ru> 20220411-alt2
- fix kdialog detection

* Mon Apr 11 2022 Vitaly Lipatov <lav@altlinux.ru> 20220411-alt1
- new version 20220411 (with rpmrb script)

* Sat Apr 02 2022 Vitaly Lipatov <lav@altlinux.ru> 20220401-alt1
- new version (20220401) with rpmgs script

* Wed Feb 09 2022 Vitaly Lipatov <lav@altlinux.ru> 20220207-alt1
- new version (20220207) with rpmgs script

* Wed Dec 29 2021 Vitaly Lipatov <lav@altlinux.ru> 20211221-alt1
- new version (20211221) with rpmgs script

* Thu Aug 26 2021 Vitaly Lipatov <lav@altlinux.ru> 20210825.2-alt1
- add vcrun2019 update sha256sum
- set our winetricks version during build

* Wed Aug 25 2021 Vitaly Lipatov <lav@altlinux.ru> 20210825.1-alt1
- add msado15 install

* Wed Aug 25 2021 Vitaly Lipatov <lav@altlinux.ru> 20210825-alt1
- new version 20210825 (with rpmrb script)

* Tue Aug 24 2021 Vitaly Lipatov <lav@altlinux.ru> 20210815-alt1
- new version 20210815 (formally 20210206-next) with rpmgs script

* Tue Feb 09 2021 Vitaly Lipatov <lav@altlinux.ru> 20210206-alt1
- new version 20210206 (with rpmrb script)

* Wed Dec 09 2020 Vitaly Lipatov <lav@altlinux.ru> 20201206-alt1
- new version 20201206 (with rpmrb script) (ALT bug 39411)

* Mon May 11 2020 Vitaly Lipatov <lav@altlinux.ru> 20200412-alt1
- new version 20200412 (with rpmrb script)

* Fri Jan 17 2020 Vitaly Lipatov <lav@altlinux.ru> 20191224-alt1
- new version 20191224 (with rpmrb script)

* Thu Sep 26 2019 Vitaly Lipatov <lav@altlinux.ru> 20190912-alt1
- new version 20190912 (with rpmrb script)

* Sat Jun 22 2019 Vitaly Lipatov <lav@altlinux.ru> 20190615-alt1
- new version 20190615 (with rpmrb script)

* Fri Apr 19 2019 Vitaly Lipatov <lav@altlinux.ru> 20190310-alt2
- fix wine-etersoft conflicts

* Mon Mar 18 2019 Vitaly Lipatov <lav@altlinux.ru> 20190310-alt1
- new version 20190310 (with rpmrb script)

* Wed Dec 19 2018 Vitaly Lipatov <lav@altlinux.ru> 20181203-alt2
- fix zenity/kdialog requires (ALT bug 35750)

* Fri Dec 07 2018 Vitaly Lipatov <lav@altlinux.ru> 20181203-alt1
- new version 20181203 (with rpmrb script)

* Sat Oct 13 2018 Vitaly Lipatov <lav@altlinux.ru> 20180815-alt1
- new version (20180815) with rpmgs script

* Sat Oct 13 2018 Vitaly Lipatov <lav@altlinux.ru> 20180603-alt1
- initial build for ALT Sisyphus

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 20180603-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Jul 01 2018 Raphael Groner <projects.rg@smart.ms> - 20180603-2
- avoid shebang warning of rpmlint for appdata

* Sat Jun 23 2018 Raphael Groner <projects.rg@smart.ms> - 20180603-1
- new version

* Mon Mar 05 2018 Raphael Groner <projects.rg@smart.ms> - 20180217-1
- new version
- drop obsolete scriptlets
- move appdata into mimeinfo

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 20171222-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Jan 22 2018 Ben Rosser <rosser.bjr@gmail.com> - 20171222-1
- Updated to latest upstream release. (#1528622)
- Moved appdata file to new appdata location, /usr/share/metainfo.
- Removed dependency on 'time' package as per #1533795.

* Sun Dec 03 2017 Raphael Groner <projects.rg@smart.ms> - 20171018-1
- new version
- ensure appdata gets installed

* Sun Aug 13 2017 Raphael Groner <projects.rg@smart.ms> - 20170731-1
- new snapshot
- add appdata

* Sun Aug 13 2017 Raphael Groner <projects.rg@smart.ms> - 20170614-1
- new version

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 20170517-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Jun 10 2017 Raphael Groner <projects.rg@smart.ms> - 20170517-1
- new version

* Tue Mar 28 2017 Raphael Groner <projects.rg@smart.ms> - 20170326-1
- new version

* Sat Feb 11 2017 Raphael Groner <projects.rg@smart.ms> - 20170207-1
- new version
- drop additional icon and desktop file in favor of upstream ones

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 20161107-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 05 2016 Builder <projects.rg@smart.ms> - 20161107-2
- add ExcludeArch

* Wed Nov 09 2016 Raphael Groner <projects.rg@smart.ms> - 20161107-1
- new version

* Mon Nov 07 2016 Raphael Groner <projects.rg@smart.ms> - 20161012-1
- new version
- disable architectures without available wine
- don't check explicitly for wine version

* Sun Oct 09 2016 Raphael Groner <projects.rg@smart.ms> - 20161005-2
- use apps subfolder for icon

* Sun Oct 09 2016 Raphael Groner <projects.rg@smart.ms> - 20161005-1
- new version
- add copyright
- add icon

* Fri Jul 29 2016 Raphael Groner <projects.rg@smart.ms> - 20160724-1
- new version

* Mon Jul 11 2016 Raphael Groner <projects.rg@smart.ms> - 20160709-1
- initial
