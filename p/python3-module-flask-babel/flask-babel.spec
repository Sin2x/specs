%define _unpackaged_files_terminate_build 1
%define oname Flask-Babel

%def_disable check

Name: python3-module-flask-babel
Version: 2.0.0
Release: alt1

Summary: Adds i18n/l10n support to Flask applications

License: BSD
Group: Development/Python3
Url: https://pypi.python.org/pypi/Flask-Babel/

Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# Source-url: %__pypi_url %oname
Source: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-intro >= 2.2.5
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-babel
%if_enabled check
BuildRequires: python3-module-pytest
%endif

%py3_provides flask_babel

%description
Adds i18n/l10n support to Flask applications with the help of the Babel
library.

%prep
%setup

%build
%python3_build_debug

%install
%python3_install

%check
%python3_test

%files
%doc docs/*.rst PKG-INFO
%python3_sitelibdir/*

%changelog
* Thu Nov 05 2020 Vitaly Lipatov <lav@altlinux.ru> 2.0.0-alt1
- new version 2.0.0 (with rpmrb script)

* Thu Nov 05 2020 Vitaly Lipatov <lav@altlinux.ru> 0.11.1-alt2
- build python3 package separately

* Tue Jan 17 2017 Igor Vlasenko <viy@altlinux.ru> 0.11.1-alt1
- automated PyPI update

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.9-alt2.git20130729.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Mon Jan 25 2016 Sergey Alembekov <rt@altlinux.ru> 0.9-alt2.git20130729
- Rebuild with "def_disable check"
- Cleanup bildreq

* Tue Oct 21 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9-alt1.git20130729
- Initial build for Sisyphus
