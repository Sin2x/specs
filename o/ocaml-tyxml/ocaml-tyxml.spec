%set_verify_elf_method textrel=relaxed
%add_ocaml_req_skip Ppx_sigs_reflected
%define libname tyxml
Name:           ocaml-%libname
Version:        4.4.0
Release:        alt2
Summary:        TyXML is a library for building statically correct HTML5 and SVG documents
License:        LGPL2.1 with exeptions
Group:          Development/ML
Url:            https://ocsigen.org/tyxml/
# https://github.com/ocsigen/tyxml
Source: %name-%version.tar
Patch0: %name-%version-%release.patch

BuildRequires: ocaml-findlib ocaml-ocamlbuild ocaml >= 4.07.1 opam dune ocaml-migrate-parsetree-devel
BuildRequires: ocaml-ocamldoc ocaml-re ocaml-ppx_tools_versioned ocaml-uutf-devel ocaml-markup-devel
BuildRequires: ocaml-re-devel ocaml-result-devel
BuildRequires(pre):rpm-build-ocaml

%package devel
Summary: Development files for programs which will use the %name
Group: Development/ML
Requires: %name = %EVR

%description
TyXML allows you to build HTML5 and SVG trees whose validity is ensured by the typechecker.
It provides a printer for said XML trees, along with a ppx syntax extension. Finally 
it also provides a functorial interface to choose your XML datastructure. 
It's part of the ocsigen project and is used in js_of_ocaml and eliom.

%description devel
This package includes development files necessary for developing 
programs which use %name

%prep
%setup
%patch0 -p1

%build
%make

%install
mkdir -p %buildroot%_libdir/ocaml/
dune install --prefix=%buildroot%prefix --libdir=%buildroot%_libdir/ocaml


%files
%doc LICENSE CHANGES.md README.md
%_libdir/ocaml/%libname
%exclude %_libdir/ocaml/%libname/*.a
%exclude %_libdir/ocaml/%libname/*.cmxa
%exclude %_libdir/ocaml/%libname/*.cmx
%exclude %_libdir/ocaml/%libname/*.mli
%_libdir/ocaml/%libname-ppx
%exclude %_libdir/ocaml/%libname/functor/*.a
%exclude %_libdir/ocaml/%libname/functor/*.cmxa
%exclude %_libdir/ocaml/%libname/functor/*.cmx
%exclude %_libdir/ocaml/%libname-ppx/*.a
%exclude %_libdir/ocaml/%libname-ppx/*.cmxa
%exclude %_libdir/ocaml/%libname-ppx/*.cmx
%exclude %_libdir/ocaml/%libname-ppx/internal/*.a
%exclude %_libdir/ocaml/%libname-ppx/internal/*.cmx
%exclude %_libdir/ocaml/%libname-ppx/internal/*.cmxa
%exclude %_libdir/ocaml/%libname-ppx/internal/*.mli
%_libdir/ocaml/%libname-jsx
%exclude %_libdir/ocaml/%libname-jsx/*.a
%exclude %_libdir/ocaml/%libname-jsx/*.cmxa
%exclude %_libdir/ocaml/%libname-jsx/*.cmx
%_libdir/ocaml/%libname-syntax
%exclude %_libdir/ocaml/%libname-syntax/*.a
%exclude %_libdir/ocaml/%libname-syntax/*.cmxa
%exclude %_libdir/ocaml/%libname-syntax/*.cmx


%files devel
%_libdir/ocaml/%libname/*.a
%_libdir/ocaml/%libname/*.cmxa
%_libdir/ocaml/%libname/*.cmx
%_libdir/ocaml/%libname/*.mli
%_libdir/ocaml/%libname/functor/*.a
%_libdir/ocaml/%libname/functor/*.cmxa
%_libdir/ocaml/%libname/functor/*.cmx
%_libdir/ocaml/%libname-ppx/*.a
%_libdir/ocaml/%libname-ppx/*.cmxa
%_libdir/ocaml/%libname-ppx/*.cmx
%_libdir/ocaml/%libname-ppx/internal/*.a
%_libdir/ocaml/%libname-ppx/internal/*.cmx
%_libdir/ocaml/%libname-ppx/internal/*.cmxa
%_libdir/ocaml/%libname-ppx/internal/*.mli
%_libdir/ocaml/%libname-jsx/*.a
%_libdir/ocaml/%libname-jsx/*.cmxa
%_libdir/ocaml/%libname-jsx/*.cmx
%_libdir/ocaml/%libname-syntax/*.a
%_libdir/ocaml/%libname-syntax/*.cmxa
%_libdir/ocaml/%libname-syntax/*.cmx

%changelog
* Tue Sep 08 2020 Anton Farygin <rider@altlinux.ru> 4.4.0-alt2
- devel parts moved to the ocaml-tyxml-devel package

* Tue Jun 30 2020 Anton Farygin <rider@altlinux.ru> 4.4.0-alt1
- 4.4.0

* Wed Jan 29 2020 Anton Farygin <rider@altlinux.ru> 4.3.0-alt3
- fix for build by dune-2

* Thu Aug 08 2019 Anton Farygin <rider@altlinux.ru> 4.3.0-alt2
- rebuilt with ocaml-re 1.9.0

* Mon Jan 21 2019 Anton Farygin <rider@altlinux.ru> 4.3.0-alt1
- 4.3.0

* Tue Oct 23 2018 Anton Farygin <rider@altlinux.ru> 4.2.0-alt1
- first build for ALT

