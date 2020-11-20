%def_disable snapshot
%define _libexecdir %prefix/libexec
%define ver_major 1.0
%define api_ver 1.0

%def_enable gtk_doc

Name: gsound
Version: %ver_major.2
Release: alt2

Summary: GSound is a small library for playing system sounds
Group: Sound
License: LGPL-2.1-or-later
Url: https://wiki.gnome.org/Projects/GSound

%if_disabled snapshot
Source: ftp://ftp.gnome.org/pub/gnome/sources/%name/%ver_major/%name-%version.tar.xz
%else
Source: %name-%version.tar
%endif
Patch: %name-1.0.2-alt-tools_makefile.patch

Requires: lib%name = %version-%release

%define glib_ver 2.36.0
%define gtk_doc_ver 1.20

BuildRequires(pre): rpm-build-gir rpm-build-vala
BuildRequires: autoconf-archive
BuildRequires: libgio-devel >= %glib_ver
BuildRequires: libcanberra-devel gobject-introspection-devel gtk-doc >= %gtk_doc_ver
BuildRequires: vala-tools libcanberra-vala

%description
GSound is a small library for playing system sounds. It's designed to be
used via GObject Introspection, and is a thin wrapper around the
libcanberra library.

%package -n lib%name
Summary: GSound library
Group: System/Libraries

%description -n lib%name
GSound is a small library for playing system sounds. It's designed to be
used via GObject Introspection, and is a thin wrapper around the
libcanberra library.

This package contains GSound shared library.

%package -n lib%name-devel
Summary: Development files for GSound
Group: Development/C
Requires: lib%name = %version-%release

%description -n lib%name-devel
The lib%name-devel package contains libraries and headers files for
developing applications that use GSound library.

%package -n lib%name-devel-doc
Summary: GSound development documentation
Group: Development/Documentation
BuildArch: noarch
Conflicts: lib%name-devel < %version

%description -n lib%name-devel-doc
This package contains documentation necessary to develop applications
that use GSound library.

%package -n lib%name-gir
Summary: GObject introspection data for the GSound
Group: System/Libraries
Requires: lib%name = %version-%release

%description -n lib%name-gir
GObject introspection data for the GSound library.

%package -n lib%name-gir-devel
Summary: GObject introspection devel data for the GSound
Group: Development/Other
BuildArch: noarch
Requires: lib%name-gir = %version-%release
Requires: lib%name-devel = %version-%release

%description -n lib%name-gir-devel
GObject introspection devel data for the GSound library.

%prep
%setup
%patch
%ifarch %e2k
# unsupported as of lcc 1.23.20
sed -i 's,--warn-all,-Wall,;s,--warn-error,-Werror,' m4/ax_compiler_flags_gir.m4
%endif

%build
%autoreconf
%configure --disable-static \
    %{?_enable_gtk_doc:--enable-gtk-doc}
%nil
%make_build

%install
%makeinstall_std

%find_lang %name

%files -f %name.lang
%_bindir/%name-play
%doc NEWS README

%files -n lib%name
%_libdir/lib%name.so.*

%files -n lib%name-devel
%_includedir/*.h
%_libdir/lib%name.so
%_pkgconfigdir/%name.pc
%_vapidir/%name.deps
%_vapidir/%name.vapi

%if_enabled gtk_doc
%files -n lib%name-devel-doc
%_datadir/gtk-doc/html/%name/
%endif

%files -n lib%name-gir
%_typelibdir/GSound-%api_ver.typelib

%files -n lib%name-gir-devel
%_girdir/GSound-%api_ver.gir

%changelog
* Fri Nov 20 2020 Yuri N. Sedunov <aris@altlinux.org> 1.0.2-alt2
- updated to 1.0.2-4-g7f42599 (gsound-play: fixed setlocale call)
- fixed build with automake-1.16.3, updated BRs

* Sat Oct 05 2019 Michael Shigorin <mike@altlinux.org> 1.0.2-alt1.1
- E2K: avoid lcc-unsupported options

* Sun Nov 01 2015 Yuri N. Sedunov <aris@altlinux.org> 1.0.2-alt1
- 1.0.2

* Mon Dec 01 2014 Yuri N. Sedunov <aris@altlinux.org> 1.0.1-alt1
- 1.0.1

* Wed Nov 26 2014 Yuri N. Sedunov <aris@altlinux.org> 1.0.0-alt1
- first build for Sisyphus

