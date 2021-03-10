%global soname dframeworkdbus
%global repo   dde-qt-dbus-factory

%def_disable clang

Name: deepin-qt-dbus-factory
Version: 5.4.4
Release: alt1
Summary: A repository stores auto-generated Qt5 dbus code
# The entire source code is GPL-3.0+ except
# libdframeworkdbus/qtdbusextended/ which is LGPL-2.1+
License: GPL-3.0+ and LGPL-2.1+
Group: Graphical desktop/Other
Url: https://github.com/linuxdeepin/dde-qt-dbus-factory
Packager: Leontiy Volodin <lvol@altlinux.org>

Source: %url/archive/%version/%repo-%version.tar.gz

%if_enabled clang
BuildRequires(pre): clang11.0-devel
%endif
BuildRequires: python3 libglvnd-devel qt5-base-devel

%description
A repository stores auto-generated Qt5 dbus code.

%package -n libdframeworkdbus2
Summary: Library for %name
Group: Development/KDE and QT

%description -n libdframeworkdbus2
A repository stores auto-generated Qt5 dbus code.
Library for %name.

%package devel
Summary: Development package for %name
Group: Graphical desktop/Other

%description devel
Header files and libraries for %name.

%prep
%setup -n %repo-%version
sed -i 's|python|python3|' libdframeworkdbus/*.{pro,py}

%build
%qmake_qt5 \
%if_enabled clang
    QMAKE_STRIP= -spec linux-clang \
%endif
    CONFIG+=nostrip \
    LIB_INSTALL_DIR=%_libdir
%make_build

%install
%makeinstall INSTALL_ROOT=%buildroot

%files -n libdframeworkdbus2
%doc README.md CHANGELOG.md technology-overview.md
%doc LICENSE
%_libdir/lib%soname.so.2*

%files devel
%_includedir/lib%soname-2.0/
%_libdir/cmake/DFrameworkdbus/
%_pkgconfigdir/%soname.pc
%_libdir/lib%soname.so

%changelog
* Wed Mar 10 2021 Leontiy Volodin <lvol@altlinux.org> 5.4.4-alt1
- New version (5.4.4) with rpmgs script.

* Tue Jan 26 2021 Leontiy Volodin <lvol@altlinux.org> 5.3.35-alt1
- New version (5.3.35) with rpmgs script.

* Wed Dec 30 2020 Leontiy Volodin <lvol@altlinux.org> 5.3.0.34-alt1
- New version (5.3.0.34) with rpmgs script.

* Wed Oct 28 2020 Leontiy Volodin <lvol@altlinux.org> 5.3.0.20-alt1
- New version (5.3.0.20) with rpmgs script.
- Fixed compatibility with qt 5.15.

* Wed Oct 07 2020 Leontiy Volodin <lvol@altlinux.org> 5.3.0.19-alt1
- New version (5.3.0.19) with rpmgs script.

* Mon Aug 31 2020 Leontiy Volodin <lvol@altlinux.org> 5.3.0.11-alt1
- Initial build for ALT Sisyphus (thanks fedora for this spec).
