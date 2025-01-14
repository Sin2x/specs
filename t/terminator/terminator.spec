%def_disable snapshot
%add_typelib_req_skiplist typelib(Gnome)
%define ver_major 2.1

Name: terminator
Version: %ver_major.2
Release: alt1

Summary: Store and run multiple GNOME terminals in one window
Group: Terminals
License: GPL-2.0
Url: https://github.com/gnome-terminator/terminator

%if_disabled snapshot
Source: %url/archive/v%version/%name-%version.tar.gz
%else
Vcs: https://github.com/gnome-terminator/terminator.git
Source: %name-%version.tar
%endif

# fc patches
Patch: terminator-1.91-fc-fix-desktop-file.patch

BuildArch: noarch

%add_python3_req_skip gi.repository.GLib

Requires: typelib(Gtk) = 3.0

BuildRequires(pre): rpm-build-python3 rpm-build-gir

BuildRequires: python3-module-wheel python3-module-setuptools
BuildRequires: python3-module-pytest-runner
BuildRequires: intltool

%description
Multiple GNOME terminals in one window. This is a project to produce an
efficient way of filling a large area of screen space with terminals.
This is done by splitting the window into a resizeable grid of terminals.
As such, you can  produce a very flexible arrangements of terminals for
different tasks.

%prep
%setup
sed -i '/#! \?\/usr.*/d' terminatorlib/*.py
%patch

%build
%pyproject_build

%install
%pyproject_install
%find_lang %name

%files -f %name.lang
%_bindir/%name
%_bindir/remotinator
%python3_sitelibdir_noarch/terminatorlib/
%python3_sitelibdir_noarch/%{pyproject_distinfo %name}
%_datadir/%name/
%_desktopdir/%name.desktop
%_iconsdir/hicolor/*/*/*.*
%_iconsdir/HighContrast/*/*/*.*
%_datadir/pixmaps/%name.png
%_datadir/metainfo/%name.metainfo.xml
%_man1dir/%name.*
%_man5dir/%{name}_config.*
%doc README* CHANGELOG*

%changelog
* Wed Oct 19 2022 Yuri N. Sedunov <aris@altlinux.org> 2.1.2-alt1
- 2.1.2
- ported to %%pyproject* macros

* Mon Apr 12 2021 Yuri N. Sedunov <aris@altlinux.org> 2.1.1-alt1
- updated to v2.1.1-2-gebe58449

* Tue Jan 05 2021 Yuri N. Sedunov <aris@altlinux.org> 2.1.0-alt1
- 2.1.0

* Wed Oct 28 2020 Yuri N. Sedunov <aris@altlinux.org> 2.0.1-alt1
- updated to v2.0.1-43-gacba6fa3

* Mon Apr 20 2020 Yuri N. Sedunov <aris@altlinux.org> 1.92-alt1
- updated to v1.92-7-gde432f73 (new Url, ported to Python3)

* Thu Dec 20 2018 Yuri N. Sedunov <aris@altlinux.org> 1.91-alt2
- fixed buildreqs

* Fri Mar 03 2017 Yuri N. Sedunov <aris@altlinux.org> 1.91-alt1
- 1.91

* Mon Nov 28 2016 Yuri N. Sedunov <aris@altlinux.org> 1.90-alt1
- 1.90

* Sun Sep 13 2015 Yuri N. Sedunov <aris@altlinux.org> 0.98-alt1
- 0.98

* Mon Nov 17 2014 Yuri N. Sedunov <aris@altlinux.org> 0.97-alt1
- first build for Sisyphus

