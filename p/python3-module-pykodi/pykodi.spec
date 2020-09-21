Name: python3-module-pykodi
Version: 0.2.0
Release: alt1

Summary: Python interface for Kodi
License: BSD
Group: Development/Python
Url: https://pypi.org/project/pykodi/

Source0: %name-%version-%release.tar

BuildArch: noarch
BuildRequires: rpm-build-python3 python3-module-setuptools

%description
%summary

%prep
%setup

%build
%python3_build

%install
%python3_install

%files
%python3_sitelibdir/pykodi
%python3_sitelibdir/pykodi-%version-*-info

%changelog
* Mon Sep 21 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.2.0-alt1
- initial
