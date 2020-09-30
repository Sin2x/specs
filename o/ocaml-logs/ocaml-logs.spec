%set_verify_elf_method textrel=relaxed
%define libname logs
Name:           ocaml-%libname
Version:        0.6.3
Release:        alt3
Summary:        Logging infrastructure for OCaml
License:        ISC
Group:          Development/ML
Url:            http://erratique.ch/software/logs
# https://github.com/dbuenzli/logs
Source: %name-%version.tar

BuildRequires: ocaml-findlib ocaml-ocamlbuild ocaml-topkg-devel ocaml >= 4.07.1 opam
BuildRequires: ocaml-fmt ocaml-lwt-devel

%package devel
Summary: Development files for programs which will use the %name
Group: Development/ML
Requires: %name = %version-%release

%description
Logs provides a logging infrastructure for OCaml. Logging is performed on sources 
whose reporting level can be set independently. Log message report is decoupled 
from logging and is handled by a reporter.

A few optional log reporters are distributed with the base library and the API 
easily allows to implement your own.

%description devel
This package includes development files necessary for developing 
programs which use %name

%prep
%setup -q

%build
sed -i 's,%%%%VERSION_NUM%%%%,%version,g' pkg/META
ocaml pkg/pkg.ml build --with-js_of_ocaml false \
                       --with-lwt true

%install
opam-installer --prefix=%buildroot%prefix --libdir=%buildroot%_libdir/ocaml

%files
%doc LICENSE.md CHANGES.md README.md
%_libdir/ocaml/%libname
%exclude %_libdir/ocaml/%libname/*.a
%exclude %_libdir/ocaml/%libname/*.cmxa
%exclude %_libdir/ocaml/%libname/*.cmx
%exclude %_libdir/ocaml/%libname/*.mli

%files devel
%_libdir/ocaml/%libname/*.a
%_libdir/ocaml/%libname/*.cmxa
%_libdir/ocaml/%libname/*.cmx
%_libdir/ocaml/%libname/*.mli

%changelog
* Wed Sep 30 2020 Anton Farygin <rider@altlinux.ru> 0.6.3-alt3
- built with lwt support

* Wed Sep 16 2020 Anton Farygin <rider@altlinux.ru> 0.6.3-alt2
- built without js_of_ocaml against cyclic dependencies

* Sat May 11 2019 Anton Farygin <rider@altlinux.ru> 0.6.3-alt1
- 0.6.3

* Wed Mar 13 2019 Anton Farygin <rider@altlinux.ru> 0.6.2-alt3
- rebuilt with js_of_ocaml

* Mon Jan 21 2019 Anton Farygin <rider@altlinux.ru> 0.6.2-alt2
- rebuild with js_of_ocaml 3.3.0

* Tue Oct 23 2018 Anton Farygin <rider@altlinux.ru> 0.6.2-alt1
- first build for ALT

