%define set_disable() %{expand:%%force_disable %1} %{expand:%%undefine _enable_%1}
%define set_enable() %{expand:%%force_enable %1} %{expand:%%undefine _disable_%1}
%define mIF_ver_gt() %if "%(rpmvercmp '%1' '%2')" > "0"
%define mIF_ver_gteq() %if "%(rpmvercmp '%1' '%2')" >= "0"
%define mIF_ver_lt() %if "%(rpmvercmp '%2' '%1')" > "0"
%define mIF_ver_lteq() %if "%(rpmvercmp '%2' '%1')" >= "0"

%define is_ffmpeg %([ -n "`rpmquery --qf '%%{SOURCERPM}' libavformat-devel 2>/dev/null | grep -e '^libav'`" ] && echo 0 || echo 1)

%def_disable debug
%def_enable libvidstab
%def_enable opencv

%define Name MLT
%define nam mlt
%define mlt_major 7
%define mlt_sover 7
%define libmlt libmlt%mlt_sover
%define mltxx_sover 7
%define libmltxx libmlt++%mltxx_sover

Name: %nam%mlt_major
Version: 7.8.0
Release: alt1
%K5init no_altplace

Summary: Multimedia framework designed for television broadcasting
License: GPL-3.0-or-later
Group: Video
Url: https://www.mltframework.org/

Source: %nam-%version.tar
Source1: mlt++-config.h
# Debian
Patch20: 01-changed-preset-path.diff
# ALT
Patch102: alt-no-version-script.patch
Patch103: alt-libav.patch
Patch104: alt-ix86.patch

# Automatically added by buildreq on Sun Mar 18 2018 (-bi)
# optimized out: elfutils gcc-c++ glib2-devel glibc-kernheaders-generic glibc-kernheaders-x86 libGL-devel libSDL-devel libX11-devel libavcodec-devel libavformat-devel libavutil-devel libcdio-paranoia libdc1394-22 libgpg-error libopencore-amrnb0 libopencore-amrwb0 libp11-kit libqt5-core libqt5-gui libqt5-svg libqt5-widgets libqt5-xml libraw1394-11 libstdc++-devel libvdpau-devel libx265-130 perl pkg-config python-base python-devel python-modules qt5-base-devel rpm-build-gir swig-data xorg-xproto-devel
#BuildRequires: frei0r-devel ladspa_sdk libSDL2-devel libSDL2_image-devel libalsa-devel libavdevice-devel libavfilter-devel libexif-devel libfftw3-devel libjack-devel libopencv-devel libpulseaudio-devel libsamplerate-devel libsox-devel libswscale-devel libxml2-devel qt5-svg-devel swig
#BuildRequires: frei0r-devel ladspa_sdk libSDL_image-devel libalsa-devel libavdevice-devel libavformat-devel libexif-devel libfftw3-devel libjack-devel libpulseaudio-devel libsamplerate-devel libsox-devel libswfdec-devel libswscale-devel libxml2-devel python-module-google python3-dev qt5-svg-devel rpm-build-ruby swig
BuildRequires(pre): rpm-build-kf5 rpm-build-python3 libavformat-devel
BuildRequires: qt5-svg-devel
BuildRequires: cmake
BuildRequires: frei0r-devel libSDL-devel libSDL2-devel libSDL2_image-devel libalsa-devel libexif-devel
BuildRequires: libavfilter-devel libswscale-devel libavdevice-devel libavformat-devel
%if %is_ffmpeg
BuildRequires: libswresample-devel
%endif
BuildRequires: libfftw3-devel libjack-devel libpulseaudio-devel libsamplerate-devel libsox-devel
BuildRequires: librubberband-devel libvorbis-devel
BuildRequires: libxml2-devel swig ladspa_sdk
%if_enabled libvidstab
BuildRequires: libvidstab-devel
%endif
%if_enabled opencv
BuildRequires: libopencv-devel
%endif
BuildRequires: python3-devel
BuildRequires: libgdk-pixbuf-devel libpango-devel

%description
%Name is a multimedia framework designed for television broadcasting.

%package -n %nam-utils
Summary: %Name utils
Group: Video
%description -n %nam-utils
%Name utils.

%package -n %libmlt
Summary: %Name framework library
Group: System/Libraries
%description -n %libmlt
%Name is a multimedia framework designed for television broadcasting.

%package -n %libmltxx
Summary: C++ wrapping for the MLT library
Group: System/Libraries
%description -n %libmltxx
This mlt sub-project provides a C++ wrapping for the MLT library.

%package -n %name-devel
Summary: Development files for %Name framework
Group: Development/C
%description -n %name-devel
Development files for %Name framework.

