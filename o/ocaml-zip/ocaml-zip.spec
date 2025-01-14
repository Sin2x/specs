%define pkgname zip
Name: ocaml-%pkgname
Version: 1.11
Release: alt1
Summary: OCaml library for reading and writing zip, jar and gzip files

Group: Development/ML
License: LGPLv2.1+ with OCaml-LGPL-linking-exception
Url: https://github.com/xavierleroy/camlzip

Provides: ocaml4-zip
Obsoletes: ocaml4-zip

Source: %name-%version.tar

BuildRequires: ocaml zlib-devel ocaml-findlib

%description
This Objective Caml library provides easy access to compressed files
in ZIP and GZIP format, as well as to Java JAR files. It provides
functions for reading from and writing to compressed files in these
formats.

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
%make_build all
%make_build allopt

cat > META <<EOF
name = "%name"
version = "%version"
requires = "unix"
description = "%description"
archive(byte) = "zip.cma"
archive(native) = "zip.cmxa"
EOF

%install
mkdir -p %buildroot%_libdir/ocaml/%pkgname
mkdir -p %buildroot%_libdir/ocaml/stublibs

export DESTDIR=%buildroot
export OCAMLFIND_DESTDIR=%buildroot%_libdir/ocaml

ocamlfind install %pkgname *.cma *.cmxa *.a *.cmx *.cmi *.mli dll*.so META

%files
%_libdir/ocaml/%pkgname
%_libdir/ocaml/stublibs/*.so
%_libdir/ocaml/stublibs/*.so.owner
%exclude %_libdir/ocaml/%pkgname/*.a
%exclude %_libdir/ocaml/%pkgname/*.cmxa
%exclude %_libdir/ocaml/%pkgname/*.cmx
%exclude %_libdir/ocaml/%pkgname/*.mli

%files devel
%_libdir/ocaml/%pkgname/*.a
%_libdir/ocaml/%pkgname/*.cmxa
%_libdir/ocaml/%pkgname/*.cmx
%_libdir/ocaml/%pkgname/*.mli

%changelog
* Wed Oct 06 2021 Anton Farygin <rider@altlinux.ru> 1.11-alt1
- 1.11

* Tue Feb 25 2020 Anton Farygin <rider@altlinux.ru> 1.10-alt1
- 1.10

* Wed Jul 31 2019 Anton Farygin <rider@altlinux.ru> 1.08-alt1
- 1.08

* Thu Oct 18 2018 Anton Farygin <rider@altlinux.ru> 1.07-alt7
- rebuilt with ocaml-4.07.1

* Tue Sep 04 2018 Anton Farygin <rider@altlinux.ru> 1.07-alt6
- rebuilt with ocaml-4.07

* Tue May 15 2018 Anton Farygin <rider@altlinux.ru> 1.07-alt5
- rebuilt for ocaml 4.06.1

* Mon Jul 10 2017 Anton Farygin <rider@altlinux.ru> 1.07-alt4
- rebuild with ocaml 4.04.2

* Wed May 03 2017 Anton Farygin <rider@altlinux.ru> 1.07-alt3
- rebuild with ocaml 4.04.1

* Wed Apr 19 2017 Anton Farygin <rider@altlinux.ru> 1.07-alt2
- rebuild with new rpm-build-ocaml
- moved outsite from site-lib dir
- split to runtime and devel packages
- fixed double requires in META

* Tue Mar 28 2017 Anton Farygin <rider@altlinux.ru> 1.07-alt1
- new version

* Wed Jun 22 2016 Andrey Bergman <vkni@altlinux.org> 1.06-alt1
- Update to version 1.06.

* Mon Jun 17 2013 Andrey Bergman <vkni@altlinux.org> 1.05-alt2
- Corrected packager field.

* Mon Jun 17 2013 Andrey Bergman <vkni@altlinux.org> 1.05-alt1
- Update to version 1.05. Built with ocaml4.

* Wed Jan 11 2012 Alexey Shabalin <shaba@altlinux.ru> 1.04-alt1
- 1.04

* Wed Sep 17 2008 Veaceslav Grecea <slavutich@altlinux.org> 1.03-alt1
- Initial build for ALTLinux

* Fri Feb 22 2008 Richard W.M. Jones <rjones@redhat.com> - 1.03-1
- Initial RPM release.
