%define rname plasma-nano

Name: plasma5-nano
Version: 5.26.3
Release: alt1
%K5init altplace

Group: Graphical desktop/KDE
Summary: KDE Plasma 5 minimal shell
Url: http://www.kde.org
License: GPL-2.0-or-later AND LGPL-2.1-or-later

Source: %rname-%version.tar

# Automatically added by buildreq on Thu Feb 20 2020 (-bi)
# optimized out: cmake cmake-modules elfutils fontconfig gcc-c++ glibc-kernheaders-generic glibc-kernheaders-x86 kf5-kconfig-devel kf5-kcoreaddons-common kf5-kcoreaddons-devel kf5-kjobwidgets-common kf5-kwidgetsaddons-common kf5-kwindowsystem-devel libglvnd-devel libgpg-error libqt5-core libqt5-dbus libqt5-gui libqt5-network libqt5-qml libqt5-quick libqt5-svg libqt5-widgets libqt5-x11extras libqt5-xml libsasl2-3 libstdc++-devel libwayland-client libxcbutil-keysyms perl python-modules python2-base python3 python3-base qt5-base-common qt5-base-devel qt5-declarative-devel rpm-build-python3 rpm-build-qml sh4
#BuildRequires: appstream extra-cmake-modules kf5-ki18n-devel kf5-kpackage-devel kf5-kservice-devel kf5-kwayland-devel kf5-plasma-framework-devel libssl-devel python-modules-compiler python3-dev qt5-translations qt5-wayland-devel rpm-build-gir
BuildRequires(pre): rpm-build-kf5
BuildRequires: qt5-base-devel qt5-wayland-devel
BuildRequires: extra-cmake-modules kf5-ki18n-devel kf5-kpackage-devel kf5-kservice-devel kf5-kwayland-devel
BuildRequires: kf5-plasma-framework-devel

%description
A minimal plasma shell package intended for embedded devices.

%package common
Summary: %name common package
Group: System/Configuration/Other
BuildArch: noarch
Requires: kf5-filesystem
%description common
%name common package

%package devel
Group: Development/KDE and QT
Summary: Development files for %name
%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%package -n libplasma-nano
Group: System/Libraries
Summary: %name library
Requires: %name-common
%description -n libplasma-nano
%name library


%prep
%setup -n %rname-%version

%build
%K5build

%install
%K5install
%find_lang %name --all-name

%files -f %name.lang
%doc LICENSES/*
%_K5qml/org/kde/plasma/private/nanoshell/
%_K5data/plasma/packages/org.kde.plasma.nano.desktoptoolbox/
%_K5data/plasma/shells/org.kde.plasma.nano/
%_K5srv/*.desktop

%changelog
* Tue Nov 08 2022 Sergey V Turchin <zerg@altlinux.org> 5.26.3-alt1
- new version

* Thu Oct 27 2022 Sergey V Turchin <zerg@altlinux.org> 5.26.2-alt1
- new version

* Wed Sep 07 2022 Sergey V Turchin <zerg@altlinux.org> 5.25.5-alt1
- new version

* Wed Aug 17 2022 Sergey V Turchin <zerg@altlinux.org> 5.25.4-alt1
- new version

* Mon Jul 11 2022 Sergey V Turchin <zerg@altlinux.org> 5.24.6-alt1
- new version

* Wed May 04 2022 Sergey V Turchin <zerg@altlinux.org> 5.24.5-alt1
- new version

* Wed Mar 30 2022 Sergey V Turchin <zerg@altlinux.org> 5.24.4-alt1
- new version

* Mon Jan 10 2022 Sergey V Turchin <zerg@altlinux.org> 5.23.5-alt1
- new version

* Wed Dec 01 2021 Sergey V Turchin <zerg@altlinux.org> 5.23.4-alt1
- new version

* Wed Nov 10 2021 Sergey V Turchin <zerg@altlinux.org> 5.23.3-alt1
- new version

* Mon Nov 01 2021 Sergey V Turchin <zerg@altlinux.org> 5.23.2-alt1
- new version

* Wed Sep 01 2021 Sergey V Turchin <zerg@altlinux.org> 5.22.5-alt1
- new version

* Tue Jul 27 2021 Sergey V Turchin <zerg@altlinux.org> 5.22.4-alt1
- new version

* Fri Jul 16 2021 Sergey V Turchin <zerg@altlinux.org> 5.22.3-alt2
- fix package

* Wed Jul 07 2021 Sergey V Turchin <zerg@altlinux.org> 5.22.3-alt1
- new version

* Thu Jul 01 2021 Sergey V Turchin <zerg@altlinux.org> 5.22.2-alt1
- new version

* Thu May 13 2021 Sergey V Turchin <zerg@altlinux.org> 5.21.5-alt1
- new version

* Tue Apr 06 2021 Sergey V Turchin <zerg@altlinux.org> 5.21.4-alt1
- new version

* Fri Mar 19 2021 Sergey V Turchin <zerg@altlinux.org> 5.21.3-alt1
- new version

* Mon Jan 11 2021 Sergey V Turchin <zerg@altlinux.org> 5.20.5-alt1
- new version

* Wed Dec 02 2020 Sergey V Turchin <zerg@altlinux.org> 5.20.4-alt1
- new version

* Wed Oct 28 2020 Sergey V Turchin <zerg@altlinux.org> 5.20.2-alt1
- new version

* Thu Sep 17 2020 Sergey V Turchin <zerg@altlinux.org> 5.19.5-alt1
- new version

* Tue Jul 28 2020 Sergey V Turchin <zerg@altlinux.org> 5.19.4-alt1
- new version

* Tue Jul 07 2020 Sergey V Turchin <zerg@altlinux.org> 5.19.3-alt1
- new version

* Thu May 07 2020 Sergey V Turchin <zerg@altlinux.org> 5.18.5-alt1
- new version

* Thu Apr 02 2020 Sergey V Turchin <zerg@altlinux.org> 5.18.4-alt1
- new version

* Wed Mar 11 2020 Sergey V Turchin <zerg@altlinux.org> 5.18.3-alt1
- new version

* Thu Feb 20 2020 Sergey V Turchin <zerg@altlinux.org> 5.18.1-alt1
- initial build
