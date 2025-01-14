%define  modulename ppx_assert
%def_with check

Name:    ocaml-%modulename
Version: 0.15.0
Release: alt1
Summary: Assert-like extension nodes that raise useful errors on failure
License: MIT
Group:   Development/ML
URL:     https://github.com/janestreet/ppx_assert
BuildRequires: dune ocaml-ppxlib-devel ocaml-ppx_cold-devel
BuildRequires: ocaml-ppx_sexp_conv-devel ocaml-ppx_compare-devel
BuildRequires: ocaml-ppx_here-devel
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
%dune_build -p %modulename

%install
%dune_install

%check
%dune_check

%files -f ocaml-files.runtime
%doc README.md

%files devel -f ocaml-files.devel

%changelog
* Tue Jan 04 2022 Anton Farygin <rider@altlinux.ru> 0.15.0-alt1
- 0.15.0

* Wed Sep 23 2020 Anton Farygin <rider@altlinux.ru> 0.14.0-alt2
- migrated to rpm-build-ocaml 1.4
- cleaned up specfile

* Thu Jul 30 2020 Mikhail Gordeev <obirvalger@altlinux.org> 0.14.0-alt1
- Initial build for Sisyphus
