%define oname neutron-vpnaas

Name: openstack-%oname
Epoch: 1
Version: 14.0.0
Release: alt1

Summary: OpenStack Networking VPNaaS

Group: System/Servers
License: ASL 2.0
Url: http://docs.openstack.org/developer/%oname

Source: https://tarballs.openstack.org/%oname/%oname-%version.tar.gz
Source1: neutron-vpn-agent.init
Source2: neutron-vpn-agent.service

BuildArch: noarch

Requires: openstack-neutron >= 1:13.0.0-alt1
Requires: python3-module-%oname = %EVR

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-pbr >= 2.0.0
BuildRequires: python3-module-six >= 1.10.0
BuildRequires: python3-module-requests >= 2.14.2
BuildRequires: python3-module-jinja2 >= 2.10
BuildRequires: python3-module-netaddr >= 0.7.18
BuildRequires: python3-module-SQLAlchemy >= 1.2.0
BuildRequires: python3-module-alembic >= 0.8.10
BuildRequires: python3-module-neutron-lib >= 1.18.0
BuildRequires: python3-module-oslo.concurrency >= 3.26.0
BuildRequires: python3-module-oslo.config >= 5.2.0
BuildRequires: python3-module-oslo.db >= 4.27.0
BuildRequires: python3-module-oslo.log >= 3.36.0
BuildRequires: python3-module-oslo.messaging >= 5.29.0
BuildRequires: python3-module-oslo.reports >= 1.18.0
BuildRequires: python3-module-oslo.serialization >= 2.18.0
BuildRequires: python3-module-oslo.service >= 1.24.0
BuildRequires: python3-module-oslo.utils >= 3.33.0
BuildRequires: python3-module-neutron >= 13.0.0.0

%description
This package contains the code for the Neutron VPN as a Service
(VPNaaS) service. This includes third-party drivers. This package
requires Neutron to run.

%package -n python3-module-%oname
Summary: Neutron VPNaaS Python3 libraries
Group: Development/Python3
Requires: python3-module-neutron >= 13.0.0.0
%add_python3_req_skip networking_brocade

%description -n python3-module-%oname
This package contains the code for the Neutron VPN as a Service
(VPNaaS) service. This includes third-party drivers. This package
requires Neutron to run.

This package contains the neutron Python3 library.

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
%add_python3_req_skip neutron_tempest_plugin
%add_python3_req_skip neutron_tempest_plugin.api
%add_python3_req_skip neutron_tempest_plugin.scenario
%add_python3_req_skip neutron_tempest_plugin.services.network.json

%description -n python3-module-%oname-tests
This package contains tests for %oname.

%prep
%setup -n %oname-%version

%build
%python3_build
PYTHONPATH=. tools/generate_config_file_samples.sh

%install
%python3_install --install-data=/

# configuration files
install -p -D -m 644 etc/neutron_vpnaas.conf.sample %buildroot%_sysconfdir/neutron/neutron_vpnaas.conf
install -p -D -m 644 etc/vpn_agent.ini.sample %buildroot%_sysconfdir/neutron/vpn_agent.ini

# Install sysV init scripts
install -p -D -m 755 %SOURCE1 %buildroot%_initdir/neutron-vpn-agent

# Install systemd units
install -p -D -m 644 %SOURCE2 %buildroot%_unitdir/neutron-vpn-agent.service

%files
%doc LICENSE
%doc README.rst
%config(noreplace) %attr(0640, root, neutron) %_sysconfdir/neutron/*.ini
%config(noreplace) %attr(0640, root, neutron) %_sysconfdir/neutron/*.conf
%config(noreplace) %attr(0640, root, neutron) %_sysconfdir/neutron/rootwrap.d/*.filters
%_initdir/neutron-vpn-agent
%_unitdir/neutron-vpn-agent.service

%files -n python3-module-%oname
%doc LICENSE
%_bindir/*
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/tests

%changelog
* Wed Oct 16 2019 Grigory Ustinov <grenka@altlinux.org> 1:14.0.0-alt1
- Build new version.
- Build without python2.

* Wed Jan 16 2019 Alexey Shabalin <shaba@altlinux.org> 1:13.0.1-alt1
- 13.0.1
- switch to python3

* Fri Jun 22 2018 Grigory Ustinov <grenka@altlinux.org> 1:10.0.0-alt2
- Fixed FTBFS (remove python-module-setuptools-tests from BR).

* Wed Jun 07 2017 Alexey Shabalin <shaba@altlinux.ru> 1:10.0.0-alt1
- 10.0.0
- add tests package

* Mon Oct 24 2016 Alexey Shabalin <shaba@altlinux.ru> 1:9.0.0-alt1
- 9.0.0

* Tue Apr 19 2016 Alexey Shabalin <shaba@altlinux.ru> 1:8.0.0-alt1
- 8.0.0

* Mon Mar 28 2016 Alexey Shabalin <shaba@altlinux.ru> 1:7.0.3-alt1
- 7.0.3

* Wed Dec 30 2015 Alexey Shabalin <shaba@altlinux.ru> 1:7.0.1-alt1
- 7.0.1

* Mon Nov 02 2015 Alexey Shabalin <shaba@altlinux.ru> 1:7.0.0-alt1
- 7.0.0

* Thu Oct 15 2015 Alexey Shabalin <shaba@altlinux.ru> 2015.1.2-alt1
- 2015.1.2

* Tue Aug 25 2015 Alexey Shabalin <shaba@altlinux.ru> 2015.1.1-alt1
- 2015.1.1

* Fri May 29 2015 Alexey Shabalin <shaba@altlinux.ru> 2015.1.0-alt1
- initial build for Kilo
