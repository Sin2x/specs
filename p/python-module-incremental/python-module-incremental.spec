%def_without check
%def_without python3
%def_with bootstrap

%define modulename incremental
Name: python-module-incremental
Version: 17.5.0
Release: alt5

Summary: Incremental is a small library that versions your Python project

Url: https://pypi.python.org/pypi/incremental
License: ASL 2.0
Group: Development/Python


Packager: Vitaly Lipatov <lav@altlinux.ru>

# Source-url: https://github.com/twisted/incremental/archive/incremental-%version.tar.gz
Source: %name-%version.tar

BuildRequires: python-devel python-module-setuptools

BuildArch: noarch

%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
%endif

# extra requires (see setup.py)
%add_python_req_skip click

%if_with bootstrap
%add_python_req_skip twisted
%if_with python3
%add_python3_req_skip twisted.python.compat twisted.python.filepath twisted.trial.unittest
%endif
%endif

#setup_python_module %modulename

%description
Incremental is a small library that versions your Python projects.

%if_with python3
%package -n python3-module-incremental
Summary: Incremental is a small library that versions your Python project
Group: Development/Python3

%description -n python3-module-incremental
Incremental is a small library that versions your Python projects.
%endif


%prep
%setup

%if_with python3
cp -fR . ../python3
%endif

%build
%python_build_debug

%if_with python3
pushd ../python3
%python3_build_debug
popd
%endif

%install
%python_install

%if_with python3
pushd ../python3
%python3_install
popd
%endif

%files
%doc README.rst
%python_sitelibdir/*

%if_with python3
%files -n python3-module-incremental
%doc README.rst
%python3_sitelibdir/*
%endif


%changelog
* Sun Nov 08 2020 Vitaly Lipatov <lav@altlinux.ru> 17.5.0-alt5
- make click require optional

* Sun Nov 08 2020 Vitaly Lipatov <lav@altlinux.ru> 17.5.0-alt4
- build python2 only

* Mon Apr 08 2019 Grigory Ustinov <grenka@altlinux.org> 17.5.0-alt3
- Bootstrap for python3.7.

* Sun Oct 14 2018 Igor Vlasenko <viy@altlinux.ru> 17.5.0-alt2.qa1
- NMU: applied repocop patch

* Thu May 10 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 17.5.0-alt2
- (NMU) Rebuilt without bootstrap.

* Tue Mar 27 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 17.5.0-alt1.1
- (NMU) Rebuilt with python-3.6.4.

* Wed Jun 14 2017 Vitaly Lipatov <lav@altlinux.ru> 17.5.0-alt1
- initial build for ALT Sisyphus

