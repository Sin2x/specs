%filter_from_requires /python2.*/d

%define prever %nil

Name: pychess
Version: 0.12.4
Release: alt3

Summary: Chess game for GNOME
License: GPLv2
Group: Games/Boards
Url: https://github.com/pychess/pychess/
Packager: Vitaly Lipatov <lav@altlinux.ru>

BuildArch: noarch

# Source-url: https://github.com/pychess/pychess/releases/download/%version/pychess-%version.tar.gz
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3 rpm-build-gir
BuildRequires: rpm-build-compat >= 1.2

# needed:
Requires: gnome-icon-theme
Requires: typelib(GtkSource) = 3.0

%add_python3_req_skip gi.repository.GdkPixbuf
%add_python3_req_skip pychess.Database
%add_python3_req_skip pychess.Database.dbwalk
%add_python3_req_skip pychess.Database.model


%description
PyChess is a GTK+ chess game for Linux. It is designed to at the same time
be easy to use, beautiful to look at, and provide advanced functions for
advanced players.

%prep
%setup -n %name-%version%{?prever}

%build
%python3_build

%install
# Fix line terminators
%__subst 's/.$//g' AUTHORS
%python3_install

#change permissions
chmod +x %buildroot%python3_sitelibdir/%name/Utils/Move.py
chmod +x %buildroot%python3_sitelibdir/%name/Players/PyChess.py
rm -rf %buildroot%_datadir/menu/

%find_lang %name

%files -f %name.lang
%doc README.md LICENSE AUTHORS
%_bindir/%name
%_datadir/%name/
%python3_sitelibdir/%name/
%python3_sitelibdir/*.egg-info
%_datadir/gtksourceview-3.0/language-specs/pgn.lang
%_datadir/appdata/pychess.appdata.xml
%_desktopdir/%name.desktop
%_iconsdir/hicolor/*/apps/*
%_pixmapsdir/*
%_man1dir/*

%changelog
* Wed Mar 25 2020 Andrey Bychkov <mrdrew@altlinux.org> 0.12.4-alt3
- Porting to python3.

* Mon Jul 30 2018 Anton Midyukov <antohami@altlinux.org> 0.12.4-alt2
- fix buildrequires and requires (Closes: 33434)

* Tue Jan 03 2017 Vitaly Lipatov <lav@altlinux.ru> 0.12.4-alt1
- new version 0.12.4 (with rpmrb script)

* Sun Aug 04 2013 Vitaly Lipatov <lav@altlinux.ru> 0.10.1-alt1
- new version 0.10.1 (with rpmrb script)

* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.10-alt1.1
- Rebuild with Python-2.7

* Sat Apr 02 2011 Vitaly Lipatov <lav@altlinux.ru> 0.10-alt1
- new version 0.10 (with rpmrb script)

* Fri Nov 13 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8.2-alt2.1
- Rebuilt with python 2.6

* Fri Jan 09 2009 Vitaly Lipatov <lav@altlinux.ru> 0.8.2-alt2
- cleanup spec, fix python-module-pygtksourceview requires (bug #16345)

* Sun Jun 08 2008 Vitaly Lipatov <lav@altlinux.ru> 0.8.2-alt1
- new version 0.8.2 (with rpmrb script)

* Tue Dec 25 2007 Vitaly Lipatov <lav@altlinux.ru> 0.8-alt1
- initial build for ALT Linux Sisyphus

* Mon Dec  3 2007 Michel Salim <michel.sylvan@gmail.com> - 0.8-0.1.beta2
- Update to 0.8beta2

* Sun Nov 11 2007 Michel Salim <michel.sylvan@gmail.com> - 0.8-0.1.beta1
- Update to 0.8beta1

* Thu Apr 19 2007 Sindre Pedersen Bjørdal <foolish[AT]guezz.net> - 0.6.0-1
- Update to 0.6.0 final

* Sun Jan 14 2007 Sindre Pedersen Bjørdal <foolish[AT]guezz.net> - 0.6.0-0.3.beta5
- Update description

* Sun Jan 14 2007 Sindre Pedersen Bjørdal <foolish[AT]guezz.net> - 0.6.0-0.2.beta5
- Fix permissions
- Fix quiet %%setup

* Sun Jan 14 2007 Sindre Pedersen Bjørdal <foolish[AT]guezz.net> - 0.6.0-0.1.beta5
- Initial build
