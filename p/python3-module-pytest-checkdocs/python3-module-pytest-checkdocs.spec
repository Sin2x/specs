%define  modulename pytest-checkdocs

%def_with check

Name:    python3-module-%modulename
Version: 2.1.1
Release: alt1

Summary: A pytest plugin that checks the long description of the project to ensure it renders properly.
License: MIT
Group:   Development/Python3
URL:     https://github.com/jaraco/pytest-checkdocs

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools_scm

%if_with check
BuildRequires: python3-module-docutils
BuildRequires: python3-module-more-itertools
BuildRequires: python3-module-pytest
BuildRequires: python3-module-tox
%endif

BuildArch: noarch
Source:  %name-%version.tar
Patch0: %name-%version-%release.patch

%description
%summary

%prep
%setup
%patch0 -p1

%build
export SETUPTOOLS_SCM_PRETEND_VERSION=%version
%python3_build

%install
export SETUPTOOLS_SCM_PRETEND_VERSION=%version
%python3_install

%check
export SETUPTOOLS_SCM_PRETEND_VERSION=%version
export PIP_NO_BUILD_ISOLATION=no
export PIP_NO_INDEX=YES
export TOXENV=py%{python_version_nodots python3}
tox.py3 --sitepackages -vv -r

%files
%python3_sitelibdir/__pycache__/*
%python3_sitelibdir/pytest_checkdocs.py
%python3_sitelibdir/*.egg-info

%changelog
* Wed Oct 14 2020 Stanislav Levin <slev@altlinux.org> 2.1.1-alt1
- 1.2.3 -> 2.1.1.

* Fri May 01 2020 Stanislav Levin <slev@altlinux.org> 1.2.3-alt2
- Fixed FTBFS.

* Tue Dec 03 2019 Anton Farygin <rider@altlinux.ru> 1.2.3-alt1
- first build for ALT

