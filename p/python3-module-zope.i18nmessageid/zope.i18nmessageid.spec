%define _unpackaged_files_terminate_build 1
%define oname zope.i18nmessageid
%define descr \
This package provides facilities for *declaring* messages within \
program source text;  translation of the messages is the responsiblity \
of the 'zope.i18n' package.

%def_without check
%def_without docs

Name: python3-module-%oname
Version: 5.0.1
Release: alt3

Summary: Message Identifiers for internationalization
Group: Development/Python3

License: ZPL-2.1
# Source-git https://github.com/zopefoundation/zope.i18nmessageid.git
Url: http://pypi.python.org/pypi/zope.i18nmessageid
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
%if_with docs
BuildRequires(pre): rpm-macros-sphinx3
BuildRequires: python3-module-sphinx
%endif

%if_with check
BuildRequires: python3-module-zope.testing python3-module-zope.testrunner
%endif

%description
%descr

%package docs
Summary: Documentation for %oname
Group: Development/Documentation

%description docs
%descr

This package contains documentation for %oname.

%package pickles
Summary: Pickles for Zope Configuration Markup Language (ZCML)
Group: Development/Python3

%description pickles
%descr

This package contains pickles for %oname.

%package tests
Summary: Tests for %oname
Group: Development/Python3
Requires: %name = %EVR

%description tests
%descr

This package contains tests for %oname.

%prep
%setup

%if_with docs
%prepare_sphinx3 .
ln -s ../objects.inv docs/
%endif

%build
%add_optflags -fno-strict-aliasing
%python3_build

%if_with docs
%make SPHINXBUILD="sphinx-build-3" -C docs pickle
%make SPHINXBUILD="sphinx-build-3" -C docs html
%endif

%install
%python3_install

%if_with docs
install -d %buildroot%python3_sitelibdir/%oname
cp -fR docs/_build/pickle %buildroot%python3_sitelibdir/%oname/
%endif

%check
# coverage is the extra dep
grep -qs "^[[:space:]]*'coverage',[[:space:]]*$" setup.py || exit 1
sed -i "/^[[:space:]]*'coverage',[[:space:]]*$/d" setup.py

export PYTHONPATH=src
python3 setup.py test -v

%files
%doc *.txt *.rst
%python3_sitelibdir/*
%exclude %python3_sitelibdir/zope/i18nmessageid/tests.*
%if_with docs
%exclude %python3_sitelibdir/*/pickle

%files docs
%doc docs/_build/html

%files pickles
%python3_sitelibdir/*/pickle
%endif

%files tests
%python3_sitelibdir/zope/i18nmessageid/tests.*

%changelog
* Mon Dec 06 2021 Grigory Ustinov <grenka@altlinux.org> 5.0.1-alt3
- Bootstrap for python3.10.

* Mon May 31 2021 Grigory Ustinov <grenka@altlinux.org> 5.0.1-alt2
- Drop specsubst scheme.

* Tue Apr 28 2020 Stanislav Levin <slev@altlinux.org> 5.0.1-alt1
- 5.0.0 -> 5.0.1.

* Thu Jan 09 2020 Grigory Ustinov <grenka@altlinux.org> 5.0.0-alt1
- Build new version.
- Fix license.

* Fri Dec 28 2018 Grigory Ustinov <grenka@altlinux.org> 4.3.1-alt1
- Build new version.

* Mon May 14 2018 Grigory Ustinov <grenka@altlinux.org> 4.1.0-alt2
- Tranfer package to subst-packaging system.

* Thu Mar 22 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 4.1.0-alt1.S1.1
- (NMU) Rebuilt with python-3.6.4.

* Tue Mar 06 2018 Stanislav Levin <slev@altlinux.org> 4.1.0-alt1.S1
- 4.0.4 -> 4.1.0

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 4.0.4-alt1.dev0.git20150309.1.1.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Fri Mar 18 2016 Ivan Zakharyaschev <imz@altlinux.org> 4.0.4-alt1.dev0.git20150309.1.1.1
- (NMU) rebuild with python3-3.5 & rpm-build-python3-0.1.10
  (for ABI dependence and new python3(*) reqs)

* Fri Mar 18 2016 Ivan Zakharyaschev <imz@altlinux.org> 4.0.4-alt1.dev0.git20150309.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Fri Jan 29 2016 Mikhail Efremov <sem@altlinux.org> 4.0.4-alt1.dev0.git20150309.1
- NMU: Use buildreq for BR.

* Sat Aug 29 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.4-alt1.dev0.git20150309
- Version 4.0.4.dev0
- Added documentation
- Enabled check

* Sat Jul 26 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.3-alt1
- Version 4.0.3

* Tue Apr 09 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.2-alt1
- Version 4.0.2

* Fri Mar 22 2013 Aleksey Avdeev <solo@altlinux.ru> 3.6.1-alt2.1
- Rebuild with Python-3.3

* Mon Apr 16 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.6.1-alt2
- Added module for Python 3

* Thu Apr 12 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 3.6.1-alt1.1
- Rebuild to remove redundant libpython2.7 dependency

* Wed Dec 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.6.1-alt1
- Version 3.6.1

* Mon Oct 24 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 3.5.3-alt4.1
- Rebuild with Python-2.7

* Tue Jun 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.5.3-alt4
- Added necessary requirements
- Excluded *.pth

* Wed Jun 22 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.5.3-alt3
- Added %%py_provides zope.i18nmessageid

* Sun May 22 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.5.3-alt2
- Don't build python-module-zope.arch

* Mon May 16 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.5.3-alt1
- Initial build for Sisyphus

