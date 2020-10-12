%def_disable clang

Name: strawberry
Version: 0.8.1
Release: alt1
Summary: Audio player and music collection organizer

# Main program: GPL-3.0-or-later
# src/engine/gstengine and src/engine/xineengine: GPL-2.0-or-later
# 3rdparty/taglib: LGPL-2.1
# 3rdparty/singleapplication and src/widgets/qocoa_mac.h: MIT
# 3rdparty/utf8-cpp: BSL
# src/core/timeconstants.h and ext/libstrawberry-common/core/logging and ext/libstrawberry-common/core/messagehandler: APSL-2.0
License: GPL-2.0-or-later and GPL-3.0-or-later and LGPL-2.1 and APSL-2.0 and MIT and BSL
Group: Sound
Url: https://www.strawberrymusicplayer.org/
Packager: Leontiy Volodin <lvol@altlinux.org>

Source: https://github.com/jonaski/strawberry/archive/%version/%name-%version.tar.gz

BuildRequires(pre): rpm-build-ninja
%if_enabled clang
BuildRequires: clang10.0-devel
%endif
BuildRequires: boost-program_options-devel ccache gcc-c++ gettext-tools glib2-devel gst-plugins1.0-devel gstreamer1.0-devel libalsa-devel libcdio-devel libchromaprint-devel libdbus-devel libfftw3-devel libgio-devel libgnutls-devel libgpod-devel libimobiledevice-devel libmtp-devel libplist-devel libprotobuf-devel libpulseaudio-devel libsqlite3-devel libtag-devel libusbmuxd-devel libvlc-devel libxine2-devel qt5-phonon-devel qt5-x11extras-devel
BuildRequires: cmake rpm-macros-cmake extra-cmake-modules desktop-file-utils libappstream-glib qt5-tools-devel protobuf-compiler libusb-devel
%ifnarch s390 s390x
BuildRequires: libgpod-devel
%endif

Requires: gst-plugins-good1.0 vlc-mini

Provides: bundled(utf8-cpp)
Provides: bundled(singleapplication)
Provides: bundled(singlecoreapplication)

%description
Strawberry is a audio player and music collection organizer.
It is a fork of Clementine. The name is inspired by the band Strawbs.

Features:
  * Play and organize music
  * Supports WAV, FLAC, WavPack, DSF, DSDIFF, Ogg Vorbis, Speex, MPC,
    TrueAudio, AIFF, MP4, MP3 and ASF
  * Audio CD playback
  * Native desktop notifications
  * Playlists in multiple formats
  * Advanced output and device options with support for bit perfect playback
    on Linux
  * Edit tags on music files
  * Fetch tags from MusicBrainz
  * Album cover art from Last.fm, Musicbrainz and Discogs
  * Song lyrics from AudD and API Seeds
  * Support for multiple backends
  * Audio analyzer
  * Equalizer
  * Transfer music to iPod, iPhone, MTP or mass-storage USB player
  * Integrated Tidal support
  * Scrobbler with support for Last.fm, Libre.fm and ListenBrainz

%prep
%setup

# Remove most 3rdparty libraries
# Unbundle taglib next release:
# https://github.com/taglib/taglib/issues/837#issuecomment-428389347

mv 3rdparty/singleapplication/LICENSE 3rdparty/singleapplication/LICENSE-singleapplication
mv 3rdparty/taglib/COPYING 3rdparty/taglib/COPYING-taglib

%build
%if_enabled clang
export CC="clang"
export CXX="clang++"
export AR="llvm-ar"
%else
export CC="gcc"
export CXX="g++"
export AR="ar"
%endif

%cmake \
  -GNinja \
  -DBUILD_WERROR=OFF \
  -DUSE_SYSTEM_TAGLIB=ON

%ninja_build -C BUILD

%install
%ninja_install -C BUILD

%check
desktop-file-validate %buildroot%_desktopdir/org.strawberrymusicplayer.strawberry.desktop
appstream-util validate-relax --nonet %buildroot%_datadir/metainfo/org.strawberrymusicplayer.strawberry.appdata.xml

%files
%doc COPYING 3rdparty/taglib/COPYING-taglib 3rdparty/singleapplication/LICENSE-singleapplication
%doc Changelog
%_bindir/strawberry
%_bindir/strawberry-tagreader
%_datadir/metainfo/org.strawberrymusicplayer.strawberry.appdata.xml
%_desktopdir/org.strawberrymusicplayer.strawberry.desktop
%_iconsdir/hicolor/*/apps/strawberry.*
%_man1dir/strawberry.1.*
%_man1dir/strawberry-tagreader.1.*

%changelog
* Mon Oct 12 2020 Leontiy Volodin <lvol@altlinux.org> 0.8.1-alt1
- New version (0.8.1) with rpmgs script.

* Sun Aug 16 2020 Leontiy Volodin <lvol@altlinux.org> 0.7.2-alt1
- New version (0.7.2) with rpmgs script.

* Sat Aug 15 2020 Leontiy Volodin <lvol@altlinux.org> 0.7.1-alt1
- New version (0.7.1) with rpmgs script.
- Built with ninja instead make.

* Tue Jul 14 2020 Leontiy Volodin <lvol@altlinux.org> 0.6.13-alt1
- New version (0.6.13) with rpmgs script.

* Thu Jun 18 2020 Leontiy Volodin <lvol@altlinux.org> 0.6.12-alt2
- Fixed build with new libusbmuxd and libplist.

* Mon Jun 08 2020 Leontiy Volodin <lvol@altlinux.org> 0.6.12-alt1
- New version (0.6.12) with rpmgs script.

* Mon May 18 2020 Leontiy Volodin <lvol@altlinux.org> 0.6.11-alt1
- New version (0.6.11) with rpmgs script.

* Fri May 01 2020 Leontiy Volodin <lvol@altlinux.org> 0.6.10-alt1
- new version (0.6.10) with rpmgs script

* Mon Apr 13 2020 Leontiy Volodin <lvol@altlinux.org> 0.6.9-alt1
- New version (0.6.9) with rpmgs script.

* Thu Jan 09 2020 Leontiy Volodin <lvol@altlinux.org> 0.6.8-alt1
- New version (0.6.8) with rpmgs script.

* Mon Dec 09 2019 Leontiy Volodin <lvol@altlinux.org> 0.6.7-alt1
- New version (0.6.7) with rpmgs script.

* Mon Nov 11 2019 Leontiy Volodin <lvol@altlinux.org> 0.6.6-alt1
- New version (0.6.6) with rpmgs script.

* Tue Oct 01 2019 Leontiy Volodin <lvol@altlinux.org> 0.6.5-alt1
- New version (0.6.5) with rpmgs script.

* Thu Sep 26 2019 Leontiy Volodin <lvol@altlinux.org> 0.6.4-alt1
- New version (0.6.4) with rpmgs script.

* Tue Aug 06 2019 Leontiy Volodin <lvol@altlinux.org> 0.6.3-alt1
- 0.6.3
- Fixed crash with vlc backend

* Mon Aug 05 2019 Leontiy Volodin <lvol@altlinux.org> 0.6.2-alt1
- 0.6.2

* Mon Jul 15 2019 Leontiy Volodin <lvol@altlinux.org> 0.5.5-alt2
- Added BR.

* Thu Jul 11 2019 Leontiy Volodin <lvol@altlinux.org> 0.5.5-alt1
- Initial build for ALT Sisyphus (thanks fedora for this spec)