%package -n %{name}xx-devel
Summary: Development files for %Name
Group: Development/C++
Requires: %name-devel
%description -n %{name}xx-devel
Development files for %Name.

%package -n python3-module-%name
Summary: Python package to work with %Name
Group: Development/Python
%description -n python3-module-%name
This module allows to work with %Name using python..

%prep
%setup -n %nam-%version
%if %is_ffmpeg
%else
%patch20 -p1
%endif
%patch102 -p1
%if %is_ffmpeg
%else
%patch103 -p1
%endif
%patch104 -p1

[ -f src/mlt++/config.h ] || \
    install -m 0644 %SOURCE1 src/mlt++/config.h

%ifarch %e2k
sed -i 's,-fno-tree-pre,,' src/modules/xine/CMakeLists.txt
%endif

%build
%mIF_ver_lt %_qt5_version 5.9
%add_optflags -std=c++11
%endif
%ifarch %e2k
# -std=c++03 by default as of lcc 1.23.12
%add_optflags -std=c++11
%endif
export CC=gcc CXX=g++ CFLAGS="%optflags" QTDIR=%_qt5_prefix
%if %is_ffmpeg
%add_optflags -DAVDATADIR="%_datadir/ffmpeg/"
%else
%add_optflags -DAVDATADIR="%_datadir/avconv/"
%endif
%K5build \
    -DSWIG_PYTHON=ON \
    -DMOD_OPENCV=%{?_enable_opencv:ON}%{!?_enable_opencv:OFF} \
    #

%install
%make -C BUILD DESTDIR=%buildroot install

%files -n %nam-utils
%_bindir/melt*
%_man1dir/*.1.*

%files -n %libmlt
%_libdir/libmlt-%mlt_major.so.%mlt_sover
%_libdir/libmlt-%mlt_major.so.*
%_libdir/mlt-%mlt_major/
%_datadir/mlt-%mlt_major/

%files -n %libmltxx
%_libdir/libmlt++-%mlt_major.so.%mltxx_sover
%_libdir/libmlt++-%mlt_major.so.*

%files -n python3-module-%name
%python3_sitelibdir/*%{name}*
%python3_sitelibdir/*/*%{name}*

%files -n %name-devel
%dir %_includedir/mlt-%mlt_major/
%_includedir/mlt-%mlt_major/framework/
%_libdir/libmlt-%mlt_major.so
%_libdir/cmake/Mlt7/
%_pkgconfigdir/mlt-framework-%mlt_major.pc

%files -n %{name}xx-devel
%_includedir/mlt-%mlt_major/mlt++/
%_libdir/libmlt++-%mlt_major.so
%_pkgconfigdir/mlt++-%mlt_major.pc

%changelog
* Wed Jul 13 2022 Sergey V Turchin <zerg@altlinux.org> 7.8.0-alt1
- new version

* Thu Nov 18 2021 Sergey V Turchin <zerg@altlinux.org> 7.2.0-alt1
- new version

* Tue Aug 31 2021 Sergey V Turchin <zerg@altlinux.org> 7.0.1-alt1
- new version

* Wed Jul 21 2021 Andrey Sokolov <keremet@altlinux.org> 6.26.1-alt2
- add build requirements for libmltgdk.so (closes 40556)

* Wed Jul 14 2021 Sergey V Turchin <zerg@altlinux.org> 6.26.1-alt1
- new version

* Thu Dec 31 2020 L.A. Kostis <lakostis@altlinux.ru> 6.24.0-alt1.1
- add libSDL support (fix flowblade segfault).

* Thu Dec 31 2020 L.A. Kostis <lakostis@altlinux.ru> 6.24.0-alt1
- new version

* Tue Aug 25 2020 Sergey V Turchin <zerg@altlinux.org> 6.22.1-alt1
- new version

* Thu Jun 11 2020 Sergey V Turchin <zerg@altlinux.org> 6.20.0-alt1
- new version

* Fri Jan 24 2020 Sergey V Turchin <zerg@altlinux.org> 6.18.0-alt1
- new version

* Wed Jul 31 2019 Michael Shigorin <mike@altlinux.org> 6.16.0-alt4
- introduced libvidstab knob (on by default)
- E2K: explicit -std=c++11; avoid lcc-unsupported option

* Fri Jul 05 2019 Sergey V Turchin <zerg@altlinux.org> 6.16.0-alt3
- build with python3

* Sun Jun 23 2019 Igor Vlasenko <viy@altlinux.ru> 6.16.0-alt2
- NMU: remove rpm-build-ubt from BR:

* Wed May 08 2019 Sergey V Turchin <zerg@altlinux.org> 6.16.0-alt1
- new version

