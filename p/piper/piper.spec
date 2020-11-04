%define git %nil

Name: piper
Version: 0.5.1
Release: alt0.1
Summary: GTK+ application to configure gaming mice using ratbagd
Group: System/Configuration/Hardware
License: GPLv2
Url: https://github.com/libratbag/%name
Source0: https://github.com/libratbag/%name/archive/v%version/%name-%version.tar.gz
Patch: %name-%version-%release.patch

BuildRequires(pre): meson
BuildRequires: python3-module-pygobject3-devel python3-dev
BuildRequires: python3-module-pycairo python3-module-lxml python3-module-evdev ratbagd >= 0.13

BuildArch: noarch

Requires: ratbagd >= 0.14

%description
Piper is a GTK+ application to configure gaming mice, using libratbag via
ratbagd.  In order to run Piper, ratbagd has to be running (without it, you'll
get to see a pretty mouse trap).

%prep
%setup
%patch -p1

%build
%meson
%meson_build

%install
%meson_install

%files
%doc README* COPYING
%_bindir/*
%dir %python3_sitelibdir_noarch/%name
%python3_sitelibdir_noarch/%name
%dir %_datadir/%name
%_datadir/%name
%_datadir/metainfo/org.freedesktop.Piper.appdata.xml
%_desktopdir/*.desktop
%_iconsdir/hicolor/scalable/apps/*.svg
%_man1dir/*

%changelog
* Wed Nov 04 2020 L.A. Kostis <lakostis@altlinux.ru> 0.5.1-alt0.1
- 0.5.1.

* Sat Mar 21 2020 L.A. Kostis <lakostis@altlinux.ru> 0.4-alt0.1
- 0.4.

* Fri Sep 13 2019 L.A. Kostis <lakostis@altlinux.ru> 0.3-alt0.1.gitc7933aa
- 0.3-13-gc7933aa.

* Mon Apr 30 2018 L.A. Kostis <lakostis@altlinux.ru> 0.2.900-alt0.3.git5f6ed20
- GIT 5f6ed20.

* Thu Jan 04 2018 L.A. Kostis <lakostis@altlinux.ru> 0.2.900-alt0.2.gitd243325
- GIT d243325.

* Wed Oct 25 2017 L.A. Kostis <lakostis@altlinux.ru> 0.2.900-alt0.1.git39ddd05
- GIT 39ddd05.
- initial build for ALTLinux.
