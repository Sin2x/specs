# git describe upstream/dolphin-emu | sed 's/-g[0-9a-f]*\(+*\)$/\1/'
%define git_version 5.0-17269
# git show-ref --heads --hash upstream/dolphin-emu
%define git_commit 48c9c224cf9f82f0f9f2690b7cc6283d7448480c

%define mgba_commit 40d4c430fc36caeb7ea32fd39624947ed487d2f2
%define zlib_ng_commit a406284705a462939c7a634119884a31b87d6af9
%define spirv_cross_version sdk-1.3.216.0
%define libspng_commit dc5b1032c08efac68ad30170f7ccbf0aa8dd55c9

Name: dolphin-emu
Version: 5.0.17269
Release: alt1

Summary: The Gamecube / Wii Emulator
License: GPLv2
Group: Emulators

Url: https://%name.org/
Packager: Nazarov Denis <nenderus@altlinux.org>

ExclusiveArch: x86_64 aarch64

# https://github.com/%name/dolphin/archive/%git_commit/dolphin-%git_commit.tar.gz
Source0: dolphin-%git_commit.tar
# https://github.com/mgba-emu/mgba/archive/%mgba_commit/mgba-%mgba_commit.tar.gz
Source1: mgba-%mgba_commit.tar
# https://github.com/zlib-ng/zlib-ng/archive/%zlib_ng_commit/zlib-ng-%zlib_ng_commit.tar.gz
Source2: zlib-ng-%zlib_ng_commit.tar
# https://github.com/KhronosGroup/SPIRV-Cross/archive/%spirv_cross_version/SPIRV-Cross-%spirv_cross_version.tar.gz
Source3: SPIRV-Cross-%spirv_cross_version.tar
# https://github.com/randy408/libspng/archive/$libspng_commit/libspng-%libspng_commit.tar.gz
Source4: libspng-%libspng_commit.tar

Patch0: %name-alt-git.patch

BuildPreReq: pkgconfig(expat)
BuildPreReq: pkgconfig(libbrotlicommon)
BuildPreReq: pkgconfig(libpcre)
BuildPreReq: pkgconfig(uuid)

BuildRequires: cmake
BuildRequires: libcubeb-devel
BuildRequires: libmbedtls-compat-devel
BuildRequires: libminiupnpc-devel
BuildRequires: llvm-devel
BuildRequires: llvm13.0-gold
BuildRequires: pkgconfig(Qt5)
BuildRequires: pkgconfig(alsa)
BuildRequires: pkgconfig(bzip2)
BuildRequires: pkgconfig(bluez)
BuildRequires: pkgconfig(fmt) >= 7.1
BuildRequires: pkgconfig(hidapi-libusb)
BuildRequires: pkgconfig(libavformat)
BuildRequires: pkgconfig(libcurl)
BuildRequires: pkgconfig(libenet)
BuildRequires: pkgconfig(libevdev)
BuildRequires: pkgconfig(liblzma)
BuildRequires: pkgconfig(libpng)
BuildRequires: pkgconfig(libpulse)
BuildRequires: pkgconfig(libswresample)
BuildRequires: pkgconfig(libswscale)
BuildRequires: pkgconfig(libxml-2.0)
BuildRequires: pkgconfig(libusb-1.0)
BuildRequires: pkgconfig(libzstd)
BuildRequires: pkgconfig(lzo2)
BuildRequires: pkgconfig(minizip-ng)
BuildRequires: pkgconfig(pugixml)
BuildRequires: pkgconfig(systemd)
BuildRequires: pkgconfig(sfml-all)
BuildRequires: pkgconfig(xcomposite)
BuildRequires: pkgconfig(xcursor)
BuildRequires: pkgconfig(xdamage)
BuildRequires: pkgconfig(xdmcp)
BuildRequires: pkgconfig(xft)
BuildRequires: pkgconfig(xi)
BuildRequires: pkgconfig(xinerama)
BuildRequires: pkgconfig(xmu)
BuildRequires: pkgconfig(xrandr)
BuildRequires: pkgconfig(xxf86vm)

%description
Dolphin-emu is a emulator for Gamecube, Wii, Triforce that lets
you run Wii/GCN/Tri games on your Windows/Linux/Mac PC system.

%prep
%setup -n dolphin-%git_commit -b 1 -b 2 -b 3 -b 4
%patch0 -p1

