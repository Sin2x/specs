%def_disable snapshot

%define _name vte
%define ver_major 0.58
%define api_ver 2.91

Name: %{_name}3
Version: %ver_major.0
Release: alt1

%def_disable static
%def_enable introspection
%def_enable gtk_doc
%def_enable check

Summary: Terminal emulator widget for use with GTK+
License: LGPL
Group: Terminals
Url: http://www.gnome.org/

Requires: lib%name = %version-%release

%if_disabled snapshot
Source: ftp://ftp.gnome.org/pub/gnome/sources/%_name/%ver_major/%_name-%version.tar.xz
%else
Source: %_name-%version.tar
%endif

%define gtk3_ver 3.8.0
%define glib_ver 2.40.0
%define pango_ver 1.22
%define gir_ver 0.10.2
%define tls_ver 3.2.7

BuildRequires(pre): meson
BuildRequires: gcc-c++ gperf
BuildRequires: libncurses-devel libcairo-devel
BuildRequires: gtk-doc >= 1.1.0
BuildRequires: libgio-devel >= %glib_ver
BuildRequires: libgtk+3-devel >= %gtk3_ver
BuildRequires: libpango-devel >= %pango_ver
BuildRequires: libgnutls-devel >= %tls_ver
BuildRequires: libfribidi-devel
BuildRequires: libpcre2-devel
BuildRequires: vala-tools libvala-devel

%{?_enable_glade:BuildRequires: libgladeui2.0-devel}
%{?_enable_introspection:BuildRequires: gobject-introspection-devel >= %gir_ver libgtk+3-gir-devel}

%description
VTE is a terminal emulator widget for use with GTK+

%package utils
Summary: VTE utilities and test programs
Group: Terminals
Requires: lib%name = %version-%release

%description utils
Utilities, samples and test programs distributed with VTE, a terminal
emulator widget for use with GTK+3.

%package -n lib%name
Summary: Terminal emulator widget library for use with GTK+3
Group: System/Libraries

%description -n lib%name
VTE is a terminal emulator widget for use with GTK+3.
This package contains the VTE shared libraries.

%package -n lib%name-devel
Summary: Development files for VTE
Group: Development/C
Requires: lib%name = %version-%release

%description -n lib%name-devel
VTE is a terminal emulator widget for use with GTK+3. This package
contains the files needed for building applications using VTE.

%package -n lib%name-devel-doc
Summary: Development documentation for VTE
Group: Development/Documentation
BuildArch: noarch
Conflicts: lib%name-devel < %version

%description -n lib%name-devel-doc
API documentation for the VTE library.
VTE is a terminal emulator widget for use with GTK+3.

%if_enabled static
%package -n lib%name-devel-static
Summary: Static libraries for VTE
Group: Development/C
Requires: lib%name-devel = %version-%release

%description -n lib%name-devel-static
VTE is a terminal emulator widget for use with GTK+3. This package
contains the libraries needed for building applications statically
linked with VTE.
%endif	# enabled static

%package -n lib%name-gir
Summary: GObject introspection data for the %name library
Group: System/Libraries
Requires: lib%name = %version-%release

%description -n lib%name-gir
GObject introspection data for the %name library

%package -n lib%name-gir-devel
Summary: GObject introspection devel data for the %name
Group: System/Libraries
BuildArch: noarch
Requires: lib%name-gir = %version-%release
Requires: lib%name-devel = %version-%release

%description -n lib%name-gir-devel
GObject introspection devel data for the %name library


%define pkgdocdir %_docdir/%name-%version

%prep
%setup -n %_name-%version

%build
%meson \
	%{?_disable introspection:-Dgir=false} \
	%{?_enable_gtk_doc:-Ddocs=true}
%meson_build

%install
%meson_install
# fix permissions
chmod 755 %buildroot%_sysconfdir/profile.d/vte.sh

install -d -m755 %buildroot%pkgdocdir
install -p -m644 AUTHORS NEWS README.md %buildroot%pkgdocdir/
install -p -m644 doc/*.txt %buildroot%pkgdocdir/

# Remove unpackaged files
find %buildroot -type f -name '*.la' -delete

%find_lang %_name-%api_ver --output=%name.lang

%check
LD_LIBRARY_PATH=%buildroot%_libdir
%meson_test

%files
%_bindir/*

%files -n lib%name -f %name.lang
%dir %pkgdocdir
%pkgdocdir/AUTHORS
%pkgdocdir/NEWS
%pkgdocdir/README.md
%_libdir/*.so.*
%_sysconfdir/profile.d/vte.sh

%files -n lib%name-devel
%pkgdocdir/*.txt
%_includedir/*
%_libdir/*.so
%_pkgconfigdir/%_name-%api_ver.pc
%_vapidir/vte-%api_ver.*
%if_enabled glade
%_datadir/glade/catalogs/vte-%api_ver.xml
%_datadir/glade/pixmaps/hicolor/*x*/actions/widget-vte-terminal.png
%endif

