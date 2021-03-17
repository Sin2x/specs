%define ocamlmod yaml
Name: ocaml-%ocamlmod
Version: 2.1.0
Release: alt3
Summary: Parse and generate YAML 1.1 files
Group: Development/ML
License: ISC
Url: https://github.com/avsm/ocaml-yaml
Source: %name-%version.tar

BuildRequires: ocaml-dune-configurator-devel ocaml-bos-devel ocaml-ctypes-devel
BuildRequires: ocaml-ppx_sexp_conv-devel ocaml-sexplib-devel ocaml-rresult-devel
BuildRequires: ocaml-fmt-devel  ocaml-logs-devel
BuildRequires: ocaml-ppxlib-devel

%description
This is an OCaml library to parse and generate the YAML file format. It is
intended to interoperable with the Ezjsonm JSON handling library, if the simple
common subset of Yaml is used. Anchors and other advanced Yaml features are not
implemented in the JSON compatibility layer.

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
%dune_build -p %ocamlmod

%install
%dune_install

%files -f ocaml-files.runtime
%doc README.md

%files devel -f ocaml-files.devel

%changelog
* Tue Mar 16 2021 Anton Farygin <rider@altlinux.org> 2.1.0-alt3
- spec BR: ocaml-dune-devel changed to ocaml-dune-configurator-devel

* Tue Sep 29 2020 Anton Farygin <rider@altlinux.ru> 2.1.0-alt2
- cleanup build requires
- migrated to rpm-build-ocaml 1.4

* Wed Jul 08 2020 Mikhail Gordeev <obirvalger@altlinux.org> 2.1.0-alt1
- Initial build for Sisyphus
