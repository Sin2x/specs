%define modulename txtorcon

Name: python3-module-txtorcon
Version: 22.0.0
Release: alt1

Summary: txtorcon password-authenticated key exchange (pure python)

Url: https://pypi.python.org/pypi/txtorcon
License: MIT
Group: Development/Python

Packager: Vitaly Lipatov <lav@altlinux.ru>

# Source-url: https://pypi.io/packages/source/t/%modulename/%modulename-%version.tar.gz
Source: %modulename-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-dev python3-module-setuptools

BuildArch: noarch

AutoReq:yes,nopython

%description
Twisted-based Tor controller client, with state-tracking and configuration abstractions.

https://txtorcon.readthedocs.org

%prep
%setup -n %modulename-%version

%build
%python3_build

%install
%python3_install

rm -rfv %buildroot%python3_sitelibdir/test/

# drop python2 files
rm -rfv %buildroot%_datadir/%modulename/examples/
rm -rfv %buildroot%_datadir/%modulename/*.py

%files
%python3_sitelibdir/%modulename/
%python3_sitelibdir/twisted/plugins/
%python3_sitelibdir/*.egg-info/
%_datadir/%modulename/

%changelog
* Mon Jul 18 2022 Vitaly Lipatov <lav@altlinux.ru> 22.0.0-alt1
- new version 22.0.0 (with rpmrb script)

* Thu Aug 26 2021 Vitaly Lipatov <lav@altlinux.ru> 21.1.0-alt1
- new version 21.1.0 (with rpmrb script)

* Thu Aug 19 2021 Vitaly Lipatov <lav@altlinux.ru> 21.0.0-alt1
- new version 21.0.0 (with rpmrb script)

* Sun Sep 20 2020 Vitaly Lipatov <lav@altlinux.ru> 20.0.0-alt1
- new version 20.0.0 (with rpmrb script)

* Mon Jan 27 2020 Vitaly Lipatov <lav@altlinux.ru> 19.1.0-alt1
- new version 19.1.0 (with rpmrb script)

* Sun Jun 09 2019 Vitaly Lipatov <lav@altlinux.ru> 19.0.0-alt1
- new version 19.0.0 (with rpmrb script)

* Tue Dec 25 2018 Vitaly Lipatov <lav@altlinux.ru> 18.3.0-alt1
- new version 18.3.0 (with rpmrb script)

* Sun Nov 04 2018 Vitaly Lipatov <lav@altlinux.ru> 0.20.0-alt1
- new version 0.20.0 (with rpmrb script)

* Sun Dec 24 2017 Vitaly Lipatov <lav@altlinux.ru> 0.19.3-alt1
- new version 0.19.3 (with rpmrb script)

* Sun Dec 24 2017 Vitaly Lipatov <lav@altlinux.ru> 0.7-alt1
- Initial build for ALT Sisyphus
