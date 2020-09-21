%set_verify_elf_method textrel=relaxed
%define libname alcotest
Name: ocaml-%libname
Version: 1.2.3
Release: alt1
Summary: Alcotest is a lightweight and colourful test framework.
Group: Development/ML
License: ISC
Url: https://github.com/mirage/alcotest
Source0: %name-%version.tar
Patch0: %name-%version-%release.patch
BuildRequires: dune >= 1.8
BuildRequires: ocaml
BuildRequires: ocaml-uutf-devel
BuildRequires: ocaml-cmdliner-devel
BuildRequires: ocaml-re-devel
BuildRequires: ocaml-astring-devel
BuildRequires: ocaml-uuidm-devel
BuildRequires: ocaml-fmt-devel
BuildRequires: libev-devel

%description
Alcotest exposes simple interface to perform unit tests. It exposes a simple
TESTABLE module type, a check function to assert test predicates and a run
function to perform a list of unit -> unit test callbacks.

Alcotest provides a quiet and colorful output where only faulty runs are fully
displayed at the end of the run (with the full logs ready to inspect), with a
simple (yet expressive) query language to select the tests to run.

%package devel
Summary: Development files for %name
Group: Development/ML
Requires: %name = %EVR

%description devel
The %name-devel package contains libraries and signature files for
developing applications that use %name.

%prep
%setup
%patch0 -p1

%build
%dune_build -p %libname

%install
%dune_install %libname
rm -rf %buildroot/usr/doc


%check
%dune_check -p %libname

%files -f ocaml-files.runtime
%doc README.md

%files devel -f ocaml-files.devel

%changelog
* Mon Sep 21 2020 Anton Farygin <rider@altlinux.ru> 1.2.3-alt1
- 1.2.3
- cleaned up build requires

* Thu Sep 10 2020 Anton Farygin <rider@altlinux.ru> 1.2.2-alt2
- FTBFS: added ocaml-uutf-devel to BuildRequires

* Wed Sep 02 2020 Anton Farygin <rider@altlinux.ru> 1.2.2-alt1
- 1.2.2

* Wed Aug 26 2020 Anton Farygin <rider@altlinux.ru> 1.2.1-alt1
- 1.2.1

* Tue Apr 14 2020 Anton Farygin <rider@altlinux.ru> 1.1.0-alt1
- 1.1.0

* Thu Feb 13 2020 Anton Farygin <rider@altlinux.ru> 1.0.1-alt1
- 1.0.1

* Fri Jan 24 2020 Anton Farygin <rider@altlinux.ru> 1.0.0-alt1
- 1.0.0

* Wed Jul 31 2019 Anton Farygin <rider@altlinux.ru> 0.8.5-alt3
- rebuilt with ocaml-4.08

* Wed Mar 13 2019 Anton Farygin <rider@altlinux.ru> 0.8.5-alt2
- rebuilt with dune-1.8

* Tue Jan 22 2019 Anton Farygin <rider@altlinux.ru> 0.8.5-alt1
- 0.8.5

* Tue Nov 06 2018 Anton Farygin <rider@altlinux.ru> 0.8.4-alt1
- first build for ALT

