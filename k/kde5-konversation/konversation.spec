

%define rname konversation
Name: kde5-%rname
Version: 22.08.3
Release: alt1
%define beta %nil
%K5init no_altplace

AutoReq: yes, nopython
%add_python3_path %_datadir/%rname
%add_findreq_skiplist %_datadir/%rname/scripts/bug

Group: Networking/IRC
Summary: Konversation is a user friendly Internet Relay Chat client.
License: GPL-2.0-or-later
Url: http://konversation.kde.org
Packager: Sergey V Turchin <zerg@altlinux.org>

Requires: qca-qt5-ossl
Requires: kde5-runtime
Provides: konversation = %version-%release
Obsoletes: konversation < %version-%release
Provides: kde4-konversation = %version-%release
Obsoletes: kde4-konversation < %version-%release

Source0: %rname-%version.tar

# Automatically added by buildreq on Tue Jun 30 2015 (-bi)
# optimized out: cmake cmake-modules docbook-dtds docbook-style-xsl elfutils kf5-kdoctools-devel libEGL-devel libGL-devel libdbusmenu-qt52 libgpg-error libjson-c libqca-qt5 libqt5-core libqt5-dbus libqt5-gui libqt5-network libqt5-printsupport libqt5-svg libqt5-widgets libqt5-x11extras libqt5-xml libstdc++-devel libxcbutil-keysyms python-base python3 python3-base qt5-base-devel xml-common xml-utils
#BuildRequires: extra-cmake-modules gcc-c++ kf5-karchive-devel kf5-kauth-devel kf5-kbookmarks-devel kf5-kcodecs-devel kf5-kcompletion-devel kf5-kconfig-devel kf5-kconfigwidgets-devel kf5-kcoreaddons-devel kf5-kdbusaddons-devel kf5-kdelibs4support kf5-kdoctools kf5-kdoctools-devel kf5-kemoticons-devel kf5-kglobalaccel-devel kf5-ki18n-devel kf5-kiconthemes-devel kf5-kidletime-devel kf5-kio-devel kf5-kitemviews-devel kf5-kjobwidgets-devel kf5-knotifications-devel kf5-knotifyconfig-devel kf5-kparts-devel kf5-kservice-devel kf5-ktextwidgets-devel kf5-kwallet-devel kf5-kwidgetsaddons-devel kf5-kwindowsystem-devel kf5-kxmlgui-devel kf5-solid-devel kf5-sonnet-devel libdb4-devel libqca-qt5-devel python-module-google qt5-phonon-devel rpm-build-gir rpm-build-python3 ruby ruby-stdlibs
BuildRequires(pre): rpm-build-kf5 rpm-build-python3
BuildRequires: extra-cmake-modules gcc-c++
BuildRequires: libqca-qt5-devel qt5-phonon-devel qt5-multimedia-devel qt5-x11extras-devel
BuildRequires: kf5-karchive-devel kf5-kauth-devel kf5-kbookmarks-devel kf5-kcodecs-devel kf5-kcompletion-devel kf5-kconfig-devel kf5-kconfigwidgets-devel
BuildRequires: kf5-kcoreaddons-devel kf5-kdbusaddons-devel kf5-kdelibs4support kf5-kdoctools kf5-kdoctools-devel kf5-kemoticons-devel
BuildRequires: kf5-kglobalaccel-devel kf5-ki18n-devel kf5-kiconthemes-devel kf5-kidletime-devel kf5-kio-devel kf5-kitemviews-devel kf5-kjobwidgets-devel
BuildRequires: kf5-knotifications-devel kf5-knotifyconfig-devel kf5-kparts-devel kf5-kservice-devel kf5-ktextwidgets-devel kf5-kwallet-devel
BuildRequires: kf5-kwidgetsaddons-devel kf5-kwindowsystem-devel kf5-kxmlgui-devel kf5-solid-devel kf5-sonnet-devel kf5-kcrash-devel
BuildRequires: kf5-knewstuff-devel

%description
Konversation is a simple and easy-to-use IRC client for KDE with support for 
SSL connections, strikeout, multi-channel joins, away/unaway messages, 
ignore list functionality, full Unicode support, the ability to auto-connect 
to a server, optional timestamps in chat windows, configurable background colors, 
and much more. 

%prep
%setup -q -n %rname-%version

%build
%K5build

%install
%K5install
%find_lang --with-kde %rname

