%set_verify_elf_method textrel=relaxed
%define  modulename ppx_js_style

Name:    ocaml-%modulename
Version: 0.14.0
Release: alt2
Summary: Code style checker for Jane Street Packages
License: MIT
Group:   Development/ML
URL:     https://github.com/janestreet/ppx_js_style

BuildRequires: dune ocaml-octavius-devel
BuildRequires: ocaml-base-devel ocaml-ppxlib-devel 
Requires: rpm-build-ocaml >= 1.1
BuildPreReq: rpm-build-ocaml >= 1.1

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
* Thu Sep 17 2020 Anton Farygin <rider@altlinux.ru> 0.14.0-alt2
- removed rpm-build-ocaml dependency for runtime package
- migrated to rpm-build-ocaml 1.4
- cleanup build requires

* Wed Jul 29 2020 Mikhail Gordeev <obirvalger@altlinux.org> 0.14.0-alt1
- Initial build for Sisyphus
