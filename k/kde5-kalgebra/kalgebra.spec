%define rname kalgebra

%ifarch %e2k ppc64le
%def_disable qtwebengine
%else
%def_enable qtwebengine
%endif

Name: kde5-%rname
Version: 22.08.3
Release: alt1
%K5init no_appdata

Group: Education
Summary: Graph Calculator
Url: http://www.kde.org
License: GPLv2+ / LGPLv2+

Requires: kf5-kirigami

Source: %rname-%version.tar

# Automatically added by buildreq on Wed Mar 30 2016 (-bi)
# optimized out: cmake cmake-modules docbook-dtds docbook-style-xsl elfutils gcc-c++ gtk-update-icon-cache kf5-kdoctools kf5-kdoctools-devel libEGL-devel libGL-devel libgpg-error libgst-plugins1.0 libncurses-devel libqt5-core libqt5-dbus libqt5-gui libqt5-network libqt5-opengl libqt5-positioning libqt5-printsupport libqt5-qml libqt5-quick libqt5-sensors libqt5-sql libqt5-svg libqt5-test libqt5-webchannel libqt5-webkit libqt5-webkitwidgets libqt5-widgets libqt5-x11extras libqt5-xml libstdc++-devel libtinfo-devel libxcbutil-keysyms python-base python-modules python3 qt5-base-devel qt5-declarative-devel rpm-build-python3 xml-common xml-utils
#BuildRequires: extra-cmake-modules kde5-analitza-devel kf5-kauth-devel kf5-kbookmarks-devel kf5-kcodecs-devel kf5-kcompletion-devel kf5-kconfig-devel kf5-kconfigwidgets-devel kf5-kcoreaddons-devel kf5-kdelibs4support kf5-kdoctools-devel kf5-ki18n-devel kf5-kio-devel kf5-kitemviews-devel kf5-kjobwidgets-devel kf5-kservice-devel kf5-kwidgetsaddons-devel kf5-kxmlgui-devel kf5-solid-devel libGLU-devel libreadline-devel python-module-google python3-base qt5-svg-devel qt5-webkit-devel ruby ruby-stdlibs
BuildRequires(pre): rpm-build-kf5 rpm-build-ubt
BuildRequires: extra-cmake-modules qt5-svg-devel qt5-declarative-devel
%if_enabled qtwebengine
BuildRequires: qt5-webengine-devel
%endif
BuildRequires: libGLU-devel libreadline-devel
BuildRequires: libncursesw-devel
BuildRequires: kde5-analitza-devel
BuildRequires: kf5-kauth-devel kf5-kbookmarks-devel kf5-kcodecs-devel kf5-kcompletion-devel kf5-kconfig-devel
BuildRequires: kf5-kconfigwidgets-devel kf5-kcoreaddons-devel kf5-kdelibs4support kf5-kdoctools-devel
BuildRequires: kf5-ki18n-devel kf5-kio-devel kf5-kitemviews-devel kf5-kjobwidgets-devel kf5-kservice-devel
BuildRequires: kf5-kwidgetsaddons-devel kf5-kxmlgui-devel kf5-solid-devel

%description
KAlgebra is an application that can replace your graphing calculator.
It has numerical, logical, symbolic, and analysis features that let you calculate
mathematical expressions on the console and graphically plot the results in 2D or 3D.
KAlgebra is rooted in the Mathematical Markup Language (MathML);
however, one does not need to know MathML to use KAlgebra.

%prep
%setup -n %rname-%version

%build
%K5build

%install
%K5install
%K5install_move data plasma kalgebramobile
%find_lang %name --with-kde --all-name

