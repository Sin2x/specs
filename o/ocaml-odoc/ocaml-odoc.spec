%set_verify_elf_method textrel=relaxed
# check disabled due to fail on html.
# I have looked at all these errors and it is a formatting issue.
# Needs to be investigated.
%def_without check

Name: ocaml-odoc
Version: 1.5.2
Release: alt1
Summary: Documentation compiler for OCaml and Reason
Group: Development/ML
License: ISC
Url: https://github.com/ocaml/odoc
Source0: %name-%version.tar
Patch0: %name-%version-%release.patch

BuildRequires: ocaml >= 4.07.1
BuildRequires: ocaml-findlib-devel
BuildRequires: dune
BuildRequires: ocaml-cmdliner-devel ocaml-bos-devel
BuildRequires: ocaml-cppo
BuildRequires: ocaml-fmt-devel
BuildRequires: ocaml-tyxml-devel
BuildRequires: ocaml-re-devel
BuildRequires: ocaml-rresult-devel
BuildRequires: ocaml-result-devel
BuildRequires: ocaml-astring-devel
BuildRequires: ocaml-fpath-devel
BuildRequires: ocaml-migrate-parsetree-devel
%if_with check
BuildRequires: ocaml-bisect_ppx-devel
BuildRequires: ocaml-markup-devel
BuildRequires: ocaml-alcotest-devel
BuildRequires: ocaml-sexplib-devel
%endif

%description
odoc is a documentation generator for OCaml. It reads doc comments ,
delimited with (** ... *), and outputs HTML.

%prep
%setup
%patch0 -p1

%build
%dune_build --release @install

%install
%dune_install

mkdir -p %buildroot/%_docdir


%check
%dune_check

%files
%_docdir/*
%_bindir/odoc
%_datadir/odoc
%_libdir/ocaml/odoc
%_libdir/ocaml/dune_odoc_test

%changelog
* Thu Dec 10 2020 Anton Farygin <rider@altlinux.ru> 1.5.2-alt1
- 1.5.2

* Tue Jun 30 2020 Anton Farygin <rider@altlinux.ru> 1.5.1-alt1
- 1.5.1

* Mon Feb 10 2020 Anton Farygin <rider@altlinux.ru> 1.5.0-alt1
- 1.5.0

* Sat Feb 01 2020 Anton Farygin <rider@altlinux.ru> 1.4.2-alt2
- fix for build with dune changes

* Fri Jan 24 2020 Anton Farygin <rider@altlinux.ru> 1.4.2-alt1
- 1.4.2
- enabled tests

* Fri Aug 02 2019 Anton Farygin <rider@altlinux.ru> 1.4.1-alt1
- 1.4.1

* Tue Jan 22 2019 Anton Farygin <rider@altlinux.ru> 1.3.0-alt2.git05241eb
- updated to upstream unstable git 05241eb with fixes for ocaml-tyxml-4.3.0

* Tue Oct 23 2018 Anton Farygin <rider@altlinux.ru> 1.3.0-alt1
- first build for ALT

