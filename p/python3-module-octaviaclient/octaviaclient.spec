%define oname octaviaclient

Name:       python3-module-%oname
Version:    2.0.1
Release:    alt2

Summary:    Octavia client for OpenStack Load Balancing

Group:      Development/Python3
License:    Apache-2.0
Url:        http://docs.openstack.org/developer/%oname

Source:     https://tarballs.openstack.org/python-%oname/python-%oname-%version.tar.gz

BuildArch:  noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-pbr >= 2.0.0
BuildRequires: python3-module-six >= 1.10.0
BuildRequires: python3-module-appdirs >= 1.3.0
BuildRequires: python3-module-babel >= 2.3.4
BuildRequires: python3-module-cliff >= 2.8.0
BuildRequires: python3-module-cmd2
BuildRequires: python3-module-debtcollector >= 1.2.0
BuildRequires: python3-module-iso8601 >= 0.1.11
BuildRequires: python3-module-keystoneauth1 >= 3.4.0
BuildRequires: python3-module-monotonic >= 0.6
BuildRequires: python3-module-netaddr >= 0.7.18
BuildRequires: python3-module-netifaces >= 0.10.4
BuildRequires: python3-module-neutronclient >= 6.7.0
BuildRequires: python3-module-openstackclient >= 3.12.0
BuildRequires: python3-module-os-client-config >= 1.28.0
BuildRequires: python3-module-osc-lib >= 1.8.0
BuildRequires: python3-module-oslo.i18n >= 3.15.3
BuildRequires: python3-module-oslo.serialization >= 2.18.0
BuildRequires: python3-module-oslo.utils >= 3.33.0
BuildRequires: python3-module-prettytable >= 0.7.1
BuildRequires: python3-module-pyparsing >= 2.1.0
BuildRequires: python3-module-pytz >= 2013.6
BuildRequires: python3-module-yaml >= 3.12
BuildRequires: python3-module-requests >= 2.14.2
BuildRequires: python3-module-simplejson >= 3.5.1
BuildRequires: python3-module-stevedore >= 1.20.0
BuildRequires: python3-module-wrapt >= 1.7.0

# doc
BuildRequires: python3-module-sphinx >= 1.6.2
BuildRequires: python3-module-openstackdocstheme >= 1.18.1
BuildRequires: python3-module-reno >= 2.5.0
BuildRequires: python3-module-sphinxcontrib-rsvgconverter

%description
This is an OpenStack Client (OSC) plugin for Octavia, an OpenStack
Load Balancing project.

%package tests
Summary: Tests for %oname
Group: Development/Python3
Requires: %name = %EVR

%description tests
This package contains tests for %oname.

%package doc
Summary: Documentation for OpenStack Octavia client
Group: Development/Documentation

%description doc
This is an OpenStack Client (OSC) plugin for Octavia, an OpenStack
Load Balancing project.

This package contains documentation for %oname.

%prep
%setup -n python-%oname-%version

# Let RPM handle the dependencies
rm -f {,test-}requirements.txt

# Prevent doc build warnings from causing a build failure
sed -i '/warning-is-error/d' setup.cfg

%build
%python3_build

export PYTHONPATH="$PWD"

# generate html docs
sphinx-build-3 doc/source html
# generate man page
sphinx-build-3 -b man doc/source man
# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}

%install
%python3_install

# install man page
install -p -D -m 644 man/python-octaviaclient.1 %buildroot%_man1dir/octaviaclient.1

%files
%doc *.rst LICENSE
%_man1dir/octaviaclient*
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests

%files tests
%python3_sitelibdir/*/tests

%files doc
%doc LICENSE html

%changelog
* Fri Jun 19 2020 Grigory Ustinov <grenka@altlinux.org> 2.0.1-alt2
- Unify documentation building.

* Fri May 15 2020 Grigory Ustinov <grenka@altlinux.org> 2.0.1-alt1
- Automatically updated to 2.0.1.
- Renamed spec file.

* Fri Oct 18 2019 Grigory Ustinov <grenka@altlinux.org> 1.10.0-alt1
- Automatically updated to 1.10.0.
- Build without python2.

* Mon Jan 14 2019 Alexey Shabalin <shaba@altlinux.org> 1.6.0-alt1
- Initial build.
