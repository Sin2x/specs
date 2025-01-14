%define _unpackaged_files_terminate_build 1
%define pypi_name yamllint

%def_with check

Name: python3-module-%pypi_name
Version: 1.28.0
Release: alt1
Summary: A linter for YAML files
Group: Development/Python
License: GPLv3
Url: https://github.com/adrienverge/yamllint
Source0: %name-%version.tar
BuildArch: noarch

BuildRequires(pre): rpm-build-python3

# build backend and its deps
BuildRequires: python3(setuptools)
BuildRequires: python3(wheel)

BuildRequires: python3-module-sphinx-sphinx-build-symlink

%if_with check
BuildRequires: /dev/pts
BuildRequires: python3(pathspec)
BuildRequires: python3(yaml)
%endif

Provides: yamllint = %EVR
Obsoletes: yamllint <= 1.24.2-alt1

%description
A linter for YAML files.

yamllint does not only check for syntax validity, but for weirdnesses like key
repetition and cosmetic problems such as lines length, trailing spaces,
indentation, etc.

%prep
%setup

%build
%pyproject_build

# man page
pushd docs
make man
popd

%install
%pyproject_install

# man page
install -D -m0644 docs/_build/man/yamllint.1 %buildroot/%_man1dir/yamllint.1

%check
cat > tox.ini <<EOF
[testenv]
commands =
    {envpython} -m unittest discover -vv tests {posargs}
EOF
export TOX_TESTENV_PASSENV='HOME'
%tox_check_pyproject

%files
%doc README.rst CHANGELOG.rst
%_man1dir/yamllint.1.*

%_bindir/yamllint
%python3_sitelibdir/yamllint/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Mon Sep 12 2022 Stanislav Levin <slev@altlinux.org> 1.28.0-alt1
- 1.24.2 -> 1.28.0.

* Mon Sep 14 2020 Stanislav Levin <slev@altlinux.org> 1.24.2-alt1
- 1.17.0 -> 1.24.2.

* Fri Sep 20 2019 Terechkov Evgenii <evg@altlinux.org> 1.17.0-alt1
- Initial build for ALT Linux Sisyphus
