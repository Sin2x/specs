%define oname keyring

%def_without check

Name: python3-module-%oname
Version: 12.0.0
Release: alt5
Summary: Keyring provides an easy way to access the system keyring service

License: MIT
Group: Development/Python3
Url: https://pypi.python.org/pypi/keyring
BuildArch: noarch

Source: %oname-%version.tar
Patch0: fix_deps.patch

BuildRequires(pre): rpm-build-python3
BuildPreReq: python-module-setuptools_scm

%if_with check
BuildRequires: python3-module-pytest
BuildRequires: python3-module-pytest-sugar
%endif

%py3_requires ctypes entrypoints json logging pluggy secretstorage

Conflicts: python-module-%oname
Obsoletes: python-module-%oname

%description
The Python keyring lib provides an easy way to access the system 
keyring service from python. It can be used in any application 
that needs safe password storage.

%package tests
Summary: Tests for keyring
Group: Development/Python3
Requires: %name = %EVR

%description tests
The Python keyring lib provides an easy way to access the system 
keyring service from python. It can be used in any application 
that needs safe password storage.

This package contains tests for keyring.

%prep
%setup -n %oname-%version
%patch0 -p0

%build
%python3_build_debug

%install
%python3_install

%files
%doc *.rst *.txt LICENSE
%_bindir/*
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests

%files tests
%python3_sitelibdir/*/tests

%changelog
* Thu Jul 15 2021 Grigory Ustinov <grenka@altlinux.org> 12.0.0-alt5
- Drop python2 support.

* Thu Oct 15 2020 Stanislav Levin <slev@altlinux.org> 12.0.0-alt4
- Made dependency on Pytest and its plugins optional.

* Thu Dec 13 2018 Evgeniy Korneechev <ekorneechev@altlinux.org> 12.0.0-alt3
- Updated deps for Python2.7

* Thu Dec 06 2018 Evgeniy Korneechev <ekorneechev@altlinux.org> 12.0.0-alt2
- Updated deps (ALT #35655)

* Mon Apr 02 2018 Andrey Bychkov <mrdrew@altlinux.org> 12.0.0-alt1
- Updated version to 12.0.0
  Fixed deps

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 5.4-alt2.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Fri Aug 04 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 5.4-alt2
- Updated build dependencies.

* Fri Jul 14 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 5.4-alt1.2
- Updated build spec

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 5.4-alt1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Sun Aug 16 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.4-alt1
- Version 5.4

* Wed Feb 25 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.2.1-alt1
- Version 5.2.1

* Tue Jul 15 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.8-alt2
- Added module for Python 3

* Fri Jul 11 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.8-alt1
- Version 3.8

* Fri Nov 29 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.2.1-alt1
- Version 3.2.1

* Tue Sep 17 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.0.3-alt1
- Version 3.0.3

* Wed Apr 03 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.2-alt1
- Initial build for Sisyphus