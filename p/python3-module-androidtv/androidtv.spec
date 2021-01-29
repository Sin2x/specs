Name: python3-module-androidtv
Version: 0.0.57
Release: alt1

Summary: State information and control of Android TV  devices via ADB
License: MIT
Group: Development/Python
Url: https://pypi.org/project/androidtv/

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
%python3_sitelibdir/androidtv
%python3_sitelibdir/androidtv-%version-*-info

%changelog
* Fri Jan 29 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.0.57-alt1
- 0.0.57 released

* Mon Nov 02 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.0.52-alt1
- 0.0.52 released

* Tue Aug 18 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.0.47-alt1
- 0.0.47 released

* Mon Jul 20 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.0.45-alt1
- initial
