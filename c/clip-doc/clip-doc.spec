Name: clip-doc
Version: 1.2.0
Release: alt2

Summary: CLIP compiler documentation
Summary(ru_RU.UTF-8): Документация к компилятору CLIP

License: GPL
Group: Development/Other
Url: http://www.itk.ru

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: ftp://ftp.itk.ru/pub/clip/clip-doc-ru-html.tar.bz2
Source1: ftp://ftp.itk.ru/pub/clip/clip-doc-en-html.tar.bz2

BuildArch: noarch

%description
This package includes the clip compiler documentation

%description -l ru_RU.UTF-8
Данный пакет содержит документацию по компилятору clip

###################################################################################
%package ru
Summary: XBASE/Clipper compatible program compiler - documentation in russian
Summary(ru_RU.UTF-8): Документация на русском для компилятора CLIP
Group: Development/Other
#Requires: clip >= 1.1.14-alt2

%description ru
This package includes the clip compiler documentation in russian language.

%description ru -l ru_RU.UTF-8
Данный пакет содержит документацию к компилятору clip на русском языке.

###################################################################################
%package en
Summary: XBASE/Clipper compatible program compiler - documentation in english
Summary(ru_RU.UTF-8): Документация на английском для компилятора CLIP
Group: Development/Other
#Requires: clip >= 1.1.14-alt2

%description en
This package includes the clip compiler documentation in english language.

%description en -l ru_RU.UTF-8
Данный пакет содержит документацию к компилятору clip на английском языке.

%prep
tar xfj %SOURCE0
tar xfj %SOURCE1

%install
DOCDIR=%buildroot%_docdir/%name-%version
%__mkdir -p $DOCDIR
cp -rf html/ru $DOCDIR
cp -rf html/en $DOCDIR

%files ru
%_docdir/%name-%version/ru

%files en
%_docdir/%name-%version/en


%changelog
* Sun Sep 20 2020 Vitaly Lipatov <lav@altlinux.ru> 1.2.0-alt2
- fix cli-doc-ru summary (ALT bug 38619)
- change charset for descriptions (KOI8-R -> UTF-8)
- drop clip requires

* Sat Nov 18 2006 Vitaly Lipatov <lav@altlinux.ru> 1.2.0-alt1
- new version (1.2.0)

* Wed May 24 2006 Vitaly Lipatov <lav@altlinux.ru> 1.1.16-alt1
- new version (1.1.16)

* Sun Dec 18 2005 Vitaly Lipatov <lav@altlinux.ru> 1.1.15-alt1
- new version

* Sun Mar 20 2005 Vitaly Lipatov <lav@altlinux.ru> 1.1.14-alt1
- separate doc package

