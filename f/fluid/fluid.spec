Name: fluid
Version: 1.2.0
Release: alt1

Summary: Library for QtQuick apps with Material Design
License: MPL-2.0
Group: Development/Other
Url: https://github.com/lirios/fluid

Source: %name-%version-%release.tar

BuildRequires: cmake cmake-modules-liri
BuildRequires: pkgconfig(Qt5Core)
BuildRequires: pkgconfig(Qt5Gui)
BuildRequires: pkgconfig(Qt5Svg)
BuildRequires: pkgconfig(Qt5Qml)
BuildRequires: pkgconfig(Qt5Quick)
BuildRequires: pkgconfig(Qt5QuickControls2)
BuildRequires: pkgconfig(Qt5QuickTest)
BuildRequires: pkgconfig(Qt5WaylandClient)
BuildRequires: pkgconfig(wayland-client)

%package demo
Summary: Fluid demo app
Group: Development/Other

%description
Fluid is a collection of cross-platform QtQuick components for building
fluid and dynamic applications, using the Material Design guidelines.

%description demo
Fluid is a collection of cross-platform QtQuick components for building
fluid and dynamic applications, using the Material Design guidelines.
This package contains demo application.

%prep
%setup

%build
%cmake -DFLUID_WITH_DOCUMENTATION=OFF
%cmake_build

%install
%cmakeinstall_std

%files
%_libdir/qt5/qml/Fluid

%files demo
%_bindir/fluid-demo
%_desktopdir/io.liri.Fluid.Demo.desktop
%_iconsdir/*/*/*/io.liri.Fluid.Demo.*

%changelog
* Thu Oct 03 2019 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.2.0-alt1
- initial
