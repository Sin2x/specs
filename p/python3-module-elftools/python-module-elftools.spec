Name: python3-module-elftools
Version: 0.27
Release: alt1

Summary: Pure-Python library for parsing and analyzing ELF files
License: Unlicense
Group: Development/Python3
Url: https://pypi.org/project/pyelftools/

Source: %name-%version.tar

BuildArch: noarch
BuildRequires: rpm-build-python3 python3-module-setuptools

%description
Pure-Python library for parsing and analyzing ELF files
and DWARF debugging information.

%prep
%setup

%build
%python3_build

%install
%python3_install

%files
%doc CHANGES LICENSE README*
%_bindir/readelf.py
%python3_sitelibdir/elftools
%python3_sitelibdir/pyelftools-%version-*-info

%changelog
* Thu Feb 11 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.27-alt1
- 0.27 released

* Thu Sep 17 2020 Grigory Ustinov <grenka@altlinux.org> 0.22-alt2.git20130619.a1d9681
- Drop python2 support.
- Disable check.

* Mon Dec 12 2016 Lenar Shakirov <snejok@altlinux.ru> 0.22-alt1.git20130619.a1d9681
- Initial build for ALT (based on 0.22-0.9.git20130619.a1d9681.fc25.src)
