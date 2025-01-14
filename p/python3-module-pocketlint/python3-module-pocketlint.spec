%define modname pocketlint

Name: python3-module-%modname
Version: 0.24
Release: alt1

Summary: Addon for Pylint
Group: Development/Python3
License: GPLv2+
Url: https://pypi.org/project/%modname

Source: https://pypi.io/packages/source/p/%modname/%modname-%version.tar.gz

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-pylint

%description
Addon pylint modules and configuration settings for checking the validity
of Python-based source projects.

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
%doc README


%changelog
* Thu Jul 14 2022 Yuri N. Sedunov <aris@altlinux.org> 0.24-alt1
- 0.24

* Fri Jul 01 2022 Yuri N. Sedunov <aris@altlinux.org> 0.23-alt1
- 0.23

* Wed Oct 06 2021 Yuri N. Sedunov <aris@altlinux.org> 0.22-alt1
- 0.22

* Tue Apr 20 2021 Yuri N. Sedunov <aris@altlinux.org> 0.21-alt1
- 0.21

* Sun Sep 01 2019 Yuri N. Sedunov <aris@altlinux.org> 0.20-alt1
- 0.20

* Thu May 02 2019 Yuri N. Sedunov <aris@altlinux.org> 0.19-alt1
- first build for Sisyphus

