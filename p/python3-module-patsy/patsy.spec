%define _unpackaged_files_terminate_build 1

%define oname patsy

Name: python3-module-%oname
Version: 0.5.1
Release: alt1
Summary: A Python package for describing statistical models and for building design matrices
License: BSD-2-Clause and Python
Group: Development/Python3
Url: http://patsy.readthedocs.org/en/latest/

BuildArch: noarch

# https://github.com/pydata/patsy.git
Source: %name-%version.tar

Patch1: %oname-alt-doc.patch

BuildRequires(pre): rpm-build-python3
BuildRequires(pre): rpm-macros-sphinx3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-pathlib2
BuildRequires: python3-module-sphinx-sphinx-build-symlink
BuildRequires: python3(numpy) python3(matplotlib) python3(IPython)

%description
A Python package for describing statistical models and for building
design matrices. It is closely inspired by and compatible with the
'formula' mini-language used in R and S.

%package tests
Summary: Tests for patsy
Group: Development/Python3
Requires: %name = %EVR

%description tests
A Python package for describing statistical models and for building
design matrices. It is closely inspired by and compatible with the
'formula' mini-language used in R and S.

This package contains tests for patsy.

%package pickles
Summary: Pickles for patsy
Group: Development/Python3

%description pickles
A Python package for describing statistical models and for building
design matrices. It is closely inspired by and compatible with the
'formula' mini-language used in R and S.

This package contains pickles for patsy.

%package docs
Summary: Documentation for patsy
Group: Development/Documentation

%description docs
A Python package for describing statistical models and for building
design matrices. It is closely inspired by and compatible with the
'formula' mini-language used in R and S.

This package contains documentation for patsy.

%prep
%setup
%patch1 -p2

%prepare_sphinx3 .
ln -s ../objects.inv doc/

%build
%python3_build_debug

%make -C doc pickle
%make -C doc html

%install
%python3_build_install

cp -fR doc/_build/pickle %buildroot%python3_sitelibdir/%oname/

%files
%doc LICENSE.txt
%doc *.rst *.md TODO
%python3_sitelibdir/%oname
%python3_sitelibdir/%oname-%version-*.egg-info
%exclude %python3_sitelibdir/%oname/pickle
%exclude %python3_sitelibdir/%oname/test_*
%exclude %python3_sitelibdir/%oname/__pycache__/test_*

%files tests
%python3_sitelibdir/%oname/test_*
%python3_sitelibdir/%oname/__pycache__/test_*

%files pickles
%python3_sitelibdir/%oname/pickle

%files docs
%doc doc/_build/html/*

%changelog
* Wed Aug 26 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 0.5.1-alt1
- Updated to upstream version 0.5.1.
- Disabled build for python-2.

* Mon Aug 07 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.4.0-alt2
- Updated build dependencies.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.4.0-alt1.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.4.0-alt1.1
- NMU: Use buildreq for BR.

* Thu Aug 20 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.0-alt1
- Version 0.4.0

* Thu Mar 05 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.0-alt1
- Version 0.3.0

* Thu Oct 24 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.1-alt1
- Initial build for Sisyphus

