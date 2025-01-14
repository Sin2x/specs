%define rname syndication

Name: kf5-%rname
Version: 5.100.0
Release: alt1
Epoch: 1
%K5init altplace

Group: Graphical desktop/KDE
Summary: RSS/Atom parser library
Url: http://www.kde.org
License: GPLv2+ / LGPLv2+

Source: %rname-%version.tar

# Automatically added by buildreq on Wed Aug 12 2015 (-bi)
# optimized out: cmake cmake-modules elfutils libEGL-devel libGL-devel libqt5-core libqt5-dbus libqt5-gui libqt5-network libqt5-widgets libqt5-x11extras libqt5-xml libstdc++-devel python-base python3 python3-base ruby ruby-stdlibs
#BuildRequires: extra-cmake-modules gcc-c++ kf5-kauth-devel kf5-kbookmarks-devel kf5-kcodecs-devel kf5-kcompletion-devel kf5-kconfig-devel kf5-kconfigwidgets-devel kf5-kcoreaddons-devel kf5-kio-devel kf5-kitemviews-devel kf5-kjobwidgets-devel kf5-kservice-devel kf5-kwidgetsaddons-devel kf5-kxmlgui-devel kf5-solid-devel libdb4-devel python-module-google qt5-base-devel rpm-build-python3 rpm-build-ruby
BuildRequires(pre): rpm-build-kf5 rpm-build-ubt
BuildRequires: extra-cmake-modules gcc-c++ qt5-base-devel
BuildRequires: kf5-kauth-devel kf5-kbookmarks-devel kf5-kcodecs-devel kf5-kcompletion-devel kf5-kconfig-devel
BuildRequires: kf5-kconfigwidgets-devel kf5-kcoreaddons-devel kf5-kio-devel kf5-kitemviews-devel kf5-kjobwidgets-devel
BuildRequires: kf5-kservice-devel kf5-kwidgetsaddons-devel kf5-kxmlgui-devel kf5-solid-devel

%description
%summary.

%package common
Summary: %name common package
Group: System/Configuration/Other
BuildArch: noarch
Requires: kf5-filesystem
Provides: kde5-syndication-common = 19
Obsoletes: kde5-syndication-common < 19
%description common
%name common package

%package devel
Group: Development/KDE and QT
Summary: Development files for %name
Provides: kde5-syndication-devel = 19
Obsoletes: kde5-syndication-devel < 19
%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%package -n libkf5syndication
Group: System/Libraries
Summary: KF5 library
Requires: %name-common = %version-%release
%description -n libkf5syndication
KF5 library


%prep
%setup -n %rname-%version

%build
%K5build

%install
%K5install
%find_lang %name --with-kde --all-name

