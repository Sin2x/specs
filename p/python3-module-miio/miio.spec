Name: python3-module-miio
Version: 0.5.4
Release: alt1

Summary: Python miIO library
License: BSD
Group: Development/Python
Url: https://pypi.org/project/python-miio/

Source0: %name-%version-%release.tar

BuildArch: noarch
BuildRequires: rpm-build-python3 python3-module-setuptools

%package -n miio-tools
Summary: miIO tools
Group: Development/Python
Requires: python3-module-miio = %version-%release

%description
This library (and its accompanying cli tool) can be used to interface
with devices using Xiaomi's miIO and miOT protocols.

%description -n miio-tools
This library (and its accompanying cli tool) can be used to interface
with devices using Xiaomi's miIO and miOT protocols.

%prep
%setup

%build
%python3_build

%install
%python3_install

%files
%python3_sitelibdir/miio
%exclude %python3_sitelibdir/miio/tests
%python3_sitelibdir/python_miio-%version-*-info

%files -n miio-tools
%_bindir/*

%changelog
* Fri Jan 29 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.5.4-alt1
- 0.5.4 released

* Fri Nov 06 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.5.3-alt2
- exclude tests from package due to excessive reqs

* Tue Sep 22 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.5.3-alt1
- 0.5.3 released

* Fri Jul 17 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.5.2.1-alt1
- initial
