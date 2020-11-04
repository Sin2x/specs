%define modulename pyrsistent

Name: python3-module-pyrsistent
Version: 0.17.3
Release: alt1

Summary: Persistent/Functional/Immutable data structures

Url: https://github.com/tobgu/pyrsistent/
License: MIT
Group: Development/Python3

# Source-url: https://pypi.io/packages/source/p/%modulename/%modulename-%version.tar.gz
Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: %name-%version.tar

BuildRequires(pre): rpm-build-intro >= 2.2.4
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools

%description
Pyrsistent is a number of persistent collections
(by some referred to as functional data structures).
Persistent in the sense that they are immutable.

%prep
%setup

%build
%python3_build

%install
%python3_install
%python3_prune
rm -rf %buildroot%python3_sitelibdir/integration/

%files
%python3_sitelibdir/*

%changelog
* Wed Nov 04 2020 Vitaly Lipatov <lav@altlinux.ru> 0.17.3-alt1
- new version 0.17.3 (with rpmrb script)

* Tue Oct 15 2019 Vitaly Lipatov <lav@altlinux.ru> 0.15.4-alt1
- initial build for ALT Sisyphus
