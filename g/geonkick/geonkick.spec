
%define _unpackaged_files_terminate_build 1

Name:     geonkick
Version:  2.9.1
Release:  alt1

Summary:  A free software percussion synthesizer
License:  GPL-3.0
Group:    Sound
Url:      https://github.com/free-sm/geonkick
# https://gitlab.com/iurie-sw/geonkick

Source:   %name-%version.tar

BuildRequires: cmake gcc-c++
BuildRequires: pkgconfig(RapidJSON)
BuildRequires: pkgconfig(cairo)
BuildRequires: pkgconfig(lv2)
BuildRequires: pkgconfig(jack)
BuildRequires: pkgconfig(sndfile)

Requires: %name-common

%description
Geonkick is a synthesizer that can synthesize elements of percussion.
The most basic examples are: kicks, snares, hit-hats, shakers, claps.

This package contains a standalone (jack) version on Geonkick.

%package  common
Group:    Sound
Summary:  Common files for Geonkick -- A free software percussion synthesizer

%description common
Geonkick is a synthesizer that can synthesize elements of percussion.
The most basic examples are: kicks, snares, hit-hats, shakers, claps.

This package contains common files that are used by all builds
of Geonkick.

%package -n lv2-geonkick-plugins
Group:    Sound
Summary:  A free software percussion synthesizer -- lv2
Requires: %name-common

%description -n lv2-geonkick-plugins
Geonkick is a synthesizer that can synthesize elements of percussion.
The most basic examples are: kicks, snares, hit-hats, shakers, claps.

This package contains Geonkick build as LV2 plugins.

%prep
%setup

# linking with libstdc++fs is not needed with and not supported by
# recent gcc/libstdc++
find . -name 'CMakeLists.txt' -exec sed -i '/lstdc++fs/d' '{}' ';'

%build
%cmake
%cmake_build

%install
%cmakeinstall_std

%files
%_bindir/*
%_man1dir/%name.*
%_desktopdir/%name.desktop
%_iconsdir/hicolor/*/apps/*
%_datadir/mime/*

%files common
%_datadir/%name

%files -n lv2-geonkick-plugins
%_libdir/lv2/*.lv2


%changelog
* Thu Aug 04 2022 Ivan A. Melnikov <iv@altlinux.org> 2.9.1-alt1
- Initial build for Sisyphus
