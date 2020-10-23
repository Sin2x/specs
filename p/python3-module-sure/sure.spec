%define _unpackaged_files_terminate_build 1
%define modname sure

%def_with check

Name: python3-module-%modname

Version: 1.4.11
Release: alt1

Summary: Assertion toolbox for python

Group: Development/Python3
License: GPLv3+
URL: https://github.com/gabrielfalcao/sure

BuildArch: noarch

Source: %name-%version.tar
Patch0: %name-%version-alt.patch

BuildRequires(pre): rpm-build-python3

%if_with check
BuildRequires: python3(mock)
BuildRequires: python3(nose)
BuildRequires: python3(tox)
%endif

%description
A Python assertion toolbox that works fine with nose.

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
tox.py3 --sitepackages -vvr

%files
%doc README.rst COPYING
%python3_sitelibdir/%modname
%python3_sitelibdir/*.egg-info

%changelog
* Fri Oct 23 2020 Stanislav Levin <slev@altlinux.org> 1.4.11-alt1
- 1.2.12 -> 1.4.11.

* Fri May 25 2018 Andrey Cherepanov <cas@altlinux.org> 1.2.12-alt2.git20150625.2
- Rebuild with python-module-six

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.2.12-alt2.git20150625.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 1.2.12-alt2.git20150625.1
- NMU: Use buildreq for BR.

* Sat Jul 25 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.12-alt2.git20150625
- Fixed for new mock

* Sat Jul 25 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.12-alt1.git20150625
- Version 1.2.12

* Mon Jan 19 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.8-alt1.git20141223
- Version 1.2.8
- Added module for Python 3

* Sat Feb 09 2013 Ivan A. Melnikov <iv@altlinux.org> 1.1.7-alt1
- New version.

* Sun Nov 04 2012 Ivan A. Melnikov <iv@altlinux.org> 1.0.6-alt1
- Initial build for Sisyphus.

