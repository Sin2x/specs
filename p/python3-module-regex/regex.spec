%define _unpackaged_files_terminate_build 1

%def_without check

%define modulename regex
Name: python3-module-regex
Version: 2020.7.14
Release: alt1

Summary: Alternative regular expression module, to replace re
License: Python
Group: Development/Python3
Url: https://pypi.org/project/regex/

Packager: Vitaly Lipatov <lav@altlinux.ru>

# Source-url: https://pypi.io/packages/source/r/%modulename/%modulename-%version.tar.gz
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3

%description
This regex implementation is backwards-compatible with the standard 're' module, but offers additional functionality.

%prep
%setup

%build
%python3_build_debug

%install
%python3_install

# don't package tests
rm -r %buildroot%python3_sitelibdir/regex/test_regex.py
rm %buildroot%python3_sitelibdir/regex/__pycache__/test_regex.*

%files
%doc README.rst docs/
%python3_sitelibdir/*

%changelog
* Mon Sep 14 2020 Stanislav Levin <slev@altlinux.org> 2020.7.14-alt1
- 2019.06.05 -> 2020.7.14.

* Sun Jun 09 2019 Vitaly Lipatov <lav@altlinux.ru> 2019.06.05-alt1
- new version 2019.06.05 (with rpmrb script)

* Sun Nov 04 2018 Vitaly Lipatov <lav@altlinux.ru> 2018.07.11-alt1
- new version 2018.07.11 (with rpmrb script)

* Sun Oct 14 2018 Igor Vlasenko <viy@altlinux.ru> 2018.02.21-alt1.qa1
- NMU: applied repocop patch

* Sat Jun 09 2018 Vitaly Lipatov <lav@altlinux.ru> 2018.02.21-alt1
- new version 2018.02.21 (with rpmrb script)

* Thu Mar 22 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 2017.09.23-alt2.1
- (NMU) Rebuilt with python-3.6.4.

* Mon Oct 02 2017 Vitaly Lipatov <lav@altlinux.ru> 2017.09.23-alt2
- drop python*(test) requires

* Mon Oct 02 2017 Vitaly Lipatov <lav@altlinux.ru> 2017.09.23-alt1
- initial build for ALT Sisyphus

