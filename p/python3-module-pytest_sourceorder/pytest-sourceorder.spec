%define _unpackaged_files_terminate_build 1

%define mname pytest_sourceorder
%def_with check

Name: python3-module-%mname
Version: 0.5.1
Release: alt2

Summary: A pytest plugin for ensuring tests within a class are run in source order
License: %gpl3plus
Group: Development/Python3
# Source-git: https://github.com/encukou/pytest-sourceorder
Url: https://pypi.org/project/pytest-sourceorder

Source: %name-%version.tar

BuildRequires(pre): rpm-build-licenses
BuildRequires(pre): rpm-build-python3

BuildArch: noarch

BuildRequires: python3-module-setuptools

%if_with check
BuildRequires: python3-module-pytest
BuildRequires: python3-module-tox
%endif

%description
Allows tests within a specially marked class to be run in source order,
instead of the "almost alphabetical" order Pytest normally uses.

%prep
%setup

%build
%python3_build

%check
cat > tox.ini <<EOF
[testenv]
usedevelop=True
whitelist_externals =
    /bin/cp
    /bin/sed
commands_pre =
    /bin/cp %_bindir/py.test3 {envbindir}/py.test
    /bin/sed -i '1c #!{envpython}' {envbindir}/py.test
commands =
    {envbindir}/py.test {posargs:-vra}
EOF
export PIP_NO_BUILD_ISOLATION=no
export PIP_NO_INDEX=YES
export TOXENV=py3
tox.py3 --sitepackages -vvr

%install
%python3_install

%files
%doc README.rst COPYING
%python3_sitelibdir/%mname-*.egg-info
%python3_sitelibdir/%mname.py
%python3_sitelibdir/__pycache__/%mname.*.py*

%changelog
* Mon Oct 19 2020 Stanislav Levin <slev@altlinux.org> 0.5.1-alt2
- Stopped Python2 package build.

* Mon Jul 23 2018 Stanislav Levin <slev@altlinux.org> 0.5.1-alt1
- 0.4 -> 0.5.1
- Build package for Python3

* Tue Dec 29 2015 Mikhail Efremov <sem@altlinux.org> 0.4-alt1
- Initial build.

