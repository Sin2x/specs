%set_verify_elf_method textrel=relaxed
Name: dune
Version: 2.1.3
Release: alt1
Summary: A composable build system for OCaml
Group: Development/ML
License: MIT
Url: https://github.com/ocaml/dune
Source0: %name-%version-%release.tar
Provides: ocaml-dune = %EVR

BuildRequires: ocaml >= 4.08.0
BuildRequires: ocaml-findlib-devel
BuildRequires: opam

# Required by tests.
BuildRequires: ocaml-menhir

%description
Dune is a build system designed for OCaml/Reason projects only. It focuses
on providing the user with a consistent experience and takes care of most of
the low-level details of OCaml compilation. All you have to do is provide a
description of your project and Dune will do the rest.

The scheme it implements is inspired from the one used inside Jane Street and
adapted to the open source world. It has matured over a long time and is used
daily by hundred of developers, which means that it is highly tested and
productive.

%package -n ocaml-dune-devel
Group: Development/ML
Summary: Development files for %name
%description -n ocaml-dune-devel
Dune is a build system designed for OCaml/Reason projects only. It focuses
on providing the user with a consistent experience and takes care of most of
the low-level details of OCaml compilation. All you have to do is provide a
description of your project and Dune will do the rest.


%prep
%setup -n %name-%version-%release

%build
./configure --libdir=%_libdir/ocaml
%make_build release VERSION=%version-%release
./dune.exe build @install

%install
./dune.exe install --destdir=%buildroot --mandir=%_mandir

%files
%doc README.md CHANGES.md
%_bindir/dune
%_man1dir/dune.1*
%_man1dir/dune-help.1*
%_man1dir/dune-printenv.1*
%_man1dir/dune-promote.1*
%_man1dir/dune-build.1*
%_man1dir/dune-cache.1*
%_man1dir/dune-clean.1*
%_man1dir/dune-compute.1.xz
%_man1dir/dune-format-dune-file.1.xz
%_man1dir/dune-upgrade.1.xz
%_man1dir/dune-exec.1*
%_man1dir/dune-external-lib-deps.1*
%_man1dir/dune-install.1*
%_man1dir/dune-init.1*
%_man1dir/dune-installed-libraries.1*
%_man1dir/dune-rules.1*
%_man1dir/dune-runtest.1*
%_man1dir/dune-subst.1*
%_man1dir/dune-uninstall.1*
%_man1dir/dune-utop.1*
%_man5dir/dune-config.5*
%_man1dir/dune-compute.1.xz
%_man1dir/dune-format-dune-file.1.xz
%_man1dir/dune-upgrade.1.xz
%dir %_libdir/ocaml/dune/
%dir %_libdir/ocaml/dune-action-plugin/
%dir %_libdir/ocaml/dune-build-info/
%dir %_libdir/ocaml/dune-configurator/
%dir %_libdir/ocaml/dune-glob/
%dir %_libdir/ocaml/dune-private-libs/
%dir %_libdir/ocaml/dune-private-libs/dune-lang/
%dir %_libdir/ocaml/dune-private-libs/dune_re/
%dir %_libdir/ocaml/dune-private-libs/ocaml-config/
%dir %_libdir/ocaml/dune-private-libs/stdune/
%_libdir/ocaml/dune*/META
%_libdir/ocaml/dune*/*.cma
%_libdir/ocaml/dune*/*.cmi
%_libdir/ocaml/dune-private-libs/*/*.cma
%_libdir/ocaml/dune-private-libs/*/*.cmi
%_libdir/ocaml/dune*/*.cmxs
%_libdir/ocaml/dune-private-libs/*/*.cmxs
%_libdir/ocaml/stublibs/dllstdune_stubs.so

%files -n ocaml-dune-devel
%_libdir/ocaml/dune*/dune-package
%_libdir/ocaml/dune*/opam
%_libdir/ocaml/dune*/*.cmt
%_libdir/ocaml/dune*/*.cmti
%_libdir/ocaml/dune*/*.ml
%_libdir/ocaml/dune*/*.mli
%_libdir/ocaml/dune-private-libs/*/*.cmt
%_libdir/ocaml/dune-private-libs/*/*.cmti
%_libdir/ocaml/dune-private-libs/*/*.ml
%_libdir/ocaml/dune-private-libs/*/*.mli
%_libdir/ocaml/dune*/*.a
%_libdir/ocaml/dune*/*.cmx
%_libdir/ocaml/dune*/*.cmxa
%_libdir/ocaml/dune-private-libs/*/*.a
%_libdir/ocaml/dune-private-libs/*/*.cmx
%_libdir/ocaml/dune-private-libs/*/*.cmxa



%changelog
* Fri Jan 24 2020 Anton Farygin <rider@altlinux.ru> 2.1.3-alt1
- 2.1.3

* Thu Jan 09 2020 Anton Farygin <rider@altlinux.ru> 2.1.2-alt1
- 2.1.2
- added devel package

* Thu Oct 17 2019 Anton Farygin <rider@altlinux.ru> 1.11.4-alt1
- 1.11.4

* Tue Sep 03 2019 Anton Farygin <rider@altlinux.ru> 1.11.3-alt1
- 1.11.3

* Wed Jul 24 2019 Anton Farygin <rider@altlinux.ru> 1.11.0-alt1
- 1.11.0

* Wed Jun 05 2019 Anton Farygin <rider@altlinux.ru> 1.10.0-alt1
- 1.10.0

* Sat May 11 2019 Anton Farygin <rider@altlinux.ru> 1.9.3-alt1
- 1.9.3

* Tue Apr 16 2019 Anton Farygin <rider@altlinux.ru> 1.9.1-alt1
- 1.9.1

* Wed Mar 13 2019 Anton Farygin <rider@altlinux.ru> 1.8.2-alt1
- 1.8.2

* Sun Jan 20 2019 Anton Farygin <rider@altlinux.ru> 1.6.3-alt1
- 1.6.3

* Fri Dec 28 2018 Anton Farygin <rider@altlinux.ru> 1.6.2-alt1
- 1.6.2

* Fri Oct 26 2018 Anton Farygin <rider@altlinux.ru> 1.4.0-alt1
- 1.4.0

* Thu Oct 18 2018 Anton Farygin <rider@altlinux.ru> 1.1.1-alt2
- rebuilt for ocaml-4.07.1

* Sat Aug 11 2018 Anton Farygin <rider@altlinux.ru> 1.1.1-alt1
- 1.1.1

* Wed May 16 2018 Anton Farygin <rider@altlinux.ru> 1.0-alt2.beta20
- update to beta20

* Tue Dec 19 2017 Anton Farygin <rider@altlinux.ru> 1.0-alt1.git4570020
- first build for ALT, based on RH spec


