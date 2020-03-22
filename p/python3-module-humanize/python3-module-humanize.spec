%define oname humanize

Name: python3-module-%oname
Version: 2.1.0
Release: alt1

Summary: Python humanize utilities

License: MIT
Group: Development/Python3
Url: https://pypi.python.org/pypi/humanize/

# Source-url: %__pypi_url %oname
Source: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools_scm python3-module-setuptools
BuildRequires: python3-module-pytest python3-module-freezegun

#py3_provides %oname

%description
This modest package contains various common humanization utilities, like
turning a number into a fuzzy human readable duration ('3 minutes ago')
or into a human readable size or throughput.

%prep
%setup

%build
%python3_build_debug

%install
%python3_install

%check
python3 setup.py test

%files
%doc README.md
%python3_sitelibdir/*

%changelog
* Sun Mar 22 2020 Vitaly Lipatov <lav@altlinux.ru> 2.1.0-alt1
- new version 2.1.0 (with rpmrb script)
- build python3 separated

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.5.1-alt1.git20141113.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.5.1-alt1.git20141113.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Mon Dec 22 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5.1-alt1.git20141113
- Initial build for Sisyphus

