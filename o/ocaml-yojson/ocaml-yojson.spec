# ./usr/lib/ocaml/yojson/yojson.cmxs: TEXTREL entry found: 0x00000000
%set_verify_elf_method textrel=relaxed
Name: ocaml-yojson
%define libname %(sed -e 's/^ocaml-//' <<< %name)
Version: 1.7.0
Release: alt2
Summary: An optimized parsing and printing library for the JSON format
Group: Development/ML
License: BSD
Url: http://opam.ocaml.org/packages/yojson/
# https://github.com/mjambon/yojson.git
Source0: %name-%version.tar
BuildRequires: ocaml >= 4.04
BuildRequires: ocaml-findlib
BuildRequires: ocaml-ocamldoc
BuildRequires: ocaml-biniou-devel
BuildRequires: ocaml-cppo
BuildRequires: ocaml-easy-format-devel
BuildRequires: opam dune

%description
Yojson is an optimized parsing and printing library for the JSON
format. It addresses a few shortcomings of json-wheel including 2x
speedup, polymorphic variants and optional syntax for tuples and
variants.

ydump is a pretty-printing command-line program provided with the
yojson package.

The program atdgen can be used to derive OCaml-JSON serializers and
deserializers from type definitions.

%package devel
Summary: Development files for %name
Requires: %name = %version-%release
Group: Development/ML

%description devel
The %name-devel package contains libraries and signature files for
developing applications that use %name.

%prep
%setup

%build
make all

%install
dune install --destdir=%buildroot

%files
%doc LICENSE.md
%dir %_libdir/ocaml/%libname/
%_bindir/ydump
%_libdir/ocaml/%libname/META
%_libdir/ocaml/%libname/*.a
%_libdir/ocaml/%libname/*.cmi
%_libdir/ocaml/%libname/*.cma
%_libdir/ocaml/%libname/*.cmxa
%_libdir/ocaml/%libname/*.cmxs

%files devel
%doc README.md Changes examples
%_libdir/ocaml/*/dune-package
%_libdir/ocaml/*/opam
%_libdir/ocaml/*/*.cmt
%_libdir/ocaml/*/*.cmti
%_libdir/ocaml/*/*.cmx
%_libdir/ocaml/*/*.mli
%_libdir/ocaml/*/*.ml

%changelog
* Thu Jan 30 2020 Anton Farygin <rider@altlinux.ru> 1.7.0-alt2
- built with dune-2.x

* Thu Mar 14 2019 Anton Farygin <rider@altlinux.ru> 1.7.0-alt1
- 1.7.0

* Thu Oct 18 2018 Anton Farygin <rider@altlinux.ru> 1.4.1-alt3
- rebuilt with ocaml-4.07.1

* Wed Sep 05 2018 Anton Farygin <rider@altlinux.ru> 1.4.1-alt2
- rebuilt with ocaml 4.07

* Sun May 20 2018 Anton Farygin <rider@altlinux.ru> 1.4.1-alt1
- 1.4.1

* Tue Jul 11 2017 Anton Farygin <rider@altlinux.ru> 1.3.3-alt3
- rebuild with ocaml 4.04.2

* Wed May 03 2017 Anton Farygin <rider@altlinux.ru> 1.3.3-alt2
- rebuild with ocaml 4.04.1

* Fri Apr 21 2017 Anton Farygin <rider@altlinux.ru> 1.3.3-alt1
- first build for ALT, based on RH spec
