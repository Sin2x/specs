Name:     gwenhywfar
Version:  5.10.1
Release:  alt1

Summary:  A multi-platform helper library for other libraries
License:  LGPL-2.1+
Group:    System/Libraries
URL:      https://www.aquamaniac.de/rdm/projects/gwenhywfar
# VCS:    https://git.aquamaniac.de/git/gwenhywfar

Packager: Andrey Cherepanov <cas@altlinux.org>

Source:   %name-%version.tar
Patch2:   %name-fix-build-with-qt5.patch

BuildRequires: gcc-c++ glibc-devel graphviz libcom_err-devel 
BuildRequires: libgnutls-devel libssl-devel tzdata
BuildRequires: libgtk+2-devel
BuildRequires: libgtk+3-devel
BuildRequires: qt5-base-devel qt5-tools
BuildRequires: zlib-devel libgcrypt-devel ncurses-devel
BuildRequires: ca-certificates

Requires: ca-certificates

%description
This is Gwenhywfar, a multi-platform helper library for networking and
security applications and libraries. It is heavily used by libchipcard
www.libchipcard.de and OpenHBCI-TNG (The Next Generation)
www.openhbci.de.

Check http://www.freesource.info/wiki/Altlinux/Policy/TLS
for ALT Linux TLS/SSL policy

%package -n lib%name
Summary: A multi-platform helper library for other libraries
Group:    System/Libraries

%description -n lib%name
This is Gwenhywfar, a multi-platform helper library for networking and
security applications and libraries. It is heavily used by libchipcard
www.libchipcard.de and OpenHBCI-TNG (The Next Generation)
www.openhbci.de.

Check http://www.freesource.info/wiki/Altlinux/Policy/TLS
for ALT Linux TLS/SSL policy

%package  -n lib%name-gtk2
Summary:  Gwenhywfar support for GTK+ 2.x
Group:    System/Libraries
Requires: lib%name = %version-%release

%description -n lib%name-gtk2
Gwenhywfar support for GTK+ 2.x.

%package  -n lib%name-gtk3
Summary:  Gwenhywfar support for GTK+ 3.x
Group:    System/Libraries
Requires: lib%name = %version-%release

%description -n lib%name-gtk3
Gwenhywfar support for GTK+ 3.x.

%package  -n lib%name-qt5
Summary:  Gwenhywfar support for Qt5
Group:    System/Libraries
Requires: lib%name = %version-%release

%description -n lib%name-qt5
Gwenhywfar support for Qt5

%package  -n lib%name-devel
Summary:  Gwenhywfar development kit
Group:    Development/C
Requires: lib%name = %version-%release
Requires: lib%name-gtk2 = %version-%release
Requires: lib%name-qt5  = %version-%release

%description -n lib%name-devel
This package contains gwenhywfar-config and header files for writing and
compiling programs using Gwenhywfar.

%prep
%setup
%patch2 -p1

%build
%undefine _configure_gettext
%autoreconf
export PATH=$PATH:%_qt5_bindir
%configure \
	--disable-static \
	--with-guis="gtk2 gtk3 qt5" \
	--with-qt5-qmake=%_bindir/qmake-qt5 \
	--with-qt5-moc=%_bindir/moc-qt5 \
	--with-qt5-uic=%_bindir/uic-qt5

%make_build

%install
%makeinstall_std
%find_lang %name

# Use system-wide ca-certificates
rm -f %buildroot%_datadir/gwenhywfar/ca-bundle.crt
ln -s %_datadir/ca-certificates/ca-bundle.crt %buildroot%_datadir/gwenhywfar/ca-bundle.crt

