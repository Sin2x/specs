%define _unpackaged_files_terminate_build 1
%define oname hiredis

%def_with check

Name: python3-module-%oname
Version: 1.1.0
Release: alt2

Summary: Python wrapper for hiredis

License: BSD
Group: Development/Python3
Url: https://github.com/redis/hiredis-py

Source: %name-%version.tar
Patch0: %name-%version-alt.patch

BuildRequires(pre): rpm-build-python3
BuildRequires: libhiredis-devel

%if_with check
BuildRequires: python3(tox)
%endif

%description
Python wrapper for hiredis.

%prep
%setup
%autopatch -p1

# use the system's one
rm -r ./vendor/hiredis/

%build
%python3_build

%install
%python3_install

%check
cat > tox.ini <<EOF
[testenv]
usedevelop=True
commands =
    {envpython} test.py
EOF
export PIP_NO_INDEX=YES
export TOXENV=py3
tox.py3 --sitepackages -vvr

%files
%python3_sitelibdir/%oname/
%python3_sitelibdir/*.egg-*

%changelog
* Tue Oct 27 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 1.1.0-alt2
- Rebuilt with new hiredis.

* Tue Oct 20 2020 Stanislav Levin <slev@altlinux.org> 1.1.0-alt1
- 1.0.1 -> 1.1.0.
- Stopped Python2 package build.
- Enabled testing.

* Tue Jan 28 2020 Vladimir Didenko <cow@altlinux.ru> 1.0.1-alt1
- 1.0.1

* Fri Sep 27 2019 Vladimir Didenko <cow@altlinux.ru> 1.0.0-alt1
- 1.0.0

* Thu Mar 22 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 0.2.0-alt1.1.1.1
- (NMU) Rebuilt with python-3.6.4.

* Thu Mar 17 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.2.0-alt1.1.1
- (NMU) rebuild with python3-3.5 & rpm-build-python3-0.1.10
  (for ABI dependence and new python3(*) reqs)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.2.0-alt1.1
- NMU: Use buildreq for BR.

* Mon Jun 29 2015 Vladimir Didenko <cow@altlinux.ru> 0.2.0-alt1
- 0.2.0

* Fri Nov 28 2014 Vladimir Didenko <cow@altlinux.ru> 0.1.5-alt1
- 0.1.5

* Tue Jun 24 2014 Vladimir Didenko <cow@altlinux.ru> 0.1.3-alt1
- initial build for Sisyphus
