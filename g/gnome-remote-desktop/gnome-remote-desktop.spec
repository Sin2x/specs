%define _userinitdir %(pkg-config systemd --variable systemduserunitdir)

%def_disable snapshot
%define _libexecdir %_prefix/libexec
%define ver_major 40
%define beta %nil

%def_enable vnc
%def_enable rdp

Name: gnome-remote-desktop
Version: %ver_major.1
Release: alt1%beta

Summary: GNOME Remote Desktop
Group: Networking/Remote access
License: GPLv2+
Url: https://gitlab.gnome.org/GNOME/gnome-remote-desktop

%if_disabled snapshot
Source: ftp://ftp.gnome.org/pub/gnome/sources/%name/%ver_major/%name-%version%beta.tar.xz
%else
Vcs: https://gitlab.gnome.org/GNOME/gnome-remote-desktop.git
Source: %name-%version.tar
%endif

%define glib_ver 2.68
%define pw_api_ver 0.3
%define pw_ver 0.3.22
%define vnc_ver 0.9.11
%define freerdp_ver 2.3.1
%define gst_ver 1.10
%define fuse_ver 3.9.1
%define xkbc_ver 1.0.0

Requires: pipewire >= %pw_ver
Requires: fuse3 >= %fuse_ver

BuildRequires(pre): meson pkgconfig(systemd)
BuildRequires: libgio-devel >= %glib_ver
BuildRequires: pkgconfig(libpipewire-%pw_api_ver) >= %pw_ver
%{?_enable_vnc:BuildRequires: libvncserver-devel >= %vnc_ver}
%{?_enable_rdp:BuildRequires: libfreerdp-devel >= %freerdp_ver}
BuildRequires: libfuse3-devel >= %fuse_ver
BuildRequires: libxkbcommon-devel >= %xkbc_ver
BuildRequires: libsecret-devel libnotify-devel libcairo-devel

%description
Remote desktop daemon for GNOME using pipewire.

%prep
%setup -n %name-%version%beta

%build
%meson \
    %{?_disable_rdp:-Drdp=false} \
    -Dsystemd_user_unit_dir=%_userinitdir
%nil
%meson_build

%install
%meson_install

%files
%_libexecdir/%name-daemon
%_userinitdir/%name.service
%_datadir/glib-2.0/schemas/org.gnome.desktop.remote-desktop.gschema.xml
%_datadir/glib-2.0/schemas/org.gnome.desktop.remote-desktop.enums.xml
%doc README

%changelog
* Sun May 02 2021 Yuri N. Sedunov <aris@altlinux.org> 40.1-alt1
- 40.1

* Sun Mar 21 2021 Yuri N. Sedunov <aris@altlinux.org> 40.0-alt1
- 40.0

* Tue Sep 08 2020 Yuri N. Sedunov <aris@altlinux.org> 0.1.9-alt1
- 0.1.9

* Sun Mar 29 2020 Yuri N. Sedunov <aris@altlinux.org> 0.1.8-alt1
- 0.1.8

* Fri Feb 22 2019 Yuri N. Sedunov <aris@altlinux.org> 0.1.7-alt1
- 0.1.7

* Fri Aug 10 2018 Yuri N. Sedunov <aris@altlinux.org> 0.1.6-alt1
- 0.1.6

* Sun Jun 10 2018 Yuri N. Sedunov <aris@altlinux.org> 0.1.4-alt1
- 0.1.4

* Sun Nov 26 2017 Yuri N. Sedunov <aris@altlinux.org> 0.1.2-alt2
- fixed build with meson-0.43

* Wed Sep 20 2017 Yuri N. Sedunov <aris@altlinux.org> 0.1.2-alt1
- first build for Sisyphus

