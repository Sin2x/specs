Name: deepin-picker
Version: 5.0.14
Release: alt1
Summary: Color picker tool for deepin
License: GPL-3.0+
Group: Graphics
Url: https://github.com/linuxdeepin/deepin-picker
Packager: Leontiy Volodin <lvol@altlinux.org>

Source: %url/archive/%version/%name-%version.tar.gz
Patch: deepin-picker_5.0.6_alt_qt5.15.patch

BuildRequires(pre): desktop-file-utils
BuildRequires: qt5-linguist dtk5-widget-devel libX11-devel libxcb-devel libxcbutil-devel libXext-devel libXtst-devel qt5-base-devel qt5-svg-devel qt5-x11extras-devel
Requires: icon-theme-hicolor

%description
Simplest color picker.

%prep
%setup
# %patch -p2
%__subst 's|=lupdate|=lupdate-qt5|;s|=lrelease|=lrelease-qt5|' %name.pro
%__subst 's|Picker;||' %name.desktop

%build
%qmake_qt5 \
    CONFIG+=nostrip \
    PREFIX=%_prefix
%make_build

%install
%makeinstall INSTALL_ROOT=%buildroot

%check
desktop-file-validate %buildroot%_desktopdir/%name.desktop

%files
%doc README.md
%doc LICENSE
%_bindir/%name
%_datadir/%name/
%_desktopdir/%name.desktop
%_iconsdir/hicolor/scalable/apps/%name.svg
%_datadir/dbus-1/services/com.deepin.Picker.service

%changelog
* Thu Apr 08 2021 Leontiy Volodin <lvol@altlinux.org> 5.0.14-alt1
- New version (5.0.14) with rpmgs script.

* Tue Nov 17 2020 Leontiy Volodin <lvol@altlinux.org> 5.0.10-alt1
- New version (5.0.10) with rpmgs script.

* Thu Nov 05 2020 Leontiy Volodin <lvol@altlinux.org> 5.0.8-alt1
- New version (5.0.8) with rpmgs script.
- Enabled debuginfo.

* Mon Aug 03 2020 Leontiy Volodin <lvol@altlinux.org> 5.0.6-alt1
- Initial build for ALT Sisyphus (thanks fedora for this spec).

