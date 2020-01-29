%set_verify_elf_method textrel=relaxed
%define libname markup
%define libnamelwt %libname-lwt
Name: ocaml-%libname
Version: 0.8.2
Release: alt1
Summary: Error-recovering streaming HTML5 and XML parsers.
License: MIT
Group: Development/ML
Url: https://github.com/aantron/markup.ml
Source: %name-%version.tar
Patch0: %name-%version-%release.patch

BuildRequires: ocaml >= 4.07.1 opam dune >= 1.4.0
BuildRequires: ocaml-uutf-devel ocaml-lwt-devel ocaml-bisect_ppx-devel ocaml-migrate-parsetree-devel ocaml-result-devel

%package devel
Summary: Development files for programs which will use the %name
Group: Development/ML
Requires: %name = %EVR

%description
Markup.ml provides an HTML parser and an XML parser. The parsers are wrapped in
a simple interface: they are functions that transform byte streams to parsing signal
streams. Streams can be manipulated in various ways, such as processing by fold,
filter, and map, assembly into DOM tree structures, or serialization back to HTML or XML.

%description devel
This package includes development files necessary for developing
programs which use %name

%package lwt
Summary: Adapter between Markup.ml and Lwt
Group: Development/ML
Requires: %name = %EVR

%package lwt-devel
Summary: Development files for programs which will use the %name-lwt
Group: Development/ML
Requires: %name-lwt = %EVR
Requires: ocaml-bisect_ppx-devel

%description lwt
Adapter between Markup.ml and Lwt

%description lwt-devel
This package includes development files necessary for developing
programs which use %name-lwt

%prep
%setup
%patch0 -p1

%build
%make

%install
dune install --destdir=%buildroot

%files
%doc LICENSE.md README.md
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

%files lwt
%_libdir/ocaml/%libnamelwt
%exclude %_libdir/ocaml/%libnamelwt/*.a
%exclude %_libdir/ocaml/%libnamelwt/*.cmxa
%exclude %_libdir/ocaml/%libnamelwt/*.cmx
%exclude %_libdir/ocaml/%libnamelwt/*.mli

%files lwt-devel
%_libdir/ocaml/%libnamelwt/*.a
%_libdir/ocaml/%libnamelwt/*.cmxa
%_libdir/ocaml/%libnamelwt/*.cmx
%_libdir/ocaml/%libnamelwt/*.mli

%changelog
* Fri Jan 24 2020 Anton Farygin <rider@altlinux.ru> 0.8.2-alt1
- 0.8.2

* Thu Aug 01 2019 Anton Farygin <rider@altlinux.ru> 0.8.1-alt1
- 0.8.1

* Tue Oct 23 2018 Anton Farygin <rider@altlinux.ru> 0.8.0-alt1
- first build for ALT

