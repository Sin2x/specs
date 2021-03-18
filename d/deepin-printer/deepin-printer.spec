%def_disable clang
%define repo dde-printer

Name: deepin-printer
Version: 0.8.5
Release: alt1
Summary: Printing utility for DDE
License: GPL-3.0+
Group: Graphical desktop/Other
Url: https://github.com/linuxdeepin/dde-printer
Packager: Leontiy Volodin <lvol@altlinux.org>

Source: %url/archive/%version/%repo-%version.tar.gz

%if_enabled clang
BuildRequires(pre): clang-devel
%else
BuildRequires(pre): gcc-c++
%endif
BuildRequires: qt5-base-devel
BuildRequires: libcups-devel
BuildRequires: qt5-tools
BuildRequires: dtk5-widget-devel
BuildRequires: libsmbclient-devel
BuildRequires: libusb-devel
BuildRequires: libgtest-devel
#Requires: icon-theme-hicolor

%description
Graphical interface to configure the printing system for DDE.

%prep
%setup -n %repo-%version
sed -i 's|lrelease|lrelease-qt5|' \
	src/{Printer,Deamon}/translate_generation.sh
sed -i 's|lupdate|lupdate-qt5|' \
	src/{Printer,Deamon}/translate_generation.sh \
	src/{Printer,Deamon}/translate_update.sh
sed -i '1i #include <stdexcept>' \
	src/cppcups/cupssnmp.cpp

%build
%qmake_qt5 \
%if_enabled clang
    QMAKE_STRIP= -spec linux-clang \
%endif
	DEFINES+="VERSION=%version" \
	CONFIG+=nostrip \
	#
%make_build

%install
%makeinstall INSTALL_ROOT=%buildroot
%find_lang %repo
chmod +x %buildroot%_sysconfdir/xdg/autostart/%repo-watch.desktop

%files -f %repo.lang
%doc README.md LICENSE
%_bindir/%repo
%_bindir/%repo-helper
%_datadir/%repo/
%_datadir/%repo-helper/
%_desktopdir/%repo.desktop
%_sysconfdir/xdg/autostart/%repo-watch.desktop
%_iconsdir/hicolor/48x48/apps/%repo.svg
%_datadir/polkit-1/actions/com.deepin.pkexec.devPrinter.policy
%dir %_datadir/deepin-manual/
%dir %_datadir/deepin-manual/manual-assets/
%dir %_datadir/deepin-manual/manual-assets/application/
%dir %_datadir/deepin-manual/manual-assets/application/%repo/
%_datadir/deepin-manual/manual-assets/application/%repo/print-manager/

%changelog
* Thu Mar 18 2021 Leontiy Volodin <lvol@altlinux.org> 0.8.5-alt1
- Initial build for ALT Sisyphus.
