%define rname kgamma5

Name: plasma5-kgamma
Version: 5.26.3
Release: alt1
%K5init altplace

Group: Graphical desktop/KDE
Summary: KDE Workspace 5 Color profiling
Url: http://www.kde.org
License: GPL-2.0-or-later

Source: %rname-%version.tar
Patch1: alt-config-path.patch.patch
Patch2: alt-xf86gammacfg-args-clear.patch

# Automatically added by buildreq on Fri Jan 15 2016 (-bi)
# optimized out: cmake cmake-modules docbook-dtds docbook-style-xsl elfutils gcc-c++ kf5-kdoctools-devel libEGL-devel libGL-devel libICE-devel libSM-devel libX11-devel libXScrnSaver-devel libXau-devel libXcomposite-devel libXcursor-devel libXdamage-devel libXdmcp-devel libXext-devel libXfixes-devel libXft-devel libXi-devel libXinerama-devel libXmu-devel libXpm-devel libXrandr-devel libXrender-devel libXt-devel libXtst-devel libXv-devel libXxf86misc-devel libXxf86vm-devel libdbusmenu-qt52 libgpg-error libjson-c libqt5-core libqt5-dbus libqt5-gui libqt5-network libqt5-printsupport libqt5-svg libqt5-widgets libqt5-x11extras libqt5-xml libstdc++-devel libxcbutil-keysyms libxkbfile-devel python-base python-modules python3 python3-base qt5-base-devel ruby ruby-stdlibs xml-common xml-utils xorg-kbproto-devel xorg-xf86miscproto-devel xorg-xf86vidmodeproto-devel xorg-xproto-devel
#BuildRequires: extra-cmake-modules kf5-karchive-devel kf5-kauth-devel kf5-kbookmarks-devel kf5-kcodecs-devel kf5-kcompletion-devel kf5-kconfig-devel kf5-kconfigwidgets-devel kf5-kcoreaddons-devel kf5-kcrash-devel kf5-kdbusaddons-devel kf5-kdelibs4support kf5-kdelibs4support-devel kf5-kdesignerplugin-devel kf5-kdoctools kf5-kdoctools-devel kf5-kemoticons-devel kf5-kguiaddons-devel kf5-ki18n-devel kf5-kiconthemes-devel kf5-kinit-devel kf5-kio-devel kf5-kitemmodels-devel kf5-kitemviews-devel kf5-kjobwidgets-devel kf5-knotifications-devel kf5-kparts-devel kf5-kservice-devel kf5-ktextwidgets-devel kf5-kunitconversion-devel kf5-kwidgetsaddons-devel kf5-kwindowsystem-devel kf5-kxmlgui-devel kf5-solid-devel kf5-sonnet-devel python-module-google qt5-x11extras-devel rpm-build-python3 rpm-build-ruby
BuildRequires(pre): rpm-build-kf5 rpm-build-ubt
BuildRequires: extra-cmake-modules qt5-base-devel qt5-x11extras-devel
BuildRequires: kf5-karchive-devel kf5-kauth-devel kf5-kbookmarks-devel kf5-kcodecs-devel kf5-kcompletion-devel
BuildRequires: kf5-kconfig-devel kf5-kconfigwidgets-devel kf5-kcoreaddons-devel kf5-kcrash-devel kf5-kdbusaddons-devel
BuildRequires: kf5-kdelibs4support kf5-kdelibs4support-devel kf5-kdesignerplugin-devel
BuildRequires: kf5-kdoctools kf5-kdoctools-devel
BuildRequires: kf5-kemoticons-devel kf5-kguiaddons-devel kf5-ki18n-devel kf5-kiconthemes-devel kf5-kinit-devel
BuildRequires: kf5-kio-devel kf5-kitemmodels-devel kf5-kitemviews-devel kf5-kjobwidgets-devel kf5-knotifications-devel
BuildRequires: kf5-kparts-devel kf5-kservice-devel kf5-ktextwidgets-devel kf5-kunitconversion-devel
BuildRequires: kf5-kwidgetsaddons-devel kf5-kwindowsystem-devel kf5-kxmlgui-devel kf5-solid-devel kf5-sonnet-devel

