%define  modulename treq
Name:    python3-module-%modulename
Version: 21.1.0
Release: alt1

Summary: Python requests like API built on top of Twisted's HTTP client.
License: MIT
Group:   Development/Python3
URL:     https://github.com/twisted/treq

Packager: Anton Midyukov <antohami@altlinux.org>

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools python3-module-incremental

BuildArch: noarch

Source:  %modulename-%version.tar

%description
treq is an HTTP library inspired by requests but written on top of Twisted's
Agents.

It provides a simple, higher level API for making HTTP requests when using
Twisted.

%prep
%setup -n %modulename-%version

%build
%python3_build

%install
%python3_install
# cleanup tests
rm -rf %buildroot%python3_sitelibdir/%modulename/test
rm -rf %buildroot%python3_sitelibdir/%modulename/testing.py

%files
%python3_sitelibdir/%modulename/
%python3_sitelibdir/*.egg-info

%changelog
* Wed May 19 2021 Anton Midyukov <antohami@altlinux.org> 21.1.0-alt1
- new version

* Sun Nov 08 2020 Vitaly Lipatov <lav@altlinux.ru> 18.6.0-alt4
- NMU: drop testing.py in additional to removed tests

* Tue Oct 01 2019 Anton Farygin <rider@altlinux.ru> 18.6.0-alt3
- removed python2 support
- removed tests from python3-module-treq package

* Mon Jan 21 2019 Anton Midyukov <antohami@altlinux.org> 18.6.0-alt2
- Added python_req_hier (Closes: 35940)

* Wed Aug 22 2018 Anton Midyukov <antohami@altlinux.org> 18.6.0-alt1
- Initial build for Sisyphus
