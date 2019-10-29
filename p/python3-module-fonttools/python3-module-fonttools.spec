%define modulename fontTools

Name: python3-module-fonttools
Version: 4.0.2
Release: alt1

Summary: Converts OpenType and TrueType fonts to and from XML

Group: Development/Tools
License: LGPL
URL: https://github.com/fonttools/fonttools/

Packager: Vitaly Lipatov <lav@altlinux.ru>

# Source-url: https://github.com/fonttools/fonttools/archive/%version.tar.gz
Source: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-compat >= 1.2
BuildRequires(pre): rpm-build-python3

BuildRequires: xorg-sdk
# python-module-PyXML python-module-ctypes
BuildRequires: python3-devel python3-module-setuptools python3-module-numpy


%global desc \
FontTools/TTX is a library to manipulate font files from Python. It supports \
reading and writing of TrueType/OpenType fonts, reading and writing of AFM \
files, reading (and partially writing) of PS Type 1 fonts. The package also \
contains a tool called TTX which converts TrueType/OpenType fonts to and \
from an XML-based format.

%description
%desc

%package -n fonttools
Group: Development/Python3
Summary: Python 3 fonttools
Requires: %name = %EVR

%description -n fonttools
%desc

%prep
%setup
sed -i '1d' Lib/fontTools/mtiLib/__init__.py

%build
%python3_build

%install
%python3_install

%files
%python3_sitelibdir/%modulename/
%python3_sitelibdir/fonttools-%version-py%__python3_version.egg-info

%files -n fonttools
%_bindir/ttx
%_bindir/pyft*
%_bindir/fonttools
%_man1dir/*


%changelog
* Sun Oct 27 2019 Vitaly Lipatov <lav@altlinux.ru> 4.0.2-alt1
- new version 4.0.2 (with rpmrb script)
- build python3 version only

* Tue Oct 15 2019 Vitaly Lipatov <lav@altlinux.ru> 3.44.0-alt1
- new version 3.44.0 (with rpmrb script)

* Fri Jun 28 2019 Vitaly Lipatov <lav@altlinux.ru> 3.43.1-alt1
- new version 3.43.1 (with rpmrb script)

* Sun Jun 09 2019 Vitaly Lipatov <lav@altlinux.ru> 3.42.0-alt1
- new version 3.42.0 (with rpmrb script)

* Thu May 30 2019 Vitaly Lipatov <lav@altlinux.ru> 3.41.2-alt1
- new version 3.41.2 (with rpmrb script)

* Wed May 08 2019 Vitaly Lipatov <lav@altlinux.ru> 3.41.0-alt1
- new version 3.41.0 (with rpmrb script)

* Wed Mar 27 2019 Vitaly Lipatov <lav@altlinux.ru> 3.39.0-alt1
- new version 3.39.0 (with rpmrb script)

* Wed Mar 20 2019 Vitaly Lipatov <lav@altlinux.ru> 3.38.0-alt1
- new version 3.38.0 (with rpmrb script)

* Sat Feb 23 2019 Vitaly Lipatov <lav@altlinux.ru> 3.37.3-alt1
- new version 3.37.3 (with rpmrb script)

* Tue Feb 12 2019 Vitaly Lipatov <lav@altlinux.ru> 3.37.0-alt1
- new version 3.37.0 (with rpmrb script)

* Sun Feb 10 2019 Vitaly Lipatov <lav@altlinux.ru> 3.35.0-alt1
- new version 3.35.0 (with rpmrb script)

* Sun Dec 23 2018 Vitaly Lipatov <lav@altlinux.ru> 3.34.2-alt1
- new version 3.34.2 (with rpmrb script)

* Sun Nov 18 2018 Vitaly Lipatov <lav@altlinux.ru> 3.32.0-alt1
- new version 3.32.0 (with rpmrb script)

* Sun Nov 04 2018 Vitaly Lipatov <lav@altlinux.ru> 3.31.0-alt1
- new version 3.31.0 (with rpmrb script)

* Thu Aug 30 2018 Vitaly Lipatov <lav@altlinux.ru> 3.29.0-alt1
- new version 3.29.0 (with rpmrb script)

* Tue Jul 03 2018 Vitaly Lipatov <lav@altlinux.ru> 3.28.0-alt1
- new version 3.28.0 (with rpmrb script)

* Sat Jun 30 2018 Vitaly Lipatov <lav@altlinux.ru> 3.27.1-alt1
- new version 3.27.1 (with rpmrb script)

* Mon May 21 2018 Vitaly Lipatov <lav@altlinux.ru> 3.26.0-alt1
- new version 3.26.0 (with rpmrb script)

* Sat Apr 21 2018 Vitaly Lipatov <lav@altlinux.ru> 3.25.0-alt1
- new version 3.25.0 (with rpmrb script)

* Tue Mar 20 2018 Vitaly Lipatov <lav@altlinux.ru> 3.24.1-alt1
- new version 3.24.1 (with rpmrb script)

* Sat Feb 24 2018 Vitaly Lipatov <lav@altlinux.ru> 3.22.0-alt1
- new version 3.22.0 (with rpmrb script)

* Wed Feb 07 2018 Vitaly Lipatov <lav@altlinux.ru> 3.21.2-alt1
- new version 3.21.2 (with rpmrb script)

* Mon Dec 04 2017 Igor Vlasenko <viy@altlinux.ru> 3.20.0-alt1
- new version 3.20.0
- added python3 subpackage
- renamed to fonttools

* Tue Nov 07 2017 Vitaly Lipatov <lav@altlinux.ru> 3.18.0-alt1
- new version 3.18.0 (with rpmrb script)

* Sun Oct 08 2017 Vitaly Lipatov <lav@altlinux.ru> 3.15.1-alt1
- new version 3.15.1 (with rpmrb script)

* Tue Nov 17 2015 Igor Vlasenko <viy@altlinux.ru> 3.0-alt1
- new version 3.0

* Fri Aug 21 2015 Vitaly Lipatov <lav@altlinux.ru> 2.5-alt1
- new version (2.5) with rpmgs script

* Sun Aug 04 2013 Vitaly Lipatov <lav@altlinux.ru> 2.4-alt1
- new version 2.4 (with rpmrb script)

* Thu Apr 12 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 2.3-alt1.1
- Rebuild to remove redundant libpython2.7 dependency

* Wed Dec 21 2011 Igor Vlasenko <viy@altlinux.ru> 2.3-alt1
- updated to 2.3

* Thu Oct 27 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 2.2-alt1.1.1
- Rebuild with Python-2.7

* Mon Jul 27 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.2-alt1.1
- Rebuild with python 2.6

* Sun Nov 30 2008 Vitaly Lipatov <lav@altlinux.ru> 2.2-alt1
- initial build for ALT Linux Sisyphus
