%define oname SQLObject

Name: python3-module-SQLObject
Version: 3.7.3
Release: alt1

Summary: Object-Relational Manager, aka database wrapper for Python
License: LGPL
Group: Development/Python3
Url: http://sqlobject.org
BuildArch: noarch

Source: http://pypi.python.org/packages/source/S/%oname/%oname-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python-tools-2to3


%description
SQLObject is a popular *Object Relational Manager* for providing an
object interface to your database, with tables as classes, rows as
instances, and columns as attributes.

SQLObject includes a Python-object-based query language that makes SQL
more abstract, and provides substantial database independence for
applications.

Supports MySQL, PostgreSQL, SQLite, Firebird, Sybase, and MaxDB (SAPDB).

%package doc
Summary: This package contains documentation for SQLObject.
Group: Development/Python

%description doc
SQLObject is a popular *Object Relational Manager* for providing an
object interface to your database, with tables as classes, rows as
instances, and columns as attributes.

SQLObject includes a Python-object-based query language that makes SQL
more abstract, and provides substantial database independence for
applications.

Supports MySQL, PostgreSQL, SQLite, Firebird, Sybase, and MaxDB (SAPDB).


%prep
%setup -n %oname-%version

sed -i 's|#!/usr/bin/env python|#!/usr/bin/env python3|' \
    $(find ./ -name '*.py')

%build
%python3_build

%install
%python3_install

%files
%doc README.rst
%_bindir/*
%python3_sitelibdir/*

%files doc
%doc docs/*


%changelog
* Fri Dec 06 2019 Andrey Bychkov <mrdrew@altlinux.org> 3.7.3-alt1
- Version updated to 3.7.3
- build for python2 disabled

* Wed May 16 2018 Andrey Bychkov <mrdrew@altlinux.org> 2.0.0-alt1.a2dev.20141028.1.2
- (NMU) rebuild with python3.6

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 2.0.0-alt1.a2dev.20141028.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Wed Jan 27 2016 Mikhail Efremov <sem@altlinux.org> 2.0.0-alt1.a2dev.20141028.1
- NMU: Use buildreq for BR.

* Fri Oct 31 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.0-alt1.a2dev.20141028
- Version 2.0.0a2dev-20141028

* Tue Aug 26 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.0-alt1.a1dev.20140817
- Version 2.0.0a1dev-20140817

* Wed Apr 17 2013 Fr. Br. George <george@altlinux.ru> 1.3.2-alt1.1
- Fix build with 2to3

* Wed Mar 20 2013 Aleksey Avdeev <solo@altlinux.ru> 1.3.2-alt1
- Version 1.3.2
- Added module for Python 3

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.13.0-alt1.1.1
- Rebuild with Python-2.7

* Mon Jul 04 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.13.0-alt1.1
- Fixed build

* Wed Oct 06 2010 Vitaly Lipatov <lav@altlinux.ru> 0.13.0-alt1
- build new version 0.13.0
- cleanup spec and build rules

* Fri Nov 20 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.10.2-alt1
- Rebuilt with python 2.6

* Mon Sep  1 2008 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.10.2-alt0.M41.1
- 0.10.2

* Thu Jan 24 2008 Grigory Batalov <bga@altlinux.ru> 0.7rc1-alt1.0.1
- Rebuilt with python-2.5.

* Sun Mar 25 2007 ALT QA Team Robot <qa-robot@altlinux.org> 0.7rc1-alt1.0
- Rebuilt with rpm-build-python-0.30-alt3.

* Sun Nov 06 2005 Maxim Bodyansky <maximbo@altlinux.ru> 0.7rc1-alt1
- Initial build for Sisyphus
