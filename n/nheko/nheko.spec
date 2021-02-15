%define _unpackaged_files_terminate_build 1

Name: nheko
Version: 0.8.1
Release: alt1

Summary: Desktop client (QT) for the Matrix protocol

Group: Development/Other
License: GPLv3
Url: https://github.com/Nheko-Reborn/nheko.git

Source: %name-%version.tar

BuildRequires: cmake gcc-c++
BuildRequires: qt5-tools-devel qt5-multimedia-devel qt5-svg-devel
BuildRequires: qt5-declarative-devel qt5-quickcontrols2-devel
BuildRequires: libqtkeychain-qt5-devel
BuildRequires: boost-asio-devel boost-devel-headers boost-signals-devel
BuildRequires: libssl-devel zlib-devel libtweeny-devel liblmdbxx-devel
BuildRequires: libmtxclient-devel liblmdb-devel cmark-devel
BuildRequires: nlohmann-json-devel libfmt-devel
BuildRequires: libolm-devel libsodium-devel libspdlog-devel
BuildRequires: gst-plugins-bad-devel gst-plugins-devel
BuildRequires: libpcre-devel
BuildRequires: libmount-devel
BuildRequires: libblkid-devel
BuildRequires: libuuid-devel
BuildRequires: libselinux-devel

# Additional (runtime) dependencies
Requires: qt5-graphicaleffects qt5-quickcontrols2 qt5-multimedia

%description
The motivation behind the project is to provide a native desktop app
for Matrix that feels more like a mainstream chat app (Riot, Telegram etc)
and less like an IRC client.

%prep
%setup

%build
%cmake -DUSE_BUNDLED_BOOST=OFF  \
       -DUSE_BUNDLED_SPDLOG=OFF \
       -DUSE_BUNDLED_OLM=OFF    \
       -DUSE_BUNDLED_CMARK=OFF  \
       -DUSE_BUNDLED_LMDBXX=OFF \
       -DUSE_BUNDLED_TWEENY=OFF \
       -DUSE_BUNDLED_MATRIX_CLIENT=OFF \
       -DCMAKE_BUILD_TYPE=Release

# Adjust nprocs for git.alt
[ ${NPROCS:-%__nprocs} -le 16 ] || NPROCS=16
%cmake_build

%install
%cmakeinstall_std

%files
%doc README.md COPYING
%_bindir/*
%_desktopdir/*.desktop
%_iconsdir/hicolor/*/apps/*.png
%_iconsdir/hicolor/*/apps/*.svg
%_datadir/metainfo/*.appdata.xml

%changelog
* Sun Feb 14 2021 Paul Wolneykien <manowar@altlinux.org> 0.8.1-alt1
- Fixed build requirements for new version.
- Fresh up to v0.8.1.

* Fri Jul 10 2020 Paul Wolneykien <manowar@altlinux.org> 0.7.2-alt2
- Fix: Additional (runtime) QT dependencies.

* Wed Jul 08 2020 Paul Wolneykien <manowar@altlinux.org> 0.7.2-alt1
- Fresh up to v0.7.2.
- Package the SVG icon.

* Tue Mar 31 2020 Paul Wolneykien <manowar@altlinux.org> 0.6.4-alt1
- New upstream: https://github.com/Nheko-Reborn/nheko.git
- Added -DCMAKE_BUILD_TYPE=Release
- New upstream version 0.6.4.

* Wed Dec 05 2018 Paul Wolneykien <manowar@altlinux.org> 0.6.2-alt2
- Adjust nprocs for git.alt (<= 16).

* Mon Dec 03 2018 Paul Wolneykien <manowar@altlinux.org> 0.6.2-alt1
- Initial release.