%__mv -Tf ../mgba-%mgba_commit Externals/mGBA/mgba
%__mv -Tf ../zlib-ng-%zlib_ng_commit Externals/zlib-ng/zlib-ng
%__mv -Tf ../SPIRV-Cross-%spirv_cross_version Externals/spirv_cross/SPIRV-Cross
%__mv -Tf ../libspng-%libspng_commit Externals/libspng/libspng

%build
%cmake .. \
	-DENABLE_LTO:BOOL=TRUE \
	-DUSE_SHARED_ENET:BOOL=TRUE \
	-DDOLPHIN_WC_DESCRIBE:STRING="%git_version" \
	-DDOLPHIN_WC_REVISION:STRING="%git_commit" \
	-DDOLPHIN_WC_BRANCH:STRING="master" \
	-DDISTRIBUTOR:STRING="ALT Linux Team" \
	-Wno-dev

%cmake_build

%install
%cmake_install
%__install -Dp -m0644 Data/51-usb-device.rules %buildroot%_udevrulesdir/51-%name-usb-device.rules
%find_lang %name

%files -f %name.lang
%_bindir/*
%_desktopdir/%name.desktop
%_datadir/%name
%_iconsdir/hicolor/256x256/apps/%name.png
%_iconsdir/hicolor/scalable/apps/%name.svg
%_man6dir/%{name}*
%config %_udevrulesdir/51-%name-usb-device.rules

%changelog
* Tue Sep 13 2022 Nazarov Denis <nenderus@altlinux.org> 5.0.17269-alt1
- Version 5.0-17269

* Wed Aug 24 2022 Nazarov Denis <nenderus@altlinux.org> 5.0.17243-alt1
- Version 5.0-17243

* Wed May 25 2022 Nazarov Denis <nenderus@altlinux.org> 5.0.16380-alt1
- Version 5.0-16380

* Sun Apr 24 2022 Nazarov Denis <nenderus@altlinux.org> 5.0.16101-alt1.1
- Fix FTBFS

* Fri Mar 25 2022 Nazarov Denis <nenderus@altlinux.org> 5.0.16101-alt1
- Version 5.0-16101

* Wed Feb 09 2022 Nazarov Denis <nenderus@altlinux.org> 5.0.15993-alt1
- Version 5.0-15993

* Wed Nov 17 2021 Nazarov Denis <nenderus@altlinux.org> 5.0.15445-alt1
- Version 5.0-15445

* Thu Oct 07 2021 Nazarov Denis <nenderus@altlinux.org> 5.0.15260-alt1
- Version 5.0-15260

* Tue Sep 07 2021 Nazarov Denis <nenderus@altlinux.org> 5.0.15105-alt1
- Version 5.0-15105

* Mon Aug 02 2021 Nazarov Denis <nenderus@altlinux.org> 5.0.14790-alt1
- Version 5.0-14790

* Sat Jul 10 2021 Nazarov Denis <nenderus@altlinux.org> 5.0.14344-alt1.1
- Fix FTBFS

* Sun Jun 06 2021 Nazarov Denis <nenderus@altlinux.org> 5.0.14344-alt1
- Version 5.0-14344

* Fri May 28 2021 Nazarov Denis <nenderus@altlinux.org> 5.0.14095-alt1
- Version 5.0-14095

* Wed Apr 07 2021 Nazarov Denis <nenderus@altlinux.org> 5.0.13963-alt1
- Version 5.0-13963

* Sun Mar 14 2021 Nazarov Denis <nenderus@altlinux.org> 5.0.13827-alt1
- Version 5.0-13827
- Enables LLVM support

* Tue Mar 09 2021 Nazarov Denis <nenderus@altlinux.org> 5.0.13817-alt1
- Version 5.0-13817

* Wed Feb 17 2021 Nazarov Denis <nenderus@altlinux.org> 5.0.13671-alt2
- Enable Link Time Optimization
- Install udev rules for GameCube Controller Adapter, Wiimotes and DolphinBar

* Wed Feb 17 2021 Nazarov Denis <nenderus@altlinux.org> 5.0.13671-alt1
- Version 5.0-13671
- Add distributor option

* Sun Feb 14 2021 Nazarov Denis <nenderus@altlinux.org> 5.0.13653-alt1
- Version 5.0.13653
- Build with minizip-ng

* Fri Feb 12 2021 Nazarov Denis <nenderus@altlinux.org> 5.0.13633-alt1
- Version 5.0-13633
- Use system headers for Vulkan

* Wed Feb 10 2021 Nazarov Denis <nenderus@altlinux.org> 5.0.13614-alt2
- Build with cubeb

* Tue Feb 09 2021 Nazarov Denis <nenderus@altlinux.org> 5.0.13614-alt1
- Version 5.0-13614

* Sun Jan 24 2021 Nazarov Denis <nenderus@altlinux.org> 5.0-alt16.gitcaff472
- Update to git commit caff472dbf27fbcc5b3d28cbf5b1789592a9f857
- Use minizip from zlib

* Mon Oct 12 2020 Nazarov Denis <nenderus@altlinux.org> 5.0-alt15.git5a939cc
- Rebuit with minizip

* Sun Oct 11 2020 Nazarov Denis <nenderus@altlinux.org> 5.0-alt14.git5a939cc
- Update to git commit 5a939cc (ALT #39062)

* Fri Jul 03 2020 Nazarov Denis <nenderus@altlinux.org> 5.0-alt13
- Don't gzip sources to sppedup rpmbuild -bp
- Update BuildRequires and BuidPreReq
- Build for aarch64

* Mon Aug 19 2019 Anton Midyukov <antohami@altlinux.org> 5.0-alt12
- add_optflags (pkg-config --cflags pango) (Fix FTBFS)

* Sun Feb 24 2019 Nazarov Denis <nenderus@altlinux.org> 5.0-alt11
- Rebuilt with new SFML

* Tue Jan 15 2019 Nazarov Denis <nenderus@altlinux.org> 5.0-alt10
- Remove %ubt macro

* Sat Jan 12 2019 Nazarov Denis <nenderus@altlinux.org> 5.0-alt9%ubt
- Fix build

* Tue Sep 18 2018 Anton Midyukov <antohami@altlinux.org> 5.0-alt8%ubt
- Rebuilt with compat-libwxGTK3.0-gtk2-devel

* Sun Jul 22 2018 Nazarov Denis <nenderus@altlinux.org> 5.0-alt7%ubt
- Rebuilt with new mbedTLS

* Sun Jun 17 2018 Nazarov Denis <nenderus@altlinux.org> 5.0-alt6%ubt
- Rebuilt with new libva

* Fri Apr 13 2018 Nazarov Denis <nenderus@altlinux.org> 5.0-alt5%ubt
- Rebuilt with new mbedTLS

* Wed Jun 07 2017 Nazarov Denis <nenderus@altlinux.org> 5.0-alt4%ubt
- Rebuilt with ffmpeg instead libav
- Add gcc fix patch

* Tue Nov 01 2016 Nazarov Denis <nenderus@altlinux.org> 5.0-alt3.1
- Rebuilt with SFML 2.4.0

* Sun Jul 17 2016 Nazarov Denis <nenderus@altlinux.org> 5.0-alt2.M80P.1
- Build for branch p8

* Sun Jul 17 2016 Nazarov Denis <nenderus@altlinux.org> 5.0-alt3
- Rebuilt with shared enet and gtest libraries

* Wed Jul 13 2016 Nazarov Denis <nenderus@altlinux.org> 5.0-alt2
- Version 5.0

* Sat Feb 20 2016 Yuri N. Sedunov <aris@altlinux.org> 5.0-alt1.rc.1
- rebuilt against libSoundTouch.so.1

* Mon Aug 03 2015 Nazarov Denis <nenderus@altlinux.org> 5.0-alt1.rc
- Version 5.0 RC

* Thu Jul 16 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.2-alt4.git20150715
- New snapshot

* Sat Mar 14 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.2-alt3.git5fafcb6.1
- Rebuilt with wxGTK3.1 (instead of wxGTK3.0) & gtk+3 (gtk+2)

* Wed Sep 17 2014 Nazarov Denis <nenderus@altlinux.org> 4.0.2-alt3.git5fafcb6
- Version from git (commit 5fafcb6)
- Rebuild with new polarssl and GLEW

* Tue Apr 22 2014 Nazarov Denis <nenderus@altlinux.org> 4.0.2-alt2
- Rebuild with new polarssl

* Sat Feb 01 2014 Nazarov Denis <nenderus@altlinux.org> 4.0.2-alt1
- Version 4.0.2

* Wed Nov 20 2013 Nazarov Denis <nenderus@altlinux.org> 4.0.1-alt3
- Rebuild with wxGTK 3.0

* Mon Nov 11 2013 Nazarov Denis <nenderus@altlinux.org> 4.0.1-alt2
- Fix build

* Tue Nov 05 2013 Nazarov Denis <nenderus@altlinux.org> 4.0.1-alt1
- Initial build for ALT Linux