Provides: kf5-kgamma = %EVR
Obsoletes: kf5-kgamma < %EVR

%description
%summary.

%prep
%setup -n %rname-%version
%patch1 -p1
%patch2 -p1

%build
%K5build

%install
%K5install
%K5install_move data kgamma
%find_lang %name --with-kde --all-name

%files -f %name.lang
%doc LICENSES/*
%_K5plug/plasma/kcminit/*kgamma*.so
%_K5plug/plasma/kcms/systemsettings/*kgamma*.so
%_K5data/kgamma/

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

* Wed Feb 19 2020 Sergey V Turchin <zerg@altlinux.org> 5.18.1-alt1
- new version

* Thu Jan 09 2020 Sergey V Turchin <zerg@altlinux.org> 5.17.5-alt1
- new version

* Thu Dec 05 2019 Sergey V Turchin <zerg@altlinux.org> 5.17.4-alt1
- new version

* Wed Nov 13 2019 Sergey V Turchin <zerg@altlinux.org> 5.17.3-alt1
- new version

* Fri Nov 01 2019 Sergey V Turchin <zerg@altlinux.org> 5.17.2-alt1
- new version

* Mon Oct 28 2019 Sergey V Turchin <zerg@altlinux.org> 5.17.1-alt1
- new version

* Thu Oct 17 2019 Sergey V Turchin <zerg@altlinux.org> 5.17.0-alt1
- new version

* Mon Sep 09 2019 Sergey V Turchin <zerg@altlinux.org> 5.16.5-alt1
- new version

* Thu Aug 01 2019 Sergey V Turchin <zerg@altlinux.org> 5.16.4-alt1
- new version

* Thu Jul 11 2019 Sergey V Turchin <zerg@altlinux.org> 5.16.3-alt1
- new version

* Wed Jun 26 2019 Sergey V Turchin <zerg@altlinux.org> 5.16.2-alt1
- new version

* Tue Jun 18 2019 Sergey V Turchin <zerg@altlinux.org> 5.16.1-alt1
- new version

* Thu Jun 06 2019 Sergey V Turchin <zerg@altlinux.org> 5.15.5-alt2
- new version

* Tue Jun 04 2019 Sergey V Turchin <zerg@altlinux.org> 5.15.5-alt1
- new version

* Wed Apr 24 2019 Sergey V Turchin <zerg@altlinux.org> 5.15.4-alt1
- new version

* Tue Mar 05 2019 Sergey V Turchin <zerg@altlinux.org> 5.12.8-alt1
- new version

* Thu Sep 27 2018 Sergey V Turchin <zerg@altlinux.org> 5.12.7-alt1
- new version

* Wed Jun 27 2018 Sergey V Turchin <zerg@altlinux.org> 5.12.6-alt1%ubt
- new version

* Thu May 03 2018 Sergey V Turchin <zerg@altlinux.org> 5.12.5-alt1%ubt
- new version

* Wed Mar 28 2018 Sergey V Turchin <zerg@altlinux.org> 5.12.4-alt1%ubt
- new version

* Tue Mar 13 2018 Sergey V Turchin <zerg@altlinux.org> 5.12.3-alt1%ubt
- new version

* Thu Mar 01 2018 Sergey V Turchin <zerg@altlinux.org> 5.12.2-alt1%ubt
- new version

* Mon Feb 19 2018 Maxim Voronov <mvoronov@altlinux.org> 5.12.0-alt2%ubt
- renamed kf5-kgamma -> plasma5-kgamma

* Wed Feb 07 2018 Sergey V Turchin <zerg@altlinux.org> 5.12.0-alt1%ubt
- new version

* Wed Jan 10 2018 Sergey V Turchin <zerg@altlinux.org> 5.11.5-alt1%ubt
- new version

* Mon Dec 11 2017 Sergey V Turchin <zerg@altlinux.org> 5.11.4-alt1%ubt
- new version

* Thu Nov 09 2017 Sergey V Turchin <zerg@altlinux.org> 5.11.3-alt1%ubt
- new version

* Tue Nov 07 2017 Sergey V Turchin <zerg@altlinux.org> 5.11.2-alt1%ubt
- new version

* Mon Sep 25 2017 Sergey V Turchin <zerg@altlinux.org> 5.10.5-alt1%ubt
- new version

* Wed Jul 19 2017 Sergey V Turchin <zerg@altlinux.org> 5.10.4-alt1%ubt
- new version

* Fri Jul 14 2017 Sergey V Turchin <zerg@altlinux.org> 5.10.3-alt1%ubt
- new version

* Wed Apr 26 2017 Sergey V Turchin <zerg@altlinux.org> 5.9.5-alt1%ubt
- new version

* Mon Apr 10 2017 Sergey V Turchin <zerg@altlinux.org> 5.9.4-alt1%ubt
- new version

* Thu Mar 09 2017 Sergey V Turchin <zerg@altlinux.org> 5.9.3-alt1%ubt
- new version

* Mon Feb 20 2017 Sergey V Turchin <zerg@altlinux.org> 5.9.2-alt1%ubt
- new version

* Mon Feb 20 2017 Sergey V Turchin <zerg@altlinux.org> 5.9.1-alt1%ubt
- new version

* Fri Dec 09 2016 Sergey V Turchin <zerg@altlinux.org> 5.8.4-alt1%ubt
- new version

* Wed Nov 16 2016 Sergey V Turchin <zerg@altlinux.org> 5.8.3-alt0.M80P.1
- build for M80P

* Tue Nov 15 2016 Sergey V Turchin <zerg@altlinux.org> 5.8.3-alt1
- new version

* Tue Oct 25 2016 Sergey V Turchin <zerg@altlinux.org> 5.8.2-alt1
- new version

* Tue Oct 18 2016 Sergey V Turchin <zerg@altlinux.org> 5.8.1-alt0.M80P.1
- build for M80P

* Fri Oct 14 2016 Sergey V Turchin <zerg@altlinux.org> 5.8.1-alt1
- new version

* Tue Oct 04 2016 Sergey V Turchin <zerg@altlinux.org> 5.8.0-alt1
- new version

* Tue Aug 30 2016 Sergey V Turchin <zerg@altlinux.org> 5.7.4-alt1
- new version

* Mon Aug 08 2016 Sergey V Turchin <zerg@altlinux.org> 5.7.3-alt1
- new version

* Tue Jul 26 2016 Sergey V Turchin <zerg@altlinux.org> 5.7.2-alt1
- new version

* Wed Jul 13 2016 Sergey V Turchin <zerg@altlinux.org> 5.7.1-alt1
- new version

* Wed Jul 06 2016 Sergey V Turchin <zerg@altlinux.org> 5.7.0-alt1
- new version

* Wed Jun 29 2016 Sergey V Turchin <zerg@altlinux.org> 5.6.5-alt1
- new version

* Wed May 11 2016 Sergey V Turchin <zerg@altlinux.org> 5.6.4-alt1
- new version

* Thu Apr 21 2016 Sergey V Turchin <zerg@altlinux.org> 5.6.3-alt1
- new version

* Wed Mar 30 2016 Sergey V Turchin <zerg@altlinux.org> 5.6.1-alt1
- new version

* Mon Mar 21 2016 Sergey V Turchin <zerg@altlinux.org> 5.6.0-alt1
- new version

* Wed Mar 09 2016 Sergey V Turchin <zerg@altlinux.org> 5.5.5-alt1
- new version

* Thu Jan 28 2016 Sergey V Turchin <zerg@altlinux.org> 5.5.4-alt1
- new version

* Fri Jan 15 2016 Sergey V Turchin <zerg@altlinux.org> 5.5.3-alt1
- initial build
