%define _unpackaged_files_terminate_build 1
%define system_wheels_path %(%__python3 -c 'import os, sys, system_seed_wheels; sys.stdout.write(os.path.dirname(system_seed_wheels.__file__))')

%def_with check
%def_without bootstrap

Name: python3-module-pip
Version: 21.1.1
Release: alt1

Summary: The PyPA recommended tool for installing Python packages
License: MIT
Group: Development/Python3
Url: https://pip.pypa.io

Source0: %name-%version.tar
Patch0: %name-%version-alt.patch

BuildRequires(pre): rpm-build-python3

# dependencies for build wheel
%if_without bootstrap
BuildRequires: python3(wheel)
BuildRequires: python3(system_seed_wheels)
%endif

%if_with check
BuildRequires: git-core
BuildRequires: python3(cryptography)
BuildRequires: python3(freezegun)
BuildRequires: python3(pretend)
BuildRequires: python3(pytest)
BuildRequires: python3(scripttest)
BuildRequires: python3(werkzeug)
BuildRequires: python3(tox)
BuildRequires: python3(tox_console_scripts)
BuildRequires: python3(tox_no_deps)
%endif

Obsoletes: python3-module-pip-pickles

%description
%summary

%add_findprov_skiplist %python3_sitelibdir/pip/_vendor/*
%filter_from_requires /python3\(\.[[:digit:]]\)\?(pip\._vendor\..*)/d

%if_without bootstrap
%package wheel
Summary: %summary
Group: Development/Python3
%py3_requires system_seed_wheels

%description wheel
%summary

Packaged as wheel. Provides the seed package for virtualenv.
%endif

%prep
%setup
%autopatch -p1

# never unbundle vendored packages
# built wheel being installed into virtualenv will lack of unbundled packages

%build
%python3_build

%install
%python3_install

# since we package python modules as arch dependent
%if "%python3_sitelibdir" != "%python3_sitelibdir_noarch"
mkdir -p %buildroot%python3_sitelibdir
mv %buildroot%python3_sitelibdir_noarch/* %buildroot%python3_sitelibdir/
%endif

%if_without bootstrap
%{python3_setup:} bdist_wheel --dist-dir %buildroot%system_wheels_path/
%endif

%check
export PIP_NO_BUILD_ISOLATION=no
export PIP_NO_INDEX=YES
export TOXENV=py3
export NO_LATEST_WHEELS=YES
export TOX_TESTENV_PASSENV='NO_LATEST_WHEELS'
tox.py3 --sitepackages --console-scripts --no-deps -vvr -s false -- \
    -m 'not network and unit'

%files
%doc *.txt *.rst
%_bindir/pip
%_bindir/pip3
%_bindir/pip%__python3_version
%python3_sitelibdir/pip/
%python3_sitelibdir/pip-*.egg-info/

%if_without bootstrap
%files wheel
%system_wheels_path/pip-%version-*.whl
%endif

%changelog
* Fri May 07 2021 Stanislav Levin <slev@altlinux.org> 21.1.1-alt1
- 21.0.1 -> 21.1.1
  (Updated bundled urllib3 1.26.2 -> 1.26.4 to fix CVE-2021-28363).
- Enabled testing (unit tests for now).

* Fri Apr 23 2021 Stanislav Levin <slev@altlinux.org> 21.0.1-alt1
- 20.1.1 -> 21.0.1.
- Built wheel package(for virtualenv).

* Thu Jun 04 2020 Fr. Br. George <george@altlinux.ru> 20.1.1-alt1
- Autobuild version bump to 20.1.1

* Fri Oct 18 2019 Stanislav Levin <slev@altlinux.org> 19.3.1-alt1
- 19.3 -> 19.3.1.

* Fri Oct 18 2019 Stanislav Levin <slev@altlinux.org> 19.3-alt1
- 19.2.3 -> 19.3.

* Thu Oct 03 2019 Fr. Br. George <george@altlinux.ru> 19.2.3-alt1
- Autobuild version bump to 19.2.3

* Thu Aug 01 2019 Stanislav Levin <slev@altlinux.org> 19.2.1-alt1
- 19.1.1 -> 19.2.1.

* Mon May 13 2019 Stanislav Levin <slev@altlinux.org> 19.1.1-alt1
- 19.0.3 -> 19.1.1.

* Fri Apr 19 2019 Mikhail Gordeev <obirvalger@altlinux.org> 19.0.3-alt2
- Change hardcoded python3 version to macros

* Fri Mar 01 2019 Stanislav Levin <slev@altlinux.org> 19.0.3-alt1
- 19.0.1 -> 19.0.3.

* Sun Jan 27 2019 Stanislav Levin <slev@altlinux.org> 19.0.1-alt1
- 18.1 -> 19.0.1.

* Thu Oct 18 2018 Fr. Br. George <george@altlinux.ru> 18.1-alt1
- Autobuild version bump to 18.1
- Pickle modules removed

* Thu Aug 02 2018 Fr. Br. George <george@altlinux.ru> 18.0-alt1
- Autobuild version bump to 18.0

* Tue Jun 12 2018 Fr. Br. George <george@altlinux.ru> 10.0.1-alt2
- Autobuild version bump to 10.0.1
- Introduce python3 generated documentation

* Tue Jun 05 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 10.0.1-alt1
- Updated to upstream version 10.0.1.

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 9.0.1-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Mon Mar 13 2017 Fr. Br. George <george@altlinux.ru> 9.0.1-alt1
- Autobuild version bump to 9.0.1

* Mon Oct 31 2016 Fr. Br. George <george@altlinux.ru> 8.1.2-alt1
- Autobuild version bump to 8.1.2
- Fix python3 version

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 8.0.2-alt1.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 8.0.2-alt1.1
- NMU: Use buildreq for BR.

* Tue Jan 26 2016 Fr. Br. George <george@altlinux.ru> 8.0.2-alt1
- Autobuild version bump to 8.0.2

* Tue Jan 26 2016 Fr. Br. George <george@altlinux.ru> 7.1.2-alt2
- New build scheme

* Sun Aug 23 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 7.1.2-alt1
- Version 7.1.2

* Wed Aug 12 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 7.1.0-alt1
- Version 7.1.0

* Mon Jan 19 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 6.0.6-alt1
- Version 6.0.6

* Wed Dec 24 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 6.0.3-alt1
- Version 6.0.3

* Tue Dec 23 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 6.0.1-alt1
- Version 6.0.1

* Sat Jul 19 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.5.6-alt1
- Version 1.5.6
- Added module for Python 3

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.0-alt1.1
- Rebuild with Python-2.7

* Fri Jun 10 2011 Sergey Alembekov <rt@altlinux.ru> 1.0-alt1
- new version
- spec fixes

* Sun Mar 20 2011 Sergey Alembekov <rt@altlinux.ru> 0.8.3-alt1
- initial build for ALTLinux
