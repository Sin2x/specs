%define oname smpplib
Name: python3-module-%oname
Version: 2.1.0
Release: alt3

Summary: SMPP library for Python

License: GNUv3
Group: Development/Python
Url: https://github.com/python-smpplib/python-smpplib

# Source-url: %__pypi_url %oname
Source: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires(pre): rpm-build-intro >= 2.2.4

%description
SMPP library for Python.

%prep
%setup

%build
%python3_build

%install
%python3_install
%python3_prune

%files
%python3_sitelibdir/*

%changelog
* Tue Nov 03 2020 Vitaly Lipatov <lav@altlinux.ru> 2.1.0-alt3
- fix requires

* Tue Nov 03 2020 Vitaly Lipatov <lav@altlinux.ru> 2.1.0-alt2
- cleanup spec

* Sat Apr 11 2020 Eugene Omelyanovich <regatio@etersoft.ru> 2.1.0-alt1
- new version (2.1.0) with rpmgs script
