%def_disable snapshot
%define modname hijri-converter
%def_enable check

Name: python3-module-%modname
Version: 2.1.1
Release: alt1

Summary: Hijri to Gregorian dates converter
Group: Development/Python3
License: MIT
Url: https://pypi.org/project/%modname

%if_disabled snapshot
Source: https://pypi.io/packages/source/h/%modname/%modname-%version.tar.gz
%else
Vcs: https://github.com/dralshehri/hijri-converter
Source: %modname-%version.tar
%endif

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel >= 3.6
%{?_enable_check:BuildRequires: python3-module-pytest}

%description
A Python package to convert accurately between Hijri and Gregorian dates
using the Umm al-Qura calendar of Saudi Arabia.

%prep
%setup -n %modname-%version

%build
%python3_build

%install
%python3_install

%check
%__python3 setup.py check

%files
%python3_sitelibdir_noarch/*
%doc README* CHANGELOG*


%changelog
* Thu Nov 05 2020 Yuri N. Sedunov <aris@altlinux.org> 2.1.1-alt1
- first build for Sisyphus


