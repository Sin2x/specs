Name: uzbl
Version: 20190110
Release: alt5
Group: Networking/WWW
License: GPL
Summary: The uzbl web interface tools
Packager: Vladislav Zavjalov <slazav@altlinux.org>
URL: http://www.uzbl.org

Source0: %name-%version.tar

BuildRequires: libwebkit2gtk-devel libgnutls-devel
BuildRequires: rpm-build-python3 python3-module-wheel python3-module-pip
BuildRequires: python3-module-mpl_toolkits
BuildRequires: python3-module-setuptools
Requires: python3-module-%name = %EVR
Requires: dmenu

%description
The uzbl web interface tools.

%package -n python3-module-%name
Summary: %name python3 module
Group: Development/Python3
BuildArch: noarch
Conflicts: %name < %version-%release

%description -n python3-module-%name
This package contains %name python3 module.

%prep
%setup

%build
%make PREFIX=/usr DOCDIR=%_docdir/uzbl LIB_SUFFIX="%_libsuff"

%install
%makeinstall PREFIX=/usr DESTDIR=%buildroot\
      DOCDIR=%buildroot/%_docdir/uzbl LIB_SUFFIX="%_libsuff"

# install vim syntax:
cp -r -- extras/vim %buildroot/%_datadir/vim

# make /usr/bin/uzbl symlink
ln -s -- uzbl-tabbed %buildroot/%_bindir/uzbl

# rm dist-info:
rm -rf %buildroot/%python3_sitelibdir_noarch/uzbl*.dist-info

%files
%_bindir/*
%dir %_libdir/uzbl
%_libdir/uzbl/*

%_desktopdir/uzbl*.desktop
%_iconsdir/hicolor/32x32/apps/uzbl.png
%_iconsdir/hicolor/48x48/apps/uzbl.png
%_iconsdir/hicolor/64x64/apps/uzbl.png
%_iconsdir/hicolor/96x96/apps/uzbl.png
%_datadir/appdata/uzbl*.xml

%_man1dir/uzbl*
%dir %_docdir/uzbl
%_docdir/uzbl/*

%_datadir/vim/ftplugin/uzbl.vim
%_datadir/vim/ftdetect/uzbl.vim
%_datadir/vim/syntax/uzbl.vim

%files -n python3-module-%name
%python3_sitelibdir_noarch/uzbl*

%changelog
* Mon Nov 16 2020 Dmitry V. Levin <ldv@altlinux.org> 20190110-alt5
- NMU.
- Fixed another FTBFS by moving python3 module into separate subpackage
  (closes: #39296, #39297).

* Mon Nov 16 2020 Vladimir D. Seleznev <vseleznv@altlinux.org> 20190110-alt4
- Fixed FTBFS.

* Sat Jan 19 2019 Vladislav Zavjalov <slazav@altlinux.org> 20190110-alt3
- Remove buildroot path from uzbl-core

* Thu Jan 17 2019 Vladislav Zavjalov <slazav@altlinux.org> 20190110-alt2
- use /usr/share/doc/uzbl instead of /usr/share/uzbl to avoid
  extra dependencies (closes #22613)

* Thu Jan 10 2019 Vladislav Zavjalov <slazav@altlinux.org> 20190110-alt1
- 2019.01.10 - "next" branch snapshot with webkit2 support
  (current stable version 0.9.2 does not support it)

* Sun Apr 14 2013 Andrey Cherepanov <cas@altlinux.org> 20111001-alt1.2
- Fix build with new glib2

* Mon Nov 07 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 20111001-alt1.1
- Rebuild with Python-2.7

* Mon Oct 24 2011 Alexey Shabalin <shaba@altlinux.ru> 20111001-alt1
- 2011.10.01 release
- build with libwebkitgtk3

* Sun Dec 05 2010 Vladislav Zavjalov <slazav@altlinux.org> 20101125-alt1
- 2010.11.25 release
- install vim syntax files
- add /usr/bin/uzbl (symlink to uzbl-tabbed)

* Wed Oct 20 2010 Vladislav Zavjalov <slazav@altlinux.org> 20100805-alt1
- 2010.08.05 release

* Sat May 08 2010 Vladislav Zavjalov <slazav@altlinux.org> 20100410-alt1
- current upstream snapshot

* Tue Feb 09 2010 Vladislav Zavjalov <slazav@altlinux.org> 20100202-alt1
- current upstream snapshot

* Fri Jan 15 2010 Vladislav Zavjalov <slazav@altlinux.org> 20100115-alt1
- current upstream snapshot

* Fri Dec 25 2009 Vladislav Zavjalov <slazav@altlinux.org> 20091224-alt1
- current upstream snapshot
- move some files from _datadir/uzbl/examples/ to _docdir/usbl/examples
  (closes: #22613)

* Wed Dec 16 2009 Vladislav Zavjalov <slazav@altlinux.org> 20091216-alt1
- build current version

* Tue Dec 08 2009 Vladislav Zavjalov <slazav@altlinux.org> 20091206-alt1
- first build for Altlinux

