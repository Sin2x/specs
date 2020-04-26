Name: ktoblzcheck
Version: 1.53
Release: alt1

Summary: A library to check account numbers and bank codes of German banks

Packager: Andrey Cherepanov <cas@altlinux.org>

License: LGPL v2+
Group: System/Libraries
Url: http://ktoblzcheck.sourceforge.net/

Source: http://prdownloads.sf.net/ktoblzcheck/%name-%version.tar.gz
Source1: %name.watch

BuildRequires(pre): cmake
BuildRequires: gcc-c++
BuildRequires: libstdc++-devel
BuildRequires: lynx
BuildRequires: python-devel
BuildRequires: python-modules-encodings
BuildRequires: recode

%description
KtoBLZCheck is a library to check account numbers and bank codes of
German banks.

Both a library for other programs as well as a short command-line tool
is available. It is possible to check pairs of account numbers and
bank codes (BLZ) of German banks, and to map bank codes (BLZ) to the
clear-text name and location of the bank.

%package devel
Summary: Header files for KtoBLZCheck library
Group: Development/Other
Requires: %name = %version-%release

%description devel
Header files for KtoBLZCheck library.

%package -n python-module-ktoblzcheck
Summary: Python binding for KtoBLZCheck library
Group: Development/Python
Requires: %name = %version-%release

%description -n python-module-ktoblzcheck
Python binding for KtoBLZCheck library.

%prep
%setup -q

%build
%cmake
%cmake_build

%install
%cmakeinstall_std

%files
%doc AUTHORS ChangeLog NEWS README.md
%_bindir/ktoblzcheck
%_bindir/ibanchk
%_libdir/libktoblzcheck.so.*
%dir %_datadir/%name/
%_datadir/%name/*.txt
%_man1dir/ktoblzcheck.1*
%_man1dir/ibanchk.1*

%files devel
%_libdir/libktoblzcheck.so
%_includedir/*.h
%_libdir/cmake/*
%_pkgconfigdir/ktoblzcheck.pc

%files -n python-module-ktoblzcheck
%python_sitelibdir/%name.*

%changelog
* Sun Apr 26 2020 Andrey Cherepanov <cas@altlinux.org> 1.53-alt1
- new version 1.53

* Mon Feb 03 2020 Andrey Cherepanov <cas@altlinux.org> 1.52-alt1
- new version 1.52
- package ibanchk

* Thu Oct 10 2019 Andrey Cherepanov <cas@altlinux.org> 1.50-alt1
- new version 1.50
- use cmake for build

* Sat Mar 04 2017 Andrey Cherepanov <cas@altlinux.org> 1.49-alt1
- new version 1.49

* Sat Apr 11 2015 Andrey Cherepanov <cas@altlinux.org> 1.48-alt1
- new version 1.48

* Mon Jul 29 2013 Andrey Cherepanov <cas@altlinux.org> 1.42-alt1
- New version 1.42

* Wed Nov 28 2012 Andrey Cherepanov <cas@altlinux.org> 1.40-alt1
- new version 1.40

* Fri Jan 20 2012 Andrey Cherepanov <cas@altlinux.org> 1.37-alt1
- New version 1.37
- Add watch file
- Remove standard library path from RPATH

* Tue Sep 06 2011 Andrey Cherepanov <cas@altlinux.org> 1.34-alt1
- New version 1.34

* Tue Nov 09 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.27-alt1.1
- Rebuilt for soname set-versions

* Wed Jun 16 2010 Andrey Cherepanov <cas@altlinux.org> 1.27-alt1
- New version (1.27)

* Thu Nov 26 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.18-alt1.qa1.1
- Rebuilt with python 2.6

* Tue Nov 24 2009 Repocop Q. A. Robot <repocop@altlinux.org> 1.18-alt1.qa1
- NMU (by repocop): the following fixes applied:
  * post_ldconfig for ktoblzcheck
  * postun_ldconfig for ktoblzcheck
  * postclean-05-filetriggers for spec file

* Sat Jul 26 2008 Vitaly Lipatov <lav@altlinux.ru> 1.18-alt1
- new version 1.18 (with rpmrb script)
- cleanup spec

* Sun May 04 2008 Vitaly Lipatov <lav@altlinux.ru> 1.17-alt1
- new version 1.17 (with rpmrb script)

* Mon Nov 20 2006 Vitaly Lipatov <lav@altlinux.ru> 1.11-alt0.1
- new version 1.11 (with rpmrb script)

* Sun May 28 2006 Vitaly Lipatov <lav@altlinux.ru> 1.10-alt0.1
- new version 1.10 (with rpmrb script)

* Sun Dec 18 2005 Vitaly Lipatov <lav@altlinux.ru> 1.8-alt0.1
- initial build for ALT Linux Sisyphus (spec from PLD)

