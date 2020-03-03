%define ver_major 0.7
%def_enable introspection
%def_enable gtk_doc
%def_enable docbook_docs
%def_enable check
%def_enable man

Name: libnotify
Version: %ver_major.9
Release: alt1

Summary: Desktop notification library
Group: System/Libraries
License: LGPL-2.1-or-later
Url: http://www.gnome.org

# https://gitlab.gnome.org/GNOME/libnotify.git
Source: %name-%version.tar
Patch: %name-%version-%release.patch

Provides: %{name}4 = %version-%release
Obsoletes: %{name}4

BuildRequires(pre): meson
BuildRequires: libgio-devel
%{?_enable_gtk_doc:BuildRequires: gtk-doc}
%{?_enable_docbook_docs:BuildRequires: xmlto}
%{?_enable_check:BuildRequires: libgtk+3-devel}
%{?_enable_introspection:BuildRequires: gobject-introspection-devel libgdk-pixbuf-gir-devel}
%{?_enable_man:BuildRequires: xsltproc docbook5-style-xsl}

%description
The library that allows applications post notifications on the desktop
in accordance to the proposed Desktop Notification Specification.

%package devel
Summary: Development files for %name
Group: Development/C
Requires: %name = %version-%release
Provides: %{name}4-devel = %version-%release
Obsoletes: %{name}4-devel

%description devel
Files needed to develop applications that use libnotify, a desktop
notification library.

%package devel-doc
Summary: Development documentation for %name
Group: Development/Documentation
BuildArch: noarch
Conflicts: %name-devel < %version
Provides: %{name}4-devel-doc = %version-%release
Obsoletes: %{name}4-devel-doc

%description devel-doc
API documentation for %name in gtk-doc format.

%package gir
Summary: GObject introspection data for libnotify
Group: System/Libraries
Requires: %name = %version-%release
Provides: %{name}4-gir = %version-%release
Obsoletes: %{name}4-gir

%description gir
GObject introspection data for the desktop notification library.

%package gir-devel
Summary: GObject introspection devel data for libnotify
Group: Development/Other
BuildArch: noarch
Requires: %name-devel = %version-%release
Requires: %name-gir = %version-%release
Provides: %{name}4-gir-devel = %version-%release
Obsoletes: %{name}4-gir-devel

%description gir-devel
GObject introspection devel data for the desktop notification library.

%package -n notify-send
Summary: A program to send desktop notifications
Group: Graphical desktop/GNOME
Requires: %name = %version-%release

%description -n notify-send
notify-send sends desktop notifications via a notification daemon from
the command line.

%prep
%setup
%patch -p1

%build
%meson \
	%{?_disable_gtk_doc:-Dgtk_doc=false} \
	%{?_disable_docbook_docs:-Ddocbook_docs=false} \
	%{?_disable_introspection:-Dintrospection=disabled} \
	%{?_disable_check:-Dtests=false} \
	%{?_disable_man:-Dman=false}
%meson_build

%install
%meson_install

%check
%meson_test

%files
%_libdir/*.so.*
%doc NEWS

%files -n notify-send
%_bindir/notify-send
%{?_enable_man:%_man1dir/notify-send.1.*}

%files devel
%_libdir/*.so
%_includedir/*
%_pkgconfigdir/*.pc
%doc NEWS %{?_enable_docbook_docs:%__builddir/docs/notification-spec.html}

%if_enabled gtk_doc
%files devel-doc
%_datadir/gtk-doc/html/*
%endif

%if_enabled introspection
%files gir
%_typelibdir/Notify-%ver_major.typelib

%files gir-devel
%_girdir/Notify-%ver_major.gir
%endif

%{?_enable_docbook_docs:%exclude %_datadir/doc/%name/}

%changelog
* Tue Mar 03 2020 Yuri N. Sedunov <aris@altlinux.org> 0.7.9-alt1
- 0.7.9

* Fri Apr 05 2019 Yuri N. Sedunov <aris@altlinux.org> 0.7.8-alt1
- 0.7.8 (ported to Meson build system)

* Sun May 06 2018 Michael Shigorin <mike@altlinux.org> 0.7.7-alt1.2
- rebuilt for e2kv4
- updated Url:

* Mon Jan 16 2017 Michael Shigorin <mike@altlinux.org> 0.7.7-alt1.1
- moved BR: libgtk+3 under check knob

* Fri Oct 14 2016 Yuri N. Sedunov <aris@altlinux.org> 0.7.7-alt1
- 0.7.7

* Tue Sep 03 2013 Alexey Shabalin <shaba@altlinux.ru> 0.7.6-alt1
- 0.7.6

* Fri Apr 06 2012 Alexey Shabalin <shaba@altlinux.ru> 0.7.5-alt1
- 0.7.5

* Thu Oct 13 2011 Alexey Shabalin <shaba@altlinux.ru> 0.7.4-alt1
- 0.7.4

* Mon May 30 2011 Alexey Shabalin <shaba@altlinux.ru> 0.7.3-alt2
- 0.7.3

* Fri Mar 18 2011 Alexey Tourbin <at@altlinux.ru> 0.6.0-alt3
- libnotify.pc: moved libnotify deps from Requires to Requires.private

* Sun Mar 13 2011 Valery Inozemtsev <shrek@altlinux.ru> 0.6.0-alt2
- rebuild for debuginfo

* Thu Nov 11 2010 Valery Inozemtsev <shrek@altlinux.ru> 0.6.0-alt1
- 0.6.0

* Tue Nov 09 2010 Victor Forsiuk <force@altlinux.org> 0.4.5-alt2
- Rebuilt for soname set-versions.

* Wed Nov 26 2008 Victor Forsyuk <force@altlinux.org> 0.4.5-alt1
- 0.4.5

* Thu Mar 22 2007 Victor Forsyuk <force@altlinux.org> 0.4.4-alt1
- 0.4.4

* Tue Jan 09 2007 Victor Forsyuk <force@altlinux.org> 0.4.3-alt1
- 0.4.3

* Tue Sep 26 2006 Mikhail Zabaluev <mhz@altlinux.ru> 0.4.2-alt1
- Rebuilt with GTK+ 0.10 to enable necessary functions
- Added libnotify-devel-doc package
- Buildreq

* Thu Jul 06 2006 Mikhail Zabaluev <mhz@altlinux.ru> 0.4.2-alt0.1
- Updated to 0.4.2
- Polished descriptions
- Spec cleanup

* Thu May 04 2006 Vital Khilko <vk@altlinux.ru> 0.4.0-alt1
- 0.4.0

* Thu Feb 02 2006 Vital Khilko <vk@altlinux.ru> 0.3.2-alt1
- 0.3.2

* Sun Sep 17 2005 Vital Khilko <vk@altlinux.ru> 0.2.1-alt1
- initial build for ALT Linux Sisyphus

* Sun Sep 17 2005 Vital Khilko <vk@altlinux.ru> 0.2.1-alt1
- initial build for ALT Linux Sisyphus
