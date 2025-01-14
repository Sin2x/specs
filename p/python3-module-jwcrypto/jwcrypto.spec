%define _unpackaged_files_terminate_build 1
%define pypi_name jwcrypto

%def_with check

%define pypi_version 1.1

Name: python3-module-%pypi_name
Version: 1.4.2
Release: alt1
Summary: JWCrypto is an implementation of the Javascript Object Signing and Encryption (JOSE) Web Standards

Group: Development/Python3
License: LGPL-3
Url: https://github.com/latchset/jwcrypto

BuildArch: noarch

Source: %name-%version.tar
Patch: %name-%version.patch

BuildRequires(pre): rpm-build-python3

# build backend and its deps
BuildRequires: python3(setuptools)
BuildRequires: python3(wheel)

%if_with check
# install_requires
BuildRequires: python3(cryptography)
BuildRequires: python3(deprecated)
%endif

%description
An implementation of the JOSE Working Group documents:
RFC 7515 - JSON Web Signature (JWS)
RFC 7516 - JSON Web Encryption (JWE)
RFC 7517 - JSON Web Key (JWK)
RFC 7518 - JSON Web Algorithms (JWA)
RFC 7519 - JSON Web Token (JWT)
RFC 7520 - Examples of Protecting Content Using JSON Object Signing and
           Encryption (JOSE)

%prep
%setup
%autopatch -p1

%build
%pyproject_build

%install
%pyproject_install

#do not pack docs and tests
rm -rfv %buildroot%_defaultdocdir/jwcrypto/
rm -rfv %buildroot%python3_sitelibdir/jwcrypto/tests*

%check
%tox_check_pyproject -- -vra

%files
%python3_sitelibdir/jwcrypto/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Tue Sep 27 2022 Stanislav Levin <slev@altlinux.org> 1.4.2-alt1
- 1.1.0 -> 1.4.2.

* Thu Dec 02 2021 Stanislav Levin <slev@altlinux.org> 1.1.0-alt1
- 1.0.0 -> 1.1.0.

* Mon Sep 06 2021 Stanislav Levin <slev@altlinux.org> 1.0.0-alt1
- 0.9.1 -> 1.0.0.

* Tue Jun 22 2021 Stanislav Levin <slev@altlinux.org> 0.9.1-alt1
- 0.8 -> 0.9.1.

* Mon Jan 25 2021 Stanislav Levin <slev@altlinux.org> 0.8-alt1
- 0.7 -> 0.8.

* Mon Aug 03 2020 Stanislav Levin <slev@altlinux.org> 0.7-alt1
- 0.6.0 -> 0.7.

* Fri Dec 07 2018 Stanislav Levin <slev@altlinux.org> 0.6.0-alt1
- 0.5.0 -> 0.6.0.

* Mon Jul 23 2018 Stanislav Levin <slev@altlinux.org> 0.5.0-alt1
- 0.4.2 -> 0.5.0

* Mon Mar 05 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 0.4.2-alt2
- Updated build dependencies.

* Tue Oct 24 2017 Stanislav Levin <slev@altlinux.org> 0.4.2-alt1
- New 0.4.2 version

* Tue May 10 2016 Mikhail Efremov <sem@altlinux.org> 0.2.1-alt1
- Initial build.

