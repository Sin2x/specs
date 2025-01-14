%{?optflags_lto:%global optflags_lto %optflags_lto -ffat-lto-objects}
%define pkgname labltk

Name: ocaml-%pkgname
Version: 8.06.11
Release: alt1

Summary: Tcl/Tk interface for OCaml
Group: Development/ML

License: LGPLv2+ with exceptions

Url: https://forge.ocamlcore.org/projects/labltk/
Source: %name-%version.tar
Conflicts: labltk
Obsoletes: %name-runtime < %EVR
Provides: %name-runtime = %EVR
BuildRequires: ocaml >= 4.12
BuildRequires: tcl-devel, tk-devel

%description
Objective Caml is a high-level, strongly-typed, functional and
object-oriented programming language from the ML family of languages.

LablTk gives OCaml program access to Tcl/Tk GUI widgets. This package
contains files needed to run bytecode OCaml programs using LablTk.

%package devel
Summary: Tk toolkit bindings for OCaml
Group: Development/ML
Requires: %name = %EVR 
Conflicts: labltk-runtime

%description devel
Objective Caml is a high-level, strongly-typed, functional and
object-oriented programming language from the ML family of languages.

LablTk gives OCaml program access to Tcl/Tk GUI widgets. This package
contains files needed to develop OCaml programs using LablTk.


%package -n ocaml-ocamlbrowser
Summary: OCaml interface browser
Group: Development/ML
Requires: %name = %EVR
Conflicts: ocamlbrowser

%description -n ocaml-ocamlbrowser
Objective Caml is a high-level, strongly-typed, functional and
object-oriented programming language from the ML family of languages.

This package provides OCamlBrowser, a source and compiled interface
browser, written using LablTk.

%prep
%setup -q

%build

find -type f | xargs sed -i -e 's/-warn-error/-w/g'
export MAKE='make --no-print-directory' 
./configure --verbose 
make all SHAREDCCCOMPOPTS='%optflags -fPIC'
make opt

%install
mkdir -p %buildroot%_bindir
mkdir -p %buildroot%_libdir/ocaml/labltk
mkdir -p %buildroot%_libdir/ocaml/stublibs

make install \
    BINDIR=%buildroot%_bindir \
    INSTALLDIR=%buildroot%_libdir/ocaml/labltk \
    STUBLIBDIR=%buildroot%_libdir/ocaml/stublibs

%files devel
%doc Changes README.mlTk
%_bindir/labltk
%_libdir/ocaml/labltk
%exclude %_libdir/ocaml/labltk/*.cmi
%exclude %_libdir/ocaml/labltk/*.cma
%exclude %_libdir/ocaml/labltk/*.cmo
%exclude %_libdir/ocaml/labltk/*.cmx

%files 
%_libdir/ocaml/stublibs/dlllabltk.so
%_libdir/ocaml/labltk/*.cmi
%_libdir/ocaml/labltk/*.cma
%_libdir/ocaml/labltk/*.cmo

%files -n ocaml-ocamlbrowser
%_bindir/ocamlbrowser

%changelog
* Tue Nov 02 2021 Anton Farygin <rider@altlinux.ru> 8.06.11-alt1
- 8.06.11

* Sun Oct 03 2021 Anton Farygin <rider@altlinux.ru> 8.06.10-alt2
- fixed build with LTO

* Thu Mar 18 2021 Anton Farygin <rider@altlinux.org> 8.06.10-alt1
- 8.06.10

* Tue Oct 13 2020 Anton Farygin <rider@altlinux.ru> 8.06.9-alt1
- 8.06.9

* Tue Sep 08 2020 Anton Farygin <rider@altlinux.ru> 8.06.8-alt2
- added devel package
- runtime part have been moved to main package

* Tue Feb 25 2020 Anton Farygin <rider@altlinux.ru> 8.06.8-alt1
- 8.06.8

* Wed Jul 24 2019 Anton Farygin <rider@altlinux.ru> 8.06.6-alt1
- 8.06.6

* Thu Oct 18 2018 Anton Farygin <rider@altlinux.ru> 8.06.5-alt2
- rebuilt for ocaml 4.07.1

* Mon Aug 13 2018 Anton Farygin <rider@altlinux.ru> 8.06.5-alt1
- 8.06.5

* Mon Dec 18 2017 Anton Farygin <rider@altlinux.ru> 8.06.4-alt1
- rebuilt for ocaml 4.06.0

* Mon Jul 10 2017 Anton Farygin <rider@altlinux.ru> 8.06.2-alt3
- rebuild with ocaml 4.04.2

* Wed May 03 2017 Anton Farygin <rider@altlinux.ru> 8.06.2-alt2
- rebuild with ocaml 4.04.1

* Wed Apr 19 2017 Anton Farygin <rider@altlinux.ru> 8.06.2-alt1
- rebuild with new rpm-build-ocaml
- added ubt

* Mon Feb 27 2017 Anton Farygin <rider@altlinux.ru> 8.06.2-alt1
- build for 4.04
- renamed back to ocaml-labltk

* Sun Jun 19 2016 Andrey Bergman <vkni@altlinux.org> 8.06.1-alt1
- Version update.

* Wed Jul 01 2015 Andrey Bergman <vkni@altlinux.org> 8.06.0-alt3
- Rebuild with new rpm-build-ocaml4.

* Tue Jun 23 2015 Andrey Bergman <vkni@altlinux.org> 8.06.0-alt2
- Added conflicts with ocaml 3 versions.

* Tue Oct 28 2014 Alexey Shabalin <shaba@altlinux.ru> 8.06.0-alt1
- initial build for ocaml4
