%define rname cantor

%def_disable python2
%def_enable python3
%def_disable luajit
%ifarch %e2k ppc64le
%def_disable qtwebengine
%else
%def_enable qtwebengine
%endif

%define cantor_sover 28
%define libcantorlibs libcantorlibs%cantor_sover
%define cantor_config_sover 0
%define libcantor_config libcantor_config%cantor_config_sover

Name: kde5-%rname
Version: 22.08.3
Release: alt1
%K5init no_appdata

Group: Education
Summary: KDE Frontend to Mathematical Software
Url: http://www.kde.org
License: GPL-2.0-or-later or GPL-3.0-only

%if_enabled qtwebengine
Requires: kde5-kalgebra
Requires: epstool
%endif

Source: %rname-%version.tar
Patch1: alt-lib-so-ver.patch
Patch2: alt-find-luajit.patch

# Automatically added by buildreq on Wed Mar 30 2016 (-bi)
# optimized out: cmake cmake-modules docbook-dtds docbook-style-xsl elfutils fontconfig gcc-c++ gtk-update-icon-cache kf5-attica-devel kf5-kdoctools kf5-kdoctools-devel libEGL-devel libGL-devel libgpg-error libqt5-core libqt5-dbus libqt5-gui libqt5-network libqt5-printsupport libqt5-script libqt5-svg libqt5-test libqt5-widgets libqt5-x11extras libqt5-xml libqt5-xmlpatterns libstdc++-devel libxcbutil-keysyms pkg-config python-base python-devel python-modules python3 python3-base qt5-base-devel rpm-build-python3 ruby ruby-stdlibs xml-common xml-utils
#BuildRequires: extra-cmake-modules kde5-analitza-devel kf5-karchive-devel kf5-kauth-devel kf5-kbookmarks-devel kf5-kcodecs-devel kf5-kcompletion-devel kf5-kconfig-devel kf5-kconfigwidgets-devel kf5-kcoreaddons-devel kf5-kcrash-devel kf5-kdelibs4support kf5-kdoctools-devel kf5-ki18n-devel kf5-kiconthemes-devel kf5-kio-devel kf5-kitemviews-devel kf5-kjobwidgets-devel kf5-knewstuff-devel kf5-kparts-devel kf5-kpty-devel kf5-kservice-devel kf5-ktexteditor-devel kf5-ktextwidgets-devel kf5-kwidgetsaddons-devel kf5-kxmlgui-devel kf5-solid-devel kf5-sonnet-devel libcln-devel liblua5-devel libluajit-devel libspectre-devel python-module-google python3-dev qt5-svg-devel qt5-xmlpatterns-devel rpm-build-ruby
BuildRequires(pre): rpm-build-kf5
BuildRequires: extra-cmake-modules qt5-svg-devel qt5-xmlpatterns-devel qt5-tools-devel
%if_enabled qtwebengine
BuildRequires: qt5-webengine-devel
%endif
BuildRequires: libcln-devel libspectre-devel libdiscount-devel libpoppler-qt5-devel
%{?_enable_python2:BuildRequires: python-devel}
%{?_enable_python3:BuildRequires: python3-devel}
%{?_enable_luajit:BuildRequires: liblua5-devel libluajit-devel}
BuildRequires: kde5-analitza-devel
BuildRequires: kf5-karchive-devel kf5-kauth-devel kf5-kbookmarks-devel kf5-kcodecs-devel kf5-kcompletion-devel kf5-kconfig-devel
BuildRequires: kf5-kconfigwidgets-devel kf5-kcoreaddons-devel kf5-kcrash-devel kf5-kdelibs4support kf5-kdoctools-devel
BuildRequires: kf5-ki18n-devel kf5-kiconthemes-devel kf5-kio-devel kf5-kitemviews-devel kf5-kjobwidgets-devel
BuildRequires: kf5-knewstuff-devel kf5-kparts-devel kf5-kpty-devel kf5-kservice-devel kf5-ktexteditor-devel
BuildRequires: kf5-ktextwidgets-devel kf5-kwidgetsaddons-devel kf5-kxmlgui-devel kf5-solid-devel kf5-sonnet-devel
BuildRequires: kf5-syntax-highlighting-devel

%description
Cantor is a front-end to powerful mathematics and statistics packages.
Cantor integrates them into the KDE Platform and provides a nice, worksheet-based, graphical user interface.
It supports environments for KAlgebra, Lua, Maxima, R, Sage, Octave, Python, Scilab, and Qalculate!

%package common
Summary: %name common package
Group: System/Configuration/Other
#BuildArch: noarch
Requires: kf5-filesystem
%description common
%name common package

%package devel
Group: Development/KDE and QT
Summary: Development files for %name
%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%package -n %libcantorlibs
Group: System/Libraries
Summary: KF5 library
Requires: %name-common = %version-%release
%description -n %libcantorlibs
KF5 library

