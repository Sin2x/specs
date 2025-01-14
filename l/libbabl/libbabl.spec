Name: libbabl
Version: 0.1.90
Release: alt1
Summary: babl is a dynamic, any to any, pixel format translation library
License: %lgpl3only
Group: System/Libraries
Url: http://www.gegl.org/babl/
Packager: Valery Inozemtsev <crux@altlinux.ru>

Source: babl-%version.tar
Patch: babl-%version-%release.patch

BuildRequires(pre): rpm-build-licenses meson
BuildRequires: gobject-introspection-devel liblcms2-devel librsvg-utils w3m inkscape ruby ruby-module-date-time vala-tools

%description
babl is a dynamic, any to any, pixel format translation library.

It allows converting between different methods of storing pixels known as pixel
formats that have with different bitdepths and other data representations, color
models and component permutations.

A vocabulary to formulate new pixel formats from existing primitives is provided
as well as the framework to add new color models and data types.

Features
 * Fast.
 * Accurate.
 * Stable, small API.
 * Self profiling and optimizing.
 * ANSI C, works on win32, linux and mac, 32bit and 64bit systems.
 * Extendable with new formats, color models, components and datatypes.
 * Reference 64bit floating point conversions for datatypes and color models.

%package gir
Summary: GObject introspection data for babl
Group: System/Libraries

%description gir
GObject introspection data for babl

%package devel
Summary: development files of babl
Group: Development/C
Requires: %name = %version-%release

%description devel
babl is a dynamic, any to any, pixel format translation library. This package
contain development files.

%prep
%setup -q -n babl-%version
%patch -p1

%build
sed "s|@BABL_GIT_VERSION@|%version|" git-version.h.in > git-version.h
%meson \
	-Dwith-docs=false
%meson_build -v

%install
%meson_install

%files
%doc AUTHORS COPYING NEWS TODO
%_libdir/*.so.*
%dir %_libdir/babl-0.1
%_libdir/babl-0.1/*.so

%files gir
%_libdir/girepository-1.0/*.typelib

%files devel
%_includedir/babl-0.1
%_libdir/*.so
%_pkgconfigdir/*.pc
%_datadir/gir-1.0/*.gir
%_vapidir/babl-*.deps
%_vapidir/babl-*.vapi

%changelog
* Tue Mar 15 2022 Valery Inozemtsev <shrek@altlinux.ru> 0.1.90-alt1
- 0.1.90

* Mon Sep 20 2021 Valery Inozemtsev <shrek@altlinux.ru> 0.1.88-alt1
- 0.1.88

* Thu Apr 01 2021 Valery Inozemtsev <shrek@altlinux.ru> 0.1.86-alt1
- 0.1.86

* Mon Dec 28 2020 Valery Inozemtsev <shrek@altlinux.ru> 0.1.84-alt1
- 0.1.84

* Fri Oct 09 2020 Valery Inozemtsev <shrek@altlinux.ru> 0.1.82-alt1
- 0.1.82

* Mon Jun 08 2020 Valery Inozemtsev <shrek@altlinux.ru> 0.1.78-alt1
- 0.1.78

* Mon Mar 02 2020 Valery Inozemtsev <shrek@altlinux.ru> 0.1.74-alt1
- 0.1.74

* Fri Nov 01 2019 Valery Inozemtsev <shrek@altlinux.ru> 0.1.72-alt1
- 0.1.72

* Thu Jun 20 2019 Valery Inozemtsev <shrek@altlinux.ru> 0.1.66-alt1
- 0.1.66

* Mon Apr 08 2019 Valery Inozemtsev <shrek@altlinux.ru> 0.1.62-alt1
- 0.1.62

* Mon Nov 12 2018 Valery Inozemtsev <shrek@altlinux.ru> 0.1.60-alt1
- 0.1.60

* Wed Aug 29 2018 Valery Inozemtsev <shrek@altlinux.ru> 0.1.56-alt1
- 0.1.56

* Thu Jul 05 2018 Valery Inozemtsev <shrek@altlinux.ru> 0.1.52-alt1
- 0.1.52

* Wed Jun 13 2018 Valery Inozemtsev <shrek@altlinux.ru> 0.1.50-alt1
- 0.1.50

* Tue May 08 2018 Valery Inozemtsev <shrek@altlinux.ru> 0.1.46-alt1
- 0.1.46

* Wed Feb 07 2018 Valery Inozemtsev <shrek@altlinux.ru> 0.1.42-alt1
- 0.1.42

* Thu May 18 2017 Valery Inozemtsev <shrek@altlinux.ru> 0.1.26-alt1
- 0.1.26

* Wed Feb 08 2017 Valery Inozemtsev <shrek@altlinux.ru> 0.1.24-alt0.M80P.1
- backport to p8 branch

* Wed Feb 01 2017 Valery Inozemtsev <shrek@altlinux.ru> 0.1.24-alt1
- 0.1.24

* Mon Feb 08 2016 Valery Inozemtsev <shrek@altlinux.ru> 0.1.14-alt1
- 0.1.14

* Tue Feb 24 2015 Valery Inozemtsev <shrek@altlinux.ru> 0.1.12-alt1
- 0.1.12

* Wed Apr 04 2012 Valery Inozemtsev <shrek@altlinux.ru> 0.1.10-alt1
- 0.1.10

* Tue Feb 15 2011 Valery Inozemtsev <shrek@altlinux.ru> 0.1.4-alt1
- 0.1.4

* Wed Nov 24 2010 Valery Inozemtsev <shrek@altlinux.ru> 0.1.2-alt2
- rebuild

* Tue Mar 30 2010 Valery Inozemtsev <shrek@altlinux.ru> 0.1.2-alt1
- 0.1.2

* Mon Jul 13 2009 Valery Inozemtsev <shrek@altlinux.ru> 0.1.0-alt1
- 0.1.0

* Fri Nov 14 2008 Valery Inozemtsev <shrek@altlinux.ru> 0.0.22-alt2
- rebuild

* Sat Sep 27 2008 Vladimir Lettiev <crux@altlinux.ru> 0.0.22-alt1
- Initial build for Sisyphus

