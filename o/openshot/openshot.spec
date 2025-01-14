
%def_enable snapshot

%ifarch %e2k ppc64le
%def_disable qtwebengine
%else
%def_enable qtwebengine
%endif

%define ver_major 2.6
%define xdg_name org.openshot.OpenShot
Name: openshot
Version: %ver_major.1
Release: alt2

Summary: Non Linear Video Editor using Python and MLT
Group: Video
License: GPL-3.0
Url: http://www.openshotvideo.com/

%define _name  %name-qt

%if_disabled snapshot
#Source: https://launchpad.net/%name/%ver_major/%version/+download/%name-qt-%version.tar.gz
Source: https://github.com/OpenShot/openshot-qt/archive/v%version/%_name-%version.tar.gz
%else
Vcs: https://github.com/OpenShot/openshot-qt.git
Source: %_name-%version.tar
%endif

# https://github.com/OpenShot/openshot-qt/pull/4527
Patch10: %_name-2.6.1-py310_fix.patch

# blender > 2.80 doesn't support 32-bit
ExcludeArch: i586 armh

Requires: python3-module-%name >= 0.2.7
Requires: blender inkscape xdg-utils

%add_typelib_req_skiplist typelib(Unity)
# should be self-satisfied
%add_python3_req_skip classes classes.legacy.openshot.classes images
# should be provided by blender
%add_python3_req_skip bpy.props
%if_enabled qtwebengine
%add_python3_req_skip PyQt5.QtWebKit PyQt5.QtWebKitWidgets
%else
%add_python3_req_skip PyQt5.QtWebEngineCore PyQt5.QtWebEngineWidgets
%endif

BuildRequires(pre): rpm-build-python3 rpm-build-gir
BuildRequires: python3-devel python3-module-setuptools python3-module-PyQt5

%description
OpenShot Video Editor is a free, open-source, non-linear video editor. It
can create and edit videos and movies using many popular video, audio,
and image formats. Create videos for YouTube, Flickr, Vimeo, Metacafe,
Xbox, and many more common formats.

%prep
%setup -n %_name-%version
%patch10 -p1 -b .python3-10

%build
%python3_build

%install
%python3_install --install-lib=%python3_sitelibdir

