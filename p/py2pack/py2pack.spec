%define oname py2pack

Name:       py2pack
Version:    0.6.4
Release:    alt2

Summary:    Generate distribution packages from Python packages on PyPI
License:    GPLv2
Group:      Development/Python3
Url:        http://github.com/saschpe/py2pack
Packager:   Vitaly Lipatov <lav@altlinux.ru>

BuildArch:  noarch

Source:     %name-%version.tar
Source44:   import.info
Patch0:     port-on-python3.patch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-jinja2 python3-module-six
BuildRequires: python3-module-cssselect python3-module-lxml
BuildRequires: python3-module-requests python-tools-2to3

Requires: python3-module-py2pack = %version-%release


%description
This script allows to generate RPM spec or DEB dsc files from Python modules.
It allows to list Python modules or search for them on the Python Package Index
(PyPI). Conveniently, it can fetch tarballs and change logs making it an
universal tool to package Python modules.

%package -n python3-module-py2pack
Summary: General purpose template engine
Group: Development/Python3

%description -n python3-module-py2pack
This script allows to generate RPM spec or DEB dsc files from Python modules.
It allows to list Python modules or search for them on the Python Package Index
(PyPI). Conveniently, it can fetch tarballs and change logs making it an
universal tool to package Python modules.

%prep
%setup -n %oname-%version
%patch0 -p2

%__subst "s|man/man1|share/man/man1|g" setup.py

%build
%python3_build

%install
%python3_install

%files
%_bindir/%oname
%_man1dir/%oname.*

%files -n python3-module-py2pack
%_docdir/%name
%python3_sitelibdir_noarch/%{oname}*


%changelog
* Fri Jan 31 2020 Andrey Bychkov <mrdrew@altlinux.org> 0.6.4-alt2
- Porting on Python3.

* Sat Aug 27 2016 Vitaly Lipatov <lav@altlinux.ru> 0.6.4-alt1
- new version 0.6.4 (with rpmrb script) from github sources

* Sat Aug 27 2016 Vitaly Lipatov <lav@altlinux.ru> 0.4.4-alt2
- initial build for ALT Linux Sisyphus

* Wed Mar 02 2016 Igor Vlasenko <viy@altlinux.ru> 0.4.4-alt1_4
- update to new release by fcimport

* Mon Oct 19 2015 Igor Vlasenko <viy@altlinux.ru> 0.4.4-alt1_3
- update to new release by fcimport

* Mon Jul 07 2014 Igor Vlasenko <viy@altlinux.ru> 0.4.4-alt1_2
- update to new release by fcimport

* Mon Sep 02 2013 Igor Vlasenko <viy@altlinux.ru> 0.4.4-alt1_1
- update to new release by fcimport

* Thu Feb 21 2013 Igor Vlasenko <viy@altlinux.ru> 0.3.17-alt1_4
- update to new release by fcimport

* Sun Dec 30 2012 Igor Vlasenko <viy@altlinux.ru> 0.3.17-alt1_3
- initial fc import

