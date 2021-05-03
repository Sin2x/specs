%define api_ver 0
%define xdg_name org.freedesktop.MalcontentControl

%def_enable check
%def_enable ui

Name: malcontent
Version: 0.10.1
Release: alt1

Summary: Parental controls implementation
Group: Security/Networking
License: LGPL-2.1-or-later and GPL-2.0-or-later
Url: https://gitlab.freedesktop.org/pwithnall/malcontent/

Source: %url/-/archive/%version/%name-%version.tar.bz2

Requires: polkit accountsservice

%define glib_ver 2.54.2
%define gtk_ver 3.24
%define accountsservice_ver 0.6.39

BuildRequires(pre): meson rpm-build-python3
BuildRequires: yelp-tools desktop-file-utils libappstream-glib-devel
BuildRequires: pkgconfig(gio-2.0) >= %glib_ver
BuildRequires: pkgconfig(dbus-1)
BuildRequires: pkgconfig(polkit-gobject-1)
BuildRequires: pkgconfig(accountsservice) >= %accountsservice_ver
BuildRequires: pkgconfig(flatpak)
BuildRequires: pkgconfig(gobject-introspection-1.0) gir(AccountsService) = 1.0
BuildRequires: pam-devel
BuildRequires: libglib-testing-devel
%{?_enable_ui:BuildRequires: pkgconfig(gtk+-3.0) >= %gtk_ver gir(Gtk) = 3.0}

%description
%name implements parental controls support which can be used by
applications to filter or limit the access of child accounts to
inappropriate content.

%package -n lib%name
Summary: Libraries for %name
Group: System/Libraries
License: LGPL-2.1-or-later

%description -n lib%name
This package contains libmalcontent.

%package -n lib%name-gir
Summary: GObject introspection data for lib%name
Group: System/Libraries
Requires: lib%name = %EVR

%description -n lib%name-gir
GObject introspection data for the %name library.

%package -n lib%name-devel
Summary: Development files for %name
Group: Development/C
License: LGPL-2.1-or-later
Requires: lib%name = %EVR

%description -n lib%name-devel
This package provides development headers and libraries for %name
library.

%package -n lib%name-ui
Summary: UI library for %name
Group: System/Libraries
License: LGPL-2.1-or-later
Requires: lib%name = %EVR

%description -n lib%name-ui
This package provides shared %name-ui library.

%package -n lib%name-ui-gir
Summary: GObject introspection data for lib%name-ui
Group: System/Libraries
Requires: lib%name-ui = %EVR
Requires: lib%name-gir = %EVR

%description -n lib%name-ui-gir
GObject introspection data for the %name-ui library.

%package -n lib%name-ui-devel
Summary: Development files for lib%name-ui
License: LGPL-2.1-or-later
Group: Development/C
Requires: lib%name-ui = %EVR
Requires: lib%name-devel = %EVR

%description -n lib%name-ui-devel
This package provides development headers and libraries for %name-ui
library.

%package control
Summary: Parental Controls UI
Group: Security/Networking
License: GPL-2.0-or-later
Requires: lib%name-ui = %EVR

%description control
This package contains a user interface for querying and setting parental
controls for users.

%package pam
Summary: Parental Controls PAM Module
Group: System/Base
License: LGPL-2.1-or-later
Requires: lib%name = %EVR

%description pam
This package contains a PAM module which prevents logins for users who
have exceeded their allowed computer time.

%package tools
Summary: Parental Controls Tools
Group: Security/Networking
License: GPL-2.0-or-later
Requires: lib%name = %EVR
Requires: lib%name-gir = %EVR

%description tools
This package contains tools for querying and updating the parental
controls settings for users.

%prep
%setup

%build
%meson -Dpamlibdir=%_pam_modules_dir \
       %{?_disable_ui:-Dui=disabled}
%nil
%meson_build

%install
%meson_install
%find_lang %name --with-gnome

%check
export LD_LIBRARY_PATH=%buildroot%_libdir
%meson_test
%{?_enable_ui:desktop-file-validate %buildroot%_desktopdir/%xdg_name.desktop
appstream-util validate-relax --nonet %buildroot%_datadir/metainfo/%xdg_name.appdata.xml}

%files -f %name.lang
%_datadir/accountsservice/interfaces/*.xml
%_datadir/dbus-1/interfaces/*.xml
%_datadir/polkit-1/actions/*.policy
%_datadir/polkit-1/rules.d/*.rules
%doc README.md NEWS

%files -n lib%name
%_libdir/libmalcontent-%api_ver.so.*

%files -n lib%name-gir
%_typelibdir/Malcontent-%api_ver.typelib

%files -n lib%name-devel
%_includedir/%name-%api_ver/
%_libdir/lib%name-%api_ver.so
%_pkgconfigdir/%name-%api_ver.pc
%_girdir/Malcontent-%api_ver.gir

%if_enabled ui
%files -n lib%name-ui
%_libdir/lib%name-ui-%api_ver.so.*

%files -n lib%name-ui-gir
%_typelibdir/MalcontentUi-%api_ver.typelib

%files -n lib%name-ui-devel
%_libdir/lib%name-ui-%api_ver.so
%_includedir/%name-ui-%api_ver/
%_pkgconfigdir/%name-ui-%api_ver.pc
%_girdir/MalcontentUi-%api_ver.gir

%files control
%_bindir/%name-control
%_desktopdir/%xdg_name.desktop
%_iconsdir/hicolor/scalable/apps/%xdg_name.svg
%_iconsdir/hicolor/symbolic/apps/%xdg_name-symbolic.svg
%_datadir/metainfo/%xdg_name.appdata.xml
%endif

%files pam
%_pam_modules_dir/pam_%{name}.so

%files tools
%_bindir/%name-client
%_man8dir/%name-client.*


%changelog
* Mon May 03 2021 Yuri N. Sedunov <aris@altlinux.org> 0.10.1-alt1
- 0.10.1
- BR: +rpm-build-python3

* Thu Dec 10 2020 Yuri N. Sedunov <aris@altlinux.org> 0.10.0-alt1
- 0.10.0

* Thu Sep 17 2020 Yuri N. Sedunov <aris@altlinux.org> 0.9.0-alt1
- first build for Sisyphus


