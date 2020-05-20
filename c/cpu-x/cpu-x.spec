# Unpackaged files in buildroot should terminate build
%define _unpackaged_files_terminate_build 1

Name: cpu-x
Version: 4.0.0
Release: alt1
Summary: CPU-X is a Free software that gathers information on CPU, motherboard and more
License: GPL-3.0-or-later
Group: System/Kernel and hardware
Url: https://github.com/X0rg/CPU-X
Source: %name-%version.tar
Buildrequires(pre): rpm-macros-cmake
Buildrequires: gcc-c++ cmake pkgconfig(gtk+-3.0) pkgconfig(libarchive) pkgconfig(libcurl) pkgconfig(libpci) pkgconfig(libprocps) pkgconfig(libstatgrab) pkgconfig(ncurses) pkgconfig(libcpuid)
Requires: icon-theme-hicolor

ExclusiveArch: %ix86 x86_64 aarch64 armh

%description
CPU-X is a Free software that gathers information on CPU, motherboard and more.
CPU-X is similar to CPU-Z (Windows), but CPU-X is a Free and Open Source
software designed for GNU/Linux; also, it works on *BSD.
This software is written in C and built with CMake tool.
It can be used in graphical mode by using GTK or in text-based mode by using
NCurses. A dump mode is present from command line.

%prep
%setup

%build
%cmake
%cmake_build

%install
%cmakeinstall_std
%find_lang %name

# Cleanup unpackage files
rm -r %buildroot%_datadir/fish
rm -r %buildroot%_datadir/zsh
rm -r %buildroot%_datadir/locale/zh_Hant

%files -f %name.lang
%_bindir/*
%_datadir/%name
%_iconsdir/hicolor/*/*/*
%_desktopdir/*
%_datadir/polkit-1/actions/*
%_datadir/metainfo/*.appdata.xml
%_datadir/bash-completion/completions/*
%_datadir/glib-2.0/schemas/*
%_prefix/libexec/*

%changelog
* Wed May 20 2020 Anton Midyukov <antohami@altlinux.org> 4.0.0-alt1
- new version 4.0.0

* Wed Apr 17 2019 Anton Midyukov <antohami@altlinux.org> 3.2.4-alt1
- new version 3.2.4
- drop xdg-su support

* Mon Oct 15 2018 Anton Midyukov <antohami@altlinux.org> 3.2.3-alt1
- new version 3.2.3

* Sun May 13 2018 Anton Midyukov <antohami@altlinux.org> 3.2.2-alt1
- new version 3.2.2

* Wed Apr 11 2018 Anton Midyukov <antohami@altlinux.org> 3.2.1-alt1
- new version 3.2.1

* Wed Jan 10 2018 Anton Midyukov <antohami@altlinux.org> 3.1.3.1-alt1
- new version 3.1.3.1

* Mon Sep 18 2017 Anton Midyukov <antohami@altlinux.org> 3.1.3-alt2
- fix run as root for sysvinit

* Tue Jan 31 2017 Anton Midyukov <antohami@altlinux.org> 3.1.3-alt1
- new version 3.1.3

* Mon Oct 24 2016 Anton Midyukov <antohami@altlinux.org> 3.1.2-alt1
- Initial build for Alt Linux Sisyphus.
