%define ver_major 4.8
%define _name cjs
%define api_ver 1.0

%def_disable check

Name: lib%_name
Version: %ver_major.0
Release: alt1

Summary: Javascript Bindings for Cinnamon
Group: System/Libraries
# The following files contain code from Mozilla which
# is triple licensed under MPL1.1/LGPLv2+/GPLv2+:
# The console module (modules/console.c)
# Stack printer (cjs/stack.c)
License: MIT and (MPL-1.1 or GPLv2+ or LGPLv2+)
Url: https://github.com/linuxmint/cjs

Source: %_name-%version.tar

%define glib_ver 2.33.14
%define gi_ver 1.33.14

BuildRequires: gcc-c++ libcairo-devel
BuildRequires: glib2-devel >= %glib_ver gobject-introspection-devel >= %gi_ver
BuildRequires: libdbus-glib-devel libreadline-devel libcairo-gobject-devel
BuildRequires: gnome-common
BuildRequires: libmozjs78-devel
BuildRequires: meson
BuildRequires: pkgconfig(sysprof-capture-4) valgrind
%{?_enable_check:BuildRequires: /proc xvfb-run dbus-tools dbus-tools-gui
BuildRequires: typelib(Clutter) typelib(Gtk) = 3.0}

# for check
BuildRequires: /proc dbus-tools-gui

%description
Cjs allows using GNOME/Cinnamon libraries from Javascript. It's based on the
Spidermonkey Javascript engine from Mozilla and the GObject introspection
framework.

%package devel
Summary: Development package for %name
Group: Development/C
Requires: %name = %version-%release

%description devel
Files for development with %name.

%set_typelibdir %_libdir/%_name/girepository-1.0


%prep
%setup -q -n %_name-%version

%build
%meson -Dinstalled-tests=false
%meson_build

%install
%meson_install

%check
export LD_LIBRARY_PATH=%buildroot%_libdir
xvfb-run %meson_test

%files
%_bindir/%_name
%_bindir/%_name-console
%_libdir/*.so.*
%dir %_datadir/cjs-1.0
%dir %_libdir/%_name/
%dir %_libdir/%_name/girepository-1.0
%_libdir/%_name/girepository-1.0/CjsPrivate-%api_ver.typelib
%exclude %_libexecdir/installed-tests/%_name
%exclude %_datadir/installed-tests/%_name/
%exclude %_datadir/glib-2.0/schemas/org.cinnamon.CjsTest.gschema.xml
%doc COPYING NEWS README

%files devel
%_includedir/%_name-%api_ver/
%_libdir/*.so
%_libdir/pkgconfig/%_name-%api_ver.pc
%_datadir/cjs-1.0/lsan
%_datadir/cjs-1.0/valgrind

%doc examples/*

%changelog
* Fri Nov 27 2020 Vladimir Didenko <cow@altlinux.org> 4.8.0-alt1
- 4.8.0

* Thu May 14 2020 Vladimir Didenko <cow@altlinux.org> 4.6.0-alt1
- 4.6.0

* Wed Nov 20 2019 Vladimir Didenko <cow@altlinux.org> 4.4.0-alt1
- 4.4.0

* Tue Jun 25 2019 Vladimir Didenko <cow@altlinux.org> 4.2.0-alt1
- 4.2.0

* Mon Feb 11 2019 Vladimir Didenko <cow@altlinux.org> 4.0.0-alt2
- fix build with new autoconf-archive

* Wed Oct 31 2018 Vladimir Didenko <cow@altlinux.org> 4.0.0-alt1
- 4.0.0

* Thu May 3 2018 Vladimir Didenko <cow@altlinux.org> 3.8.0-alt1
- 3.8.0

* Wed Nov 22 2017 Vladimir Didenko <cow@altlinux.org> 3.6.1-alt1
- 3.6.1

* Fri Oct 27 2017 Vladimir Didenko <cow@altlinux.org> 3.6.0-alt1
- 3.6.0

* Wed Aug 23 2017 Vladimir Didenko <cow@altlinux.org> 3.4.4-alt1
- 3.4.4

* Fri Jul 7 2017 Vladimir Didenko <cow@altlinux.org> 3.4.3-alt1
- 3.4.3

* Thu Jun 29 2017 Vladimir Didenko <cow@altlinux.org> 3.4.2-alt1
- 3.4.2-2-g10805ea

* Mon Jun 5 2017 Vladimir Didenko <cow@altlinux.org> 3.4.1-alt1
- 3.4.1-1-gc7cb693

* Thu May 4 2017 Vladimir Didenko <cow@altlinux.org> 3.4.0-alt1
- 3.4.0

* Fri Nov 11 2016 Vladimir Didenko <cow@altlinux.org> 3.2.0-alt1
- 3.2.0

* Thu May 12 2016 Vladimir Didenko <cow@altlinux.org> 3.0.1-alt1
- 3.0.1

* Mon Apr 25 2016 Vladimir Didenko <cow@altlinux.org> 3.0.0-alt1
- 3.0.0

* Mon Oct 19 2015 Vladimir Didenko <cow@altlinux.org> 2.8.0-alt1
- 2.8.0

* Tue Jun 23 2015 Vladimir Didenko <cow@altlinux.org> 2.6.2-alt1
- 2.6.2

* Tue May 19 2015 Vladimir Didenko <cow@altlinux.org> 2.6.0-alt1
- 2.6.0

* Tue Apr 14 2015 Vladimir Didenko <cow@altlinux.org> 2.5.0-alt1
- 2.5.0

* Fri Oct 31 2014 Vladimir Didenko <cow@altlinux.org> 2.4.0-alt1
- 2.4.0

* Mon Apr 14 2014 Vladimir Didenko <cow@altlinux.org> 2.3.1-alt1
- git 20141014

* Mon Apr 14 2014 Vladimir Didenko <cow@altlinux.org> 2.2.0-alt1
- 2.2.0

* Mon Apr 7 2014 Vladimir Didenko <cow@altlinux.org> 2.0.0-alt2
- git20140405

* Thu Oct 10 2013 Vladimir Didenko <cow@altlinux.org> 2.0.0-alt1
- 2.0.0

* Wed Sep 25 2013 Yuri N. Sedunov <aris@altlinux.org> 0.0.1-alt2
- rebuild for GNOME-3.10

* Wed Jul 31 2013 Vladimir Didenko <cow@altlinux.org> 0.0.1-alt1
- Initial build - git20130721
