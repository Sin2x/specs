Name: goverlay
Version: 0.3.8
Release: alt1

Summary: Graphical UI to help manage Linux overlays
License: GPLv3
Group: System/Configuration/Hardware

Url: https://github.com/benjamimgois/goverlay
Source: https://github.com/benjamimgois/goverlay/archive/%version/%name-%version.tar.gz
Patch: goverlay-enable-debuginfo-generation.patch

ExclusiveArch: %ix86 x86_64
BuildRequires: lazarus

Requires: mangohud

#Recommends: git
#Recommends: mesa-demos
#Recommends: vkbasalt
#Recommends: vulkan-tools

%description
GOverlay is an opensource project that aims to create a graphical UI to
help manage Linux overlays. Currently supported:

- MangoHUD
- vkBasalt

%prep
%setup

%build
%make_build

%install
%makeinstall_std prefix=%prefix

%files
%doc LICENSE
%_bindir/%name
%_desktopdir/%name.desktop
%_datadir/metainfo/%name.metainfo.xml
%_iconsdir/hicolor/*/apps/%name.png
%_man1dir/%name.1*

%changelog
* Wed Apr 21 2021 Michael Shigorin <mike@altlinux.org> 0.3.8-alt1
- initial build for ALT Sisyphus (thx Mageia)

* Fri Oct 16 2020 akien <akien> 0.3.8-1.mga8
+ Revision: 1636448
- Version 0.3.8
- Version 0.3.6

* Mon Jul 06 2020 akien <akien> 0.3.5-1.mga8
+ Revision: 1602481
- Version 0.3.5

* Fri Mar 13 2020 akien <akien> 0.2-1.mga8
+ Revision: 1556067
- Version 0.2

* Tue Mar 10 2020 akien <akien> 0.1.3-1.mga8
+ Revision: 1555273
- imported package goverlay

