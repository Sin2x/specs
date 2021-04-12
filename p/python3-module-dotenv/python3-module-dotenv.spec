%define oname dotenv

Name: python3-module-%oname
Version: 0.17.0
Release: alt1

Summary: Reads the key-value pair from .env file and adds them to environment variable.

License: BSD-3-Clause
Group: Development/Python
Url: https://github.com/theskumar/python-dotenv

Source: %name-%version.tar
BuildArch: noarch

AutoReqProv: nopython
%define __python %nil

BuildRequires(pre): rpm-build-python3

%description
Reads the key-value pair from .env file and adds them to environment
variable. It is great for managing app settings during development
and in production using 12-factor principles.

%prep
%setup -n %name-%version

%build
# We don't support IPython for now (requires additional dependencies)
rm -f src/dotenv/ipython.py
%python3_build

%install
%python3_install

%files
%_bindir/%oname
%python3_sitelibdir/%oname/
%python3_sitelibdir/*.egg-*

%changelog
* Mon Apr 12 2021 Vladimir Didenko <cow@altlinux.org> 0.17.0-alt1
- new version

* Mon Dec 21 2020 Vladimir Didenko <cow@altlinux.org> 0.15.0-alt1
- new version

* Fri Jul 3 2020 Vladimir Didenko <cow@altlinux.org> 0.14.0-alt1
- new version

* Wed Mar 11 2020 Vladimir Didenko <cow@altlinux.org> 0.12.0-alt1
- initial build for Sisyphus
