%define _unpackaged_files_terminate_build 1

Name: wl-clipboard
Version: 1.0.0.0.53.c010972
Release: alt1
Summary: Command-line copy/paste utilities for Wayland
Group: System/X11
License: GPLv3+
Url: https://github.com/bugaevc/wl-clipboard
Source0: %name-%version.tar

BuildRequires: meson
BuildRequires: wayland-devel libwayland-client-devel wayland-protocols

%description
Command-line Wayland clipboard utilities, `wl-copy` and `wl-paste`,
that let you easily copy data between the clipboard and Unix pipes,
sockets, files and so on.

%prep
%setup

%build
%meson
%meson_build

%install
%meson_install

%check
%meson_test

%files
%doc README.md COPYING
%_bindir/wl-copy
%_bindir/wl-paste
%_man1dir/*
%_datadir/bash-completion/completions/*

%changelog
* Tue Aug 20 2019 Alexey Shabalin <shaba@altlinux.org> 1.0.0.0.53.c010972-alt1
- initial package

