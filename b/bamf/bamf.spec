%define _libexecdir %_prefix/libexec
%define ver_major 0.5
%def_enable check

Name: bamf
Version: %ver_major.4
Release: alt1

Summary: BAMF Application Matching Framework
License: GPLv3/LGPLv3
Group: Graphical desktop/Other
Url: https://launchpad.net/bamf

Source: https://launchpad.net/%name/%ver_major/%version/+download/%name-%version.tar.gz

# Debian
Patch10: 1001_remove-former-mono-macros.patch
Patch11: 1002_spelling-fix.patch
Patch12: 1003_add-compile-warning-flags.patch
Patch13: 1004_py2to3_gtester2xunit.patch

BuildRequires: libgtk+3-devel gtk-doc gnome-common
BuildRequires: libdbus-glib-devel libwnck3-devel libgtop-devel
BuildRequires: gobject-introspection-devel vala-tools
BuildRequires: python3-module-lxml
BuildRequires: xvfb-run dbus-tools-gui
BuildRequires: libstartup-notification-devel systemd-devel

%description
BAMF Application Matching Framework.

%package -n bamfdaemon
Summary: Window matching library - daemon
Group: Graphical desktop/Other

%description -n bamfdaemon
bamf matches application windows to desktop files.

This package contains the daemon used by the library and a gio
module that facilitates the matching of applications started
through GDesktopAppInfo

%package -n libbamf3
Summary: Window matching library - shared library
Group: System/Libraries
Obsoletes: libbamf3-0
Provides: libbamf3-0 = %version-%release

%description -n libbamf3
bamf matches application windows to desktop files.

This package contains shared libraries to be used by applications.

%package -n libbamf3-devel
Summary: Window matching library - development files
Group: Development/C
Requires: libbamf3 = %version-%release

%description -n libbamf3-devel
bamf matches application windows to desktop files.

This package contains files that are needed to build applications.

%package -n libbamf3-devel-doc
Summary: Window matching library - documentation
Group: Development/Documentation
BuildArch: noarch
Conflicts: libbamf3-devel < %version

%description -n libbamf3-devel-doc
bamf matches application windows to desktop files.

This package contains the daemon used by the library and a gio
module that facilitates the matching of applications started
through GDesktopAppInfo.

This package contains the documentation.

%package -n libbamf3-vala
Summary: Vala language bindings for bamf3 library
Group: Development/Other
BuildArch: noarch
Requires: libbamf3 = %version-%release

%description -n libbamf3-vala
This package provides Vala language bindings for bamf3 library.

%package -n libbamf3-gir
Summary: GObject introspection data for bamf3 library
Group: System/Libraries
Requires: libbamf3 = %version-%release

%description -n libbamf3-gir
GObject introspection data for bamf3 library.

%package -n libbamf3-gir-devel
Summary: GObject introspection devel data for bamf3 library.
Group: System/Libraries
BuildArch: noarch
Requires: libbamf3-gir = %version-%release
Requires: libbamf3-devel = %version-%release

%description -n libbamf3-gir-devel
GObject introspection devel data for bamf3 library.


%prep
%setup
%patch10 -p1
%patch11 -p1
%patch12 -p1
%patch13 -p1

%build
export PYTHON=%__python3
%autoreconf
%configure \
  --enable-headless-tests
%make_build V=1

%install
%makeinstall_std

%check
%make check

%files -n bamfdaemon
%_libexecdir/bamf/bamfdaemon
%_datadir/dbus-1/services/org.ayatana.bamf.service
%_prefix/lib/systemd/user/bamfdaemon.service

# upstart stuff
%exclude %_libexecdir/bamf/bamfdaemon-dbus-runner
%exclude %_datadir/upstart/sessions/bamfdaemon.conf

%files -n libbamf3
%_libdir/libbamf3.so.*

%files -n libbamf3-devel
%_includedir/libbamf3/
%_libdir/libbamf3.so
%_pkgconfigdir/libbamf3.pc

%files -n libbamf3-devel-doc
%_datadir/gtk-doc/html/libbamf/

%files -n libbamf3-vala
%_datadir/vala/vapi/libbamf3.vapi

%files -n libbamf3-gir
%_libdir/girepository-1.0/Bamf-3.typelib

%files -n libbamf3-gir-devel
%_datadir/gir-1.0/Bamf-3.gir

%changelog
* Sat Aug 1 2020 Yuri N. Sedunov <aris@altlinux.org> 0.5.4-alt1
- 0.5.4
- applied debian patchset

* Mon Sep 25 2017 Yuri N. Sedunov <aris@altlinux.org> 0.5.3-alt3
- rebuilt against libgtop-2.0.so.11

* Sun Dec 11 2016 Yuri N. Sedunov <aris@altlinux.org> 0.5.3-alt2
- fixed build

* Thu Sep 29 2016 Yuri N. Sedunov <aris@altlinux.org> 0.5.3-alt1
- 0.5.3

* Mon Sep 07 2015 Yuri N. Sedunov <aris@altlinux.org> 0.5.1-alt1
- 0.5.1

* Tue Jun 10 2014 Yuri N. Sedunov <aris@altlinux.org> 0.5.0-alt3
- rebuilt against libgtop-2.0.so.10

* Sun Nov 24 2013 Igor Zubkov <icesik@altlinux.org> 0.5.0-alt2
- Vala stuff

* Wed Nov 20 2013 Igor Zubkov <icesik@altlinux.org> 0.5.0-alt1
- 0.5.0

* Tue Oct 08 2013 Igor Zubkov <icesik@altlinux.org> 0.2.126-alt1
- build for Sisyphus

