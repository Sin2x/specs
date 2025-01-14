Summary: Ristretto is an image-viewer for the Xfce Desktop Environment
Name: ristretto
Version: 0.12.3
Release: alt1
License: GPLv2+
Url: https://docs.xfce.org/apps/ristretto/start

Vcs: https://gitlab.xfce.org/apps/ristretto.git
Source: %name-%version.tar
Patch: %name-%version-%release.patch
Patch1: fix_for_libmagic_4.patch

Group: Graphical desktop/XFce
Packager: Xfce Team <xfce@packages.altlinux.org>

BuildPreReq: rpm-build-xfce4 xfce4-dev-tools >= 4.16.0
BuildRequires: libxfce4ui-gtk3-devel libxfce4util-devel libxfconf-devel
BuildRequires: intltool libexif-devel libcairo-devel libmagic-devel

%define _unpackaged_files_terminate_build 1

%description
Ristretto is a fast and lightweight image-viewer for the Xfce desktop
environment.

%prep
%setup
%patch -p1
case "$(rpm -q --qf "%%{VERSION}" libmagic-devel)" in
	4.*)
%patch1 -p1
	;;
esac

%build
%xfce4reconf
%configure \
	--enable-maintainer-mode \
	--enable-debug=minimum
%make_build

%install
%makeinstall_std
%find_lang %name

%files -f %name.lang
%doc README.md NEWS AUTHORS
%_bindir/*
%_desktopdir/*.desktop
%_datadir/metainfo/*.appdata.xml
%_iconsdir/hicolor/*/apps/*

%changelog
* Mon Jul 11 2022 Mikhail Efremov <sem@altlinux.org> 0.12.3-alt1
- Updated to 0.12.3.

* Fri Jan 14 2022 Mikhail Efremov <sem@altlinux.org> 0.12.2-alt1
- Updated to 0.12.2.

* Wed Dec 01 2021 Mikhail Efremov <sem@altlinux.org> 0.12.1-alt2
- Fixed build with libmagic-4.x.

* Fri Nov 26 2021 Mikhail Efremov <sem@altlinux.org> 0.12.1-alt1
- Updated to 0.12.1.

* Mon Oct 11 2021 Mikhail Efremov <sem@altlinux.org> 0.12.0-alt1
- Updated to 0.12.0.

* Fri Jun 11 2021 Mikhail Efremov <sem@altlinux.org> 0.11.0-alt1
- Dropped exo-csource from BR.
- Added Vcs tag.
- Updated Url tag.
- Don't use rpm-build-licenses.
- Updated to 0.11.0.

* Wed Aug 14 2019 Mikhail Efremov <sem@altlinux.org> 0.10.0-alt1
- Updated to 0.10.0.
- Workaround for segfault.

* Sun Jul 21 2019 Mikhail Efremov <sem@altlinux.org> 0.8.5-alt1
- Updated to 0.8.5.

* Mon Apr 08 2019 Mikhail Efremov <sem@altlinux.org> 0.8.4-alt1
- Updated to 0.8.4.

* Fri Aug 17 2018 Mikhail Efremov <sem@altlinux.org> 0.8.3-alt2
- Update url.
- Rebuild with libxfconf-0.so.3.

* Wed Jul 18 2018 Mikhail Efremov <sem@altlinux.org> 0.8.3-alt1
- Updated to 0.8.3.

* Wed Feb 01 2017 Mikhail Efremov <sem@altlinux.org> 0.8.2-alt1
- Enabled debug (minimum).
- Updated to 0.8.2.

* Thu Oct 06 2016 Mikhail Efremov <sem@altlinux.org> 0.8.1-alt1
- Updated to 0.8.1.

* Fri Mar 06 2015 Mikhail Efremov <sem@altlinux.org> 0.8.0-alt1
- Fix Xfce name (XFCE -> Xfce).
- Drop obsoleted translations patch.
- Updated to 0.8.0.

* Tue May 21 2013 Mikhail Efremov <sem@altlinux.org> 0.6.3-alt2
- Add ristretto-0.6-translations.patch.
- Patch from upstream:
  + Fixed an overflow when comparing filenames with large
    numbers in them.

* Wed Aug 08 2012 Mikhail Efremov <sem@altlinux.org> 0.6.3-alt1
- Updated to 0.6.3.

* Thu Jun 07 2012 Mikhail Efremov <sem@altlinux.org> 0.6.0-alt2
- Fix segfault when image-quality property is changed (from upstream).

* Sun Apr 29 2012 Mikhail Efremov <sem@altlinux.org> 0.6.0-alt1
- Updated to 0.6.0.

* Tue Apr 17 2012 Mikhail Efremov <sem@altlinux.org> 0.5.2-alt1
- Updated to 0.5.2.

* Tue Jan 17 2012 Mikhail Efremov <sem@altlinux.org> 0.3.2-alt1
- Build documentation again.
- Updated to 0.3.2.

* Wed Jan 11 2012 Mikhail Efremov <sem@altlinux.org> 0.3.1-alt1
- Updated to 0.3.1.

* Thu Nov 17 2011 Mikhail Efremov <sem@altlinux.org> 0.3.0-alt2
- Build documentation.

* Mon Nov 14 2011 Mikhail Efremov <sem@altlinux.org> 0.3.0-alt1
- Updated to 0.3.0.

* Fri Oct 21 2011 Mikhail Efremov <sem@altlinux.org> 0.2.0-alt1
- Updated to 0.2.0.

* Thu Oct 13 2011 Mikhail Efremov <sem@altlinux.org> 0.1.1-alt1
- Drop obsoleted patch.
- Updated to 0.1.1.

* Thu Mar 17 2011 Mikhail Efremov <sem@altlinux.org> 0.0.93-alt1
- Add patches from upstream:
    + Fix opening of directories from the command-line.
    + Include string.h in thumbnailer.c.
- Drop dsofix.patch (fixed in upstream).
- Updated to 0.0.93.

* Wed Feb 09 2011 Mikhail Efremov <sem@altlinux.org> 0.0.91-alt1
- Fix DSO linking (patch from Fedora).
- Spec updated, tar.gz -> tar.
- Drop watch file.
- Updated to 0.0.91.

* Fri May 08 2009 Ilya Mashkin <oddity@altlinux.ru> 0.0.21-alt2
- fix build, update requires

* Mon Dec 29 2008 Eugene Ostapets <eostapets@altlinux.ru> 0.0.21-alt1
- new version

* Sat May 10 2008 Eugene Ostapets <eostapets@altlinux.ru> 0.0.19-alt1
- new version

* Mon Jan 28 2008 Eugene Ostapets <eostapets@altlinux.ru> 0.0.16-alt1
- new version

* Wed Dec 26 2007 Eugene Ostapets <eostapets@altlinux.ru> 0.0.15-alt1
- first build for Sisyphus

