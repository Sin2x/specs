%define rname colord-kde
Name: kde5-colord
Version: 0.5.0
Release: alt1
%K5init altplace

Group: Graphical desktop/KDE
Summary: Colord support for KDE
Url: https://invent.kde.org/graphics/colord-kde/
License: GPL-2.0-or-later

Requires: colord plasma5-systemsettings

Source: %rname-%version.tar
# upstream
Patch1: 0001-Remove-unused-dependencies.patch
Patch2: 0003-Add-categorized-logging.patch
Patch3: 0004-Avoid-crash-on-exit-on-wayland.patch
Patch4: 0005-Fix-colord-helper-DBus-annotations.patch

# Automatically added by buildreq on Mon Sep 12 2022 (-bi)
# optimized out: cmake cmake-modules debugedit elfutils fontconfig fontconfig-devel gcc-c++ glibc-kernheaders-generic glibc-kernheaders-x86 kf5-kauth-devel kf5-kcodecs-devel kf5-kconfig-devel kf5-kcoreaddons-devel kf5-kwidgetsaddons-devel libICE-devel libSM-devel libX11-devel libXScrnSaver-devel libXau-devel libXcomposite-devel libXcursor-devel libXdamage-devel libXdmcp-devel libXext-devel libXfixes-devel libXft-devel libXi-devel libXinerama-devel libXmu-devel libXpm-devel libXrandr-devel libXrender-devel libXt-devel libXtst-devel libXv-devel libXxf86misc-devel libXxf86vm-devel libctf-nobfd0 libfreetype-devel libglvnd-devel libgpg-error libqt5-core libqt5-dbus libqt5-gui libqt5-waylandclient libqt5-widgets libqt5-x11extras libqt5-xml libsasl2-3 libssl-devel libstdc++-devel libwayland-client libwayland-cursor libxcb-devel libxkbcommon-devel libxkbfile-devel pkg-config python-modules python2-base python3 python3-base python3-dev python3-module-paste qt5-base-common qt5-base-devel rpm-build-file rpm-build-python3 rpm-macros-python sh4 tzdata xorg-proto-devel xorg-xf86miscproto-devel
#BuildRequires: appstream extra-cmake-modules kf5-kcmutils-devel kf5-kconfigwidgets-devel kf5-kdbusaddons-devel kf5-ki18n-devel kf5-kservice-devel kf5-kwindowsystem-devel libXaw-devel libXres-devel liblcms2-devel libxcbutil-devel libxcbutil-icccm-devel libxkbcommon-x11-devel lua5.3 python-modules-compiler python3-module-setuptools python3-module-zope qt5-imageformats qt5-svg-devel qt5-wayland-devel qt5-webengine-devel qt5-x11extras-devel
BuildRequires(pre): rpm-build-kf5
BuildRequires: extra-cmake-modules
BuildRequires: qt5-base-devel qt5-x11extras-devel
BuildRequires: liblcms2-devel
BuildRequires: libXrandr-devel libXaw-devel libXres-devel libxcb-devel
BuildRequires: kf5-kcmutils-devel kf5-kconfigwidgets-devel kf5-kdbusaddons-devel kf5-ki18n-devel
BuildRequires: kf5-kservice-devel kf5-kwindowsystem-devel

%description
KDE support for colord including KDE Daemon module and System Settings module.

%prep
%setup -n %rname-%version
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1

%build
%K5build

%install
%K5install
%K5install_move data locale
%find_lang %name --with-kde --all-name

%files -f %name.lang
%doc MAINTAINERS TODO
%_K5bin/colord*
%_K5xdgapp/colord*.desktop
%_K5plug/*_colord.so
%_K5srv/*_colord.desktop
%_K5srv/kded/*colord.desktop

%changelog
* Mon Sep 12 2022 Sergey V Turchin <zerg@altlinux.org> 0.5.0-alt1
- initial build
