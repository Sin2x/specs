%def_without test

Name: python3-module-spyder-kernels
Version: 1.8.1
Release: alt1

License: MIT
Group: Development/Python
Url: https://github.com/spyder-ide/spyder-kernels

Summary: Jupyter Kernels for the Spyder console

# Source-url: https://github.com/spyder-ide/spyder-kernels/archive/v%version.tar.gz
Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-python3 rpm-build-intro

BuildRequires: python3-module-cloudpickle python3-module-flaky

%description
Package that provides Jupyter kernels for use with the consoles of Spyder,
the Scientific Python Development Environment.

These kernels can launched either through Spyder itself
or in an independent Python session, and allow for interactive
or file-based execution of Python code inside Spyder.

%prep
%setup

%build
%python3_build

%install
%python3_install

%if_with test
%check
%python3_test
%endif

%files
%python3_sitelibdir/*

%changelog
* Tue Feb 04 2020 Vitaly Lipatov <lav@altlinux.ru> 1.8.1-alt1
- initial build for ALT Sisyphus