%package -n %libcantor_config
Group: System/Libraries
Summary: KF5 library
Requires: %name-common = %version-%release
%description -n %libcantor_config
KF5 library


%prep
%setup -n %rname-%version
%patch1 -p1
%patch2 -p1

#LUA_BASE_VER=`echo "%{get_version libluajit-devel}" | sed -E 's|^([[:digit:]]+\.[[:digit:]]).*|\1|'`
#pushd src/backends/lua
#for f in *.{h,cpp} ; do
#    sed -i "s|luajit-2.0/lua.hpp|luajit-${LUA_BASE_VER}/lua.hpp|" $f
#done
#popd

%build
%if_enabled qtwebengine
%K5build \
    -DKDE_INSTALL_INCLUDEDIR=%_K5inc \
    #
%endif

%install
%if_enabled qtwebengine
%K5install
%K5install_move data cantor knsrcfiles
mv %buildroot/%_K5xdgmime/cantor{,-kde5}.xml
%find_lang %name --with-kde --all-name
%else
mkdir -p %buildroot
%endif

%files
%if_enabled qtwebengine
%_K5bin/cantor*
%_K5lib/cantor_pythonbackend.so
%_K5plug/kf5/parts/*cantor*.so
%_K5plug/cantor/
%_K5data/cantor/
%_K5cfg/*.kcfg
%_K5xdgapp/org.kde.cantor.desktop
%_K5icon/*/*/apps/*.*
%_K5xmlgui/cantor/
%_K5data/knsrcfiles/*cantor*.knsrc
%_K5xdgmime/*cantor*.xml
%endif

%if_enabled qtwebengine
%files common -f %name.lang
%doc LICENSES/*

%files devel
%_K5inc/cantor/
%_K5link/lib*.so
%_libdir/cmake/Cantor/

%files -n %libcantorlibs
%_K5lib/libcantorlibs.so.%cantor_sover
%_K5lib/libcantorlibs.so.*
%files -n %libcantor_config
%_K5lib/libcantor_config.so.%cantor_config_sover
%_K5lib/libcantor_config.so.*
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
- build empty package on e2k and ppc64le

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

* Tue Mar 23 2021 Egor Ignatov <egori@altlinux.org> 20.12.3-alt2
- fix octave backend

* Fri Mar 12 2021 Sergey V Turchin <zerg@altlinux.org> 20.12.3-alt1
- new version

* Wed Mar 10 2021 Egor Ignatov <egori@altlinux.org> 20.12.2-alt2
- Fix octave backend
  + Add epstool dependency to prevent crash on plotting
  + Add patch to use gnuplot graphics toolkit by default

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

* Mon Oct 28 2019 Sergey V Turchin <zerg@altlinux.org> 19.08.2-alt1
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

* Thu Jul 26 2018 Sergey V Turchin <zerg@altlinux.org> 18.04.3-alt1
- new version

* Thu Jul 05 2018 Sergey V Turchin <zerg@altlinux.org> 18.04.2-alt1
- new version

* Fri May 25 2018 Sergey V Turchin <zerg@altlinux.org> 18.04.1-alt1
- new version

* Thu Mar 22 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 17.12.3-alt1.1
- (NMU) Rebuilt with python-3.6.4.

* Tue Mar 13 2018 Sergey V Turchin <zerg@altlinux.org> 17.12.3-alt1
- new version

* Tue Nov 14 2017 Sergey V Turchin <zerg@altlinux.org> 17.08.3-alt1
- new version

* Fri Jul 14 2017 Sergey V Turchin <zerg@altlinux.org> 17.04.3-alt1
- new version

* Thu Jun 15 2017 Sergey V Turchin <zerg@altlinux.org> 17.04.2-alt1
- new version

* Wed Jun 07 2017 Sergey V Turchin <zerg@altlinux.org> 17.04.1-alt1
- new version
- don't build lua backend

* Thu Apr 13 2017 Sergey V Turchin <zerg@altlinux.org> 16.12.3-alt2
- fix to build with luajit-2.0

* Thu Apr 06 2017 Sergey V Turchin <zerg@altlinux.org> 16.12.3-alt1
- new version

* Thu Sep 22 2016 Sergey V Turchin <zerg@altlinux.org> 16.08.1-alt1
- new version

* Mon Jul 04 2016 Sergey V Turchin <zerg@altlinux.org> 16.04.2-alt1
- new version

* Thu May 12 2016 Sergey V Turchin <zerg@altlinux.org> 16.04.1-alt1
- new version

* Sun Apr 03 2016 Ivan Zakharyaschev <imz@altlinux.org> 15.12.2-alt1.1
- (NMU) rebuild with python3-3.5 & rpm-build-python3-0.1.10
  (for ABI dependence and new python3(*) reqs)

* Thu Mar 17 2016 Sergey V Turchin <zerg@altlinux.org> 15.12.2-alt1
- initial build
