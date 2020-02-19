%define _libexecdir %_prefix/libexec

Name: xplayer-plparser
Version: 1.0.2
Release: alt2

Summary: Shared libraries of the Xplayer media player play list parser
Group: System/Libraries
License: GPL
URL: https://github.com/linuxmint/%name

Source: %name-%version.tar
Patch: %name-%version.patch

BuildRequires: gnome-common gobject-introspection-devel gtk-doc intltool libarchive-devel
BuildRequires: libgcrypt-devel libgmime-devel libquvi0.9-devel libsoup-devel libxml2-devel

%description
Shared libraries that come with the Xplayer media player.

%package -n lib%name
Summary: Shared libraries of the Xplayer media player play list parser
Group: System/Libraries

%description -n lib%name
Shared libraries that come with the Xplayer media player.

%package -n lib%name-devel
Summary: Development files for Xplayer media player play list parser
Group: Development/C

%description -n lib%name-devel
This package provides files needed to build applications using Xplayer
libraries.

%package -n lib%name-devel-doc
Summary: Development documentation for Xplayer media player play list parser
Group: Development/Documentation
BuildArch: noarch

%description -n lib%name-devel-doc
This package contains documentation needed to develop applications using Xplayer
libraries.

%package -n lib%name-gir
Summary: GObject introspection data for %name
Group: System/Libraries

%description -n lib%name-gir
GObject introspection data for the Xplayer playlist parser library

%package -n lib%name-gir-devel
Summary: GObject introspection devel data for %name
Group: System/Libraries
BuildArch: noarch

%description -n lib%name-gir-devel
GObject introspection devel data for the Xplayer playlist parser library

%prep
%setup -q
%patch -p1
[ ! -d m4 ] && mkdir m4

%build
%autoreconf
%configure \
	--disable-static \
	--enable-gtk-doc \
	--enable-introspection

%make_build

%install
%make DESTDIR=%buildroot install

%find_lang --with-gnome --output=%name.lang xplayer-pl-parser

%files -n lib%name -f %name.lang
%doc AUTHORS NEWS README
%_libdir/*.so.*
%_libexecdir/xplayer-pl-parser-videosite

%files -n lib%name-devel
%_includedir/*
%_libdir/*.so
%_pkgconfigdir/*.pc

%files -n lib%name-devel-doc
%_datadir/gtk-doc/html/*

%files -n lib%name-gir
%_libdir/girepository-1.0/*

%files -n lib%name-gir-devel
%_datadir/gir-1.0/*

%changelog
* Wed Feb 19 2020 Valery Inozemtsev <shrek@altlinux.ru> 1.0.2-alt2
- fixed build for sisyphus

* Tue Sep 27 2016 Vladimir Didenko <cow@altlinux.org> 1.0.2-alt1
- 1.0.2

* Wed Mar 2 2016 Vladimir Didenko <cow@altlinux.org> 1.0.1-alt1
- Initial build for Sisyphus
