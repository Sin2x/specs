Name: deepin-screensaver
Version: 5.0.4
Release: alt1
Summary: Screensaver Tool
License: GPL-3.0+
Group: Graphical desktop/Other
Url: https://github.com/linuxdeepin/deepin-screensaver
Packager: Leontiy Volodin <lvol@altlinux.org>

Source: %url/archive/%version/%name-%version.tar.gz

BuildRequires: gcc-c++ qt5-base-devel qt5-x11extras-devel qt5-declarative-devel libXScrnSaver-devel
# BuildRequires: xscreensaver-modules xscreensaver-modules-gl

%description
Deepin screensaver viewer and tools.

%package modules
Summary: Screensaver modules
Group: Graphical desktop/Other
BuildArch: noarch
AutoReq: no
Requires: xscreensaver-modules xscreensaver-modules-gl

%description modules
Extra modules for Deepin Screensaver.

%prep
%setup
%__subst 's|/lib/|/libexec/|' common.pri xscreensaver/xscreensaver.pro
%__subst 's|/usr/lib|/usr/libexec|' common.pri tools/preview/main.cpp

%build
%qmake_qt5 PREFIX=%prefix
%make_build

%install
%makeinstall INSTALL_ROOT=%buildroot

%files
%doc CHANGELOG.md
%_bindir/%name
%_datadir/dbus-1/services/*
%_datadir/dbus-1/interfaces/*

%files modules
%_prefix/libexec/%name/

%changelog
* Fri Sep 11 2020 Leontiy Volodin <lvol@altlinux.org> 5.0.4-alt1
- Initial build for ALT Sisyphus (thanks fedora for this spec).
