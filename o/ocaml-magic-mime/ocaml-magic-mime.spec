%set_verify_elf_method textrel=relaxed
%define  modulename magic-mime

Name:    ocaml-%modulename
Version: 1.1.2
Release: alt2
Summary: An OCaml library for mapping filenames to common MIME types
License: ISC
Group:   Development/ML
URL:     https://github.com/mirage/ocaml-magic-mime 
BuildRequires: dune ocaml
BuildRequires: rpm-build-ocaml >= 1.4
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
%dune_build -p %{modulename}

%install
%dune_install

%check
%dune_check

%files -f ocaml-files.runtime
%doc README.md

%files devel -f ocaml-files.devel

%changelog
* Thu Oct 15 2020 Anton Farygin <rider@altlinux.ru> 1.1.2-alt2
- migrated to rpm-build-ocaml-1.4

* Thu Sep 10 2020 Anton Farygin <rider@altlinux.ru> 1.1.2-alt1
- first build for ALT