%files -n lib%name-devel-doc
%doc %_datadir/gtk-doc/html/*

%if_enabled static
%files -n lib%name-devel-static
%_libdir/*.a
%endif	# enabled static

%if_enabled introspection
%files -n lib%name-gir
%_typelibdir/Vte-%api_ver.typelib

%files -n lib%name-gir-devel
%_girdir/Vte-%api_ver.gir
%endif

%changelog
* Mon Sep 09 2019 Yuri N. Sedunov <aris@altlinux.org> 0.58.0-alt1
- 0.58.0

* Tue May 07 2019 Yuri N. Sedunov <aris@altlinux.org> 0.56.3-alt1
- 0.56.3

* Wed Apr 24 2019 Yuri N. Sedunov <aris@altlinux.org> 0.56.2-alt1
- 0.56.2

* Tue Apr 09 2019 Yuri N. Sedunov <aris@altlinux.org> 0.56.1-alt1
- 0.56.1

* Tue Mar 12 2019 Yuri N. Sedunov <aris@altlinux.org> 0.56.0-alt1
- 0.56.0

* Wed Dec 19 2018 Yuri N. Sedunov <aris@altlinux.org> 0.54.3-alt1
- 0.54.3

* Mon Oct 22 2018 Yuri N. Sedunov <aris@altlinux.org> 0.54.2-alt1
- 0.54.2

* Tue Sep 25 2018 Yuri N. Sedunov <aris@altlinux.org> 0.54.1-alt1
- 0.54.1

* Wed Sep 19 2018 Yuri N. Sedunov <aris@altlinux.org> 0.54.0-alt2
- rebuild with atk-2.30.0

* Sun Sep 02 2018 Yuri N. Sedunov <aris@altlinux.org> 0.54.0-alt1
- updated to 0.54.0-9-g8f4e3c19

* Mon May 21 2018 Yuri N. Sedunov <aris@altlinux.org> 0.52.2-alt1
- 0.52.2

* Mon Apr 09 2018 Yuri N. Sedunov <aris@altlinux.org> 0.52.1-alt1
- 0.52.1

* Sun Mar 18 2018 Yuri N. Sedunov <aris@altlinux.org> 0.52.0-alt1.1
- added Url tag

* Tue Mar 13 2018 Yuri N. Sedunov <aris@altlinux.org> 0.52.0-alt1
- 0.52.0

* Tue Oct 31 2017 Yuri N. Sedunov <aris@altlinux.org> 0.50.2-alt1
- 0.50.2

* Mon Oct 02 2017 Yuri N. Sedunov <aris@altlinux.org> 0.50.1-alt1
- 0.50.1

* Mon Sep 11 2017 Yuri N. Sedunov <aris@altlinux.org> 0.50.0-alt1
- 0.50.0

* Wed May 10 2017 Yuri N. Sedunov <aris@altlinux.org> 0.48.3-alt1
- 0.48.3

* Mon Apr 10 2017 Yuri N. Sedunov <aris@altlinux.org> 0.48.2-alt1
- 0.48.2

* Wed Mar 22 2017 Yuri N. Sedunov <aris@altlinux.org> 0.48.1-alt1
- 0.48.1

* Mon Nov 07 2016 Yuri N. Sedunov <aris@altlinux.org> 0.46.1-alt1
- 0.46.1

* Mon Sep 19 2016 Yuri N. Sedunov <aris@altlinux.org> 0.46.0-alt1
- 0.46.0

* Mon May 09 2016 Yuri N. Sedunov <aris@altlinux.org> 0.44.2-alt1
- 0.44.2

* Mon Apr 11 2016 Yuri N. Sedunov <aris@altlinux.org> 0.44.1-alt1
- 0.44.1

* Sat Mar 19 2016 Yuri N. Sedunov <aris@altlinux.org> 0.44.0-alt1
- 0.44.0

* Tue Mar 15 2016 Yuri N. Sedunov <aris@altlinux.org> 0.42.5-alt1
- 0.42.5

* Thu Feb 11 2016 Yuri N. Sedunov <aris@altlinux.org> 0.42.4-alt1
- 0.42.4

* Thu Jan 28 2016 Yuri N. Sedunov <aris@altlinux.org> 0.42.3-alt1
- 0.42.3

* Thu Jan 28 2016 Yuri N. Sedunov <aris@altlinux.org> 0.42.1-alt3
- fised permissions for %%_sysconfdir/profile.d/vte.sh

* Wed Dec 09 2015 Yuri N. Sedunov <aris@altlinux.org> 0.42.1-alt2
- rebuilt against libgnutls.so.30

* Mon Oct 12 2015 Yuri N. Sedunov <aris@altlinux.org> 0.42.1-alt1
- 0.42.1

* Mon Sep 21 2015 Yuri N. Sedunov <aris@altlinux.org> 0.42.0-alt1
- 0.42.0

* Mon May 11 2015 Yuri N. Sedunov <aris@altlinux.org> 0.40.2-alt1
- 0.40.2

* Wed Mar 25 2015 Yuri N. Sedunov <aris@altlinux.org> 0.40.0-alt1
- 0.40.0

* Tue Dec 16 2014 Yuri N. Sedunov <aris@altlinux.org> 0.38.3-alt1
- 0.38.3

* Mon Nov 10 2014 Yuri N. Sedunov <aris@altlinux.org> 0.38.2-alt1
- 0.38.2

* Tue Oct 14 2014 Yuri N. Sedunov <aris@altlinux.org> 0.38.1-alt1
- 0.38.1

* Sun Sep 14 2014 Yuri N. Sedunov <aris@altlinux.org> 0.38.0-alt1
- 0.38.0

* Fri Jun 27 2014 Yuri N. Sedunov <aris@altlinux.org> 0.36.3-alt1
- 0.36.3

* Tue May 13 2014 Yuri N. Sedunov <aris@altlinux.org> 0.36.2-alt1
- 0.36.2

* Sat Apr 26 2014 Yuri N. Sedunov <aris@altlinux.org> 0.36.1-alt1
- 0.36.1

* Mon Mar 24 2014 Yuri N. Sedunov <aris@altlinux.org> 0.36.0-alt1
- 0.36.0

* Tue Mar 18 2014 Yuri N. Sedunov <aris@altlinux.org> 0.35.90-alt1
- 0.35.90

* Tue Oct 15 2013 Yuri N. Sedunov <aris@altlinux.org> 0.34.9-alt1
- 0.34.9

* Tue Sep 17 2013 Yuri N. Sedunov <aris@altlinux.org> 0.34.8-alt1
- 0.34.8

* Sun Jul 07 2013 Yuri N. Sedunov <aris@altlinux.org> 0.34.7-alt1
- 0.34.7

* Mon Jun 10 2013 Yuri N. Sedunov <aris@altlinux.org> 0.34.6-alt1
- 0.34.6

* Mon May 13 2013 Yuri N. Sedunov <aris@altlinux.org> 0.34.5-alt1
- 0.34.5

* Mon Apr 15 2013 Yuri N. Sedunov <aris@altlinux.org> 0.34.4-alt1
- 0.34.4

* Tue Mar 26 2013 Yuri N. Sedunov <aris@altlinux.org> 0.34.3-alt1
- 0.34.3

* Tue Nov 13 2012 Yuri N. Sedunov <aris@altlinux.org> 0.34.2-alt1
- 0.34.2

* Tue Oct 16 2012 Yuri N. Sedunov <aris@altlinux.org> 0.34.1-alt1
- 0.34.1

* Mon Sep 17 2012 Yuri N. Sedunov <aris@altlinux.org> 0.34.0-alt1
- 0.34.0

* Thu Sep 06 2012 Yuri N. Sedunov <aris@altlinux.org> 0.33.90-alt1
- 0.33.90

* Wed May 30 2012 Yuri N. Sedunov <aris@altlinux.org> 0.32.2-alt1
- 0.32.2

* Mon Apr 16 2012 Yuri N. Sedunov <aris@altlinux.org> 0.32.1-alt1
- 0.32.1

* Mon Mar 19 2012 Yuri N. Sedunov <aris@altlinux.org> 0.32.0-alt1
- 0.32.0

* Wed Nov 23 2011 Yuri N. Sedunov <aris@altlinux.org> 0.30.1-alt2
- applied patch proposed in
  http://bugzilla-attachments.gnome.org/attachment.cgi?id=201649
  (ALT #26611)

* Mon Oct 17 2011 Yuri N. Sedunov <aris@altlinux.org> 0.30.1-alt1
- 0.30.1

* Mon Sep 26 2011 Yuri N. Sedunov <aris@altlinux.org> 0.30.0-alt1
- 0.30.0

* Mon Aug 29 2011 Yuri N. Sedunov <aris@altlinux.org> 0.28.2-alt1
- 0.28.2

* Wed Jun 15 2011 Yuri N. Sedunov <aris@altlinux.org> 0.28.1-alt1
- 0.28.1

* Mon Apr 04 2011 Yuri N. Sedunov <aris@altlinux.org> 0.28.0-alt1
- 2.28.0

* Thu Feb 24 2011 Yuri N. Sedunov <aris@altlinux.org> 0.27.90-alt1
- first build for Sisyphus.

