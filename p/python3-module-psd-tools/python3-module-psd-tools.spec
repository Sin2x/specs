%define  modulename psd_tools

Name:    python3-module-psd-tools
Version: 1.9.16
Release: alt1

Summary: Python package for reading Adobe Photoshop PSD files

License: MIT
Group:   Development/Python3
URL:     https://github.com/psd-tools/psd-tools

Packager: Vitaly Lipatov <lav@altlinux.ru>

BuildArch: noarch

BuildRequires(pre): rpm-build-python3 rpm-build-intro
BuildRequires: python3-dev python3-module-setuptools

%py3_use docopt >= 0.5
%py3_use Pillow


# Source-url: https://github.com/psd-tools/psd-tools/archive/v%version.tar.gz
Source: %name-%version.tar

%description
psd-tools is a Python package for working with
Adobe Photoshop PSD files as described in specification.

Note:
In order to extract images from 32bit PSD files PIL/Pillow
must be built with LITTLECMS or LITTLECMS2 support.

%prep
%setup

%build
%python3_build

%install
%python3_install

%files
%doc README.rst
%_bindir/psd-tools
%python3_sitelibdir_noarch/%modulename/
%python3_sitelibdir_noarch/*.egg-info

%changelog
* Sat Oct 17 2020 Vitaly Lipatov <lav@altlinux.ru> 1.9.16-alt1
- initial build for ALT Sisyphus