%files -n lib%name -f %name.lang
%doc AUTHORS README TODO
%_bindir/gct-tool
%_bindir/gsa
%_libdir/*.so.*
%exclude %_libdir/libgwengui-gtk2.so.*
%exclude %_libdir/libgwengui-gtk3.so.*
%exclude %_libdir/libgwengui-qt5.so.*
%_libdir/%name/
%_datadir/gwenhywfar/ca-bundle.crt
%_datadir/gwenhywfar/dialogs/*.dlg

%files -n lib%name-gtk2
%_libdir/libgwengui-gtk2.so.*

%files -n lib%name-gtk3
%_libdir/libgwengui-gtk3.so.*

%files -n lib%name-qt5
%_libdir/libgwengui-qt5.so.*

%files -n lib%name-devel
%_bindir/%name-config
%_bindir/xmlmerge
%_bindir/mklistdoc
%_bindir/typemaker
%_bindir/typemaker2
%_libdir/*.so
%_includedir/gwenhywfar5/
%_pkgconfigdir/*
%_datadir/%name/typemaker2/*
%_datadir/aclocal/gwenhywfar.m4
%_libdir/cmake/*
# gwenbuild
%_bindir/gwbuild
%_datadir/gwenbuild/templates/project.tmpl
%_datadir/gwenhywfar/gwenbuild/builders

%changelog
* Sat Aug 13 2022 Andrey Cherepanov <cas@altlinux.org> 5.10.1-alt1
- New version.

* Sun Jul 31 2022 Andrey Cherepanov <cas@altlinux.org> 5.9.10-alt1
- New version.

* Wed Feb 16 2022 Andrey Cherepanov <cas@altlinux.org> 5.9.0-alt1
- New version.

* Fri Jan 14 2022 Andrey Cherepanov <cas@altlinux.org> 5.8.2-alt1
- New version.

* Mon Jan 03 2022 Andrey Cherepanov <cas@altlinux.org> 5.8.1-alt1
- New version.

* Mon Sep 27 2021 Andrey Cherepanov <cas@altlinux.org> 5.7.3-alt1
- New version.

* Sun Sep 19 2021 Andrey Cherepanov <cas@altlinux.org> 5.7.2-alt1
- New version.

* Mon Sep 13 2021 Andrey Cherepanov <cas@altlinux.org> 5.7.1-alt1
- New version.

* Fri Jul 02 2021 Andrey Cherepanov <cas@altlinux.org> 5.6.0-alt2
- Build without qt4.

* Tue Feb 16 2021 Andrey Cherepanov <cas@altlinux.org> 5.6.0-alt1
- New version.

* Sun Feb 14 2021 Andrey Cherepanov <cas@altlinux.org> 5.5.1-alt1
- New version.

* Wed Dec 23 2020 Andrey Cherepanov <cas@altlinux.org> 5.4.1-alt1
- New version.
- Fix License tag.

* Tue Feb 04 2020 Andrey Cherepanov <cas@altlinux.org> 5.1.2-alt1
- New version.

* Thu Oct 10 2019 Andrey Cherepanov <cas@altlinux.org> 4.99.22rc6-alt0.1
- New version.

* Thu Aug 29 2019 Andrey Cherepanov <cas@altlinux.org> 4.20.2-alt1
- New version.

* Wed Aug 29 2018 Grigory Ustinov <grenka@altlinux.org> 4.20.1-alt1.1
- NMU: Rebuild with new openssl 1.1.0.

* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 4.20.1-alt1
- New version.

* Mon Apr 02 2018 Andrey Cherepanov <cas@altlinux.org> 4.20.0-alt2
- Build gtk3 bindings.

* Fri Mar 02 2018 Andrey Cherepanov <cas@altlinux.org> 4.20.0-alt1
- New version.

* Mon Feb 19 2018 Andrey Cherepanov <cas@altlinux.org> 4.19.0-alt1
- New version.
- Build with Qt5.

* Tue Aug 01 2017 Andrey Cherepanov <cas@altlinux.org> 4.18.0-alt1
- New version

* Thu Mar 02 2017 Andrey Cherepanov <cas@altlinux.org> 4.17.0-alt1
- New version

* Tue Jun 21 2016 Andrey Cherepanov <cas@altlinux.org> 4.15.3-alt1
- New version

* Sun Dec 27 2015 Andrey Cherepanov <cas@altlinux.org> 4.14.0-alt3
- Update watch file after upstream site reconstruction
- Fix build with new gnutls
- Package cmake files

* Mon Dec 21 2015 Andrey Cherepanov <cas@altlinux.org> 4.14.0-alt2
- Do not use strict extension for man pages

* Wed May 27 2015 Andrey Cherepanov <cas@altlinux.org> 4.14.0-alt1
- new version 4.14.0

* Thu Apr 02 2015 Andrey Cherepanov <cas@altlinux.org> 4.13.1-alt1
- new version 4.13.1

* Wed Nov 28 2012 Andrey Cherepanov <cas@altlinux.org> 4.3.3-alt1
- new version 4.3.3

* Mon Jan 16 2012 Andrey Cherepanov <cas@altlinux.org> 4.3.1-alt1
- New version 4.3.1
- Add watch file

* Tue Sep 06 2011 Andrey Cherepanov <cas@altlinux.org> 4.2.1-alt1
- New version 4.2.1
- Use system-wide ca-certificates (closes: #10901)

* Thu Mar 03 2011 Andrey Cherepanov <cas@altlinux.org> 4.0.7-alt1
- New version 4.0.7
- Exclude qt4 and gtk+ libraries in separate packages

* Mon Oct 04 2010 Andrey Cherepanov <cas@altlinux.org> 3.11.3-alt2
- rebuild with new openssl

* Fri Apr 02 2010 Andrey Cherepanov <cas@altlinux.org> 3.11.3-alt1
- new version 3.11.3

* Wed Apr 15 2009 Vitaly Lipatov <lav@altlinux.ru> 3.8.0-alt1
- new version 3.8.0 (with rpmrb script)

* Mon Nov 24 2008 Vitaly Lipatov <lav@altlinux.ru> 3.5.2-alt1
- new version 3.5.2 (with rpmrb script)

* Sat Jul 26 2008 Vitaly Lipatov <lav@altlinux.ru> 3.2.0-alt2
- cleanup spec, move gct-tool to original dir
- fix bug #10901 (use ca-bundle.crt from datadir/ca-certificates/)

* Tue Apr 22 2008 Vitaly Lipatov <lav@altlinux.ru> 3.2.0-alt1
- new version 3.2.0 (with rpmrb script)
- update buildreqs

* Wed Apr 11 2007 Vitaly Lipatov <lav@altlinux.ru> 2.5.4-alt1
- new version 2.5.4
- do not pack /etc/gwen-public-ca.crt
- update buildreq, fix x86_64 build (use --with-openssl-libs (thanks at@))

* Mon Sep 11 2006 Vitaly Lipatov <lav@altlinux.ru> 2.4.0-alt0.1
- new version 2.4.0
- update buildreq

* Mon May 01 2006 Vitaly Lipatov <lav@altlinux.ru> 2.2.0-alt0.1
- new version

* Mon Dec 19 2005 Vitaly Lipatov <lav@altlinux.ru> 1.19.2-alt0.1
- new version

* Mon Aug 22 2005 Igor Muratov <migor@altlinux.org> 1.16.0-alt1
- new version

* Wed Aug 10 2005 Igor Muratov <migor@altlinux.org> 1.14.0-alt1
- new version

* Sun Mar 06 2005 Vitaly Lipatov <lav@altlinux.ru> 1.7.1-alt1
- first build for ALT Linux Sisyphus

