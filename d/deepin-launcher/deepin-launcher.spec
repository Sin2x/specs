%global repo dde-launcher

Name: deepin-launcher
Version: 5.3.0.22
Release: alt1
Summary: Deepin desktop-environment - Launcher module
License: GPL-3.0+
Group: Graphical desktop/Other
Url: https://github.com/linuxdeepin/dde-launcher
Packager: Leontiy Volodin <lvol@altlinux.org>

Source: %url/archive/%version/%repo-%version.tar.gz

BuildRequires(pre): rpm-build-ninja
BuildRequires: gcc-c++ cmake qt5-tools-devel dtk5-core-devel dtk5-widget-devel deepin-qt-dbus-factory-devel gsettings-qt-devel libxcbutil-icccm-devel qt5-base-devel qt5-svg-devel qt5-x11extras-devel
# Requires: deepin-menu deepin-daemon startdde icon-theme-hicolor

%description
%summary.

%package devel
Summary: Development package for %name
Group: Graphical desktop/Other
BuildArch: noarch

%description devel
Header files and libraries for %name.

%prep
%setup -n %repo-%version
%__subst 's|lrelease|lrelease-qt5|' translate_generation.sh
# for Qt 5.15
%__subst '/include <QPainter>/a #include <QPainterPath>' src/widgets/miniframenavigation.cpp src/widgets/avatar.cpp src/widgets/miniframebutton.cpp

%build
%cmake_insource \
    -GNinja \
    -DCMAKE_INSTALL_PREFIX=%_prefix
%ninja_build

%install
%ninja_install

%files
%doc LICENSE
%_bindir/%repo
%_datadir/%repo/
%_datadir/dbus-1/services/*.service
%_iconsdir/hicolor/scalable/apps/%name.svg

%files devel
%_includedir/%repo/

%changelog
* Mon Oct 12 2020 Leontiy Volodin <lvol@altlinux.org> 5.3.0.22-alt1
- New version (5.3.0.22) with rpmgs script.

* Tue Aug 18 2020 Leontiy Volodin <lvol@altlinux.org> 5.3.0.5-alt1
- Initial build for ALT Sisyphus (thanks fedora and archlinux for this spec).
