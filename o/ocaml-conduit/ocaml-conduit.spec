%set_verify_elf_method textrel=relaxed
%define  modulename conduit

Name:    ocaml-%modulename
Version: 2.2.2
Release: alt1
Summary: An OCaml network connection establishment library
License: ISC
Group:   Development/ML
URL:     https://github.com/mirage/ocaml-conduit
Source:  %name-%version.tar
Patch0:   %name-%version-%release.patch
BuildRequires: dune
BuildRequires: ocaml-logs-devel
BuildRequires: ocaml-uri-devel
BuildRequires: ocaml-lwt-devel
BuildRequires: ocaml-base-devel
BuildRequires: ocaml-sexplib-devel
BuildRequires: ocaml-astring-devel
BuildRequires: ocaml-ppx_sexp_conv-devel
BuildRequires: ocaml-ipaddr-devel
BuildPreReq: rpm-build-ocaml >= 1.4

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
%patch0 -p1

%build
%dune_build -p %modulename,%modulename-lwt,%modulename-lwt-unix

%install
%dune_install %modulename %modulename-lwt %modulename-lwt-unix

# tests disabled due to the need for packages from mirageOS
#check
#dune_check

%files -f ocaml-files.runtime
%doc README.md LICENSE.md CHANGES.md

%files devel -f ocaml-files.devel

%changelog
* Fri Sep 11 2020 Anton Farygin <rider@altlinux.ru> 2.2.2-alt1
- first build for ALT
