Name: liri-power-manager
Version: 0.9.0
Release: alt1

Summary: Power management support for Liri
License: GPL
Group: Graphical desktop/Other
Url: https://github.com/lirios/power-manager

Source: %name-%version-%release.tar

BuildRequires: gcc-c++ cmake cmake-modules-liri
BuildRequires: qt5-tools-devel kf5-solid-devel
BuildRequires: pkgconfig(Qt5Core)
BuildRequires: pkgconfig(Qt5Qml)
BuildRequires: pkgconfig(Qt5QuickControls2)
BuildRequires: pkgconfig(Qt5Svg)
BuildRequires: pkgconfig(Qt5GSettings)
BuildRequires: pkgconfig(Liri1Core)
BuildRequires: pkgconfig(Liri1Daemon)
BuildRequires: qml(Fluid.Controls)
BuildRequires: qml(QtGraphicalEffects)

%description
%summary

%prep
%setup

%build
%cmake
%cmake_build

%install
%cmakeinstall_std

%files
%_prefix/lib/systemd/user/*

%_libdir/qt5/plugins/liri/daemon/libpower.so
%_libdir/qt5/qml/Liri/Power

%_datadir/liri-settings/modules/power
%_datadir/liri-settings/translations/modules/*.qm
%_datadir/liri-shell/indicators/power
%_datadir/liri-power-manager
%_datadir/glib-2.0/schemas/*.xml

%changelog
* Fri Nov 01 2019 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.9.0-alt1
- initial
