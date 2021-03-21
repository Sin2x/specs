%define  modulename ppx_variants_conv
Name:    ocaml-%modulename
Version: 0.14.1
Release: alt2

Summary: Generation of accessor and iteration functions for ocaml variant types
License: MIT
Group:   Development/ML
URL:     https://github.com/janestreet/ppx_variants_conv

BuildRequires: dune ocaml-ppxlib-devel ocaml-base-devel
BuildRequires: ocaml-variantslib-devel
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
%dune_build -p %modulename

%install
%dune_install

%check
%dune_check

%files -f ocaml-files.runtime
%doc README.md

%files devel -f ocaml-files.devel

%changelog
* Sun Mar 21 2021 Anton Farygin <rider@altlinux.org> 0.14.1-alt2
- simplified specfile with macros from rpm-build-ocaml 1.4

* Wed Sep 09 2020 Anton Farygin <rider@altlinux.ru> 0.14.1-alt1
- 0.14.1

* Wed Jul 29 2020 Mikhail Gordeev <obirvalger@altlinux.org> 0.14.0-alt1
- Initial build for Sisyphus
