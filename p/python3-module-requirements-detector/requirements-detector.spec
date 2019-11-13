%define _unpackaged_files_terminate_build 1
%define oname requirements-detector

Name: python3-module-%oname
Version: 0.6
Release: alt2

Summary: Python tool to find and list requirements of a Python project
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/requirements-detector/
# https://github.com/landscapeio/requirements-detector.git
BuildArch: noarch

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-astroid python3-module-nose
BuildRequires: python3-module-coverage

%py3_provides requirements_detector
%py3_requires astroid


%description
requirements-detector is a simple Python tool which attempts to find and
list the requirements of a Python project.

When run from the root of a Python project, it will try to ascertain
which libraries and the versions of those libraries that the project
depends on.

%prep
%setup

%build
%python3_build_debug

%install
%python3_install

%check
python3 setup.py test
nosetests3 -v -s --with-coverage \
	--cover-package requirements_detector \
	--cover-inclusive

%files
%doc *.md
%_bindir/*
%python3_sitelibdir/*


%changelog
* Wed Nov 13 2019 Andrey Bychkov <mrdrew@altlinux.org> 0.6-alt2
- python2 disabled

* Mon Sep 10 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 0.6-alt1
- Updated to upstream version 0.6.

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.5.2-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Tue Jan 17 2017 Igor Vlasenko <viy@altlinux.ru> 0.5.2-alt1
- automated PyPI update

* Wed Mar 16 2016 Denis Medvedev <nbr@altlinux.org> 0.4.1-alt2.git20160316
- typo in summary fixed.

* Wed Mar 16 2016 Denis Medvedev <nbr@altlinux.org> 0.4.1-alt1.git20160316
- Merged upstream version 0.4.1.

* Tue Mar 24 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4-alt1.git20150323
- Initial build for Sisyphus

