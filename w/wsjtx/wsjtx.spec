Name: wsjtx
Version: 2.5.4
Release: alt1
Summary: WSJT-X implements communication protocols or "modes" called JT4, JT9, JT65, and WSPR
License: GPL-3.0
Group: Engineering
Url: http://physics.princeton.edu/pulsar/k1jt/wsjtx.html

# Source-url: http://physics.princeton.edu/pulsar/k1jt/%name-%version.tgz
Source: %name-%version.tar

Buildrequires(pre): rpm-macros-cmake
BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: ctags
BuildRequires: openmpi-devel
BuildRequires: hamlib-devel
BuildRequires: pkgconfig(libxslt)
BuildRequires: libudev-devel
BuildRequires: boost-program_options-devel
BuildRequires: boost-filesystem-devel
BuildRequires: boost-log-devel
BuildRequires: libgomp-devel
BuildRequires: libportaudio2-devel
BuildRequires: libfftw3-devel
BuildRequires: pkgconfig(libusb-1.0)
BuildRequires: qt5-base-devel
BuildRequires: qt5-tools-devel
BuildRequires: pkgconfig(Qt5Concurrent)
BuildRequires: pkgconfig(Qt5Multimedia)
BuildRequires: pkgconfig(Qt5SerialPort)
BuildRequires: ImageMagick-tools
BuildRequires: dos2unix
BuildRequires: desktop-file-utils
BuildRequires: makeinfo
BuildRequires: asciidoctor
BuildRequires: asciidoc-a2x

Provides: %name-data = %EVR
Obsoletes: %name-data < %EVR

%description
WSJT-X implements communication protocols or "modes" called JT4, JT9, JT65, and
WSPR, as well as one called Echo for detecting and measuring your radio signals
reflected from the Moon.  The JTxx modes were all designed for making reliable,
confirmed QSOs under extreme weak-signal conditions.  They use nearly identical
message structure and "source encoding," the efficient compression of standard
messages.  JT65 was designed for EME ("moonbounce") on the VHF/UHF bands, and
has also proved very popular and effective for worldwide QRP communication at
HF. In contrast, JT9 is optimized for the LF, MF, and HF bands.  JT9 is about 2
dB more sensitive than JT65 while using less than 10 procent of the bandwidth.
With either JT9 or JT65, world-wide QSOs are possible with power levels of a few
watts and compromise antennas.  JT4 is particularly optimized for EME on the
microwave bands from 2.3 to 24 GHz.  Finally, as described more fully on its
own page, WSPR mode implements a protocol designed for probing potential
propagation paths with low-power transmissions.  WSPR has now been fully
implemented within WSJT-X, including automatic band-hopping, so all modes are
available in a single program.

%prep
%setup

# remove bundled hamlib
rm -f src/hamlib.tgz*
tar -xzf src/%name.tgz

# remove archive
rm -f src/wsjtx.tgz*

pushd %name
# remove bundled boost
rm -rf boost

# convert CR + LF to LF
dos2unix *.ui *.iss *.txt
popd

%build
%define optflags_lto %nil

pushd %name
%cmake -DWSJT_GENERATE_DOCS=TRUE \
       -Dhamlib_STATIC=FALSE \
       -DBoost_NO_SYSTEM_PATHS=FALSE
%cmake_build
popd

%install
pushd %name
%cmakeinstall_std
%find_lang %name

for x in 16 32 48; do
    mkdir -p %buildroot%_iconsdir/hicolor/$x'x'$x/apps/
    convert %buildroot%_pixmapsdir/wsjtx_icon.png -resize $x'x'$x %buildroot/%_iconsdir/hicolor/$x'x'$x/apps/wsjtx_icon.png
done

# desktop files
desktop-file-validate %buildroot%_desktopdir/wsjtx.desktop
desktop-file-validate %buildroot%_desktopdir/message_aggregator.desktop

# fix docs
install -p -m 0644 -t %buildroot%_docdir/%name GUIcontrols.txt jt9.txt \
  v1.7_Features.txt wsjtx_changelog.txt

popd

%files -f %name/%name.lang
%_bindir/*
%_desktopdir/*.desktop
%_man1dir/*
%exclude %_pixmapsdir/*
%_liconsdir/wsjtx_icon.png
%_niconsdir/wsjtx_icon.png
%_miconsdir/wsjtx_icon.png
%_datadir/%name
%_docdir/%name

%changelog
* Sat Mar 12 2022 Anton Midyukov <antohami@altlinux.org> 2.5.4-alt1
- new version (2.5.4) with rpmgs script (Closes: 42108)
- cleanup spec
- drop old patches
- obsoletes data subpackage

* Sat Aug 28 2021 Anton Midyukov <antohami@altlinux.org> 2.2.2-alt2
- disable LTO compiler flag

* Sun Aug 16 2020 Anton Midyukov <antohami@altlinux.org> 2.2.2-alt1
- new version (2.2.2) with rpmgs script

* Sun Jan 12 2020 Anton Midyukov <antohami@altlinux.org> 2.1.2-alt1
- new version (2.1.2) with rpmgs script

* Thu Oct 24 2019 Anton Midyukov <antohami@altlinux.org> 2.1.0-alt1
- new version (2.1.0) with rpmgs script

* Sun Dec 23 2018 Anton Midyukov <antohami@altlinux.org> 2.0.0-alt1
- new version (2.0.0) with rpmgs script

* Wed Jun 27 2018 Anton Midyukov <antohami@altlinux.org> 1.9.1-alt1.S1
- new version 1.9.1

* Wed May 16 2018 Anton Midyukov <antohami@altlinux.org> 1.9.0-alt2.S1
- Added alt-cmake.patch (thanks darktemplar)

* Mon May 14 2018 Anton Midyukov <antohami@altlinux.org> 1.9.0-alt1.S1
- Release candidate 1.9.0-RC4

* Thu Nov 23 2017 Anton Midyukov <antohami@altlinux.org> 1.8.0-alt2.S1
- Release 1.8.0
- Build with system hamlib
- Build with system boost
- Enable build documentation
- Exclusive arch x86-64

* Mon Sep 04 2017 Anton Midyukov <antohami@altlinux.org> 1.8.0-alt1
- Release candidate 2

* Wed Aug 02 2017 Anton Midyukov <antohami@altlinux.org> 1.7.0-alt2
- Fix requires

* Tue Jan 31 2017 Anton Midyukov <antohami@altlinux.org> 1.7.0-alt1
- new version (1.7.0) with rpmgs script

* Thu Oct 20 2016 Anton Midyukov <antohami@altlinux.org> 1.6.0-alt1
- Initial build for Alt Linux Sisyphus.
