%define _unpackaged_files_terminate_build 1

%def_disable	build_test

Name: opencpn
Version: 5.7.1
Release: alt0.2
Summary: A free and open source software for marine navigation

Group: Other
License: GPL-2.0-or-later
Url: http://opencpn.org
Source0: OpenCPN-%version.tar.gz
Source1: %name.desktop

ExcludeArch: ppc64le

Requires: %name-data

# Automatically added by buildreq on Mon Mar 25 2013
# optimized out: cmake-modules fontconfig fontconfig-devel glib2-devel libGL-devel libICE-devel libSM-devel libX11-devel libXau-devel libXext-devel libXfixes-devel libXft-devel libXi-devel libXrender-devel libatk-devel libcairo-devel libfreetype-devel libgdk-pixbuf libgdk-pixbuf-devel libgio-devel libpango-devel libstdc++-devel pkg-config xorg-kbproto-devel xorg-xf86miscproto-devel xorg-xproto-devel
BuildRequires: bzlib-devel cmake gcc-c++ libGLU-devel libXScrnSaver-devel libXcomposite-devel libXcursor-devel libXdamage-devel libXdmcp-devel libXinerama-devel libXpm-devel libXrandr-devel libXt-devel libXtst-devel libXv-devel libXxf86misc-devel libXxf86vm-devel libxkbfile-devel zlib-devel
BuildRequires: lsb-release libflac-devel libogg-devel libvorbis-devel libopus-devel

BuildRequires: libwxGTK3.2-devel libgtk+3-devel

BuildRequires: libcairo-devel libdrm-devel libtiff-devel libmount-devel libblkid-devel
BuildRequires: libselinux-devel libxkbcommon-devel libwayland-cursor-devel libwayland-egl-devel
BuildRequires: libepoxy-devel at-spi2-atk-devel libat-spi2-core-devel

BuildRequires: libffi-devel libfribidi-devel libuuid-devel libpixman-devel
BuildRequires: libthai-devel libdatrie-devel

BuildRequires: tinyxml-devel libgps-devel libportaudio2-devel libcurl-devel libexpat-devel
BuildRequires: liblz4-devel liblzma-devel libsndfile-devel libarchive-devel libelf-devel
BuildRequires: libexif-devel libwxsvg-devel libsqlite3-devel libusb-devel
BuildRequires: libjpeg-devel libjasper-devel libbrotli-devel

#Sisyphus:
#[x86_64] Package 'libpcre2-8', required by 'glib-2.0', not found
#[x86_64] Package libpcre2-8 was not found in the pkg-config search path.
#[x86_64] Perhaps you should add the directory containing `libpcre2-8.pc'
BuildRequires: libpcre2-devel

# use bundled wxcurl: none in Sisyphus 20190327
# use bundled unarr : none in Sisyphus 20190327

%description
OpenCPN is a free software project to create a concise chart plotter
and navigation software, for use underway or as a planning tool.
OpenCPN is developed by a team of active sailors using real world
conditions for program testing and refinement. Files developed in
this project are copyright (c) The OpenCPN developers and distributed
using a GPLv2+ license. OpenCPN also uses code from other sources
with other licenses (look to the LICENSING file).

%package data
Summary: Architecture independent files for OpenCPN
Group: Other
BuildArch: noarch
Requires: icon-theme-hicolor

%description data
Architecture independent files for OpenCPN.

%prep
%setup -n OpenCPN-%version

%build

#-DOCPN_BUILD_TEST=0: https://github.com/OpenCPN/OpenCPN/issues/2799
%if_enabled build_test
%cmake -DBUNDLE_DOCS=1 -DBUNDLE_TCDATA=1 -DBUNDLE_GSHHS=1
%else
%cmake -DBUNDLE_DOCS=1 -DBUNDLE_TCDATA=1 -DBUNDLE_GSHHS=1 -DOCPN_BUILD_TEST=0
%endif

%cmake_build

%install
%cmake_install
cp -f %SOURCE1 %buildroot%_datadir/applications

# It is copied from %%_builddir by %%doc macro, so removed from %%buildroot
# /usr/share/doc/opencpn/changelog
# /usr/share/doc/opencpn/copyright
rm -rf %buildroot/%_datadir/doc

%find_lang %name
%find_lang --append --output=%name.lang %name-dashboard_pi
%find_lang --append --output=%name.lang %name-grib_pi
%find_lang --append --output=%name.lang %name-wmm_pi
%find_lang --append --output=%name.lang %name-chartdldr_pi