* Tue Mar 26 2019 Sergey V Turchin <zerg@altlinux.org> 6.12.0-alt1
- new version

* Wed Jul 11 2018 Sergey V Turchin <zerg@altlinux.org> 6.10.0-alt1.1
- fix build requires

* Fri Jul 06 2018 Sergey V Turchin <zerg@altlinux.org> 6.10.0-alt1
- new version

* Thu Jun 14 2018 Sergey V Turchin <zerg@altlinux.org> 6.8.0-alt1
- new version

* Thu Apr 05 2018 Oleg Solovyov <mcpain@altlinux.org> 6.6.0-alt2
- rebuild with libvidstab

* Sun Mar 18 2018 Fr. Br. George <george@altlinux.ru> 6.6.0-alt1
- Autobuild version bump to 6.6.0

* Tue Dec 26 2017 Sergey V Turchin <zerg@altlinux.org> 6.4.1-alt5
- fix to build with glibc-2.26

* Wed Nov 01 2017 Sergey V Turchin <zerg@altlinux.org> 6.4.1-alt4.1
- fix compile flags

* Wed Nov 01 2017 Sergey V Turchin <zerg@altlinux.org> 6.4.1-alt4
- Allow Mlt::Repository to be deleted without bad side effect (ALT#34108)

* Tue Jun 20 2017 Sergey V Turchin <zerg@altlinux.org> 6.4.1-alt3
- fix find ffmpeg presets
- update Debian patches

* Tue Jun 06 2017 Sergey V Turchin <zerg@altlinux.org> 6.4.1-alt2
- rebuild with ffmpeg

* Tue Apr 04 2017 Sergey V Turchin <zerg@altlinux.org> 6.4.1-alt1
- new version
- build without libswfdec (ALT#33326)

* Thu Apr 28 2016 Sergey V Turchin <zerg@altlinux.org> 6.2.0-alt4
- fix obsoletes

* Wed Apr 27 2016 Sergey V Turchin <zerg@altlinux.org> 6.2.0-alt3
- fix build requires

* Tue Apr 26 2016 Sergey V Turchin <zerg@altlinux.org> 6.2.0-alt2
- fix build requires

* Tue Apr 26 2016 Sergey V Turchin <zerg@altlinux.org> 6.2.0-alt1
- new version

* Fri Sep 25 2015 Sergey V Turchin <zerg@altlinux.org> 0.9.8-alt1
- new version

* Wed Jul 29 2015 Sergey V Turchin <zerg@altlinux.org> 0.9.6-alt2
- build with qt5

* Mon Jun 15 2015 Sergey V Turchin <zerg@altlinux.org> 0.9.6-alt1
- new version

* Thu Apr 16 2015 Sergey V Turchin <zerg@altlinux.org> 0.9.2-alt1.M70P.1
- build for M70P

* Fri Feb 27 2015 Denis Smirnov <mithraen@altlinux.ru> 0.9.2-alt2
- rebuild with new sox

* Fri Oct 17 2014 Sergey V Turchin <zerg@altlinux.org> 0.9.2-alt1
- new version

* Fri Oct 17 2014 Sergey V Turchin <zerg@altlinux.org> 0.9.0-alt0.M70P.1
- built for M70P

* Tue May 27 2014 Sergey V Turchin <zerg@altlinux.org> 0.9.0-alt1
- new version

* Tue Oct 08 2013 Sergey V Turchin <zerg@altlinux.org> 0.8.8-alt3
- rebuilt with new libav

* Thu May 23 2013 Sergey V Turchin <zerg@altlinux.org> 0.8.8-alt2
- disable VDPAU by default ( http://www.kdenlive.org/mantis/view.php?id=3070 )

* Thu Jan 31 2013 Sergey V Turchin <zerg@altlinux.org> 0.8.8-alt1
- new version

* Tue Oct 16 2012 Denis Smirnov <mithraen@altlinux.ru> 0.7.8-alt1.1
- rebuild with new sox

* Wed May 16 2012 Sergey V Turchin <zerg@altlinux.org> 0.7.8-alt1
- new version

* Fri May 04 2012 Sergey V Turchin <zerg@altlinux.org> 0.7.6-alt0.M60P.2
- rebuild with libav

* Thu Dec 29 2011 Sergey V Turchin <zerg@altlinux.org> 0.7.6-alt0.M60P.1
- built for M60P

* Mon Dec 12 2011 Sergey V Turchin <zerg@altlinux.org> 0.7.6-alt1
- new version

* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.7.4-alt1.1
- Rebuild with Python-2.7

* Fri Aug 12 2011 Sergey V Turchin <zerg@altlinux.org> 0.7.4-alt0.M60P.1
- built for M60P

* Thu Aug 11 2011 Sergey V Turchin <zerg@altlinux.org> 0.7.4-alt1
- new version

* Fri Jul 08 2011 Sergey V Turchin <zerg@altlinux.org> 0.7.2-alt1
- new version

* Wed Apr 27 2011 Sergey V Turchin <zerg@altlinux.org> 0.7.0-alt1
- new version

* Thu Sep 16 2010 Sergey V Turchin <zerg@altlinux.org> 0.5.10-alt0.M51.1
- built for M51

* Wed Sep 15 2010 Sergey V Turchin <zerg@altlinux.org> 0.5.10-alt1
- new version

* Thu Jun 17 2010 Sergey V Turchin <zerg@altlinux.org> 0.5.4-alt1.M51.1
- built for M51

* Thu Jun 17 2010 Sergey V Turchin <zerg@altlinux.org> 0.5.4-alt2
- fix build flags

* Thu Jun 17 2010 Sergey V Turchin <zerg@altlinux.org> 0.5.4-alt1
- 0.5.4

* Wed Apr 14 2010 Maxim Ivanov <redbaron at altlinux.org> 0.5.2-alt1
- 0.5.2

* Tue Jan 12 2010 Slava Dubrovskiy <dubrsl@altlinux.org> 0.4.6-alt2
- Add subpackage python-module-name

* Thu Nov 12 2009 Maxim Ivanov <redbaron at altlinux.org> 0.4.6-alt1
- 0.4.6
- mlt++.so.2 -> mlt++.so.3 soname change

* Fri Jul 31 2009 Denis Smirnov <mithraen@altlinux.ru> 0.4.4-alt1
- 0.4.4

* Sun Jun 28 2009 Maxim Ivanov <redbaron at altlinux.org> 0.4.2-alt1.git2b33565
- Bump to 0.4.2
- inigo utility renamed to melt
- mlt-config removed, use `pkg-config mlt-framework` instead
- miracle, humperdink and valerie are moved to separate project
- mlt++ is not part of main tree

* Sat May 16 2009 Maxim Ivanov <redbaron at altlinux.org> 0.3.8-alt2
- Fix missed libm dynamic link, closes #20024

* Sat Apr 18 2009 Maxim Ivaniv <redbaron at altlinux.org> 0.3.8-alt1
- 0.3.8

* Thu Feb 05 2009 Valery Inozemtsev <shrek@altlinux.ru> 0.3.6-alt1
- 0.3.6

* Wed Dec 31 2008 Valery Inozemtsev <shrek@altlinux.ru> 0.3.4-alt1
- 0.3.4

* Fri Dec 12 2008 Valery Inozemtsev <shrek@altlinux.ru> 0.3.2-alt1
- 0.3.2

* Thu Aug 07 2008 Valery Inozemtsev <shrek@altlinux.ru> 0.3.0-alt1
- 0.3.0

* Fri Jun 13 2008 Valery Inozemtsev <shrek@altlinux.ru> 0.2.5-alt1.svn1045
- rebuild with libquicktime.so.102

* Thu Dec 20 2007 Valery Inozemtsev <shrek@altlinux.ru> 0.2.5-alt0.svn1045
- SVN revision r1045 2007-12-08

* Mon Sep 03 2007 Alexey Morsov <swi@altlinux.ru> 0.2.4-alt1
- 0.2.4
- new patch set (thanks to shrek@)
- lot of bug fixes

* Fri Jun 29 2007 Alexey Morsov <swi@altlinux.ru> 0.2.2-alt0.7
- changes for new ffmpeg

* Mon Apr 23 2007 Alexey Morsov <swi@altlinux.ru> 0.2.2-alt0.6
- add patch from gentoo to fix mmx on ix86
- disable mmx

* Fri Apr 20 2007 Alexey Morsov <swi@altlinux.ru> 0.2.2-alt0.5
- remove disable_fox and arch dependencies from spec (for sox >= 13.0)
- add patch for build with sox
- add sox in BR due to bug in req's in sox-devel

* Wed Feb 14 2007 Alexey Morsov <swi@altlinux.ru> 0.2.2-alt0.4
- add Packager (swi@)

* Wed Feb 14 2007 Led <led@altlinux.ru> 0.2.2-alt0.3
- fixed name-0.2.2-modulesdir.patch

* Tue Feb 13 2007 Led <led@altlinux.ru> 0.2.2-alt0.2
- added name-0.2.2-configure.patch
- added name-0.2.2-x86_64.patch

* Tue Feb 13 2007 Led <led@altlinux.ru> 0.2.2-alt0.1
- initial build
- added name-0.2.2-modulesdir.patch
