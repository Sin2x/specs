%define  modulename domain-name
Name:    ocaml-%modulename
Version: 0.3.0
Release: alt2
Summary: An OCaml library for RFC 1035 Internet domain names
License: ISC
Group:   Development/ML
URL:     https://opam.ocaml.org/packages/domain-name/
BuildRequires: dune
BuildRequires: ocaml-astring-devel
BuildRequires: ocaml-fmt-devel
BuildRequires: ocaml-alcotest-devel
BuildPreReq: rpm-build-ocaml >= 1.1
Source:  %name-%version.tar

%description
%summary

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
%dune_build -p %modulename

%install
%dune_install

%check
%dune_check

%files -f ocaml-files.runtime
%doc README.md

%files devel -f ocaml-files.devel

%changelog
* Tue Apr 20 2021 Anton Farygin <rider@altlinux.ru> 0.3.0-alt2
- migrated to rpm-build-ocaml 1.4

* Thu Sep 10 2020 Anton Farygin <rider@altlinux.ru> 0.3.0-alt1
- first build for ALT

