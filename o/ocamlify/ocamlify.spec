Name: ocamlify
Version: 0.0.2
Release: alt3
Summary: Include files in OCaml code
License: LGPL with static compilation exception
Group: Development/ML
Url: http://ocamlify.forge.ocamlcore.org/
# https://github.com/gildor478/ocamlify
Source0: %name-%version.tar
Patch0: ocamlify-0.0.2-oasis-0.4.11.patch
BuildRequires: ocaml-findlib
BuildRequires: ocaml-ocamlbuild, ocaml-ocamlbuild-devel
Requires: ocaml

%description
OCamlify allows to create OCaml source code by including whole files into
OCaml string or string list. The code generated can be compiled as a
standard OCaml file. It allows embedding external resources as OCaml code.

%prep
%setup
%patch0 -p1


%build
ocaml setup.ml -configure --prefix %buildroot/usr
ocaml setup.ml -build

%install
mkdir -p %buildroot/usr
ocaml setup.ml -install

%files
%doc AUTHORS.txt COPYING.txt INSTALL.txt README.txt
%_bindir/ocamlify

%changelog
* Tue Feb 25 2020 Anton Farygin <rider@altlinux.ru> 0.0.2-alt3
- updated setup.ml by oasis 0.4.11

* Wed Jul 31 2019 Anton Farygin <rider@altlinux.ru> 0.0.2-alt2
- rebuilt with ocaml-4.08

* Wed Oct 31 2018 Anton Farygin <rider@altlinux.ru> 0.0.2-alt1
- first build for ALT with patches from Mageia

