%define rname alt-app-starter

Name: %rname
Version: 1.1.3
Release: alt1
%K5init altplace

Group: Graphical desktop/KDE
Summary: The tool to run programs as another user
License: GPLv2

Source: %rname-%version.tar

BuildRequires(pre): rpm-build-kf5
BuildRequires: extra-cmake-modules
BuildRequires: gcc-c++
BuildRequires: kf5-kactivities-devel
BuildRequires: kf5-kcmutils-devel
BuildRequires: kf5-kdeclarative-devel
BuildRequires: kf5-kdesu-devel
BuildRequires: kf5-kdoctools-devel-static
BuildRequires: kf5-ki18n-devel
BuildRequires: kf5-kiconthemes-devel
BuildRequires: kf5-kinit-devel
BuildRequires: kf5-kio-devel
BuildRequires: kf5-kpackage-devel
BuildRequires: kf5-kpty-devel
BuildRequires: kf5-kwindowsystem-devel
BuildRequires: plasma5-workspace-devel
BuildRequires: qt5-base-devel
BuildRequires: qt5-script-devel
BuildRequires: qt5-svg-devel
BuildRequires: qt5-x11extras-devel
BuildRequires: qt5-base-devel
BuildRequires: qt5-tools
Requires: qt5-translations

%description
Alt-App-Starter is the tool to quickly run programs as another user.
This tool was designed to work with KDE.

%prep
%setup -n %rname-%version

%build
%K5build 
lrelease-qt5 translations/alt-app-starter_ru.ts

%install
%K5install

# translations
mkdir -p %buildroot/%_qt5_translationdir/
install -m 0644 translations/*.qm %buildroot/%_qt5_translationdir/

%find_lang --with-qt --all-name %rname

%files -f %rname.lang
%doc COPYING*
%_K5bin/*
%_K5xdgapp/*.desktop

%changelog
* Thu Feb 06 2020 Pavel Moseev <mars@altlinux.org>  1.1.3-alt1
- fix launch of console applications (closes: #37872)
- upgrade the utility description in the spec file (closes: #37978)
- fix behavior of utility after successful application launch (closes: #37979)
- fix some user interface elements (closes: #37980)
- preferred terminal emulator is read from system settings

* Fri Jan 24 2020 Pavel Moseev <mars@altlinux.org>  1.1.2-alt1
- fix user interface translation

* Thu Jan 23 2020 Pavel Moseev <mars@altlinux.org>  1.1.1-alt1
- fix application title icon (#37870)
- fix behavior of alt-app-starter utility after starting selected app. (#37871)
- removed unused interface elements (#37873)

* Mon Jan 13 2020 Pavel Moseev <mars@altlinux.org>  1.1.0-alt1
- First version. Initial build

