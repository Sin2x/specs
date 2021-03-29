%define _unpackaged_files_terminate_build 1
%define oname toml

%def_with check

Name: python3-module-%oname
Version: 0.10.2
Release: alt2

Summary: A Python library for parsing and creating TOML.
License: MIT
Group: Development/Python3
# Source-git: https://github.com/uiri/toml.git
Url: https://pypi.org/project/toml/

Source: %name-%version.tar
Patch: %name-%version-alt.patch

BuildRequires(pre): rpm-build-python3

%if_with check
BuildRequires: golang-github-burntsushi-toml-test
BuildRequires: python3(numpy)
BuildRequires: python3(tox)
BuildRequires: python3(tox_console_scripts)
%endif

BuildArch: noarch

%description
TOML aims to be a minimal configuration file format that's easy to read due to
obvious semantics. TOML is designed to map unambiguously to a hash table. TOML
should be easy to parse into data structures in a wide variety of languages.
This package loads toml file into python dictionary and dump dictionary into
toml file.

%prep
%setup
%patch -p1

%build
%python3_build

%install
%python3_install

%check
ln -s %_datadir/toml-test toml-test
export PIP_NO_INDEX=YES
export TOXENV=py3
tox.py3 --sitepackages --console-scripts -vvr -- -vra

%files
%python3_sitelibdir/toml/
%python3_sitelibdir/toml-*.egg-info/

%changelog
* Sat Mar 27 2021 Stanislav Levin <slev@altlinux.org> 0.10.2-alt2
- Dropped runtime dependency on numpy.

* Tue Mar 02 2021 Grigory Ustinov <grenka@altlinux.org> 0.10.2-alt1
- Automatically updated to 0.10.2.
- Added bootstrap knob.
- Enabled check.

* Sun Jan 31 2021 Grigory Ustinov <grenka@altlinux.org> 0.10.1-alt2
- Bootstrap for python3.9.

* Tue Sep 08 2020 Stanislav Levin <slev@altlinux.org> 0.10.1-alt1
- 0.10.0 -> 0.10.1.
- Built Python3 module from its own src package.

* Mon Apr 27 2020 Stanislav Levin <slev@altlinux.org> 0.10.0-alt4
- Applied upstream fix.

* Fri Aug 09 2019 Stanislav Levin <slev@altlinux.org> 0.10.0-alt3
- Fixed testing against Pytest 5.

* Fri Mar 15 2019 Stanislav Levin <slev@altlinux.org> 0.10.0-alt2
- Fixed FTBFS.

* Tue Oct 09 2018 Stanislav Levin <slev@altlinux.org> 0.10.0-alt1
- Initial build for sisyphus.