%if_enabled build_test
rm -rf %buildroot/%_libdir/cmake
rm -rf %buildroot/%_includedir
rm -rf %buildroot/%_libdir/*.a
rm -rf %buildroot/%_pkgconfigdir
%endif

%files
%doc data/license.txt
%doc data/copyright
%doc data/changelog
%doc LICENSING

%_bindir/opencpn
%_bindir/opencpn-cmd

%dir %_libdir/%name
%_libdir/opencpn/*_pi.so

%files data -f %name.lang
%doc data/doc/*
%_man1dir/opencpn.*

%_datadir/metainfo/opencpn.appdata.xml

%dir %_datadir/%name
%dir %_datadir/%name/sounds
%dir %_datadir/%name/gshhs
%dir %_datadir/%name/tcdata
%dir %_datadir/%name/s57data
%dir %_datadir/%name/uidata
%dir %_datadir/%name/plugins

%_datadir/%name/sounds/*
%_datadir/%name/gshhs/*
%_datadir/%name/tcdata/*
%_datadir/%name/s57data/*
%_datadir/%name/uidata/*
%_datadir/%name/plugins/*

%_datadir/%name/license.txt
%_datadir/%name/ocpn-plugins.xml

%dir %_datadir/%name/doc
%_datadir/%name/doc/help_web.html

%_datadir/%name/opencpn.png

%_iconsdir/hicolor/64x64/apps/*
%_iconsdir/hicolor/48x48/apps/*
%_iconsdir/hicolor/scalable/apps/*
%_datadir/applications/%name.desktop

%_datadir/%name/COPYING.gplv2
%_datadir/%name/COPYING.gplv3
%_datadir/%name/COPYING.lgplv2
%_datadir/%name/COPYING.lgplv3
%_datadir/%name/CoC-909_2013-InlandECDIS_20170308s.pdf
%_datadir/%name/LICENSING
%_datadir/%name/LINUX_DEVICES.md
%_datadir/%name/authors.html
%_datadir/%name/license.html

%changelog
* Sun Oct 30 2022 Sergey Y. Afonin <asy@altlinux.org> 5.7.1-alt0.2
- changes in spec file:
  + removed build time switch for switching gtk+2/gtk+3
  + added build time switch for enable build tests

* Sat Oct 29 2022 Sergey Y. Afonin <asy@altlinux.org> 5.7.1-alt0.1
- New (development) version, 20221029 snapshot (due to build with libwxGTK 3.2)
- removed patches:
  + opencpn-5.0.0-mga-missing_glx_include.patch
  + opencpn-5.2.4-dashboard.cpp.patch
- switched to libpcre2-devel (due to same change of glib-2.0)

* Wed Apr 28 2021 Arseny Maslennikov <arseny@altlinux.org> 5.2.4-alt1.1
- NMU: spec: adapted to new cmake macros.

* Sun Feb 07 2021 Sergey Y. Afonin <asy@altlinux.org> 5.2.4-alt1
- New version
- added opencpn-5.2.4-dashboard.cpp.patch

* Wed Feb 03 2021 Sergey Y. Afonin <asy@altlinux.org> 5.2.0-alt1
- New version
- added icon-theme-hicolor to Requires of data subpackage
- removed patches:
  + opencpn-5.0.0-aarch64-plugindir.patch
  + opencpn-5.0.0-detection_of_wxWebview.patch

* Thu Apr 30 2020 Sergey Y. Afonin <asy@altlinux.org> 5.0.0-alt5
- built with GTK+3 (due to same change of libwxsvg-1.5.22-alt2)
- updated %%description

* Tue Apr 28 2020 Sergey Y. Afonin <asy@altlinux.org> 5.0.0-alt4
- updated License tag to SPDX syntax, changed to GPL-2.0-or-later
- built with GTK+2
- added patches from https://github.com/OpenCPN/OpenCPN/issues/1494
  + opencpn-5.0.0-mga-missing_glx_include.patch (fixed build with wxGTK 3.1.3)
  + opencpn-5.0.0-aarch64-plugindir.patch

* Tue Apr 21 2020 Sergey Y. Afonin <asy@altlinux.org> 5.0.0-alt3
- fixed FTBFS: added opencpn-5.0.0-detection_of_wxWebview.patch
- added build time switch for switching gtk+2/gtk+3 (in spec-file)

* Tue Aug 20 2019 Anton Midyukov <antohami@altlinux.org> 5.0.0-alt2
- add_optflags (pkg-config --cflags pango) (Fix FTBFS)
- ExcludeArch: ppc64le

* Thu Mar 28 2019 Sergey Y. Afonin <asy@altlinux.ru> 5.0.0-alt1
- New version (thanx to TEAM)
- Built with wxGTK3.1
- Added some system libraries for building (ALT #36402)
- Disabled opencpn-4.4.0-fix_library_path.patch

* Wed Aug 22 2018 Grigory Ustinov <grenka@altlinux.org> 4.4.0-alt2
- Fix library path.
- Little cleanup spec.
- Fix bogus date in changelog.

* Thu Dec 01 2016 Sergey Y. Afonin <asy@altlinux.ru> 4.4.0-alt1
- New version

* Sun Feb 16 2014 Sergey Y. Afonin <asy@altlinux.ru> 3.2.2-alt1
- New version
- Moved architecture-independent data to noarch subpackage %name-data

* Wed Apr 03 2013 Sergey Y. Afonin <asy@altlinux.ru> 3.2.0-alt1
- Initial build for ALT Linux

* Sat Sep 22 2012 Eric 'Sparks' Christensen <sparks@fedoraproject.org> - 3.0.2-1
- Initial package.
