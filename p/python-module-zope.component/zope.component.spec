%define _unpackaged_files_terminate_build 1
%define oname zope.component

%def_without check

Name: python-module-%oname
Version: 4.5
Release: alt4

Summary: Zope Component Architecture
License: ZPLv2.1
Group: Development/Python
# Source-git https://github.com/zopefoundation/zope.component.git
Url: http://pypi.python.org/pypi/zope.component

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python
BuildRequires(pre): rpm-build-python3

BuildRequires: python-module-setuptools
BuildRequires: python3-module-setuptools

%if_with check
BuildRequires: python-module-zope.testing
BuildRequires: python-module-zope.testrunner
BuildRequires: python-module-zope.configuration
BuildRequires: python-module-zope.interface
BuildRequires: python-module-zope.event
BuildRequires: python-module-zope.location
BuildRequires: python-module-zope.proxy
BuildRequires: python-module-zope.security
BuildRequires: python-module-zope.deferredimport
BuildRequires: python-module-zope.hookable
BuildRequires: python-module-zope.deprecation
BuildRequires: python3-module-zope.testing
BuildRequires: python3-module-zope.testrunner
BuildRequires: python3-module-zope.configuration
BuildRequires: python3-module-zope.interface
BuildRequires: python3-module-zope.event
BuildRequires: python3-module-zope.location
BuildRequires: python3-module-zope.proxy
BuildRequires: python3-module-zope.security
BuildRequires: python3-module-zope.deferredimport
BuildRequires: python3-module-zope.hookable
BuildRequires: python3-module-zope.deprecation
%endif

%py_requires zope.interface zope.event zope.configuration
%py_requires zope.deferredimport zope.deprecation
%py_requires zope.hookable zope.i18nmessageid
%py_requires zope.proxy zope.schema zope.security


%description
This package is intended to be independently reusable in any Python
project. It is maintained by the Zope Toolkit project.

This package represents the core of the Zope Component Architecture.
Together with the 'zope.interface' package, it provides facilities for
defining, registering and looking up components.

%package -n python3-module-%oname
Summary: Zope Component Architecture (Python 3)
Group: Development/Python3
%py3_requires zope

%description -n python3-module-%oname
This package is intended to be independently reusable in any Python
project. It is maintained by the Zope Toolkit project.

This package represents the core of the Zope Component Architecture.
Together with the 'zope.interface' package, it provides facilities for
defining, registering and looking up components.

%package -n python3-module-%oname-tests
Summary: Tests for zope.component (Python 3)
Group: Development/Python3
Requires: python3-module-%oname = %EVR
%py3_requires zope.testing zope.testrunner

%description -n python3-module-%oname-tests
This package contains tests for %oname

%package tests
Summary: Tests for zope.component
Group: Development/Python
Requires: %name = %EVR
%py_requires zope.testing zope.testrunner zope.configuration

%description tests
This package contains tests for %oname

%prep
%setup -n %name
rm -rf ../python3
cp -a . ../python3

%build
%python_build
pushd ../python3
%python3_build
popd

%install
%python_install
%if "%python_sitelibdir_noarch" != "%python_sitelibdir"
install -d %buildroot%python_sitelibdir
mv %buildroot%python_sitelibdir_noarch/* \
	%buildroot%python_sitelibdir/
%endif

pushd ../python3
%python3_install
popd
%if "%python3_sitelibdir_noarch" != "%python3_sitelibdir"
install -d %buildroot%python3_sitelibdir
mv %buildroot%python3_sitelibdir_noarch/* \
	%buildroot%python3_sitelibdir/
%endif

%if_with check
%check
export PYTHONPATH=src
zope-testrunner --test-path=src -vv

pushd ../python3
zope-testrunner3 --test-path=src -vv
popd
%endif

%files
%doc *.txt
%python_sitelibdir/*
%exclude %python_sitelibdir/*.pth
%exclude %python_sitelibdir/*/*/test*

%files tests
%python_sitelibdir/*/*/test*

%files -n python3-module-%oname
%doc *.txt
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*.pth
%exclude %python3_sitelibdir/*/*/test*
%exclude %python3_sitelibdir/*/*/*/test*

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/*/test*
%python3_sitelibdir/*/*/*/test*

%changelog
* Sun Jun 23 2019 Igor Vlasenko <viy@altlinux.ru> 4.5-alt4
- NMU: remove rpm-build-ubt from BR:

* Tue Mar 05 2019 Andrey Bychkov <mrdrew@altlinux.org> 4.5-alt3
- check disabled for build in p8

* Fri Mar 01 2019 Andrey Bychkov <mrdrew@altlinux.org> 4.5-alt2
- requires fixed

* Wed Feb 27 2019 Andrey Bychkov <mrdrew@altlinux.org> 4.5-alt1
- Version updated to 4.5

* Fri Feb 16 2018 Stanislav Levin <slev@altlinux.org> 4.4.1-alt1%ubt
- 4.2.3 -> 4.4.1

* Tue Jun 07 2016 Ivan Zakharyaschev <imz@altlinux.org> 4.2.3-alt1.dev0.git20150604.1.1.1
- (AUTO) subst_x86_64.

* Mon Mar 14 2016 Ivan Zakharyaschev <imz@altlinux.org> 4.2.3-alt1.dev0.git20150604.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 4.2.3-alt1.dev0.git20150604.1
- NMU: Use buildreq for BR.

* Wed Aug 26 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.2.3-alt1.dev0.git20150604
- Version 4.2.3.dev0

* Sun Feb 22 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.2.2-alt1.dev0.git20150128
- Version 4.2.2.dev0

* Sat Jul 26 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.2.1-alt1
- Version 4.2.1

* Mon Apr 15 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.1.0-alt1.1
- Use 'find... -exec...' instead of 'for ... $(find...'

* Sun Mar 03 2013 Aleksey Avdeev <solo@altlinux.ru> 4.1.0-alt1
- Version 4.1.0-alt1

* Mon Apr 16 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.12.1-alt1
- Version 3.12.1
- Added module for Python 3

* Mon Dec 12 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.12.0-alt1
- Version 3.12.0

* Mon Oct 24 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 3.10.0-alt4.1
- Rebuild with Python-2.7

* Tue Jun 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.10.0-alt4
- Added necessary requirements for tests

* Sun Jun 19 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.10.0-alt3
- Add necessary requiresments
- Excludes *.pth

* Thu May 19 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.10.0-alt2
- Set archdep for package

* Mon May 16 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.10.0-alt1
- Initial build for Sisyphus
