Name: flam3
Version: 3.1.1
Release: alt2

Summary: Programs to generate and render cosmic recursive fractal flames
License: GPL-3.0-or-later
Group: Graphics
Url: https://flam3.com
Vcs: https://github.com/scottdraves/flam3

Source: %name-%version.tar
Patch1: 001-manpage_whatis_fix.patch
Patch2: 002-libxml.patch
Patch3: 003-ljpeg.patch
Patch4: 004-flam3.patch
Patch5: 005-readme.patch
Patch6: 006-icu67.patch
Patch7: 007-autoconf.patch

Requires: %name-palettes = %EVR

# Automatically added by buildreq on Mon Dec 07 2020 (-bi)
BuildRequires: libjpeg-devel libpng-devel libxml2-devel zlib-devel

%description
Flam3 renders fractal flames and manipulates their genomes.

%package devel
Summary: Development environment for building applications with %name
Group: Development/C
Requires: %name = %EVR

%description devel
This package contains the files needed to develop programs which use
the %name library.

%package palettes
Summary: The %name palettes xml file
Group: Graphics
BuildArch: noarch

%description palettes
The %name palettes xml file.

%prep
%setup
%autopatch -p1

%build
%autoreconf
%configure --enable-shared --disable-static
%make_build

%install
%makeinstall_std
%find_lang %name

%define _stripped_files_terminate_build 1
%define _unpackaged_files_terminate_build 1

%files -f %name.lang
%_libdir/lib%name.so.*
%_bindir/%name-*
%_man1dir/%{name}*.1*
%doc README.txt COPYING

%files -n %name-palettes
%_datadir/%name

%files -n %name-devel
%_includedir/*.*
%_libdir/lib%name.so
%_pkgconfigdir/%name.pc

%changelog
* Mon Dec 07 2020 Dmitry V. Levin <ldv@altlinux.org> 3.1.1-alt2
- Imported patches from Debian.
- %%configure --enable-shared --disable-static.

* Mon Dec 07 2020 Motsyo Gennadi <drool@altlinux.ru> 3.1.1-alt1
- 3.1.1

* Sat Oct 18 2014 Motsyo Gennadi <drool@altlinux.ru> 3.0.1-alt1
- 3.0.1

* Tue Dec 04 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.7.18-alt2.1
- Fixed built with libpng15

* Thu Jan 28 2010 Alexandra Panyukova <mex3@altlinux.org> 2.7.18-alt2
- palettes subpackage made noarch (repocop) (Closes: 20867)

* Wed Jul 22 2009 Alexandra Panyukova <mex3@altlinux.ru> 2.7.18-alt1
- new version

* Fri Apr 11 2008 Alexandra Panyukova <mex3@altlinux.ru> 2.7.11-alt1
- new version

* Fri Jan 5 2008 Alexandra Panyukova <mex3@altlinux.ru> 2.7.7-alt1
- 2.7.7
- added %name-devel package
- added %name-devel-static package
- added %name-palettes package

* Wed Apr 11 2007 Alexandra Panyukova <mex3@altlinux.ru> 2.7.2-alt1
- Initial build