%files common -f %name.lang
%doc LICENSES/* README.md
%_datadir/qlogging-categories5/*.*categories

%files devel
#%_K5inc/syndication_version.h
%_K5inc/Syndication/
%_K5link/lib*.so
%_K5lib/cmake/KF5Syndication/
%_K5archdata/mkspecs/modules/qt_Syndication.pri

%files -n libkf5syndication
%_K5lib/libKF5Syndication.so.*

%changelog
* Mon Nov 14 2022 Sergey V Turchin <zerg@altlinux.org> 1:5.100.0-alt1
- new version

* Tue Oct 11 2022 Sergey V Turchin <zerg@altlinux.org> 1:5.99.0-alt1
- new version

* Mon Sep 12 2022 Sergey V Turchin <zerg@altlinux.org> 1:5.98.0-alt1
- new version

* Mon Aug 15 2022 Sergey V Turchin <zerg@altlinux.org> 1:5.97.0-alt1
- new version

* Mon Jul 11 2022 Sergey V Turchin <zerg@altlinux.org> 1:5.96.0-alt1
- new version

* Tue Jun 14 2022 Sergey V Turchin <zerg@altlinux.org> 1:5.95.0-alt1
- new version

* Mon May 16 2022 Sergey V Turchin <zerg@altlinux.org> 1:5.94.0-alt1
- new version

* Mon Apr 11 2022 Sergey V Turchin <zerg@altlinux.org> 1:5.93.0-alt1
- new version

* Mon Mar 14 2022 Sergey V Turchin <zerg@altlinux.org> 1:5.92.0-alt1
- new version

* Mon Feb 14 2022 Sergey V Turchin <zerg@altlinux.org> 1:5.91.0-alt1
- new version

* Mon Jan 10 2022 Sergey V Turchin <zerg@altlinux.org> 1:5.90.0-alt1
- new version

* Thu Dec 16 2021 Sergey V Turchin <zerg@altlinux.org> 1:5.89.0-alt1
- new version

* Mon Nov 15 2021 Sergey V Turchin <zerg@altlinux.org> 1:5.88.0-alt1
- new version

* Mon Oct 11 2021 Sergey V Turchin <zerg@altlinux.org> 1:5.87.0-alt1
- new version

* Mon Sep 13 2021 Sergey V Turchin <zerg@altlinux.org> 1:5.86.0-alt1
- new version

* Mon Aug 16 2021 Sergey V Turchin <zerg@altlinux.org> 1:5.85.0-alt1
- new version

* Tue Jul 13 2021 Sergey V Turchin <zerg@altlinux.org> 1:5.84.0-alt1
- new version

* Thu Jul 01 2021 Sergey V Turchin <zerg@altlinux.org> 1:5.83.0-alt1
- new version

* Wed May 12 2021 Sergey V Turchin <zerg@altlinux.org> 1:5.82.0-alt1
- new version

* Mon Apr 12 2021 Sergey V Turchin <zerg@altlinux.org> 1:5.81.0-alt1
- new version

* Thu Mar 18 2021 Sergey V Turchin <zerg@altlinux.org> 1:5.80.0-alt1
- new version

* Mon Feb 15 2021 Sergey V Turchin <zerg@altlinux.org> 1:5.79.0-alt1
- new version

* Sun Jan 10 2021 Sergey V Turchin <zerg@altlinux.org> 1:5.78.0-alt1
- new version

* Mon Dec 14 2020 Sergey V Turchin <zerg@altlinux.org> 1:5.77.0-alt1
- new version

* Mon Nov 16 2020 Sergey V Turchin <zerg@altlinux.org> 1:5.76.0-alt1
- new version

* Tue Oct 13 2020 Sergey V Turchin <zerg@altlinux.org> 1:5.75.0-alt1
- new version

* Mon Sep 14 2020 Sergey V Turchin <zerg@altlinux.org> 1:5.74.0-alt1
- new version

* Tue Aug 11 2020 Sergey V Turchin <zerg@altlinux.org> 1:5.73.0-alt1
- new version

* Thu Jul 23 2020 Sergey V Turchin <zerg@altlinux.org> 1:5.72.0-alt1
- new version

* Tue May 12 2020 Sergey V Turchin <zerg@altlinux.org> 1:5.70.0-alt1
- new version

* Wed Apr 15 2020 Sergey V Turchin <zerg@altlinux.org> 1:5.69.0-alt1
- new version

* Mon Mar 16 2020 Sergey V Turchin <zerg@altlinux.org> 1:5.68.0-alt1
- new version

* Mon Feb 10 2020 Sergey V Turchin <zerg@altlinux.org> 1:5.67.0-alt1
- new version

* Mon Jan 13 2020 Sergey V Turchin <zerg@altlinux.org> 1:5.66.0-alt1
- new version

* Mon Dec 16 2019 Sergey V Turchin <zerg@altlinux.org> 1:5.65.0-alt1
- new version

* Mon Nov 11 2019 Sergey V Turchin <zerg@altlinux.org> 1:5.64.0-alt1
- new version

* Tue Oct 15 2019 Sergey V Turchin <zerg@altlinux.org> 1:5.63.0-alt1
- new version

* Mon Sep 16 2019 Sergey V Turchin <zerg@altlinux.org> 1:5.62.0-alt1
- new version

* Mon Aug 12 2019 Sergey V Turchin <zerg@altlinux.org> 1:5.61.0-alt1
- new version

* Mon Jul 15 2019 Sergey V Turchin <zerg@altlinux.org> 1:5.60.0-alt1
- new version

* Tue Jun 11 2019 Sergey V Turchin <zerg@altlinux.org> 1:5.59.0-alt1
- new version

* Mon Jun 03 2019 Sergey V Turchin <zerg@altlinux.org> 1:5.58.0-alt1
- new version

* Mon Apr 15 2019 Sergey V Turchin <zerg@altlinux.org> 1:5.57.0-alt1
- new version

* Fri Mar 15 2019 Sergey V Turchin <zerg@altlinux.org> 1:5.56.0-alt1
- new version

* Mon Feb 11 2019 Sergey V Turchin <zerg@altlinux.org> 1:5.55.0-alt1
- new version

* Mon Feb 04 2019 Sergey V Turchin <zerg@altlinux.org> 1:5.54.0-alt1
- new version
- moved from apps

* Tue Jul 24 2018 Sergey V Turchin <zerg@altlinux.org> 18.04.3-alt1%ubt
- new version

* Tue Jun 26 2018 Sergey V Turchin <zerg@altlinux.org> 18.04.2-alt1%ubt
- new version

* Tue May 15 2018 Sergey V Turchin <zerg@altlinux.org> 18.04.1-alt1%ubt
- new version

* Wed Mar 14 2018 Sergey V Turchin <zerg@altlinux.org> 17.12.3-alt1%ubt
- new version

* Tue Feb 13 2018 Sergey V Turchin <zerg@altlinux.org> 17.12.2-alt1%ubt
- new version

* Thu Nov 09 2017 Sergey V Turchin <zerg@altlinux.org> 17.08.3-alt1%ubt
- new version

* Thu Nov 09 2017 Sergey V Turchin <zerg@altlinux.org> 17.08.2-alt1%ubt
- new version

* Fri Jul 14 2017 Sergey V Turchin <zerg@altlinux.org> 17.04.3-alt1%ubt
- new version

* Wed Jun 14 2017 Sergey V Turchin <zerg@altlinux.org> 17.04.2-alt1%ubt
- new version

* Mon May 15 2017 Sergey V Turchin <zerg@altlinux.org> 17.04.1-alt1%ubt
- new version

* Mon Apr 24 2017 Sergey V Turchin <zerg@altlinux.org> 17.04.0-alt1%ubt
- new version

* Wed Mar 15 2017 Sergey V Turchin <zerg@altlinux.org> 16.12.3-alt1%ubt
- new version

* Thu Mar 09 2017 Sergey V Turchin <zerg@altlinux.org> 16.12.2-alt1%ubt
- new version

* Mon Nov 28 2016 Sergey V Turchin <zerg@altlinux.org> 16.08.3-alt0.M80P.1
- build for M80P

* Fri Nov 25 2016 Sergey V Turchin <zerg@altlinux.org> 16.08.3-alt1
- new version

* Mon Sep 19 2016 Sergey V Turchin <zerg@altlinux.org> 16.08.1-alt1
- new version

* Fri Aug 19 2016 Sergey V Turchin <zerg@altlinux.org> 16.08.0-alt1
- new version

* Wed Jul 13 2016 Sergey V Turchin <zerg@altlinux.org> 16.04.3-alt1
- new version

* Thu Jun 30 2016 Sergey V Turchin <zerg@altlinux.org> 16.04.2-alt1
- new version

* Tue May 10 2016 Sergey V Turchin <zerg@altlinux.org> 16.04.1-alt1
- new version

* Mon Apr 25 2016 Sergey V Turchin <zerg@altlinux.org> 16.04.0-alt1
- new version

* Tue Mar 22 2016 Sergey V Turchin <zerg@altlinux.org> 15.12.3-alt1
- new version

* Thu Feb 25 2016 Sergey V Turchin <zerg@altlinux.org> 15.12.2-alt1
- new version

* Tue Jan 19 2016 Sergey V Turchin <zerg@altlinux.org> 15.12.1-alt1
- new version

* Mon Dec 21 2015 Sergey V Turchin <zerg@altlinux.org> 15.12.0-alt1
- new version

* Thu Nov 12 2015 Sergey V Turchin <zerg@altlinux.org> 15.08.3-alt1
- new version

* Wed Oct 14 2015 Sergey V Turchin <zerg@altlinux.org> 15.08.2-alt1
- new version

* Wed Sep 16 2015 Sergey V Turchin <zerg@altlinux.org> 15.08.1-alt1
- new version

* Thu Aug 20 2015 Sergey V Turchin <zerg@altlinux.org> 15.08.0-alt1
- new version

* Mon Aug 10 2015 Sergey V Turchin <zerg@altlinux.org> 15.7.90-alt1
- initial build
