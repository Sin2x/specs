%define _unpackaged_files_terminate_build 1

%define oname prompt_toolkit

Name: python3-module-%oname
Version: 3.0.7
Release: alt1
Summary: Library for building powerful interactive command lines in Python
License: BSD-3-Clause
Group: Development/Python3
Url: https://github.com/prompt-toolkit/python-prompt-toolkit

BuildArch: noarch

# https://github.com/jonathanslenders/python-prompt-toolkit.git
Source: %name-%version.tar

Patch1: %oname-alt-docs.patch

%add_findreq_skiplist %python3_sitelibdir/%oname/eventloop/win32.py
%add_findreq_skiplist %python3_sitelibdir/%oname/input/win32.py

BuildRequires(pre): rpm-build-python3
BuildRequires(pre): rpm-macros-sphinx3
BuildRequires: python3-devel python3-module-setuptools
BuildRequires: python3-module-wcwidth
BuildRequires: python3-module-pytest
BuildRequires: python3-module-html5lib python3-module-sphinx
BuildRequires: python3-module-alabaster python3-module-docutils python3-module-objects.inv

%description
prompt_toolkit is a library for building powerful interactive command
lines in Python.

%package pickles
Summary: Pickles for %oname
Group: Development/Python3

%description pickles
prompt_toolkit is a library for building powerful interactive command
lines in Python.

This package contains pickles for %oname.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
prompt_toolkit is a library for building powerful interactive command
lines in Python.

This package contains documentation for %oname.

%prep
%setup
%patch1 -p1

%prepare_sphinx3 .
ln -s ../objects.inv docs/

%build
%python3_build_debug

%install
%python3_install

export PYTHONPATH=%buildroot%python3_sitelibdir
%make -C docs pickle SPHINXBUILD=sphinx-build-3
%make -C docs html SPHINXBUILD=sphinx-build-3
cp -fR docs/_build/pickle %buildroot%python3_sitelibdir/%oname/

%check
export PYTHONPATH=%buildroot%python3_sitelibdir
py.test3

%files
%doc LICENSE
%doc CHANGELOG *.rst
%python3_sitelibdir/%oname
%python3_sitelibdir/%oname-%version-py*.egg-info
%exclude %python3_sitelibdir/%oname/pickle

%files pickles
%python3_sitelibdir/%oname/pickle

%files docs
%doc examples docs/_build/html

%changelog
* Mon Sep 14 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 3.0.7-alt1
- Updated to upstream release 3.0.7.
- Dropped python-2 support.

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.0.14-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Wed Aug 02 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 1.0.14-alt1
- Update to upstream release 1.0.14.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.46-alt1.git20150808.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.46-alt1.git20150808.1
- NMU: Use buildreq for BR.

* Sat Aug 08 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.46-alt1.git20150808
- Initial build for Sisyphus