%files
%_bindir/*
%python3_sitelibdir/%{name}_qt/
%python3_sitelibdir/*.egg-info/
%_pixmapsdir/*
%_desktopdir/*
%_iconsdir/hicolor/*/*/%{name}-qt*
%_datadir/mime/packages/*
%_datadir/metainfo/%xdg_name.appdata.xml
%doc AUTHORS README*


%changelog
* Thu Mar 17 2022 Yuri N. Sedunov <aris@altlinux.org> 2.6.1-alt2
- updated to v2.6.1-74-gb72327d1 from develop branch as in fedora/rpmfusion
  openshot-2.6.2*fc37.src.rpm package
- applied fixes for Python-3.10

* Fri Feb 04 2022 Sergey V Turchin <zerg@altlinux.org> 2.6.1-alt1.1
- using qtwebkit instead of qtwebengine on e2k and ppc64le

* Tue Sep 07 2021 Yuri N. Sedunov <aris@altlinux.org> 2.6.1-alt1
- 2.6.1

* Wed Aug 25 2021 Yuri N. Sedunov <aris@altlinux.org> 2.6.0-alt1
- 2.6.0

* Fri Jul 02 2021 Yuri N. Sedunov <aris@altlinux.org> 2.5.2-alt2
- removed QtWebKitWidgets dependency (ALT #40362)

* Sun Feb 21 2021 Yuri N. Sedunov <aris@altlinux.org> 2.5.2-alt1
- 2.5.2

* Thu Sep 10 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 2.5.1-alt3
- NMU: package is no longer noarch (ALT #38916)

* Thu Sep 10 2020 Yuri N. Sedunov <aris@altlinux.org> 2.5.1-alt2
- rebuilt for 64-bit platforms only (ALT #38916)

* Mon Mar 16 2020 Yuri N. Sedunov <aris@altlinux.org> 2.5.1-alt1
- 2.5.1

* Mon Feb 10 2020 Yuri N. Sedunov <aris@altlinux.org> 2.5.0-alt1
- 2.5.0

* Sat Mar 30 2019 Yuri N. Sedunov <aris@altlinux.org> 2.4.4-alt1
- 2.4.4

* Sun Sep 23 2018 Yuri N. Sedunov <aris@altlinux.org> 2.4.3-alt1
- 2.4.3

* Sat Jun 30 2018 Yuri N. Sedunov <aris@altlinux.org> 2.4.2-alt1
- 2.4.2

* Mon Nov 13 2017 Yuri N. Sedunov <aris@altlinux.org> 2.4.1-alt1
- 2.4.1

* Fri Sep 08 2017 Yuri N. Sedunov <aris@altlinux.org> 2.4.0-alt1
- 2.4.0

* Fri Jun 02 2017 Yuri N. Sedunov <aris@altlinux.org> 2.3.4-alt1
- 2.3.4

* Mon May 29 2017 Yuri N. Sedunov <aris@altlinux.org> 2.3.3-alt1
- 2.3.3

* Fri May 12 2017 Yuri N. Sedunov <aris@altlinux.org> 2.3.2-alt1
- 2.3.2

* Wed Apr 05 2017 Yuri N. Sedunov <aris@altlinux.org> 2.3.1-alt1
- 2.3.1

* Sat Apr 01 2017 Yuri N. Sedunov <aris@altlinux.org> 2.3.0-alt1
- 2.3.0

* Thu Jan 26 2017 Yuri N. Sedunov <aris@altlinux.org> 2.2.0-alt1
- 2.2.0 (qt5)

* Fri Sep 19 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.4.4-alt1.alpha1.bzr20131031
- Version 1.4.4~alpha1

* Tue Oct 02 2012 Slava Dubrovskiy <dubrsl@altlinux.org> 1.4.3-alt1
- New version

* Mon Apr 02 2012 Slava Dubrovskiy <dubrsl@altlinux.org> 1.4.2-alt3
- Rebuild with Blender

* Mon Mar 12 2012 Slava Dubrovskiy <dubrsl@altlinux.org> 1.4.2-alt2
- Add patch openshot-1.4.2-fix-dialog.patch for fix (ALT #25659) thanks serpiph@

* Tue Feb 07 2012 Slava Dubrovskiy <dubrsl@altlinux.org> 1.4.2-alt1
- New version (bugfix release)

* Mon Jan 30 2012 Slava Dubrovskiy <dubrsl@altlinux.org> 1.4.1-alt1
- New version

* Sat Oct 22 2011 Vitaly Kuznetsov <vitty at altlinux.ru> 1.4.0-alt1.1
- Rebuild with Python-2.7

* Fri Sep 30 2011 Slava Dubrovskiy <dubrsl@altlinux.org> 1.4.0-alt1
- New version

* Tue May 10 2011 Slava Dubrovskiy <dubrsl@altlinux.org> 1.3.1-alt1
- New version

* Sun Feb 27 2011 Slava Dubrovskiy <dubrsl@altlinux.org> 1.3.0-alt1
- New version

* Wed Sep 22 2010 Slava Dubrovskiy <dubrsl@altlinux.org> 1.2.2-alt1
- New version
- Close (ALT #24125)

* Mon Apr 19 2010 Slava Dubrovskiy <dubrsl@altlinux.org> 1.1.3-alt1
- New version

* Tue Mar 16 2010 Slava Dubrovskiy <dubrsl@altlinux.org> 1.1.1-alt1
- New version

* Tue Jan 12 2010 Slava Dubrovskiy <dubrsl@altlinux.org> 1.0.0-alt1
- Build for ALT
