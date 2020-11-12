%define oname jsonschema

Name:		python3-module-%oname
Version:	3.2.0
Release:	alt3

Summary:	An implementation of JSON Schema validation for Python

License:	MIT
Group:		Development/Python3
URL:		http://pypi.python.org/pypi/jsonschema/


# Source-url: %__pypi_url %oname
Source0:	%name-%version.tar

BuildArch:	noarch

BuildRequires(pre): rpm-build-intro >= 2.2.5
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools
BuildRequires: python3-module-nose python3-module-mock
BuildRequires: python3-module-vcversioner
BuildRequires: python3-module-setuptools_scm
# BuildRequires for tests
BuildRequires: python3-module-attrs
BuildRequires: python3-module-pyrsistent
BuildRequires: python3-module-twisted-core-tests
BuildRequires: python3-module-pyperf

%description
jsonschema is JSON Schema validator currently based on
http://tools.ietf.org/html/draft-zyp-json-schema-03

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
jsonschema is JSON Schema validator currently based on
http://tools.ietf.org/html/draft-zyp-json-schema-03

This package contains tests for %oname.

%prep
%setup

%build
%python3_build

%install
%python3_install
%python3_prune
rm -rfv %buildroot%python3_sitelibdir/%oname/benchmarks/

%check
nosetests3 -v

%files
%doc *.rst COPYING
%_bindir/*
%python3_sitelibdir/*
%if 0
%exclude %python3_sitelibdir/*/tests

%files tests
%python3_sitelibdir/*/tests
%endif

%changelog
* Thu Nov 12 2020 Vitaly Lipatov <lav@altlinux.ru> 3.2.0-alt3
- use python3-module-twisted-core-tests for tests
- cleanup spec: add URL for tarball, don't pack sources to gz
- disable tests packing

* Fri Oct 30 2020 Vitaly Lipatov <lav@altlinux.ru> 3.2.0-alt2
- NMU: drop benchmarks packing

* Fri Jul 03 2020 Vladimir Didenko <cow@altlinux.org> 3.2.0-alt1
- Updated to upstream release 3.2.0
- Build python3 version as separate package

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 2.6.0-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Tue Aug 01 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 2.6.0-alt1
- Updated to upstream release 2.6.0.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 2.5.1-alt1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Wed Jul 29 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.5.1-alt1
- Version 2.5.1

* Fri Oct 17 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.4.0-alt1
- Version 2.4.0
- Added module for Python 3

* Thu Sep 13 2012 Pavel Shilovsky <piastry@altlinux.org> 0.2-alt1
- Initial release for Sisyphus (based on Fedora)
