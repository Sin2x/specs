%define oname xlib

%def_without check

Name: python3-module-%oname
Version: 0.29
Release: alt1

Summary: Python X Library

Group: Development/Python3
License: LGPL
Url: https://github.com/python-xlib/python-xlib

Source: %name-%version.tar

BuildRequires: /usr/bin/texi2html
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools python3-module-setuptools_scm

%if_with check
BuildRequires: python3-module-six
BuildRequires: python3(mock)
BuildRequires: python3-module-pytest
%endif

%description
The Python X Library is a complete X11R6 client-side implementation,
written in pure Python. It can be used to write low-levelish X Windows
client applications in Python.

%package docs
Summary: Documentation and examples for Python X Library
Group: Development/Documentation
BuildArch: noarch

%description docs
The Python X Library is a complete X11R6 client-side implementation,
written in pure Python. It can be used to write low-levelish X Windows
client applications in Python.

This package contains documentation and examples for Python X Library.

%prep
%setup

%build
%python3_build

pushd doc/html
%make SRCS=$PWD/../src TOPSRC=$PWD/../src/python-xlib.texi
popd

%install
%python3_install

# hack for x86_64 build
test -d %buildroot%_libdir || mv %buildroot%prefix/lib %buildroot%_libdir || :

%check
python3 setup.py test
py.test3 -vv

%files
%doc README.rst LICENSE TODO
%python3_sitelibdir/*

%files docs
%doc examples doc/html/*.html

%changelog
* Mon Nov 23 2020 Grigory Ustinov <grenka@altlinux.org> 0.29-alt1
- Automatically updated to 0.29.

* Tue Nov 10 2020 Grigory Ustinov <grenka@altlinux.org> 0.28-alt1
- Automatically updated to 0.28.

* Tue Sep 15 2020 Grigory Ustinov <grenka@altlinux.org> 0.27-alt1
- Automatically updated to 0.27.
- Drop python2 support.

* Thu Dec 19 2019 Grigory Ustinov <grenka@altlinux.org> 0.26-alt1
- Build new version 0.26.

* Tue May 14 2019 Grigory Ustinov <grenka@altlinux.org> 0.25-alt1
- New version 0.25

* Wed Mar 07 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 0.21-alt1
- Updated to upstream version 0.21.

* Tue Jan 03 2017 Anton Midyukov <antohami@altlinux.org> 0.18-alt1
- New version 0.18

* Mon Dec 07 2015 Igor Vlasenko <viy@altlinux.ru> 0.15-alt2.rc1.svn20131015
- added perl patch

* Wed Aug 27 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.15-alt1.rc1.svn20131015
- Snapshot from svn

* Mon Oct 24 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.15-alt1.rc1.1
- Rebuild with Python-2.7

* Sun Nov 28 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.15-alt1.rc1
- Version 0.15rc1

* Mon Nov 16 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.14-alt1.1.1
- Rebuilt with python 2.6

* Thu Jan 24 2008 Grigory Batalov <bga@altlinux.ru> 0.14-alt1.1
- Rebuilt with python-2.5.

* Tue Oct 16 2007 Vitaly Lipatov <lav@altlinux.ru> 0.14-alt1
- new version 0.14 (with rpmrb script)

* Tue Sep 12 2006 Vitaly Lipatov <lav@altlinux.ru> 0.12-alt2
- override alt1 in incoming :)
- fix hack for x86_64 :)

* Tue Jun 20 2006 Vitaly Lipatov <lav@altlinux.ru> 0.12-alt0.2
- hack for build at x86_64 (fix bug #9710)

* Sun Dec 18 2005 Vitaly Lipatov <lav@altlinux.ru> 0.12-alt0.1
- initial build for ALT Linux Sisyphus
