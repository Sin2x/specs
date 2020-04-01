%define _unpackaged_files_terminate_build 1
%define oname zope.tales

%def_with check

Name: python3-module-%oname
Version: 5.0.2
Release: alt1

Summary: Zope Template Application Language Expression Syntax (TALES)
License: ZPLv2.1
Group: Development/Python3
# Source-git https://github.com/zopefoundation/zope.tales.git
Url: http://pypi.python.org/pypi/zope.tales

Source: %oname-%version.tar
Patch0: fix-import.patch

BuildRequires(pre): rpm-build-python3

%if_with check
BuildRequires: python3-module-zope.testrunner
BuildRequires: python3-module-zope.testing
BuildRequires: python3-module-six
BuildRequires: python3-module-zope.tales
BuildRequires: python3-module-zope.tales-tests
%endif

%py3_requires zope.interface six


%description
Template Attribute Language - Expression Syntax.

%package tests
Summary: Tests for zope.tales (Python 3)
Group: Development/Python3
Requires: python3-module-%oname = %EVR
%py3_requires zope.testrunner

%description tests
This package contains tests for %oname

%prep
%setup -q -n %oname-%version
%patch0 -p2

%build
%python3_build

%install
%python3_install

%if "%python3_sitelibdir_noarch" != "%python3_sitelibdir"
install -d %buildroot%python3_sitelibdir
mv %buildroot%python3_sitelibdir_noarch/* \
	%buildroot%python3_sitelibdir/
%endif

%check
%if 0
zope-testrunner3 --test-path=src -vv
%endif

%files
%doc *.txt *.rst
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*.pth
%exclude %python3_sitelibdir/*/*/tests

%files tests
%python3_sitelibdir/*/*/tests


%changelog
* Wed Apr 01 2020 Andrey Bychkov <mrdrew@altlinux.org> 5.0.2-alt1
- Version updated to 5.0.2.

* Mon Dec 02 2019 Andrey Bychkov <mrdrew@altlinux.org> 4.2.0-alt4
- python2 disabled

* Sun Jun 23 2019 Igor Vlasenko <viy@altlinux.ru> 4.2.0-alt3
- NMU: remove rpm-build-ubt from BR:

* Sat Jun 15 2019 Igor Vlasenko <viy@altlinux.ru> 4.2.0-alt2
- NMU: remove %ubt from release

* Tue Feb 20 2018 Stanislav Levin <slev@altlinux.org> 4.2.0-alt1%ubt
- 4.1.1 -> 4.2.0

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 4.1.1-alt1.1.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Mon Jun 06 2016 Ivan Zakharyaschev <imz@altlinux.org> 4.1.1-alt1.1.1
- (AUTO) subst_x86_64.

* Mon Mar 14 2016 Ivan Zakharyaschev <imz@altlinux.org> 4.1.1-alt1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Fri Aug 28 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.1.1-alt1
- Version 4.1.1
- Enabled check

* Tue Dec 30 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.1.0-alt1
- Version 4.1.0

* Mon Dec 02 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.2-alt1
- Version 4.0.2

* Wed Apr 10 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.1-alt1
- Version 4.0.1

* Fri Mar 22 2013 Aleksey Avdeev <solo@altlinux.ru> 3.5.1-alt4.1
- Rebuild with Python-3.3

* Tue Apr 17 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.5.1-alt4
- Added module for Python 3

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 3.5.1-alt3.1
- Rebuild with Python-2.7

* Wed Jun 29 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.5.1-alt3
- Added necessary requirements
- Excluded *.pth

* Thu May 19 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.5.1-alt2
- Set as archdep package

* Tue May 17 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.5.1-alt1
- Initial build for Sisyphus

