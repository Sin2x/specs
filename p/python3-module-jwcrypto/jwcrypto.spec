%define _unpackaged_files_terminate_build 1

%define mname jwcrypto
%def_with check

Name: python3-module-%mname
Version: 0.8
Release: alt1
Summary: JWCrypto is an implementation of the Javascript Object Signing and Encryption (JOSE) Web Standards

Group: Development/Python3
License: LGPL-3
Url: https://github.com/latchset/jwcrypto

BuildArch: noarch

Source: %name-%version.tar
Patch: %name-%version.patch

BuildRequires(pre): rpm-build-python3

BuildRequires: python3-module-setuptools

%if_with check
BuildRequires: python3-module-tox
BuildRequires: python3-module-cryptography
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
%python3_build_debug

%check
export PIP_NO_INDEX=YES
tox.py3 --sitepackages -e py38 -vvr -- -v

%install
%python3_install
#do not pack docs and tests
rm -rfv %buildroot%_defaultdocdir/%mname
rm -rfv %buildroot%python3_sitelibdir/%mname/tests*

%files
%python3_sitelibdir/%mname
%python3_sitelibdir/%mname-%version-py*.egg-info

%changelog
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

