%global appid net.lutris.Lutris
Name: lutris
Version: 0.5.7.1
Release: alt1
Summary: Manager for game installation and execution
License: GPL-2.0 and GPL-2.0+ and GPL-3.0+ and CC0-1.0 and LGPL-2.1+ and CC-BY-NC-SA-2.0 and CC-BY-SA-3.0
Group: Games/Other
Url: http://lutris.net

Source: http://lutris.net/releases/lutris_%version.tar.xz
Patch: lutris_0.5.7_alt_python3_pixbuf_path.patch

BuildRequires(pre): meson
# Automatically added by buildreq on Fri Aug 30 2019 (-bi)
# optimized out: bash4 bashrc kmod perl python-base python-modules python3 python3-base python3-dev python3-module-pkg_resources rpm-build-python3 sh4 tzdata xz
BuildRequires: eject fuse python3-module-setuptools rpm-build-gir unzip xlsfonts
# Requires: cabextract fluid-soundfont-gm python3-module-Pillow python3-module-yaml python3-module-pygobject python3-module-requests winetricks libgdk-pixbuf-gir libgnome-desktop3-gir xrandr pciutils
Requires: python3-module-pygobject3 python3-module-yaml python3-module-requests python3-module-pylint python3-module-distro python3-module-setproctitle python3-module-Pillow libgdk-pixbuf-gir libgnome-desktop3-gir libwebkit2gtk-gir libnotify-gir libgtk+3-gir
# settings menu
# Requires: lsblk glxinfo
# controller support
Requires: python3-module-evdev
# Recommends: psmisc p7zip curl cabextract xrandr glibc-gconv-modules winetricks

BuildArch: noarch

%description
Lutris allows to gather and manage (install, configure and launch)
all games acquired from any source, in a single interface.
This includes, for example, Steam or Desura games, Windows games (WINE),
or emulated console games and browser games.

Recommends for install: psmisc p7zip curl cabextract xrandr glibc-gconv-modules winetricks

%prep
%setup -n %name
%patch -p2

%build
%meson
%meson_build

%install
%meson_install

%files
%doc README.rst CONTRIBUTING.md AUTHORS
%doc LICENSE
%_bindir/%name
%_datadir/%name/
%_desktopdir/%appid.desktop
%_iconsdir/hicolor/scalable/apps/%name.svg
%_iconsdir/hicolor/??x??/apps/%name.png
%_iconsdir/hicolor/???x???/apps/%name.png
%python3_sitelibdir/%name/
%dir %_datadir/metainfo/
%_datadir/metainfo/%appid.metainfo.xml
%_datadir/locale/*/LC_MESSAGES/%name.mo
%_man1dir/%name.1.xz

%changelog
* Thu Jul 23 2020 Leontiy Volodin <lvol@altlinux.org> 0.5.7.1-alt1
- New version (0.5.7.1) with rpmgs script.
- Rewritten requires list.
- Built with meson.

* Sun Jul 05 2020 Leontiy Volodin <lvol@altlinux.org> 0.5.7-alt1
- New version (0.5.7) with rpmgs script.
- Updated license tag.
- Removed psmisc from requires.

* Mon Jun 08 2020 Leontiy Volodin <lvol@altlinux.org> 0.5.6-alt2
- Fixed build errors.

* Thu Apr 16 2020 Leontiy Volodin <lvol@altlinux.org> 0.5.6-alt1
- New version (0.5.6) with rpmgs script.

* Mon Apr 13 2020 Leontiy Volodin <lvol@altlinux.org> 0.5.5-alt1
- New version (0.5.5) with rpmgs script.

* Mon Dec 09 2019 Leontiy Volodin <lvol@altlinux.org> 0.5.4-alt1
- New version (0.5.4).

* Mon Sep 09 2019 Leontiy Volodin <lvol@altlinux.org> 0.5.3-alt1
- New version (0.5.3) with rpmgs script.

* Fri Aug 30 2019 Leontiy Volodin <lvol@altlinux.org> 0.5.2.2-alt1
- Initial build for ALT Sisyphus (thanks opensuse for this spec) (ALT #37168).