%files -f %name.lang
%_K5bin/*algebra*
#%_K5data/kalgebramobile/
%_K5xdgapp/*algebra*.desktop
%_K5icon/*/*/apps/*algebra.*
%if_enabled qtwebengine
%_K5data/plasma/plasmoids/org.kde.graphsplasmoid/
%_datadir/katepart5/syntax/kalgebra.xml
%_K5srv/graphsplasmoid.desktop
%endif

%changelog
* Mon Nov 07 2022 Sergey V Turchin <zerg@altlinux.org> 22.08.3-alt1
- new version

* Tue Oct 18 2022 Sergey V Turchin <zerg@altlinux.org> 22.08.2-alt1
- new version

* Wed Sep 21 2022 Sergey V Turchin <zerg@altlinux.org> 22.08.1-alt1
- new version

* Tue Jul 12 2022 Sergey V Turchin <zerg@altlinux.org> 22.04.3-alt1
- new version

* Fri Jun 10 2022 Sergey V Turchin <zerg@altlinux.org> 22.04.2-alt1
- new version

* Mon May 23 2022 Sergey V Turchin <zerg@altlinux.org> 22.04.1-alt1
- new version

* Sat Mar 05 2022 Sergey V Turchin <zerg@altlinux.org> 21.12.3-alt1
- new version

* Tue Feb 01 2022 Sergey V Turchin <zerg@altlinux.org> 21.12.1-alt2
- build without qtwebengine on e2k and ppc64le

* Tue Jan 18 2022 Sergey V Turchin <zerg@altlinux.org> 21.12.1-alt1
- new version

* Mon Nov 08 2021 Sergey V Turchin <zerg@altlinux.org> 21.08.3-alt1
- new version

* Fri Oct 08 2021 Sergey V Turchin <zerg@altlinux.org> 21.08.2-alt1
- new version

* Mon Sep 06 2021 Sergey V Turchin <zerg@altlinux.org> 21.08.1-alt1
- new version

* Fri Aug 27 2021 Sergey V Turchin <zerg@altlinux.org> 21.08.0-alt1
- new version

* Fri Jul 09 2021 Sergey V Turchin <zerg@altlinux.org> 21.04.3-alt1
- new version

* Tue May 25 2021 Sergey V Turchin <zerg@altlinux.org> 21.04.1-alt1
- new version

* Fri Mar 12 2021 Sergey V Turchin <zerg@altlinux.org> 20.12.3-alt1
- new version

* Wed Feb 17 2021 Sergey V Turchin <zerg@altlinux.org> 20.12.2-alt1
- new version

* Tue Dec 22 2020 Sergey V Turchin <zerg@altlinux.org> 20.12.0-alt1
- new version

* Wed Nov 25 2020 Sergey V Turchin <zerg@altlinux.org> 20.08.3-alt1
- new version

* Thu Oct 15 2020 Sergey V Turchin <zerg@altlinux.org> 20.08.2-alt1
- new version

* Wed Sep 23 2020 Sergey V Turchin <zerg@altlinux.org> 20.08.1-alt1
- new version

* Wed Aug 19 2020 Sergey V Turchin <zerg@altlinux.org> 20.04.3-alt1
- new version

* Fri Mar 13 2020 Sergey V Turchin <zerg@altlinux.org> 19.12.3-alt1
- new version

* Thu Jan 23 2020 Sergey V Turchin <zerg@altlinux.org> 19.12.1-alt1
- new version

* Wed Nov 27 2019 Sergey V Turchin <zerg@altlinux.org> 19.08.3-alt1
- new version

* Tue Sep 10 2019 Sergey V Turchin <zerg@altlinux.org> 19.08.1-alt1
- new version

* Thu Aug 29 2019 Sergey V Turchin <zerg@altlinux.org> 19.08.0-alt1
- new version

* Fri Jul 19 2019 Sergey V Turchin <zerg@altlinux.org> 19.04.3-alt1
- new version

* Thu Jun 06 2019 Sergey V Turchin <zerg@altlinux.org> 19.04.1-alt1
- new version

* Wed May 08 2019 Sergey V Turchin <zerg@altlinux.org> 19.04.0-alt1
- new version

* Thu Mar 21 2019 Sergey V Turchin <zerg@altlinux.org> 18.12.3-alt1
- new version

* Thu Feb 28 2019 Sergey V Turchin <zerg@altlinux.org> 18.12.2-alt1
- new version

* Thu Jul 26 2018 Sergey V Turchin <zerg@altlinux.org> 18.04.3-alt1%ubt
- new version

* Thu Jul 05 2018 Sergey V Turchin <zerg@altlinux.org> 18.04.2-alt1%ubt
- new version

* Wed May 30 2018 Sergey V Turchin <zerg@altlinux.org> 18.04.1-alt2%ubt
- build with ncurses

* Fri May 25 2018 Sergey V Turchin <zerg@altlinux.org> 18.04.1-alt1%ubt
- new version

* Thu May 03 2018 Sergey V Turchin <zerg@altlinux.org> 17.12.3-alt2%ubt
- fix requires

* Tue Mar 13 2018 Sergey V Turchin <zerg@altlinux.org> 17.12.3-alt1%ubt
- new version

* Tue Nov 14 2017 Sergey V Turchin <zerg@altlinux.org> 17.08.3-alt1%ubt
- new version

* Fri Jul 14 2017 Sergey V Turchin <zerg@altlinux.org> 17.04.3-alt1%ubt
- new version

* Thu Jun 15 2017 Sergey V Turchin <zerg@altlinux.org> 17.04.2-alt1%ubt
- new version

* Wed Jun 07 2017 Sergey V Turchin <zerg@altlinux.org> 17.04.1-alt1%ubt
- new version

* Thu Apr 06 2017 Sergey V Turchin <zerg@altlinux.org> 16.12.3-alt1%ubt
- new version

* Thu Sep 22 2016 Sergey V Turchin <zerg@altlinux.org> 16.08.1-alt1
- new version

* Mon Jul 04 2016 Sergey V Turchin <zerg@altlinux.org> 16.04.2-alt1
- new version

* Thu May 12 2016 Sergey V Turchin <zerg@altlinux.org> 16.04.1-alt1
- new version

* Thu Mar 17 2016 Sergey V Turchin <zerg@altlinux.org> 15.12.2-alt1
- initial build
