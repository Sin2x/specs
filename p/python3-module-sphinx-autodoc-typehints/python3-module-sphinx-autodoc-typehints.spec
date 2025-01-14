%define modname sphinx-autodoc-typehints
%define pypi_name sphinx_autodoc_typehints
%def_disable check

Name: python3-module-%modname
Version: 1.19.2
Release: alt1

Summary: Type hints (PEP 484) support for the Sphinx autodoc extension
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/%modname

Vcs: https://github.com/tox-dev/sphinx-autodoc-typehints.git
#Source: https://github.com/tox-dev/%modname/archive/%version/%modname-%version.tar.gz
Source: https://pypi.io/packages/source/s/%modname/%pypi_name-%version.tar.gz

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools_scm python3-module-wheel
%{?_enable_check:BuildRequires: python3-module-tox
BuildRequires: python3-module-pytest python3-module-sphobjinv
BuildRequires: python3-module-coverage python3-module-covdefaults
BuildRequires: python3-module-diff-cover python3-module-twine}

%description
This Sphinx extension allows to use Python 3 annotations for
documenting acceptable argument types and return value types of
functions.

%prep
%setup -n %pypi_name-%version

%build
%pyproject_build

%install
%pyproject_install

%check
%tox_check

%files
%python3_sitelibdir_noarch/%pypi_name
%python3_sitelibdir_noarch/%{pyproject_distinfo %pypi_name}
%doc README* CHANGELOG*


%changelog
* Tue Aug 09 2022 Yuri N. Sedunov <aris@altlinux.org> 1.19.2-alt1
- 1.19.2

* Mon Aug 01 2022 Yuri N. Sedunov <aris@altlinux.org> 1.19.1-alt1
- 1.19.1

* Fri Jul 29 2022 Yuri N. Sedunov <aris@altlinux.org> 1.19.0-alt1
- 1.19.0
- ported to %%pyproject* macros

* Tue Jun 14 2022 Yuri N. Sedunov <aris@altlinux.org> 1.18.3-alt1
- 1.18.3

* Fri May 06 2022 Yuri N. Sedunov <aris@altlinux.org> 1.18.1-alt1
- 1.18.1

* Sat Mar 05 2022 Yuri N. Sedunov <aris@altlinux.org> 1.17.0-alt1
- 1.17.0

* Fri Jan 28 2022 Yuri N. Sedunov <aris@altlinux.org> 1.16.0-alt1
- 1.16.0

* Thu Jan 20 2022 Yuri N. Sedunov <aris@altlinux.org> 1.15.3-alt1
- 1.15.3

* Mon Jan 10 2022 Yuri N. Sedunov <aris@altlinux.org> 1.15.1-alt1
- 1.15.1

* Wed Jan 05 2022 Yuri N. Sedunov <aris@altlinux.org> 1.13.1-alt1
- 1.13.1 (supported Python 3.10)

* Thu Apr 15 2021 Yuri N. Sedunov <aris@altlinux.org> 1.12.0-alt1
- 1.12.0

* Sun Mar 07 2021 Yuri N. Sedunov <aris@altlinux.org> 1.11.1-alt1
- first build for Sisyphus




