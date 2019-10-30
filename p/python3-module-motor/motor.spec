%define oname motor

%def_disable check

Name: python3-module-%oname
Version: 2.0.0
Release: alt2

Summary: Non-blocking MongoDB driver for Tornado

License: ASLv2.0
Group: Development/Python3
Url: https://pypi.python.org/pypi/motor/

BuildArch: noarch

# https://github.com/mongodb/motor.git
# Source-url: https://pypi.io/packages/source/m/%oname/%oname-%version.tar.gz
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools
BuildRequires: python3-module-tornado
BuildRequires: python3-module-pymongo python3-module-gridfs
BuildRequires: python3-module-sphinx-devel
BuildRequires: python3(aiohttp)

%py3_provides %oname
%py3_requires tornado pymongo gridfs


%description
Motor is a full-featured, non-blocking MongoDB driver for Python Tornado
applications.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
Motor is a full-featured, non-blocking MongoDB driver for Python Tornado
applications.

This package contains documentation for %oname.

%prep
%setup

%prepare_sphinx3 .
ln -s ../objects.inv doc/

%build
%python3_build_debug

%install
%python3_install

%if_with doc
make -C doc SPHINXBUILD=py3_sphinx-build
%endif

%check
python3 setup.py test

%files
%doc *.rst
%python3_sitelibdir/*

%if_with doc
%files docs
%doc doc/_build/html/*
%endif


%changelog
* Wed Oct 30 2019 Andrey Bychkov <mrdrew@altlinux.org> 2.0.0-alt2
- disable python2, enable python3

* Sat Jun 01 2019 Vitaly Lipatov <lav@altlinux.ru> 2.0.0-alt1
- new version (2.0.0) with rpmgs script
- switch to build from tarball

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.2.0-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Wed Dec 20 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 1.2.0-alt1
- Updated to upstream version 1.2.0.

* Thu Oct 27 2016 Vladimir Didenko <cow@altlinux.org> 0.7-alt1.git20161010
- New version (closes: #31269)

* Thu Feb 26 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4-alt1.git20140705
- Initial build for Sisyphus
