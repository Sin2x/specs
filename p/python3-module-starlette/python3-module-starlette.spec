%define  modulename starlette

Name:    python3-module-%modulename
Version: 0.14.2
Release: alt1

Summary: The little ASGI framework that shines

License: BSD-3-Clause
Group:   Development/Python3
URL:     https://www.starlette.io/

Packager: Vitaly Lipatov <lav@altlinux.ru>

# Source-url: https://github.com/encode/starlette/archive/%version.tar.gz
Source:  %modulename-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-dev python3-module-setuptools

BuildArch: noarch

%description
Starlette is a lightweight ASGI framework/toolkit,
which is ideal for building high performance asyncio services.

It is production-ready, and gives you the following:

Seriously impressive performance.
WebSocket support.
GraphQL support.
In-process background tasks.
Startup and shutdown events.
Test client built on requests.
CORS, GZip, Static Files, Streaming responses.
Session and Cookie support.
100%% test coverage.
100%% type annotated codebase.
Zero hard dependencies.


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
* Thu Feb 11 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.14.2-alt1
- 0.14.2

* Thu May 28 2020 Vitaly Lipatov <lav@altlinux.ru> 0.13.4-alt1
- initial build for Sisyphus
