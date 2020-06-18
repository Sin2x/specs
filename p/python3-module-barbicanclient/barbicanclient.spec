%define oname barbicanclient

Name:       python3-module-%oname
Version:    4.10.0
Release:    alt1

Summary:    Client Library for OpenStack Barbican Key Management API

License:    Apache-2.0
Url:        http://docs.openstack.org/developer/python-%oname
Group:      Development/Python3

Source:     https://tarballs.openstack.org/python-%oname/python-%oname-%version.tar.gz

BuildArch:  noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-pbr >= 2.0.0
BuildRequires: python3-module-requests >= 2.14.2
BuildRequires: python3-module-six >= 1.10.0
BuildRequires: python3-module-cliff >= 2.8.0
BuildRequires: python3-module-oslo.config >= 3.14.0
BuildRequires: python3-module-keystoneauth1 >= 3.4.0
BuildRequires: python3-module-oslo.i18n >= 3.15.3
BuildRequires: python3-module-oslo.serialization >= 2.18.0
BuildRequires: python3-module-oslo.utils >= 3.33.0
BuildRequires: python3-module-sphinx
BuildRequires: python3-module-openstackdocstheme >= 1.18.1
BuildRequires: python3-module-reno
BuildRequires: python3-module-sphinxcontrib-rsvgconverter

%description
There is a Python library for accessing the API (barbicanclient module),
and a command-line script (barbican).

%package tests
Summary: Tests for %oname
Group: Development/Python3
Requires: %name = %EVR

%description tests
This package contains tests for %oname.

%package doc
Summary:    Documentation for OpenStack Barbican Key Management API
Group:  Development/Documentation

%description doc
Documentation for the client library for interacting with Openstack
Barbican Key Management API.

%prep
%setup -n python-%oname-%version

# Let RPM handle the dependencies
rm -f test-requirements.txt requirements.txt

# Remove bundled egg-info
rm -rf python_barbicanclient.egg-info
# let RPM handle deps
sed -i '/setup_requires/d; /install_requires/d; /dependency_links/d' setup.py

%build
%python3_build

%install
%python3_install

# Build HTML docs and man page
python3 setup.py build_sphinx
rm -f doc/build/html/.buildinfo

%files
%_bindir/barbican
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests

%files tests
%python3_sitelibdir/*/tests

%files doc
%doc LICENSE doc/build/html

%changelog
* Fri May 15 2020 Grigory Ustinov <grenka@altlinux.org> 4.10.0-alt1
- Automatically updated to 4.10.0.
- Renamed spec file.

* Fri Oct 18 2019 Grigory Ustinov <grenka@altlinux.org> 4.9.0-alt1
- Automatically updated to 4.9.0.
- Build without python2.

* Wed Aug 14 2019 Grigory Ustinov <grenka@altlinux.org> 4.8.1-alt1
- Automatically updated to 4.8.1

* Mon Dec 10 2018 Alexey Shabalin <shaba@altlinux.org> 4.7.1-alt1
- 4.7.1

* Tue Oct 09 2018 Grigory Ustinov <grenka@altlinux.org> 4.7.0-alt1
- Autoupdated to 4.7.0.

* Fri Jul 20 2018 Grigory Ustinov <grenka@altlinux.org> 4.6.0-alt1
- new version 4.6.0

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 4.2.0-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Tue May 30 2017 Alexey Shabalin <shaba@altlinux.ru> 4.2.0-alt1
- 4.2.0
- add test packages

* Tue Oct 18 2016 Alexey Shabalin <shaba@altlinux.ru> 4.1.0-alt1
- 4.1.0

* Thu Apr 14 2016 Alexey Shabalin <shaba@altlinux.ru> 4.0.1-alt1
- 4.0.1

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 3.3.0-alt1.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 3.3.0-alt1.1
- NMU: Use buildreq for BR.

* Thu Oct 29 2015 Alexey Shabalin <shaba@altlinux.ru> 3.3.0-alt1
- 3.3.0

* Tue Mar 31 2015 Alexey Shabalin <shaba@altlinux.ru> 3.0.3-alt1
- 3.0.3

* Thu Mar 12 2015 Alexey Shabalin <shaba@altlinux.ru> 3.0.2-alt1
- Initial release for Sisyphus

