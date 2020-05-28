%define  modulename httpcore

Name:    python3-module-%modulename
Version: 0.9.1
Release: alt1

Summary: A minimal HTTP client

License: BSD 3-Clause License
Group:   Development/Python3
URL:     https://www.encode.io/httpcore/

Packager: Vitaly Lipatov <lav@altlinux.ru>

# Source-url: https://github.com/encode/httpcore/archive/%version.tar.gz
Source:  %modulename-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-dev python3-module-setuptools

BuildArch: noarch

%description
The HTTP Core package provides a minimal low-level HTTP client,
which does one thing only. Sending HTTP requests.

It does not provide any high level model abstractions over the API,
does not handle redirects, multipart uploads, building authentication headers,
transparent HTTP caching, URL parsing, session cookie handling,
content or charset decoding, handling JSON,
environment based configuration defaults, or any of that Jazz.

Some things HTTP Core does do:

* Sending HTTP requests.
* Provides both sync and async interfaces.
* Supports HTTP/1.1 and HTTP/2.
* Async backend support for asyncio and trio.
* Automatic connection pooling.
* HTTP(S) proxy support.

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
* Thu May 28 2020 Vitaly Lipatov <lav@altlinux.ru> 0.9.1-alt1
- initial build for Sisyphus
