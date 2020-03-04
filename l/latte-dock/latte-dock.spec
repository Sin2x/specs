Name: latte-dock
Version: 0.9.9
Release: alt1
Summary: Latte is a dock based on plasma frameworks

License: GPLv2+
Group: Graphical desktop/KDE
Url: https://github.com/KDE/%name
Packager: Artyom Bystrov <arbars@altlinux.org>

Source: %name-%version.tar

BuildRequires: xdg-utils
BuildRequires: libxdg-basedir-devel
BuildRequires: cmake
BuildRequires: rpm-macros-cmake
BuildRequires: rpm-build-kf5
BuildRequires: rpm-build-xdg
BuildRequires: libxcb-devel
BuildRequires: libxcbutil-devel
BuildRequires: libSM-devel
BuildRequires: extra-cmake-modules
BuildRequires: qt5-x11extras-devel
BuildRequires: kf5-karchive-devel
BuildRequires: kf5-kactivities-devel
BuildRequires: kf5-kcoreaddons-devel
BuildRequires: kf5-kdbusaddons-devel
BuildRequires: kf5-kdeclarative-devel
BuildRequires: kf5-knewstuff-devel
BuildRequires: kf5-knotifications-devel
BuildRequires: kf5-kiconthemes-devel
BuildRequires: kf5-ki18n-devel
BuildRequires: kf5-kpackage-devel
BuildRequires: qt5-base-devel
BuildRequires: kf5-kwayland-devel
BuildRequires: kf5-kwindowsystem-devel
BuildRequires: kf5-kxmlgui-devel
BuildRequires: kf5-kglobalaccel-devel
BuildRequires: kf5-kguiaddons-devel
BuildRequires: kf5-kcrash-devel
BuildRequires: plasma5-libksysguard-devel
BuildRequires: kf5-kservice-devel
BuildRequires: kf5-plasma-framework-devel

%description
Latte is a dock based on plasma frameworks that provides an elegant and
intuitive experience for your tasks and plasmoids. It animates its contents by
using parabolic zoom effect and tries to be there only when it is needed.

"Art in Coffee"

%prep
%setup

%build
%K5build  


%install

make install/fast DESTDIR=%{buildroot} -C BUILD

%files
%_K5bin/%name
%_datadir/metainfo/org.kde.%name.appdata.xml
%_datadir/metainfo/org.kde.latte.plasmoid.appdata.xml
%_datadir/metainfo/org.kde.latte.shell.appdata.xml
%_K5xdgapp/org.kde.%name.desktop
%_K5data/dbus-1/interfaces/org.kde.LatteDock.xml
%_K5icon/breeze/*/*/*
%_K5icon/hicolor/*/*/*
%_datadir/knotifications5/lattedock.notifyrc
%_K5srv/plasma-applet-org.kde.latte.containment.desktop
%_K5srv/plasma-applet-org.kde.latte.plasmoid.desktop
%_K5srv/plasma-shell-org.kde.latte.shell.desktop
%_K5srv/plasma-containmentactions-lattecontextmenu.desktop
%_datadir/kservicetypes5/latte-indicator.desktop
%_K5data/plasma/plasmoids/org.kde.latte.containment/
%_K5data/plasma/plasmoids/org.kde.latte.plasmoid/
%_K5data/plasma/shells/org.kde.latte.shell/
%_datadir/latte
%_qt5_qmldir/org/kde/latte
%_qt5_plugindir/plasma_containmentactions_lattecontextmenu.so
%_qt5_plugindir/kpackage/packagestructure/latte_packagestructure_indicator.so
%_K5xdgconf/latte-layouts.knsrc
%_K5xdgconf/latte-indicators.knsrc

%changelog
* Sun Mar 01 2020 Artyom Bystrov <arbars@altlinux.org> 0.9.9-alt1
- initial build for ALT Sisyphus
