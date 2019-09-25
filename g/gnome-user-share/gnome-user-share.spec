%define _libexecdir %_prefix/libexec
%define ver_major 3.34
%define httpd /usr/sbin/httpd2
%define modules_path %_sysconfdir/httpd2/modules

%def_enable nautilus

Name: gnome-user-share
Version: %ver_major.0
Release: alt1

Summary: Gnome user file sharing
Group: Graphical desktop/GNOME
License: GPLv2+
Url: https://www.gnome.org

Source: ftp://ftp.gnome.org/pub/gnome/sources/%name/%ver_major/%name-%version.tar.xz

%define glib_ver 2.58
%define nautilus_ver 3.27.90

Requires: apache2 >= 2.2
Requires: apache2-mod_dnssd >= 0.6

BuildRequires(pre): meson
BuildRequires: yelp-tools desktop-file-utils
BuildRequires: libgio-devel >= %glib_ver libgtk+3-devel libnotify-devel libcanberra-gtk3-devel
BuildRequires: libselinux-devel libgudev-devel
BuildRequires: apache2 apache2-mod_dnssd pkgconfig(systemd)
%{?_enable_nautilus:BuildRequires: libnautilus-devel >= %nautilus_ver}

%description
gnome-user-share is a small package that binds together various free
software projects to bring easy to use user-level file sharing to the
masses.

The program is meant to run in the background when the user is logged
in, and when file sharing is enabled a webdav server is started that
shares the $HOME/Public folder. The share is then published to all
computers on the local network using mDNS/rendezvous, so that it shows
up in the Network location in Gnome.

The dav server used is apache, so you need that installed. Avahi or
Howl is used for mDNS support, so you need to have that installed and
mDNSResolver running.

%prep
%setup

%build
%meson -Dhttpd=%httpd \
       -Dmodules-path=%modules_path \
       %{?_enable_nautilus:-Dnautilus_extension=true}
%nil
%meson_build

%install
%meson_install
%find_lang --with-gnome %name

%files -f gnome-user-share.lang
%_libexecdir/%name-webdav
%_desktopdir/%name-webdav.desktop
%_datadir/%name/
%{?_enable_nautilus:%_libdir/nautilus/extensions-3.0/libnautilus-share-extension.so}
%_datadir/GConf/gsettings/%name.convert
%_datadir/glib-2.0/schemas/org.gnome.desktop.file-sharing.gschema.xml
%_prefix/lib/systemd/user/%name-webdav.service
%doc README NEWS


%changelog
* Fri Sep 06 2019 Yuri N. Sedunov <aris@altlinux.org> 3.34.0-alt1
- 3.34.0 (ported to Meson build system)

* Mon Mar 11 2019 Yuri N. Sedunov <aris@altlinux.org> 3.32.0.1-alt1
- 3.32.0.1

* Tue Apr 10 2018 Yuri N. Sedunov <aris@altlinux.org> 3.28.0-alt1
- 3.28.0

* Tue Feb 13 2018 Yuri N. Sedunov <aris@altlinux.org> 3.27.90-alt1
- 3.27.90

* Tue Sep 20 2016 Yuri N. Sedunov <aris@altlinux.org> 3.18.3-alt1
- 3.18.3

* Wed Aug 31 2016 Yuri N. Sedunov <aris@altlinux.org> 3.18.2-alt1
- 3.18.2

* Mon Mar 21 2016 Yuri N. Sedunov <aris@altlinux.org> 3.18.1-alt1
- 3.18.1

* Mon Sep 21 2015 Yuri N. Sedunov <aris@altlinux.org> 3.18.0-alt1
- 3.18.0

* Thu Dec 18 2014 Yuri N. Sedunov <aris@altlinux.org> 3.14.2-alt1
- 3.14.2

* Fri Nov 21 2014 Yuri N. Sedunov <aris@altlinux.org> 3.14.1-alt1
- 3.14.1

* Thu Oct 02 2014 Yuri N. Sedunov <aris@altlinux.org> 3.14.0-alt1
- first build for Sisyphus

