%set_verify_elf_method textrel=relaxed
%define  modulename fieldslib

Name:    ocaml-%modulename
Version: 0.14.0
Release: alt2

Summary: OCaml record fields as first class values
License: MIT
Group:   Development/ML
URL:     https://github.com/janestreet/fieldslib

Packager: Mikhail Gordeev <obirvalger@altlinux.org>

BuildRequires: dune ocaml-base-devel
Requires: rpm-build-ocaml >= 1.1
BuildPreReq: rpm-build-ocaml >= 1.4
Source:  %modulename-%version.tar

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
%setup -n %modulename-%version

%build
%dune_build --release @install

%install
%dune_install

%check
%dune_check

%files -f ocaml-files.runtime

%files devel -f ocaml-files.devel

%changelog
* Sat Sep 12 2020 Anton Farygin <rider@altlinux.ru> 0.14.0-alt2
- built with rpm-build-ocaml-1.4 to resolve requirements in cohttp devel package

* Thu Jul 30 2020 Mikhail Gordeev <obirvalger@altlinux.org> 0.14.0-alt1
- Initial build for Sisyphus
