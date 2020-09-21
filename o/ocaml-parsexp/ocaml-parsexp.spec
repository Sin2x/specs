%set_verify_elf_method textrel=relaxed
%define libname parsexp
Name: ocaml-%libname
Version: 0.14.0
Release: alt3
Summary: S-expression parsing library for ocaml
Group: Development/ML
License: Apache-2.0
Url: https://github.com/ocaml-ppx/ppx_derivers
Source0: %name-%version.tar
BuildRequires: dune >= 1.8
BuildRequires: ocaml
BuildRequires: ocaml-findlib 
BuildRequires: ocaml-sexplib0-devel >= 0.14.0
BuildRequires: ocaml-base-devel >= 0.14.0
BuildRequires: rpm-build-ocaml >= 1.4

%description
This library provides generic parsers for parsing S-expressions from strings or
other medium.

The library is focused on performances but still provide full generic parsers
that can be used with strings, bigstrings, lexing buffers, character streams or
any other sources effortlessly.

It provides three different class of parsers:

    the normal parsers, producing [Sexp.t] or [Sexp.t list] values
    
    the parsers with positions, building compact position sequences so that one
    can recover original positions in order to report properly located errors at
    little cost
    
    the Concrete Syntax Tree parsers, produce values of type [Parsexp.Cst.t]
    which record the concrete layout of the s-expression syntax, including 
    comments

%package devel
Summary: Development files for %name
Group: Development/ML
Requires: %name = %EVR
Requires: ocaml-base-devel >= 0.14.0

%description devel
The %name-devel package contains libraries and signature files for
developing applications that use %name.

%prep
%setup

%build
%dune_build -p %libname 

%install
%dune_install 
rm -rf %buildroot/usr/share/doc

%check
%dune_check

%files -f ocaml-files.runtime
%doc README.org CHANGES.md

%files devel -f ocaml-files.devel

%changelog
* Fri Sep 18 2020 Anton Farygin <rider@altlinux.ru> 0.14.0-alt3
- mirated to rpm-build-ocaml 1.4
- added ocaml-base-devel dependency to devel package

* Tue Sep 08 2020 Anton Farygin <rider@altlinux.ru> 0.14.0-alt2
- cmxa have been moved to devel package

* Wed Jun 17 2020 Anton Farygin <rider@altlinux.ru> 0.14.0-alt1
- 0.14.0

* Wed Jan 29 2020 Anton Farygin <rider@altlinux.ru> 0.13.0-alt1
- 0.13.0

* Wed Mar 13 2019 Anton Farygin <rider@altlinux.ru> 0.12.0-alt1
- 0.12.0

* Wed Oct 31 2018 Anton Farygin <rider@altlinux.ru> 0.11.0-alt1
- first build for ALT


