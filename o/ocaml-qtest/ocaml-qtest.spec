%set_verify_elf_method textrel=relaxed
%define libname qtest
Name: ocaml-%libname
Version: 2.11.2
Release: alt1
Summary: Inline (Unit) Tests for OCaml
License: GPLv3
Group: Development/ML
Url: https://github.com/c-cube/ocaml-containers/
Source0: %name-%version.tar
BuildRequires:  dune 
BuildRequires: ocaml-qcheck-devel ocaml-ounit-devel ocaml-base-devel 

%description
qtest extracts inline unit tests written using a special syntax in comments.
Those tests are then run using the oUnit framework and the qcheck library. The
possibilities range from trivial tests -- extremely simple to use -- to
sophisticated random generation of test cases.

%package devel
Summary: Development files for %name
Group: Development/ML
Requires: %name = %EVR

%description devel
The %name-devel package contains libraries and signature files for
developing applications that use %name.

%prep
%setup

%build
%dune_build -p %libname

%install
%dune_install

%check
%dune_check

%files -f ocaml-files.runtime
%doc README.adoc HOWTO.adoc
%_bindir/qtest

%files devel -f ocaml-files.devel

%changelog
* Fri Mar 19 2021 Anton Farygin <rider@altlinux.org> 2.11.2-alt1
- 2.11.2

* Tue Sep 29 2020 Anton Farygin <rider@altlinux.ru> 2.11.1-alt1
- 2.11.1

* Tue Jun 16 2020 Anton Farygin <rider@altlinux.ru> 2.11-alt1
- 2.11

* Fri Feb 21 2020 Anton Farygin <rider@altlinux.ru> 2.10.1-alt3
- oUnit to ounit2 replace has been moved to specfile

* Mon Feb 17 2020 Anton Farygin <rider@altlinux.ru> 2.10.1-alt2
- update build requires for new ounit2 and qcheck packages

* Fri Jan 24 2020 Anton Farygin <rider@altlinux.ru> 2.10.1-alt1
- 2.10.1

* Wed Nov 07 2018 Anton Farygin <rider@altlinux.ru> 2.9-alt1
- first build for ALT


