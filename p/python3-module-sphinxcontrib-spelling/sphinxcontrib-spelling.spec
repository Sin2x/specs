%define mname sphinxcontrib
%define oname %mname-spelling

Name: python3-module-sphinxcontrib-spelling
Version: 7.2.1
Release: alt1

Summary: Sphinx "spelling" extension

License: BSD
Group: Development/Python3
Url: https://pypi.python.org/pypi/sphinxcontrib-spelling

Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# Source-url: %__pypi_url %oname
Source: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-intro >= 2.1.3
BuildRequires(pre): rpm-build-python3

BuildRequires(pre): rpm-macros-sphinx3
BuildRequires: python3-module-sphinx-sphinx-build-symlink

# generated by 'epm restore --dry-run' from sphinxcontrib-spelling/requirements.txt
%py3_use enchant >= 3.1.1
%py3_use sphinx >= 3.0.0

# generated by 'epm restore --dry-run' from sphinxcontrib-spelling/setup.py setup_requires
%py3_buildrequires pbr


%description
This package contains sphinxcontrib.spelling, a spelling checker for
Sphinx-based documentation. It uses PyEnchant to produce a report
showing misspelled words.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation

%description docs
This package contains sphinxcontrib.spelling, a spelling checker for
Sphinx-based documentation. It uses PyEnchant to produce a report
showing misspelled words.

This package contains documentation for %oname.

%package -n python3-module-%mname
Summary: Core package of %mname
Group: Development/Python3
%py3_provides %mname

%description -n python3-module-%mname
Core package of %mname.

%prep
%setup

%prepare_sphinx3 docs

%build
%python3_build

%install
%python3_install
%python3_prune
install -p -m644 %mname/__init__.py \
	%buildroot%python3_sitelibdir/%mname/

export PYTHONPATH=%buildroot%python3_sitelibdir
%make -C docs html

%files
%doc AUTHORS ChangeLog README
%python3_sitelibdir/%mname/*
%python3_sitelibdir/*.egg-info
%exclude %python3_sitelibdir/%mname/__init__.py
%exclude %python3_sitelibdir/%mname/__pycache__/__init__.*

%files -n python3-module-%mname
%dir %python3_sitelibdir/%mname
%dir %python3_sitelibdir/%mname/__pycache__
%python3_sitelibdir/%mname/__init__.py
%python3_sitelibdir/%mname/__pycache__/__init__.*

%files docs
%doc docs/build/html/*


%changelog
* Fri Aug 13 2021 Vitaly Lipatov <lav@altlinux.ru> 7.2.1-alt1
- new version 7.2.1 (with rpmrb script)

* Fri Aug 13 2021 Vitaly Lipatov <lav@altlinux.ru> 2.1.1-alt3
- build python3 module separately

* Tue May 15 2018 Andrey Bychkov <mrdrew@altlinux.org> 2.1.1-alt2.1.2
- (NMU) rebuild with python3.6

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 2.1.1-alt2.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 2.1.1-alt2.1
- NMU: Use buildreq for BR.

* Wed Apr 22 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.1.1-alt2
- Added module for Python 3

* Wed Jul 16 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.1.1-alt1
- Version 2.1.1

* Fri Nov 29 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.4-alt1
- Initial build for Sisyphus
