%set_verify_elf_method textrel=relaxed
%define libname gen
Name: ocaml-%libname
Version: 0.5.3
Release: alt3
Summary: Simple and efficient iterators (modules Gen and GenLabels).
License: BSD
Group: Development/ML
Url: https://github.com/c-cube/sequence/
Source0: %name-%version.tar
BuildRequires: ocaml-findlib-devel ocaml-dune-devel ocaml-result-devel
BuildRequires: ocaml-qcheck-devel ocaml-ounit-devel ocaml-odoc ocaml-qtest-devel

%description
%name provides additional modules GenClone and GenMList for lower-level control
over persistency and duplication of iterators.

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
sed -si 's,Pervasives.,Stdlib.,g' src/gen.ml
%dune_build -p %libname

%install
%dune_install

%check
# check disabled on armh due to https://github.com/ocaml/dune/issues/2527
%ifnarch armh
%dune_check
%endif

%files -f ocaml-files.runtime
%doc README.md LICENSE CHANGELOG.md


%files devel -f ocaml-files.devel

%changelog
* Thu Dec 24 2020 Anton Farygin <rider@altlinux.ru> 0.5.3-alt3
- disabled check on armh due to incompatibilty -nodynlink and PIE

* Tue Sep 29 2020 Anton Farygin <rider@altlinux.ru> 0.5.3-alt2
- enabled tests
- migrated to rpm-build-ocaml 1.4

* Tue Jun 16 2020 Anton Farygin <rider@altlinux.ru> 0.5.3-alt1
- 0.5.3

* Fri Jan 31 2020 Anton Farygin <rider@altlinux.ru> 0.5.2-alt3
- rebuilt by dune-2.x

* Sat Aug 03 2019 Anton Farygin <rider@altlinux.ru> 0.5.2-alt2
- rebuilt with ocaml-4.08

* Sat Jun 01 2019 Anton Farygin <rider@altlinux.ru> 0.5.2-alt1
- 0.5.2

* Wed Nov 07 2018 Anton Farygin <rider@altlinux.ru> 0.5.1-alt1
- first build for ALT


