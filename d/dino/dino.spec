%def_disable snapshot

%define rdn_name im.dino.Dino

Name: dino
Version: 0.2.0
Release: alt2

Summary: Modern Jabber/XMPP client
License: GPL-3.0
Group: Networking/Instant messaging
Url: https://dino.im

%if_disabled snapshot
Source: https://github.com/%name/%name/archive/v%version/%name-%version.tar.gz
%else
Source: %name-%version.tar
%endif
# up
Patch: dino-9acb54df9254609f2fe4de83c9047d408412de28.patch

Requires: lib%name = %EVR

BuildRequires(pre): cmake
BuildRequires: vala-tools libgtk+3-devel libgee0.8-devel libsoup-devel
BuildRequires: libicu-devel pkgconfig(libqrencode) >= 4.0 libgcrypt-devel
BuildRequires: libgpgme-devel libsignal-protocol-c-devel libsqlite3-devel

%description
Dino is a modern open-source chat client for the desktop. It focuses on
providing a clean and reliable Jabber/XMPP experience while having your
privacy in mind.

%package -n lib%name
Summary: Dino shared libraries
Group: System/Libraries

%description -n lib%name
Dino is a modern open-source chat client for the desktop.
This package provides shared libraries for Dino.

%package -n lib%name-devel
Summary: Development files for Dino libraries
Group: Development/C
Requires: lib%name = %EVR

%description -n lib%name-devel
Dino is a modern open-source chat client for the desktop.
This package provides libraries and headers needed to develop Dino plugins.

%prep
%setup -n %name-%version
%patch -p1

%build
%cmake
# SMP-incompatible build
%make -C BUILD

%install
%cmakeinstall_std
%find_lang --all-name --output=%name.lang %name


%files -f %name.lang
%_bindir/%name
%_desktopdir/%rdn_name.desktop
%_datadir/dbus-1/services/%rdn_name.service
%_datadir/metainfo/%rdn_name.appdata.xml
%_iconsdir/hicolor/*/*/*.svg
%dir %_libdir/%name
%dir %_libdir/%name/plugins
%_libdir/%name/plugins/http-files.so
%_libdir/%name/plugins/omemo.so
%_libdir/%name/plugins/openpgp.so
%doc README*

%files -n lib%name
%_libdir/lib%name.so.*
%_libdir/libqlite.so.*
%_libdir/libxmpp-vala.so.*

%files -n lib%name-devel
%_includedir/*.h
%_libdir/lib%name.so
%_libdir/libqlite.so
%_libdir/libxmpp-vala.so
# vapi(icu-uc) required, but
#$ find ./ -name "*icu-uc*"
#./main/vapi/icu-uc.vapi
#./xmpp-vala/vapi/icu-uc.vapi
#%_vapidir/*

%changelog
* Tue Apr 13 2021 Yuri N. Sedunov <aris@altlinux.org> 0.2.0-alt2
- fixed build with vala >= 0.50.4 (upstream patch)

* Fri Nov 13 2020 Yuri N. Sedunov <aris@altlinux.org> 0.2.0-alt1
- 0.2.0

* Sat Oct 31 2020 Yuri N. Sedunov <aris@altlinux.org> 0.1.0-alt3
- updated to v0.1.0-157-gdba63b1

* Mon Aug 03 2020 Yuri N. Sedunov <aris@altlinux.org> 0.1.0-alt2
- updated to v0.1.0-125-gff9a9a0

* Fri Jan 31 2020 Yuri N. Sedunov <aris@altlinux.org> 0.1.0-alt1
- first build for Sisyphus

