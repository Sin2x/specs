%define _unpackaged_files_terminate_build 1
%define oname pycodestyle

Name: python3-module-%oname
Version: 2.6.0
Release: alt1

Summary: Python style guide checker
License: Expat
Group: Development/Python3
Url: https://pypi.org/project/pycodestyle/
BuildArch: noarch

# https://github.com/PyCQA/pycodestyle.git
Source: %name-%version.tar
Patch0: %name-%version-alt.patch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3(tox)


%description
pycodestyle is a tool to check your Python code against some of the style
conventions in PEP 8.

%prep
%setup
%autopatch -p1

%build
%python3_build

%install
%python3_install

pushd %buildroot%_bindir
for i in $(ls); do
    mv $i $i.py3
done

%check
export PIP_NO_INDEX=YES
export TOXENV=py%{python_version_nodots python3}
tox.py3 --sitepackages -vvr

%files
%doc README.rst LICENSE CONTRIBUTING.rst CHANGES.txt
%_bindir/pycodestyle.py3
%python3_sitelibdir/pycodestyle.py
%python3_sitelibdir/__pycache__/pycodestyle.cpython-*
%python3_sitelibdir/pycodestyle-%version-py%_python3_version.egg-info/


%changelog
* Mon Oct 19 2020 Stanislav Levin <slev@altlinux.org> 2.6.0-alt1
- 2.5.0 -> 2.6.0.

* Wed Feb 12 2020 Andrey Bychkov <mrdrew@altlinux.org> 2.5.0-alt2
- Build for python2 disabled.

* Fri Mar 22 2019 Stanislav Levin <slev@altlinux.org> 2.5.0-alt1
- new version 2.5.0

* Fri Oct 26 2018 Mikhail Gordeev <obirvalger@altlinux.org> 2.4.0-alt1
- new version 2.4.0

* Fri Dec 01 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 2.3.1-alt1
- Initial build for ALT.
