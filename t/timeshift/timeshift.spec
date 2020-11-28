%define _unpackaged_files_terminate_build 1

Name: timeshift
Version: 20.11.1
Summary: System restore tool for Linux
Release: alt1
License: GPLv3
Group: Archiving/Backup
URL: https://github.com/teejee2008/timeshift.git
Source: %name-%version.tar

BuildRequires: vala
BuildRequires: libjson-glib-devel
BuildRequires: libgee0.8-devel
BuildRequires: libvte3-devel
Requires: rsync

%description
System restore tool for Linux. Creates filesystem snapshots using
rsync+hardlinks, or BTRFS snapshots. Supports scheduled snapshots, multiple back
up levels, and exclude filters. Snapshots can be restored while system is
running or from Live CD/USB.

%prep
%setup

%build
%make_build

%install
%makeinstall_std
rm -f %buildroot%_bindir/%name-uninstall
%find_lang %name

%files -f %name.lang
%_bindir/%name
%_bindir/%name-gtk
%_bindir/%name-launcher
%_man1dir/%name.1.xz
%_datadir/%name/images/*
%_sysconfdir/%name/default.json
%_desktopdir/%name-gtk.desktop
%_iconsdir/hicolor/*/apps/%name.png
%_datadir/metainfo/%name.appdata.xml
%_datadir/polkit-1/actions/in.teejeetech.pkexec.timeshift.policy
%doc README.md

%changelog
* Tue Nov 24 2020 Alexander Makeenkov <amakeenk@altlinux.org> 20.11.1-alt1
- Updated to version 20.11.1

* Sun Mar 08 2020 Alexander Makeenkov <amakeenk@altlinux.org> 20.03-alt1
- New version

* Tue Nov 05 2019 Alexander Makeenkov <amakeenk@altlinux.org> 19.08.1-alt1
- New version 19.08.1
- Fixed build

* Tue Feb 12 2019 Mikhail Savostyanov <mik@altlinux.org> 19.01-alt1
- New version 19.01

* Wed Apr 18 2018 Mikhail Savostyanov <mik@altlinux.org> 18.4-alt1
- New version 18.4

* Fri Feb 9 2018 Mikhail Savostyanov <mik@altlinux.org> 18.2-alt1
- initial build for ALT
