%global repo dde-network-utils

Name: deepin-network-utils
Version: 5.4.5
Release: alt1
Summary: Deepin desktop-environment - network utils
License: GPL-3.0-or-later
Group: Graphical desktop/Other
Url: https://github.com/linuxdeepin/dde-network-utils
Packager: Leontiy Volodin <lvol@altlinux.org>

Source: %url/archive/%version/%repo-%version.tar.gz

BuildRequires: gcc-c++
BuildRequires: deepin-qt-dbus-factory-devel
BuildRequires: qt5-base-devel
BuildRequires: qt5-linguist
BuildRequires: gsettings-qt-devel
# BuildRequires: libgio-qt-devel
BuildRequires: libgtest-devel

%description
Deepin desktop-environment - network utils.

%package -n libddenetworkutils
Summary: Library for %name
Group: Graphical desktop/Other

%description -n libddenetworkutils
Deepin desktop-environment - network utils.
Library for %name

%package devel
Summary: Development package for %name
Group: Graphical desktop/Other

%description devel
Header files and libraries for %name.

%prep
%setup -n %repo-%version
sed -i 's|lrelease|lrelease-qt5|' translate_generation.sh
sed -i 's|/lib$|/%_lib|' dde-network-utils/dde-network-utils.pro

%build
%qmake_qt5 \
    CONFIG+=nostrip \
    PREFIX=%prefix
%make_build

%install
%makeinstall INSTALL_ROOT=%buildroot

%files -n libddenetworkutils
%doc README.md
%_libdir/lib%{repo}.so.1
%_libdir/lib%{repo}.so.1.*
%_datadir/%repo/

%files devel
%_includedir/libddenetworkutils/
%_pkgconfigdir/%repo.pc
%_libdir/lib%{repo}.so

%changelog
* Thu Apr 08 2021 Leontiy Volodin <lvol@altlinux.org> 5.4.5-alt1
- New version (5.4.5) with rpmgs script.

* Mon Jan 25 2021 Leontiy Volodin <lvol@altlinux.org> 5.3.0.8-alt1
- New version (5.3.0.8) with rpmgs script.

* Tue Oct 13 2020 Leontiy Volodin <lvol@altlinux.org> 5.3.0.5-alt1
- New version (5.3.0.5) with rpmgs script.

* Mon Jul 27 2020 Leontiy Volodin <lvol@altlinux.org> 5.1.0.2-alt1
- Initial build for ALT Sisyphus (thanks fedora for this spec).
