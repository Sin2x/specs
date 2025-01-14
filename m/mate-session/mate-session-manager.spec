%define _libexecdir %_prefix/libexec
%define rname mate-session-manager

Name: mate-session
Version: 1.26.0
Release: alt2
Epoch: 1
Summary: MATE Desktop session manager
License: GPLv2+
Group: Graphical desktop/MATE
Url: http://mate-desktop.org/
Packager: Valery Inozemtsev <shrek@altlinux.ru>

Requires: mate-control-center mate-polkit mate-desktop polkit

Source: %rname-%version.tar
Source1: mate-submodules-%rname.tar
Patch: %rname-%version-%release.patch
Patch1: mate-submodules-libegg.patch

BuildRequires: mate-common libSM-devel libXtst-devel libdbus-glib-devel libgtk+3-devel libsystemd-devel
BuildRequires: glib2-devel libXcomposite-devel libepoxy-devel xmlto xorg-xtrans-devel

%description
This package contains a session that can be started from a display
manager such as MDM. It will load all necessary applications for a
full-featured user session.

%prep
%setup -q -n %rname-%version -a1
%patch -p1
%patch1 -p0

cat << __EOF__ > mate-submodules/Makefile.am
SUBDIRS = libegg
__EOF__

%build
%autoreconf
%configure \
	--enable-ipv6 \
	--with-default-wm=marco \
	--with-systemd \
	--enable-docbook-docs \
	--disable-schemas-compile

%make_build

%install
%make DESTDIR=%buildroot install

sed -i 's,^Icon=$,Icon=mate-desktop,' %buildroot%_datadir/xsessions/mate.desktop

mkdir -p %buildroot%_sysconfdir/X11/wmsession.d/
cat << __EOF__ > %buildroot%_sysconfdir/X11/wmsession.d/02Mate
NAME=Mate
ICON=%_iconsdir/hicolor/scalable/apps/mate-desktop.svg
DESC=Mate (Gnome 2) Environment
EXEC=%_bindir/mate-session
SCRIPT:
exec %_bindir/mate-session
__EOF__

%find_lang %rname --with-gnome --all-name

%files -f %rname.lang
%doc AUTHORS COPYING README
%_docdir/%rname
%_sysconfdir/X11/wmsession.d/*Mate*
%_bindir/mate-*
%_libexecdir/mate-session-check-accelerated*
%_desktopdir/mate-session-properties.desktop
%_datadir/%rname
%_iconsdir/hicolor/*/apps/*.*
%_datadir/glib-2.0/schemas/org.mate.session.gschema.xml
%_datadir/xsessions/mate.desktop
%_man1dir/*.1*

%changelog
* Wed Oct 26 2022 Valery Inozemtsev <shrek@altlinux.ru> 1:1.26.0-alt2
- merged p10 branch

* Fri Aug 06 2021 Valery Inozemtsev <shrek@altlinux.ru> 1:1.26.0-alt1
- 1.26.0

* Fri Aug 14 2020 Valery Inozemtsev <shrek@altlinux.ru> 1:1.24.1-alt1
- 1.24.1

* Tue Feb 25 2020 Valery Inozemtsev <shrek@altlinux.ru> 1:1.24.0-alt1
- 1.24.0

* Fri Feb 21 2020 Valery Inozemtsev <shrek@altlinux.ru> 1:1.22.2-alt2
- upstream: fix timeout with gnome-keyring 3.34
- update russian translation (closes: #37402, #37730)

* Tue Oct 15 2019 Valery Inozemtsev <shrek@altlinux.ru> 1:1.22.2-alt1
- 1.22.2

* Thu Apr 25 2019 Valery Inozemtsev <shrek@altlinux.ru> 1:1.22.1-alt1
- 1.22.1

* Mon Mar 04 2019 Valery Inozemtsev <shrek@altlinux.ru> 1:1.22.0-alt1
- 1.22.0

* Mon Dec 24 2018 Valery Inozemtsev <shrek@altlinux.ru> 1:1.20.2-alt1
- 1.20.2

* Mon Oct 22 2018 Valery Inozemtsev <shrek@altlinux.ru> 1:1.20.1-alt1
- 1.20.1

* Wed Mar 28 2018 Valery Inozemtsev <shrek@altlinux.ru> 1:1.20.0-alt2
- mate.desktop: add path to mate-session

* Thu Mar 15 2018 Valery Inozemtsev <shrek@altlinux.ru> 1:1.20.0-alt1
- initial build from git.mate-desktop.org

* Tue Feb 20 2018 Vladimir D. Seleznev <vseleznv@altlinux.org> 1.20.0-alt1_1
- new fc release
