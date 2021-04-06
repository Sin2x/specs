%define  modulename httpx

Name:    python3-module-%modulename
Version: 0.17.1
Release: alt1

Summary: A next generation HTTP client for Python

License: BSD 3-Clause License
Group:   Development/Python3
URL:     https://www.python-httpx.org/

Packager: Vitaly Lipatov <lav@altlinux.ru>

# Source-url: https://github.com/encode/httpx/archive/%version.tar.gz
Source:  %modulename-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-dev python3-module-setuptools

BuildArch: noarch

%description
HTTPX is a fully featured HTTP client for Python 3,
which provides sync and async APIs, and support for both HTTP/1.1 and HTTP/2.

Note: HTTPX should be considered in beta.
We believe we've got the public API to a stable point now,
but would strongly recommend pinning your dependencies to the 0.13.* release,
so that you're able to properly review API changes between package updates.
A 1.0 release is expected to be issued sometime around mid-2020.

%prep
%setup -n %modulename-%version

%build
%python3_build

%install
%python3_install

%files
%python3_sitelibdir/%modulename/
%python3_sitelibdir/*.egg-info/

%changelog
* Tue Apr 06 2021 Vitaly Lipatov <lav@altlinux.ru> 0.17.1-alt1
- new version 0.17.1 (with rpmrb script)

* Mon Nov 02 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.16.1-alt1
- 1.16.1

* Thu May 28 2020 Vitaly Lipatov <lav@altlinux.ru> 0.13.2-alt1
- initial build for Sisyphus
