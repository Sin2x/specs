%define _unpackaged_files_terminate_build 1
%define oname pytest-enabler

%def_with check

Name: python3-module-%oname
Version: 1.2.0
Release: alt1

Summary: Pytest plugin for configuration of another plugins
License: MIT
Group: Development/Python3
# Source-git: https://github.com/jaraco/pytest-enabler.git
Url: https://pypi.org/project/pytest-enabler/

Source: %name-%version.tar
Patch0: %name-%version-alt.patch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3(setuptools_scm)
BuildRequires: python3(toml)

%if_with check
BuildRequires: python3(jaraco.context)
BuildRequires: python3(jaraco.functools)
BuildRequires: python3(pytest)
BuildRequires: python3(tox)
BuildRequires: python3(tox_console_scripts)
BuildRequires: python3(tox_no_deps)
%endif

BuildArch: noarch

%py3_provides %oname

%description
%oname plugin allows configuration of Pytest plugins if present, but omits the
settings if the plugin is not present.

%prep
%setup
%autopatch -p1

%build
export SETUPTOOLS_SCM_PRETEND_VERSION=%version
%python3_build

%install
export SETUPTOOLS_SCM_PRETEND_VERSION=%version
%python3_install

%check
export SETUPTOOLS_SCM_PRETEND_VERSION=%%version
export PIP_NO_BUILD_ISOLATION=no
export PIP_NO_INDEX=YES
export TOXENV=py3
tox.py3 --sitepackages --console-scripts --no-deps -vvr -- -vra

%files
%doc README.rst
%python3_sitelibdir/pytest_enabler/
%python3_sitelibdir/pytest_enabler-%version-py%_python3_version.egg-info/

%changelog
* Fri Mar 26 2021 Stanislav Levin <slev@altlinux.org> 1.2.0-alt1
- Initial build for Sisyphus.
