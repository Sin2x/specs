%define ocamlmod ppx_inline_test
%set_verify_elf_method textrel=relaxed
Name: ocaml-%ocamlmod
Version: 0.14.1
Release: alt1
Summary: Syntax extension for writing in-line tests in ocaml code
Group: Development/ML
License: MIT
Url: https://github.com/janestreet/ppx_inline_test
Source: %name-%version.tar
Patch0: %name-%version-%release.patch

BuildRequires: ocaml >= 4.10
BuildRequires: ocaml-ppxlib-devel
BuildRequires: ocaml-time_now-devel
BuildRequires: ocaml-base-devel
BuildRequires: dune
BuildRequires: rpm-build-ocaml >= 1.4

%description
Syntax extension for writing in-line tests in ocaml code.
Part of the Jane Street's PPX rewriters collection.

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
%dune_build @install

%install
%dune_install

# tests is broken in upstream
#check
#dune_check

%files -f ocaml-files.runtime
%doc LICENSE.md

%files devel -f ocaml-files.devel
%doc README.md CHANGES.md

%changelog
* Fri Sep 18 2020 Anton Farygin <rider@altlinux.ru> 0.14.1-alt1
- 0.14.1
- cleanup spec
- devel parts moved from the main package

* Thu Aug 06 2020 Anton Farygin <rider@altlinux.ru> 0.14.0-alt1
- first build for ALT

