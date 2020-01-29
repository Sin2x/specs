%set_verify_elf_method textrel=relaxed
Name: cinaps
Version: 0.13.0
Release: alt1
Summary: Trivial metaprogramming tool.
License: Apache-2.0
Group: Development/ML
Url: https://github.com/ocaml-ppx/ppxlib
Source0: %name-%version.tar
BuildRequires: ocaml-findlib-devel dune opam  ocaml-re-devel

%description
Cinaps is a trivial Metaprogramming tool using the OCaml toplevel. It is based
on the same idea as expectation tests. The user write some OCaml code inside
special comments and cinaps make sure that what follows is what is printed by
the OCaml code.

%prep
%setup

%build
make

%install
dune install --prefix=%buildroot%prefix --libdir=%buildroot%_libdir/ocaml

%files
%doc README.org
%dir %_libdir/ocaml/%name
%_bindir/cinaps
%_libdir/ocaml/%name/META
%_libdir/ocaml/%name/dune-package
%_libdir/ocaml/%name/opam
%_libdir/ocaml/%name/runtime

%changelog
* Wed Jan 29 2020 Anton Farygin <rider@altlinux.ru> 0.13.0-alt1
- 0.13.0

* Mon Jul 01 2019 Anton Farygin <rider@altlinux.ru> 0.12.0-alt1
- 0.12.0

* Tue Nov 06 2018 Anton Farygin <rider@altlinux.ru> 0.11.0-alt1
- first build for ALT
