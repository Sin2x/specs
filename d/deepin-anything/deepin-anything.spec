%define _sysusersdir /lib/sysusers.d

Name: deepin-anything
Version: 5.0.18
Release: alt1
Summary: Global search tool for Deepin
License: GPL-3.0+
Group: Graphical desktop/Other
Url: https://github.com/linuxdeepin/deepin-anything
Packager: Leontiy Volodin <lvol@altlinux.org>

Source: %url/archive/%version/%name-%version.tar.gz
Source1: deepin-anything-server.sysusers
# Patch from archlinux
Patch: 0001-linux-5.6.patch

BuildRequires: gcc-c++ qt5-base-devel udisks2-qt5-devel libmount-devel dtk5-core-devel libpcre-devel glib2-devel libpcre-devel

%description
File manager front end of Deepin OS.

%package -n lib%name
Summary: Libraries for %name
Group: System/Libraries

%description -n lib%name
This packages provides libraries for %name.

%package devel
Summary: Development package for %name
Group: Development/Other

%description devel
This package provides header files and libraries for %name.

%prep
%setup
#%patch -p1
sed -i 's|/usr/lib/$(DEB_HOST_MULTIARCH)|%_libdir|; s|/usr/lib/modules-load.d|%_sysconfdir/modules-load.d|' Makefile
sed -i 's|Anthing|Anything|' server/monitor/systemd.sysusers.d/deepin-anything-monitor.conf
sed -i 's|$$PREFIX/lib/sysusers.d|/lib/sysusers.d|' server/monitor/src/src.pro
sed -i 's|#include <pcre.h>|#include <pcre/pcre.h>|' library/src/fs_buf.c

%build
export PATH=%_qt5_bindir:$PATH
%make VERSION=%version

%install
%makeinstall_std
mv -f %buildroot%_sysconfdir/dbus-1/system.d %buildroot%_datadir/dbus-1/system.d
install -Dm644 %SOURCE1 %buildroot%_sysusersdir/deepin-anything-server.conf
rm -rf %buildroot/usr/src/deepin-anything-0.0/

%files
%doc README.md LICENSE CHANGELOG.md
%_bindir/*
%_datadir/dbus-1/system.d/com.deepin.anything.conf
%_unitdir/*.service
%_sysusersdir/*.conf
%_datadir/dbus-1/system-services/com.deepin.anything.service
%_sysconfdir/modules-load.d/anything.conf

%files -n lib%name
%_libdir/libanything.so.*
%_libdir/libdeepin-anything-server-lib.so.*

%files devel
%_libdir/libanything.so
%_libdir/libdeepin-anything-server-lib.so
%dir %_libdir/deepin-anything-server-lib/
%dir %_libdir/deepin-anything-server-lib/plugins/
%dir %_libdir/deepin-anything-server-lib/plugins/handlers/
%_libdir/deepin-anything-server-lib/plugins/handlers/libupdate-lft.so
%_libdir/deepin-anything-server-lib/plugins/handlers/README.txt
%dir %_includedir/%{name}*/
%dir %_includedir/%name/index/
%_includedir/%{name}*/*.h
%_includedir/%name/index/*.h
%_pkgconfigdir/deepin-anything-server-lib.pc
%_datadir/dbus-1/interfaces/com.deepin.anything.xml

%changelog
* Wed Oct 05 2022 Leontiy Volodin <lvol@altlinux.org> 5.0.18-alt1
- New version (5.0.18).

* Tue Aug 16 2022 Leontiy Volodin <lvol@altlinux.org> 5.0.13-alt2
- Changed default paths.

* Fri Feb 25 2022 Leontiy Volodin <lvol@altlinux.org> 5.0.13-alt1
- New version (5.0.13).

* Mon May 31 2021 Leontiy Volodin <lvol@altlinux.org> 5.0.9-alt1
- New version (5.0.9) with rpmgs script.

* Mon Feb 08 2021 Leontiy Volodin <lvol@altlinux.org> 5.0.7-alt1
- New version (5.0.7) with rpmgs script.

* Tue Sep 29 2020 Leontiy Volodin <lvol@altlinux.org> 5.0.1-alt1
- Initial build for ALT Sisyphus (thanks archlinux for the patch).
