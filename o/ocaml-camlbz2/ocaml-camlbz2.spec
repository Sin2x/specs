Name: ocaml-camlbz2
Version: 0.7.0
Release: alt1
Summary: OCaml bindings for the libbz2
License: LGPLv2 with OCaml-LGPL-linking-exception
Group: Development/ML
Url: http://camlbz2.forge.ocamlcore.org/
Source0: %name-%version.tar
BuildRequires: ocaml
BuildRequires: ocaml-findlib
BuildRequires: bzlib-devel

%description
CamlBZ2 provides OCaml bindings for libbz2 (AKA bzip2), a popular
compression library which typically compresses better (i.e., smaller
resulting files) than gzip.

Using CamlBZ2 you can read and write compressed "files", where
files can be anything offering an in_channel/out_channel abstraction
(files, sockets, ...).

Also, with CamlBZ2 you can compress and decompress strings in memory
using the bzip2 compression algorithm.

%package devel
Summary: Development files for %name
Group: Development/ML
Requires: %name = %EVR
Requires: bzlib-devel

%description devel
The %name-devel package contains libraries and signature files for
developing applications that use %name.

%prep
%setup

%build
%autoreconf
%configure
make

%install
export DESTDIR=%buildroot
export OCAMLFIND_DESTDIR=%buildroot/%_libdir/ocaml
export DLLDIR=$OCAMLFIND_DESTDIR/stublibs
mkdir -p $OCAMLFIND_DESTDIR/bz2
mkdir -p $DLLDIR
make install

%files
%doc BUGS COPYING ChangeLog INSTALL LICENSE README ROADMAP
%dir %_libdir/ocaml/bz2
%_libdir/ocaml/bz2/META
%_libdir/ocaml/bz2/*.cma
%_libdir/ocaml/bz2/*.cmi
%_libdir/ocaml/stublibs/*.so*

%files devel
%_libdir/ocaml/bz2/*.a
%_libdir/ocaml/bz2/*.cmxa
%_libdir/ocaml/bz2/*.cmx
%_libdir/ocaml/bz2/*.mli

%changelog
* Mon Mar 22 2021 Anton Farygin <rider@altlinux.org> 0.7.0-alt1
- 0.7.0

* Sat Mar 16 2019 Anton Farygin <rider@altlinux.ru> 0.6.0-alt1
- first build for ALT
- ported from String to Bytes to avoid problems with latest ocaml and safe-string defaults
