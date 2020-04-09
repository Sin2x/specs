%define oname prometheus_client

Name: python3-module-%oname
Version: 0.3.0
Release: alt2

Summary: The Python client for Prometheus
Url: https://github.com/kovidgoyal/html5-parser
License: ASL 2.0
Group: Development/Python3

Packager: Vitaly Lipatov <lav@altlinux.ru>

# Source-url: https://github.com/prometheus/client_python/archive/v%version.tar.gz
Source: %oname-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-python3 rpm-build-intro >= 2.1.4
BuildRequires: python3-module-decorator python3-module-pytest

%description
The Python client for Prometheus.

%prep
%setup -q -n %oname-%version

%build
%python3_build_debug

%install
%python3_install

%check
%files
%doc README.md MAINTAINERS.md
%python3_sitelibdir/%oname/
%python3_sitelibdir/%oname-*.egg-info

%changelog
* Thu Apr 09 2020 Andrey Bychkov <mrdrew@altlinux.org> 0.3.0-alt2
- Build for python2 disabled.

* Wed Jun 12 2019 Vitaly Lipatov <lav@altlinux.ru> 0.3.0-alt1
- new version 0.3.0 (with rpmrb script)

* Tue Jul 03 2018 Vitaly Lipatov <lav@altlinux.ru> 0.2.0-alt1
- initial build for ALT Sisyphus