# purge use of /usr/bin/env
sed -i \
  -e "s|^#!/usr/bin/env bash|#!/bin/bash|g" \
  -e "s|^#!/usr/bin/env perl|#!/usr/bin/perl|g" \
  -e "s|^#!/usr/bin/env python$|#!%{__python3}|g" \
  %buildroot/%_datadir/%rname/scripts/* \
  %buildroot/%_datadir/%rname/scripting_support/python/konversation/*.py

%files -f %rname.lang
%doc AUTHORS README ChangeLog
%doc LICENSES/*
%_K5bin/*
%_K5xdgapp/org.kde.%rname.desktop
%_K5icon/hicolor/*/*/*.*
%_datadir/kconf_update/*
%_datadir/qlogging-categories5/*.*categories
%_datadir/%rname/
%_datadir/knsrcfiles/konversation*.*
#%_K5srv/*
%_K5notif/*
#%_K5xmlgui/*
%_K5dbus_srv/*.service

%changelog
* Mon Nov 07 2022 Sergey V Turchin <zerg@altlinux.org> 22.08.3-alt1
- new version

* Tue Oct 18 2022 Sergey V Turchin <zerg@altlinux.org> 22.08.2-alt1
- new version

* Thu Sep 15 2022 Sergey V Turchin <zerg@altlinux.org> 22.08.1-alt1
- new version

* Mon Jul 11 2022 Sergey V Turchin <zerg@altlinux.org> 22.04.3-alt1
- new version

* Fri Jun 10 2022 Sergey V Turchin <zerg@altlinux.org> 22.04.2-alt1
- new version

* Fri May 13 2022 Sergey V Turchin <zerg@altlinux.org> 22.04.1-alt1
- new version

* Fri Mar 04 2022 Sergey V Turchin <zerg@altlinux.org> 21.12.3-alt1
- new version

* Mon Jan 17 2022 Sergey V Turchin <zerg@altlinux.org> 21.12.1-alt1
- new version

* Mon Nov 08 2021 Sergey V Turchin <zerg@altlinux.org> 21.08.3-alt1
- new version

* Fri Oct 08 2021 Sergey V Turchin <zerg@altlinux.org> 21.08.2-alt1
- new version

* Thu Sep 02 2021 Sergey V Turchin <zerg@altlinux.org> 21.08.1-alt1
- new version

* Mon Aug 23 2021 Sergey V Turchin <zerg@altlinux.org> 21.08.0-alt1
- new version

* Thu Jul 08 2021 Sergey V Turchin <zerg@altlinux.org> 21.04.3-alt1
- new version

* Thu Jun 10 2021 Sergey V Turchin <zerg@altlinux.org> 21.04.2-alt1
- new version

* Wed May 19 2021 Sergey V Turchin <zerg@altlinux.org> 21.04.1-alt1
- new version

* Thu Mar 11 2021 Sergey V Turchin <zerg@altlinux.org> 20.12.3-alt1
- new version

* Fri Feb 05 2021 Sergey V Turchin <zerg@altlinux.org> 20.12.2-alt1
- new version

* Tue Jan 19 2021 Sergey V Turchin <zerg@altlinux.org> 20.12.1-alt1
- new version

* Wed Aug 26 2020 Sergey V Turchin <zerg@altlinux.org> 1.7.5-alt6
- fix compile with Qt 5.15

* Mon Jan 27 2020 Sergey V Turchin <zerg@altlinux.org> 1.7.5-alt5
- fix compile with new Qt

* Tue Jul 09 2019 Sergey V Turchin <zerg@altlinux.org> 1.7.5-alt4
- build with python3
- obsolete kde4-konversation

* Mon Oct 29 2018 Sergey V Turchin <zerg@altlinux.org> 1.7.5-alt3
- update russian translation

* Fri Oct 26 2018 Sergey V Turchin <zerg@altlinux.org> 1.7.5-alt2
- update russian translation

* Tue Aug 21 2018 Sergey V Turchin <zerg@altlinux.org> 1.7.5-alt1
- new version

* Tue Nov 21 2017 Sergey V Turchin <zerg@altlinux.org> 1.7.4-alt1
- new version

* Wed Jan 20 2016 Sergey V Turchin <zerg@altlinux.org> 1.6-alt2
- fix docs placement

* Mon Jun 29 2015 Sergey V Turchin <zerg@altlinux.org> 1.6-alt1
-  initial build
