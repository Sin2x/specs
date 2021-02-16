Name: manatee-open
Version: 2.167.10
Release: alt4

Summary: Manatee is a corpus management tool
License: LGPLv2+
Group: System/Libraries
Url: http://nlp.fi.muni.cz/trac/noske/wiki/Downloads
Packager: Kirill Maslinsky <kirill@altlinux.org>
BuildRequires: gcc-c++ libpcre-devel perl-devel python3-module-setuptools libicu-devel libltdl7-devel swig
Conflicts: finlib
Obsoletes: finlib finlib-devel


Source: %name-%version.tar
Patch: %name-%version-%release.patch

%description
Manatee is a corpus management tool including corpus building and indexing,
fast querying and providing basic statistical measures. It utilitates a fast
indexing library called Finlib. 

%prep
%setup
%patch -p1

%build
#export MANATEE_REGISTRY=%_localstatedir/manatee
%configure PYTHON=python3 --with-icu
%make_build

%install
%makeinstall_std

%files 
%_libdir/*.so.*
%_bindir/*
%python3_sitelibdir/*.py*
%python3_sitelibdir/_manatee.so
%doc doc/*

%changelog
* Tue Feb 16 2021 Kirill Maslinsky <kirill@altlinux.org> 2.167.10-alt4
- fix build with python3.9 SWIG API

* Mon Apr 06 2020 Kirill Maslinsky <kirill@altlinux.org> 2.167.10-alt3
- remove ExclusiveArch: x86_64 (build on i586 fixed)

* Mon Apr 06 2020 Kirill Maslinsky <kirill@altlinux.org> 2.167.10-alt2
- fix typo in python shebangs

* Thu Mar 12 2020 Kirill Maslinsky <kirill@altlinux.org> 2.167.10-alt1
- 2.167.10
- built with python3
- drop java and ruby API, as apparently dropped upstream

* Wed Jan 02 2019 Kirill Maslinsky <kirill@altlinux.org> 2.158.8-alt1
- 2.158.8
- fix build with libicu >= 6.1
- drop dependency on finlib-devel

* Wed Jan 31 2018 Kirill Maslinsky <kirill@altlinux.org> 2.151.5-alt1
- 2.151.5

* Wed Oct 26 2016 Kirill Maslinsky <kirill@altlinux.org> 2.139.3-alt3
- build only for x86_64 (i586 unsupported upstream)

* Wed Oct 19 2016 Kirill Maslinsky <kirill@altlinux.org> 2.139.3-alt2
- fix build

* Wed Oct 19 2016 Kirill Maslinsky <kirill@altlinux.org> 2.139.3-alt1
- 2.139.3

* Sat Dec 05 2015 Kirill Maslinsky <kirill@altlinux.org> 2.130.6-alt1
- 2.130.6

* Wed Mar 18 2015 Kirill Maslinsky <kirill@altlinux.org> 2.107.1-alt1
- 2.107.1

* Wed Oct 02 2013 Kirill Maslinsky <kirill@altlinux.org> 2.59.1-alt1
- 2.59.1

* Tue Apr 10 2012 Kirill Maslinsky <kirill@altlinux.org> 2.33.1-alt1
- Initial build for Sisyphus

