%define  modulename pre-commit

Name:    python3-module-%modulename
Version: 2.8.2
Release: alt1

Summary: A framework for managing and maintaining multi-language pre-commit hooks.

License: MIT
Group:   Development/Python3
URL:     https://github.com/pre-commit/pre-commit

Packager: Grigory Ustinov <grenka@altlinux.org>

BuildRequires(pre): rpm-build-python3

BuildArch: noarch

Source:  %modulename-%version.tar

%description
%summary

%prep
%setup -n %modulename-%version

%build
%python3_build

%install
%python3_install

%files
%doc *.md
%_bindir/*
%python3_sitelibdir/pre_commit
%python3_sitelibdir/*.egg-info

%changelog
* Sun Nov 08 2020 Grigory Ustinov <grenka@altlinux.org> 2.8.2-alt1
- Initial build for Sisyphus.
