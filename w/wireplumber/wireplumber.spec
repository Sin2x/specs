%define _unpackaged_files_terminate_build 1

%def_enable introspection

# These come from meson.build.
%define apiversion 0.4
%define soversion 0

Name: wireplumber
Version: 0.3.60.103.g9609a79903ab
Release: alt1

Summary: a modular session/policy manager for PipeWire

License: MIT
Group: Sound
URL: https://pipewire.pages.freedesktop.org/wireplumber/

BuildRequires(pre): meson
BuildRequires: pkgconfig(gobject-2.0) >= 2.58
BuildRequires: pkgconfig(gmodule-2.0) >= 2.58
BuildRequires: pkgconfig(gio-2.0) >= 2.58
BuildRequires: pkgconfig(gio-unix-2.0) >= 2.58
BuildRequires: pkgconfig(libpipewire-0.3) >= 0.3.23
BuildRequires: liblua5.3-devel
%if_enabled introspection
BuildRequires: gobject-introspection-devel
%endif

Source: %name-%version.tar

%package -n lib%name
Summary: the client library for WirePlumber
Group: System/Libraries

%package -n lib%name-devel
Summary: development files of the client library for WirePlumber
Group: Development/C

%if_enabled introspection
%package -n lib%name-gir
Summary: GObject introspection data for lib%name
Group: System/Libraries
Requires: lib%name = %EVR

%package -n lib%name-gir-devel
Summary: GObject introspection development data for lib%name
Group: Development/Other
Requires: lib%name-gir = %EVR
Requires: lib%name-devel = %EVR

%endif

%description
WirePlumber is a modular session / policy manager for PipeWire and a
GObject-based high-level library that wraps PipeWire's API, providing
convenience for writing the daemon's modules as well as external tools
for managing PipeWire.

%description -n lib%name
WirePlumber is a modular session / policy manager for PipeWire and a
GObject-based high-level library that wraps PipeWire's API, providing
convenience for writing the daemon's modules as well as external tools
for managing PipeWire.

This package contains the client library.

%description -n lib%name-devel
WirePlumber is a modular session / policy manager for PipeWire and a
GObject-based high-level library that wraps PipeWire's API, providing
convenience for writing the daemon's modules as well as external tools
for managing PipeWire.

This package contains the development files for the client library.

%if_enabled introspection
%description -n lib%name-gir
WirePlumber is a modular session / policy manager for PipeWire and a
GObject-based high-level library that wraps PipeWire's API, providing
convenience for writing the daemon's modules as well as external tools
for managing PipeWire.

This package contains GObject introspection data for lib%name.

%description -n lib%name-gir-devel
WirePlumber is a modular session / policy manager for PipeWire and a
GObject-based high-level library that wraps PipeWire's API, providing
convenience for writing the daemon's modules as well as external tools
for managing PipeWire.

This package contains GObject introspection development data for lib%name.

%endif

%prep
%setup

%build
%meson \
    -Dsystem-lua=true \
    #

%meson_build

%install
%meson_install

%files
%doc NEWS.md README.md
%_sysconfdir/wireplumber
%_bindir/wireplumber
%_bindir/wpctl
%_datadir/wireplumber

%files -n lib%name
%_libdir/libwireplumber-%apiversion.so.%soversion.*
%_libdir/libwireplumber-%apiversion.so.%soversion
# plugins
%_libdir/wireplumber-%apiversion

%files -n lib%name-devel
%_pkgconfigdir/wireplumber-%apiversion.pc
%_libdir/libwireplumber-%apiversion.so
%_includedir/wireplumber-%apiversion

%if_enabled introspection
%files -n lib%name-gir
%_typelibdir/Wp-%apiversion.typelib

%files -n lib%name-gir-devel
%_girdir/Wp-%apiversion.gir
%endif

%changelog
* Thu Mar 18 2021 Arseny Maslennikov <arseny@altlinux.org> 0.3.60.103.g9609a79903ab-alt1
- 0.3.60.63.g24a260030bab -> 0.3.60.103.g9609a79903ab.

* Sun Feb 21 2021 Arseny Maslennikov <arseny@altlinux.org> 0.3.60.63.g24a260030bab-alt1
- Initial build for ALT Sisyphus.
