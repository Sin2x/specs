%define  modulename cstruct

# TODO: async
%define opamodules cstruct,cstruct-unix,cstruct-lwt,cstruct-sexp
Name:    ocaml-%modulename
Version: 6.0.0
Release: alt1
Summary: access C-like structures directly from OCaml
License: ISC
Group:   Development/ML
URL:     https://github.com/mirage/ocaml-cstruct
Source:  %name-%version.tar
Patch0:   %name-%version-%release.patch
BuildRequires: dune
BuildRequires: ocaml-bigarray-compat-devel
BuildRequires: ocaml-fmt-devel
BuildRequires: ocaml-lwt-devel
BuildRequires: ocaml-sexplib-devel
BuildRequires: ocaml-alcotest-devel
BuildRequires: ocaml-migrate-parsetree-devel
BuildRequires: ocaml-cppo
BuildRequires: ocaml-alcotest-devel
BuildPreReq: rpm-build-ocaml >= 1.1

%description
Cstruct is a library and syntax extension to make it easier to access C-like
structures directly from OCaml.  It supports both reading and writing to these
structures, and they are accessed via the `Bigarray` module.

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
%dune_build -p %opamodules

%install
%dune_install `echo "%opamodules"|tr ',' ' '` 

%check
%dune_check -p %opamodules

%files -f ocaml-files.runtime
%doc README.md
%_libdir/ocaml/%{modulename}/*.js

%files devel -f ocaml-files.devel

%changelog
* Fri Mar 26 2021 Anton Farygin <rider@altlinux.org> 6.0.0-alt1
- 6.0.0

* Sat Mar 20 2021 Anton Farygin <rider@altlinux.org> 5.3.0-alt2
- removed ppx submodule

* Thu Sep 10 2020 Anton Farygin <rider@altlinux.ru> 5.3.0-alt1
- first build for ALT
