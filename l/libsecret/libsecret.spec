%def_disable snapshot

%define ver_major 0.20
%define api_ver 1

%def_disable static
%def_enable introspection
%def_enable vala
%def_enable gtk_doc
%def_enable man
%def_disable check

Name: libsecret
Version: %ver_major.5
Release: alt1

Summary: A client library for the Secret Service DBus API
Group: System/Libraries
License: LGPL-2.1
Url: https://wiki.gnome.org/Projects/Libsecret

%if_disabled snapshot
Source: ftp://ftp.gnome.org/pub/gnome/sources/%name/%ver_major/%name-%version.tar.xz
%else
Vcs: https://gitlab.gnome.org/GNOME/libsecret.git
Source: %name-%version.tar
%endif
Patch: %name-0.20.0-alt-python3_shebang.patch

%define glib_ver 2.44.0
%define vala_ver 0.17.2.12
%define gcrypt_ver 1.4.5

BuildRequires(pre): meson >= 0.50
BuildRequires(pre): rpm-macros-valgrind
BuildRequires: libgio-devel >= %glib_ver
BuildRequires: libgcrypt-devel >= %gcrypt_ver
BuildRequires: libtpm2-tss-devel
%{?_enable_introspection:BuildRequires: gobject-introspection-devel}
%{?_enable_vala:BuildRequires: vala-tools >= %vala_ver}
%{?_enable_gtk_doc:BuildRequires: gi-docgen}
%{?_enable_man:BuildRequires: xsltproc docbook-style-xsl}
%{?_enable_check:
BuildRequires: /proc fuse-gvfs dbus-tools-gui python3-module-dbus-gobject
BuildRequires: python3-module-pygobject3 python3-module-mock libgjs}

%ifarch %valgrind_arches
BuildRequires: valgrind-devel
%endif

%description
libsecrets is a client for the Secret Service DBus API. The Secret
Service allows storage of passwords in a common way on the desktop.
Supported by gnome-keyring and ksecretservice.

%package devel
Summary: Development files and libraries for %name
Group: Development/C
Requires: %name = %version-%release

%description devel
libsecrets is a client for the Secret Service DBus API. The Secret
Service allows storage of passwords in a common way on the desktop.
Supported by gnome-keyring and ksecretservice.

This package provides files for development with %name.

%package devel-doc
Summary: Development documentaion for %name
Group: Development/C
BuildArch: noarch
Conflicts: %name < %version

%description devel-doc
libsecrets is a client for the Secret Service DBus API. The Secret
Service allows storage of passwords in a common way on the desktop.
Supported by gnome-keyring and ksecretservice.

This package provides development documentations for %name.

%package gir
Summary: GObject introspection data for %name
Group: System/Libraries
Requires: %name = %version-%release

%description gir
GObject introspection data for the %name library.

%package gir-devel
Summary: GObject introspection devel data for %name
Group: System/Libraries
BuildArch: noarch
Requires: %name-gir = %version-%release
Requires: %name-devel = %version-%release

%description gir-devel
GObject introspection devel data for %name.

%prep
%setup
%patch -p1

%build
%meson \
%{?_disable_introspection:-Dintrospection=false} \
%{?_disable_vala:-Dvapi=false} \
%{?_disable_gtk_doc:-Dgtk_doc=false} \
%{?_disable_man:-Dmanpage=false}
%nil
%meson_build

%install
%meson_install
%find_lang %name

%check
export LD_LIBRARY_PATH=%buildroot%_libdir
dbus-run-session %meson_test

%files -f %name.lang
%_bindir/secret-tool
%_libdir/%name-%api_ver.so.*
%{?_enable_man:%_man1dir/secret-tool.1.*}
%doc README* NEWS

%files devel
%_includedir/%name-%api_ver
%_libdir/%name-%api_ver.so
%_pkgconfigdir/%name-%api_ver.pc
%_pkgconfigdir/%name-unstable.pc
%if_enabled vala
%_vapidir/%name-%api_ver.vapi
%_vapidir/%name-%api_ver.deps
%endif

%if_enabled gtk_doc
%files devel-doc
%_datadir/doc/%name-%api_ver
%endif

%if_enabled introspection
%files gir
%_typelibdir/Secret-%api_ver.typelib

%files gir-devel
%_girdir/Secret-%api_ver.gir
%endif


%changelog
* Mon Feb 28 2022 Yuri N. Sedunov <aris@altlinux.org> 0.20.5-alt1
- 0.20.5

