Name: seatd
Version: 0.5.0.9.g5ad91ae
Release: alt1
Summary: Minimal seat management daemon and universal library
License: MIT
Url: https://github.com/kennylevinsen/seatd
Group: System/Configuration/Boot and Init

Source0: %name-%version.tar
Source1: %name.init
Source2: %name.runner
Source3: %name.sysconfig

%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1

%set_verify_elf_method strict

%define _libexecdir /usr/libexec

%define soversion 1
%define soname seat%soversion

BuildRequires:  meson
BuildRequires:  scdoc

%description
Seat management takes care of mediating access to shared devices (graphics,
input), without requiring the applications needing access to be root.

%package -n lib%soname
Summary:  The seat library
Group:    System/Libraries

%description -n lib%soname
A seat management library allowing applications to use whatever seat management
is available.

%package -n lib%soname-devel
Summary:  Development libraries for lib%soname
Group:    Development/C

%description -n lib%soname-devel
Header and Library files for doing development for lib%soname.

%prep
%setup

%build
%meson
%meson_build

%install
%meson_install

install -m755 -pD %SOURCE1 %buildroot%_initdir/%name
install -m755 -pD %SOURCE2 %buildroot%_libexecdir/%name-runner
install -m644 -pD %SOURCE3 %buildroot%_sysconfdir/sysconfig/%name
install -m644 -pD contrib/systemd/seatd.service %buildroot%_unitdir/%name.service

%post
%post_service %name

%preun
%preun_service %name

%files
%doc LICENSE
%doc README.md
%config(noreplace) %_sysconfdir/sysconfig/%name
%_initdir/%name
%_unitdir/%name.service
%_libexecdir/%name-runner
%_bindir/%name
%_man1dir/*

%files -n lib%soname
%_libdir/*.so.*

%files -n lib%soname-devel
%_libdir/*.so
%_includedir/*.h
%_pkgconfigdir/*.pc

%changelog
* Fri Mar 26 2021 Alexey Gladkov <legion@altlinux.ru> 0.5.0.9.g5ad91ae-alt1
- Initial build
