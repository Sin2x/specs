%define _name lurch

Name: purple-plugin-lurch
Version: 0.6.8
Release: alt1

Summary: OMEMO for libpurple
License: GPL-3.0-only
Group: Networking/Instant messaging

Url: https://github.com/gkdr/lurch

# repacked https://github.com/gkdr/lurch/releases/download/v%version/lurch-%version-src.tar.gz
Source: %_name-%version-src.tar

Patch1: 0001-SUSE-libomemo-fix-dino-compat.patch
Patch2: 0002-ALT-fix-linking-with-libjabber.so.patch

BuildRequires: cmake gcc-c++ libgcrypt-devel libmxml-devel libpurple-devel libsqlite3-devel libxml2-devel

%description
This plugin brings Double Ratchet to libpurple applications such as
Pidgin by implementing OMEMO.

%prep
%setup -n %_name-%version
%autopatch -p2

%build
export CFLAGS='%optflags'
%make_build

%install
%makeinstall_std

%files
%doc LICENSE README.md
%_libdir/purple-2/%_name.so

%changelog
* Sat Oct 05 2019 Vladimir D. Seleznev <vseleznv@altlinux.org> 0.6.8-alt1
- Initial build for ALT Sisyphus based on openSUSE spec file.