* Wed Aug 18 2021 Yuri N. Sedunov <aris@altlinux.org> 0.20.4-alt2
- libsecret/secret-methods.c: applied upstream patch
  "Create default collection after DBus.Error.UnknownObject"
  (ALT #40714)

* Fri Oct 23 2020 Yuri N. Sedunov <aris@altlinux.org> 0.20.4-alt1
- 0.20.4

* Wed Apr 15 2020 Yuri N. Sedunov <aris@altlinux.org> 0.20.3-alt1
- 0.20.3

* Wed Mar 11 2020 Yuri N. Sedunov <aris@altlinux.org> 0.20.2-alt1
- 0.20.2

* Tue Jan 28 2020 Yuri N. Sedunov <aris@altlinux.org> 0.20.1-alt1
- 0.20.1

* Mon Jan 13 2020 Yuri N. Sedunov <aris@altlinux.org> 0.20.0-alt1
- 0.20.0

* Sat Sep 28 2019 Yuri N. Sedunov <aris@altlinux.org> 0.19.1-alt2
- updated to 0.19.1-2-g67680a6 (fixed build w/o valgrind)

* Fri Sep 06 2019 Yuri N. Sedunov <aris@altlinux.org> 0.19.1-alt1
- 0.19.1 (ported to Meson build system)

* Sat Mar 02 2019 Yuri N. Sedunov <aris@altlinux.org> 0.18.8-alt1
- 0.18.8

* Fri Jan 11 2019 Yuri N. Sedunov <aris@altlinux.org> 0.18.7-alt2
- disabled %%check

* Sat Dec 29 2018 Yuri N. Sedunov <aris@altlinux.org> 0.18.7-alt1
- 0.18.7

* Thu Mar 29 2018 Yuri N. Sedunov <aris@altlinux.org> 0.18.6-alt1
- 0.18.6

* Wed Mar 01 2017 Michael Shigorin <mike@altlinux.org> 0.18.5-alt1.1
- BOOTSTRAP: introduce check knob (*off* by default
  as %%check section is apparently disabled by now)

* Fri Mar 25 2016 Yuri N. Sedunov <aris@altlinux.org> 0.18.5-alt1
- 0.18.5

* Tue Jan 19 2016 Yuri N. Sedunov <aris@altlinux.org> 0.18.4-alt1
- 0.18.4

* Mon Aug 03 2015 Yuri N. Sedunov <aris@altlinux.org> 0.18.3-alt1
- 0.18.3

* Tue Apr 14 2015 Yuri N. Sedunov <aris@altlinux.org> 0.18.2-alt1
- 0.18.2

* Fri Oct 17 2014 Yuri N. Sedunov <aris@altlinux.org> 0.18.1-alt1
- after 0.18.1 snapshot (bfe9f3514)

* Fri Mar 07 2014 Yuri N. Sedunov <aris@altlinux.org> 0.18-alt1
- 0.18

* Mon Aug 26 2013 Yuri N. Sedunov <aris@altlinux.org> 0.16-alt1
- 0.16

* Fri Apr 12 2013 Yuri N. Sedunov <aris@altlinux.org> 0.15-alt2
- added vala bindigs to -devel subpackage  (ALT #28841)

* Mon Mar 18 2013 Yuri N. Sedunov <aris@altlinux.org> 0.15-alt1
- 0.15

* Tue Mar 05 2013 Yuri N. Sedunov <aris@altlinux.org> 0.14-alt1
- 0.14

* Sun Feb 17 2013 Yuri N. Sedunov <aris@altlinux.org> 0.13-alt1
- 0.13
- made %%check using xvfb-run

* Tue Oct 16 2012 Yuri N. Sedunov <aris@altlinux.org> 0.11-alt1
- 0.11

* Tue Sep 18 2012 Yuri N. Sedunov <aris@altlinux.org> 0.10-alt1
- 0.10

* Thu Sep 06 2012 Yuri N. Sedunov <aris@altlinux.org> 0.9-alt1
- 0.9

* Mon Jun 25 2012 Yuri N. Sedunov <aris@altlinux.org> 0.3-alt1
- 0.3

* Mon Apr 16 2012 Yuri N. Sedunov <aris@altlinux.org> 0.2-alt1
- 0.2

* Sun Mar 25 2012 Yuri N. Sedunov <aris@altlinux.org> 0.1-alt1
- first build for Sisyphus

