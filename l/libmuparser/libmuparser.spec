Name: libmuparser
Version: 2.2.6.1
Release: alt2

Summary: a fast math parser library
License: MIT
Group: System/Libraries

Url: http://muparser.beltoforion.de/
# Source-url: https://github.com/beltoforion/muparser/archive/v%version.tar.gz
Source: %name-%version.tar
Packager: Vitaly Lipatov <lav@altlinux.ru>

# Automatically added by buildreq on Wed Mar 03 2010
BuildRequires: gcc-c++

%description
The main objective of this project is to provide a fast and easy way
of doing this. muParser is an extensible high performance math parser
library. It is based on transforming an expression into a bytecode and
precalculating constant parts of it.

%package -n %{name}2
Summary: %summary
Group: Development/Other

%description -n %{name}2
The main objective of this project is to provide a fast and easy way
of doing this. muParser is an extensible high performance math parser
library. It is based on transforming an expression into a bytecode and
precalculating constant parts of it.

%package devel
Summary: Header files for %name
Group: Development/Other
Requires: %{name}2 = %version-%release

%description devel
Header files for %name library.

%prep
%setup
sed -i 's|^\(CXXFLAGS.*\)|\1 -g|' Makefile.in

%build
%ifarch %e2k
# -std=c++03 by default as of lcc 1.23.20
%add_optflags -std=c++11
%endif
%configure --enable-shared=yes --disable-samples
%make_build

%install
%makeinstall_std

%files -n %{name}2
%doc Changes.txt License.txt
%_libdir/%{name}*.so.*

%files devel
#doc examples
%_libdir/%name.so
%_includedir/*
%_pkgconfigdir/*

%changelog
* Wed Oct 16 2019 Michael Shigorin <mike@altlinux.org> 2.2.6.1-alt2
- E2K: explicit -std=c++11

* Mon Jun 03 2019 Vitaly Lipatov <lav@altlinux.ru> 2.2.6.1-alt1
- new version 2.2.6.1 (with rpmrb script)

* Wed Mar 20 2019 Vitaly Lipatov <lav@altlinux.ru> 2.2.6-alt1
- new version (2.2.6) with rpmgs script

* Tue Jan 19 2016 Andrey Cherepanov <cas@altlinux.org> 2.2.5-alt1
- New version

* Sun Aug 04 2013 Vitaly Lipatov <lav@altlinux.ru> 2.2.3-alt1
- new version 2.2.3 (with rpmrb script)

* Thu Mar 17 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.32-alt1.qa2
- Rebuilt for debuginfo

* Thu Nov 25 2010 Igor Vlasenko <viy@altlinux.ru> 1.32-alt1.qa1
- rebuild using girar-nmu to require/provide setversion 
  by request of mithraen@

* Wed Mar 03 2010 Vitaly Lipatov <lav@altlinux.ru> 1.32-alt1
- new version 1.32
- moved to git, cleanup spec
- build without samples

* Sat Nov 15 2008 Vitaly Lipatov <lav@altlinux.ru> 1.30-alt2
- fix build with gcc 4.3
- remove post_ldconfig

* Mon Jun 23 2008 Vitaly Lipatov <lav@altlinux.ru> 1.30-alt1
- new version 1.30 (with rpmrb script)
- change license field to MIT

* Sun Feb 03 2008 Vitaly Lipatov <lav@altlinux.ru> 1.28-alt1
- new version

* Sun Sep 16 2007 Vitaly Lipatov <lav@altlinux.ru> 1.2.1-alt1
- initial build for ALT Linux Sisyphus
