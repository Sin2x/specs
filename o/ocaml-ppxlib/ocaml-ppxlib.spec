%define libname ppxlib

# tests fail on armh:
#( cd _build/default && /usr/bin/ocamlopt.opt -w -24 -o src/.cinaps/cinaps.exe /usr/lib/ocaml/unix.cmxa -I /usr/lib/ocaml /usr/lib/ocaml/cinaps/runtime/cinaps_runtime.cmxa /usr/lib/ocaml/re/re.cmxa src/cinaps/ppxlib_cinaps_helpers.cmxa src/.cinaps/.cinaps.eobjs/native/dune__exe__Cinaps.cmx)
# /usr/bin/ld.default: src/.cinaps/.cinaps.eobjs/native/dune__exe__Cinaps.o: relocation R_ARM_THM_MOVW_ABS_NC against `camlCinaps_runtime' can not be used when making a shared object; recompile with -fPIC
# src/.cinaps/.cinaps.eobjs/native/dune__exe__Cinaps.o: in function `.L297':
# :(.text+0xdec): dangerous relocation: unsupported relocation
# ...
# ...
# /usr/bin/ld.default: warning: creating DT_TEXTREL in a PIE
# collect2: error: ld returned 1 exit status
# File "caml_startup", line 1:
# Error: Error during linking (exit code 1)

%ifarch armh
%def_without check
%endif

Name: ocaml-%libname
Version: 0.22.0
Release: alt1
Summary: Base library and tools for ppx rewriters.
License: MIT
Group: Development/ML
Url: https://github.com/ocaml-ppx/ppxlib
Source0: %name-%version.tar
Patch0: %name-%version-%release.patch
BuildRequires: ocaml-findlib-devel dune cinaps ocaml-result-devel
BuildRequires: ocaml-re-devel ocaml-compiler-libs-devel ocaml-ppx_derivers-devel
BuildRequires: ocaml-sexplib0-devel ocaml-migrate-parsetree-devel ocaml-stdio-devel
BuildRequires: ocaml-base-devel

%description
A comprehensive toolbox for ppx development. It features:

 * a OCaml AST / parser / pretty-printer snapshot,to create a full frontend
   independent of the version of OCaml;
 * a library for library for ppx rewriters in general, and type-driven code
   generators in particular;
 * a feature-full driver for OCaml AST transformers;
 * a quotation mechanism allowing to write values representing the OCaml AST
   in the OCaml syntax;
 * a generator of open recursion classes from type definitions.

%package devel
Summary: Development files for %name
Group: Development/ML
Requires: %name = %version-%release
Requires: ocaml-result-devel

%description devel
The %name-devel package contains libraries and signature files for
developing applications that use %name.

%prep
%setup
%patch0 -p1

%build
sed -i 's/ stdlib-shims//' */dune
%dune_build -p %libname

%install
%dune_install
rm -rf %buildroot%_bindir

%check
%dune_check

%files -f ocaml-files.runtime
%doc README.md LICENSE.md CHANGES.md


%files devel -f ocaml-files.devel

%changelog
* Sat Mar 20 2021 Anton Farygin <rider@altlinux.org> 0.22.0-alt1
- 0.22.0

* Sat Dec 12 2020 Anton Farygin <rider@altlinux.ru> 0.15.0-alt2
- added upstream patch fix build with ocaml 4.11
- used macros from rpm-build-ocaml 1.4

* Wed Sep 15 2020 Anton Farygin <rider@altlinux.ru> 0.15.0-alt1
- 0.15.0
 
* Thu Sep 10 2020 Anton Farygin <rider@altlinux.ru> 0.13.0-alt3
- added ocaml-result-devel to devel package requires
- added ocaml-base-devel to buildrequires

* Thu Sep 10 2020 Anton Farygin <rider@altlinux.ru> 0.13.0-alt2
- fixed depends in devel package

* Fri Apr 24 2020 Anton Farygin <rider@altlinux.ru> 0.13.0-alt1
- 0.13.0

* Fri Feb 28 2020 Anton Farygin <rider@altlinux.ru> 0.12.0-alt2
- build for ocaml-4.10
- cleanup spec

* Wed Jan 29 2020 Anton Farygin <rider@altlinux.ru> 0.12.0-alt1
- 0.12.0

* Mon Aug 05 2019 Anton Farygin <rider@altlinux.ru> 0.9.0-alt1
- 0.9.0

* Wed Jul 31 2019 Anton Farygin <rider@altlinux.ru> 0.8.1-alt1
- 0.8.1

* Fri Jun 07 2019 Anton Farygin <rider@altlinux.ru> 0.8.0-alt1
- 0.8.0

* Wed Mar 13 2019 Anton Farygin <rider@altlinux.ru> 0.5.0-alt2
- rebuilt with ocaml-stdio-0.12.0

* Mon Jan 21 2019 Anton Farygin <rider@altlinux.ru> 0.5.0-alt1
- 0.5.0

* Tue Nov 06 2018 Anton Farygin <rider@altlinux.ru> 0.3.1-alt1
- first build for ALT


