Name: python3-module-huawei-lte-api
Version: 1.4.17
Release: alt1

Summary: Python API For huawei LAN/WAN LTE Modems
License: LGPLv3
Group: Development/Python
Url: https://pypi.org/project/huawei-lte-api/

Source0: %name-%version-%release.tar

BuildArch: noarch
BuildRequires: rpm-build-python3 python3-module-setuptools python3-module-pytest-runner

%description
%summary

%prep
%setup

%build
%python3_build

%install
%python3_install

%files
%python3_sitelibdir/huawei_lte_api
%python3_sitelibdir/huawei_lte_api-%version-*-info

%changelog
* Fri Jan 29 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.4.17-alt1
- 1.4.17 released

* Tue Jul 21 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.4.12-alt1
- 1.4.12 released

* Tue Jan 14 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.4.7-alt1
- 1.4.7 released
