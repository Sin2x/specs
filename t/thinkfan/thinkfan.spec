%define _unpackaged_files_terminate_build 1

Name: thinkfan
Version: 1.2.1
Release: alt1
Summary: simple and lightweight fan control program
Group: System/Configuration/Hardware
License: GPL-3.0+
Url: http://sourceforge.net/projects/thinkfan/

# https://github.com/vmatare/thinkfan.git
Source: %name-%version.tar

Patch1: thinkfan-install.patch
Patch2: thinkfan-alt-paths.patch

BuildRequires: cmake gcc-c++ libatasmart-devel
BuildRequires: libyaml-cpp-devel
BuildRequires: libsystemd-devel

%description
Thinkfan is a simple, lightweight fan control program. Originally designed
specifically for IBM/Lenovo Thinkpads, it now supports any kind of system via
the sysfs hwmon interface (/sys/class/hwmon). It is designed to eat as little
CPU power as possible.

%prep
%setup
%patch1 -p1
%patch2 -p1

%build
%cmake \
	-DUSE_ATASMART:BOOL=ON \
	%nil

%cmake_build

%install
%cmakeinstall_std

%files
%doc COPYING
%doc README.md examples/*
%dir %_sysconfdir/systemd/system/thinkfan.service.d
%config(noreplace) %_sysconfdir/systemd/system/thinkfan.service.d/override.conf
%_unitdir/*.service
%_sbindir/%name
%_man1dir/%name.1*
%_man5dir/*.5*

%changelog
* Tue Apr 13 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 1.2.1-alt1
- Updated to upstream version 1.2.1.

* Sun Sep 14 2014 Terechkov Evgenii <evg@altlinux.org> 0.9.1-alt1
- Initial build for ALT Linux Sisyphus
