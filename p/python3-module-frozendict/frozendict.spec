%def_without check

%define modulename frozendict
Name: python3-module-frozendict
Version: 1.2
Release: alt2

Summary: An immutable dictionary

Url: https://pypi.python.org/pypi/frozendict
License: MIT
Group: Development/Python3

Packager: Vitaly Lipatov <lav@altlinux.ru>

# Source-url: https://pypi.io/packages/source/f/%modulename/%modulename-%version.tar.gz
Source: %modulename-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-python3

%description
frozendict is an immutable wrapper around dictionaries that implements
the complete mapping interface. It can be used as a drop-in replacement
for dictionaries where immutability is desired.

%prep
%setup -n %modulename-%version

%build
%python3_build

%install
%python3_install

%files
%doc README.rst
%python3_sitelibdir/*

%changelog
* Thu Jul 22 2021 Grigory Ustinov <grenka@altlinux.org> 1.2-alt2
- Drop python2 support.

* Sun Oct 14 2018 Igor Vlasenko <viy@altlinux.ru> 1.2-alt1.qa1
- NMU: applied repocop patch

* Wed Jun 14 2017 Vitaly Lipatov <lav@altlinux.ru> 1.2-alt1
- initial build for ALT Sisyphus
