%define _unpackaged_files_terminate_build 1
%define oname pytest-asyncio

%def_with check

Name: python3-module-%oname
Version: 0.15.0
Release: alt1

Summary: Pytest support for asyncio
License: Apache-2.0
Group: Development/Python3
Url: https://github.com/pytest-dev/pytest-asyncio
BuildArch: noarch

Source: %name-%version.tar
Patch0: %name-%version-alt.patch

BuildRequires(pre): rpm-build-python3
%py3_provides %oname

%if_with check
BuildRequires: python3(hypothesis)
BuildRequires: python3(tox)
BuildRequires: python3(tox_no_deps)
BuildRequires: python3(tox_console_scripts)
%endif

%description
pyee supplies a BaseEventEmitter object that is similar to the EventEmitter
class from Node.js. It also supplies a number of subclasses with added support
for async and threaded programming in python, such as async/await as seen in
python 3.5+.

%prep
%setup
%autopatch -p1

%build
%python3_build

%install
%python3_install

%check
export PIP_NO_BUILD_ISOLATION=no
export PIP_NO_INDEX=YES
export TOXENV=py3
tox.py3 --sitepackages --console-scripts --no-deps -vvr

%files
%doc *.rst LICENSE
%python3_sitelibdir/*

%changelog
* Mon Apr 19 2021 Stanislav Levin <slev@altlinux.org> 0.15.0-alt1
- 0.14.0 -> 0.15.0.

* Tue Sep 08 2020 Stanislav Levin <slev@altlinux.org> 0.14.0-alt1
- 0.10.0 -> 0.14.0.

* Tue Jan 14 2020 Andrey Bychkov <mrdrew@altlinux.org> 0.10.0-alt1
- Initial build for Sisyphus

