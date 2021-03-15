%def_disable clang
%def_enable cmake

Name: deepin-image-viewer
Version: 5.6.3.73
Release: alt2.gitb4da182
Summary: Image viewer for Deepin
License: GPL-3.0+
Group: Graphics
Url: https://github.com/linuxdeepin/deepin-image-viewer
Packager: Leontiy Volodin <lvol@altlinux.org>

Source: %url/archive/%version/%name-%version.tar.gz

%if_enabled clang
BuildRequires(pre): clang11.0-devel
%else
BuildRequires(pre): gcc-c++ libgomp10-devel
%endif
%if_enabled cmake
BuildRequires(pre): cmake rpm-build-ninja
%endif
BuildRequires: qt5-base-devel
BuildRequires: qt5-tools-devel
BuildRequires: libraw-devel
BuildRequires: qt5-tools
BuildRequires: libexif-devel
BuildRequires: dtk5-widget-devel
BuildRequires: libgio-qt-devel
BuildRequires: udisks2-qt5-devel
BuildRequires: qt5-svg-devel
BuildRequires: qt5-x11extras-devel
BuildRequires: libfreeimage-devel
Requires: deepin-qt5integration

%description
%summary.

%prep
%setup
sed -i 's|lrelease|lrelease-qt5|' src/src.pro
# Our build of freeimage disabled support for these formats like archlinux
sed -i '/FIF_FAXG3/d' src/src/utils/unionimage.cpp

%build
%if_enabled cmake
%cmake_insource \
	-GNinja
%ninja_build
%else
%qmake_qt5 \
%if_enabled clang
    QMAKE_STRIP= -spec linux-clang \
%endif
    CONFIG+=nostrip \
    PREFIX=%prefix
%make_build
%endif

%install
%if_enabled cmake
%ninja_install
%else
%makeinstall INSTALL_ROOT=%buildroot
%endif
%find_lang %name

%files -f %name.lang
%doc LICENSE README.md
%_bindir/%name
%_desktopdir/%name.desktop
%_datadir/%name/
%dir %_datadir/deepin-manual/
%dir %_datadir/deepin-manual/manual-assets/
%dir %_datadir/deepin-manual/manual-assets/application/
%dir %_datadir/deepin-manual/manual-assets/application/%name/
%_datadir/deepin-manual/manual-assets/application/%name/image-viewer/
%_iconsdir/hicolor/scalable/apps/%name.svg
%_qt5_plugindir/imageformats/libxraw.so
%_datadir/dbus-1/services/com.deepin.ImageViewer.service

%changelog
* Mon Mar 15 2021 Leontiy Volodin <lvol@altlinux.org> 5.6.3.73-alt2.gitb4da182
- Updated from commit b4da182b92425880e208c127d5712aef840200a4.
- Built with cmake and ninja instead qmake and make.

* Mon Jan 25 2021 Leontiy Volodin <lvol@altlinux.org> 5.6.3.73-alt1
- New version (5.6.3.73) with rpmgs script.

* Fri Dec 11 2020 Leontiy Volodin <lvol@altlinux.org> 5.6.3.69-alt1
- Initial build for ALT Sisyphus.

