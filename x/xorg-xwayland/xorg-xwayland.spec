%define _libexecdir /usr/libexec
%define _deffontdir catalogue:%_sysconfdir/X11/fontpath.d

Name: xorg-xwayland
Version: 21.1.0
Release: alt1
Epoch: 2
License: MIT
Summary: Wayland X server
Group: System/X11
Url: http://xorg.freedesktop.org
Packager: Valery Inozemtsev <shrek@altlinux.ru>

Source: %name-%version.tar
Patch: %name-%version-%release.patch

Requires: xorg-server-common

BuildRequires: meson egl-wayland-devel libEGL-devel libGL-devel libXaw-devel libXdmcp-devel libXfont-devel libXfont2-devel libXpm-devel
BuildRequires: libXrender-devel libXres-devel libXtst-devel libXv-devel libaudit-devel libdbus-devel libdmx-devel libdrm-devel libepoxy-devel
BuildRequires: libgbm-devel libpciaccess-devel libpixman-devel libselinux-devel libssl-devel libtirpc-devel libudev-devel libwayland-client-devel
BuildRequires: libxcb-render-util-devel libxcbutil-devel libxcbutil-icccm-devel libxcbutil-image-devel libxcbutil-keysyms-devel libxkbfile-devel
BuildRequires: libxshmfence-devel wayland-protocols xorg-xtrans-devel libgcrypt-devel xkbcomp rendercheck

%description
Xwayland is an X server for running X clients under Wayland

%package devel
Summary: Development package
Group: Development/C

%description devel
The development package provides the developmental files which are
necessary for developing Wayland compositors using Xwayland

%prep
%setup -q
%patch -p1

%build
%meson \
	-Dxwayland_eglstream=true \
	-Ddefault_font_path=%_deffontdir \
	-Dxkb_output_dir=%_localstatedir/xkb \
	-Dxcsecurity=true \
	-Dglamor=true \
	-Ddri3=true

%meson_build

%install
%meson_install

%files
%_bindir/Xwayland
%_man1dir/Xwayland.1*

%files devel
%_pkgconfigdir/*.pc

%changelog
* Fri Mar 19 2021 Valery Inozemtsev <shrek@altlinux.ru> 2:21.1.0-alt1
- initial release

