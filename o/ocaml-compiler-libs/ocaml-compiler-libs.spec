%set_verify_elf_method textrel=relaxed
%define libname ocaml-compiler-libs
Name: %libname
Version: 0.12.3
Release: alt1
Summary: OCaml compiler libraries repackaged
License: Apache-2.0
Group: Development/ML
Url: https://github.com/janestreet/ocaml-compiler-libs
Source0: %name-%version.tar
BuildRequires: ocaml-findlib-devel dune 

%description
This packages exposes the OCaml compiler libraries repackages under the toplevel
names Ocaml_common, Ocaml_bytecomp, ...

%package devel
Summary: Development files for %name
Group: Development/ML
Requires: %name = %version-%release

%description devel
The %name-devel package contains libraries and signature files for
developing applications that use %name.

%prep
%setup

%build
%dune_build -p %libname

%install
%dune_install

%files -f ocaml-files.runtime
%doc README.org

%files devel -f ocaml-files.devel

%changelog
* Mon Sep 28 2020 Anton Farygin <rider@altlinux.ru> 0.12.3-alt1
- 0.12.3

* Thu Sep 10 2020 Anton Farygin <rider@altlinux.ru> 0.12.1-alt2
- built using --release option

* Wed Feb 26 2020 Anton Farygin <rider@altlinux.ru> 0.12.1-alt1
- 0.12.1

* Wed Jul 31 2019 Anton Farygin <rider@altlinux.ru> 0.12.0-alt1
- 0.12.0

* Wed Mar 13 2019 Anton Farygin <rider@altlinux.ru> 0.11.0-alt2
- rebuilt with dune-1.8 

* Tue Nov 06 2018 Anton Farygin <rider@altlinux.ru> 0.11.0-alt1
- first build for ALT


