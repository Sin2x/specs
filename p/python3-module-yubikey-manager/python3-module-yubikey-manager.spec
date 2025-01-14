%define _unpackaged_files_terminate_build 1

Name: python3-module-yubikey-manager
Version: 4.0.9
Release: alt4

Summary: Tool for managing your YubiKey configuration
License: BSD-2-Clause
Group: Development/Python3
Url: https://github.com/Yubico/yubikey-manager
BuildArch: noarch

Source0: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3(setuptools)
BuildRequires: python3(unittest)
BuildRequires: python3(poetry-core)
BuildRequires: python3(fido2)
BuildRequires: python3(click)
BuildRequires: python3(makefun)
BuildRequires: python3(OpenSSL)
BuildRequires: libpcsclite-devel

Requires: ykpers
Requires: libykpers-1
Requires: pcsc-lite-ccid

%description
Python 3.6 (or later) library for configuring a YubiKey.

%package -n ykman
Summary: YubiKey Manager (command line tool for configuring a YubiKey)
Group: System/Configuration/Hardware
Requires: %name = %EVR

%description -n ykman
Python 3.6 (or later) command line tool for configuring a YubiKey.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

install -pD -m0644 man/ykman.1 %buildroot%_man1dir/ykman.1

%check
%tox_check_pyproject

%files
%doc COPYING NEWS
%python3_sitelibdir/*

%files -n ykman
%doc COPYING NEWS
%_bindir/*
%_man1dir/*

%changelog
* Wed Sep 14 2022 Stanislav Levin <slev@altlinux.org> 4.0.9-alt4
- NMU: Fixed FTBFS (poetry-core 1.1.0).

* Sat Sep 10 2022 Anton Zhukharev <ancieg@altlinux.org> 4.0.9-alt3
- add ykpers dependency

* Mon Jul 25 2022 Anton Zhukharev <ancieg@altlinux.org> 4.0.9-alt2
- add pcsc-lite-ccid dependency

* Sat Jul 23 2022 Anton Zhukharev <ancieg@altlinux.org> 4.0.9-alt1
- initial build for Sisyphus

