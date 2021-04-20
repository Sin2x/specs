%define _unpackaged_files_terminate_build 1
%define oname flake8

%def_with check

Name: python3-module-%oname
Version: 3.9.1
Release: alt1

Summary: Code checking using pep8 and pyflakes
Group: Development/Python3
License: MIT
Url: http://pypi.python.org/pypi/flake8
# https://gitlab.com/pycqa/flake8.git
BuildArch: noarch

Source: %name-%version.tar
Patch0: %name-%version-alt.patch

BuildRequires(pre): rpm-build-python3

%if_with check
BuildRequires: python3(mccabe)
BuildRequires: python3(mock)
BuildRequires: python3(pycodestyle)
BuildRequires: python3(pyflakes)
BuildRequires: python3(tox)
BuildRequires: python3(tox_no_deps)
BuildRequires: python3(tox_console_scripts)
%endif

%py3_requires mccabe
%py3_requires pycodestyle
%py3_requires pyflakes

%description
Flake8 is a wrapper around these tools:

- PyFlakes - pep8 - Ned's McCabe script

Flake8 runs all tools by launching the single 'flake8' script, but ignores
pep8 and PyFlakes extended options and just uses defaults. It displays the
warnings in a per-file, merged output.

It also adds a few features:

- files that contains with this header are skipped::

- lines that contains a "# NOQA" comment at the end will not issue a
warning. - a Mercurial hook.

- a McCabe complexity checker.

%prep
%setup
%autopatch -p1

%build
%python3_build_debug

%install
%python3_install

%check
export PIP_NO_INDEX=YES
export TOXENV=py3
tox.py3 --sitepackages --console-scripts --no-deps -vvr

%files
%doc README.rst LICENSE
%_bindir/flake8
%python3_sitelibdir/flake8/
%python3_sitelibdir/flake8-*.egg-info/

%changelog
* Tue Apr 20 2021 Stanislav Levin <slev@altlinux.org> 3.9.1-alt1
- 3.8.4 -> 3.9.1.

* Mon Oct 19 2020 Stanislav Levin <slev@altlinux.org> 3.8.4-alt1
- 3.7.9 -> 3.8.4.

* Sat Nov 16 2019 Stanislav Levin <slev@altlinux.org> 3.7.9-alt1
- 3.7.8 -> 3.7.9.

* Tue Aug 13 2019 Stanislav Levin <slev@altlinux.org> 3.7.8-alt1
- 3.7.7 -> 3.7.8.

* Thu Aug 08 2019 Stanislav Levin <slev@altlinux.org> 3.7.7-alt2
- Fixed testing against Pytest 5.

* Fri Mar 22 2019 Stanislav Levin <slev@altlinux.org> 3.7.7-alt1
- 3.6.0 -> 3.7.7.

* Mon Jan 28 2019 Mikhail Gordeev <obirvalger@altlinux.org> 3.6.0-alt2
- Use executable on python3

* Sat Oct 27 2018 Stanislav Levin <slev@altlinux.org> 3.6.0-alt1
- 3.5.0 -> 3.6.0.

* Fri May 25 2018 Andrey Bychkov <mrdrew@altlinux.org> 3.5.0-alt2.1
- rebuild with python3.6

* Fri Feb 16 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 3.5.0-alt2
- Updated build dependencies.

* Fri Dec 01 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 3.5.0-alt1
- Updated to upstream version 3.5.0.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 2.4.1-alt1.git20150710.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 2.4.1-alt1.git20150710.1
- NMU: Use buildreq for BR.

* Sun Aug 02 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.4.1-alt1.git20150710
- Snapshot from git

* Fri Jul 31 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.4.1-alt1
- Version 2.4.1

* Tue Apr 28 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.4.0-alt1
- Version 2.4.0

* Mon Feb 16 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.3.0-alt1
- Version 2.3.0

* Sat Nov 08 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.2.5-alt1
- Version 2.2.5

* Fri Aug 01 2014 Lenar Shakirov <snejok@altlinux.ru> 2.1.0-alt1
- First build for ALT (based on Fedora 2.1.0-3.fc21.src)
