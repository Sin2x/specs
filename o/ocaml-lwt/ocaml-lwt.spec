# on i586: verify-elf: ERROR: ./usr/lib/ocaml/site-lib/lwt/lwt.cmxs: TEXTREL entry found: 0x00000000
%set_verify_elf_method textrel=relaxed
Name: ocaml-lwt
Version: 5.3.0
Release: alt3
Summary: OCaml lightweight thread library

Group: Development/ML
License: MIT
Url: http://ocsigen.org/lwt/
# https://github.com/ocsigen/lwt
Source: %name-%version.tar
Patch0: %name-%version-alt.patch

BuildRequires: ocaml-findlib ocaml-ocamldoc termutils ocaml-ssl ocaml-react glib2-devel libev-devel chrpath
BuildRequires: dune ocaml-cppo ocaml-bisect_ppx-devel ocaml-ocplib-endian-devel
BuildRequires: ocaml-migrate-parsetree-devel ocaml-ppx_tools_versioned-devel ocaml-result-devel
BuildRequires: ocaml-dune-devel

%description
Lwt is a lightweight thread library for Objective Caml.  This library
is part of the Ocsigen project.

%package devel
Summary: Development files for %name
Group: Development/ML
Requires: %name = %EVR
Requires: ocaml-ocplib-endian-devel

%description devel
The %name-devel package contains libraries and signature files for
developing applications that use %name.

%prep
%setup
%patch0 -p1

%build
%dune_build --release @install

%install
%dune_install

%check
%dune_check

%files -f ocaml-files.runtime
%doc CHANGES README.md

%files devel -f ocaml-files.devel
%_libdir/ocaml/lwt/unix/*.h

%changelog
* Thu Dec 10 2020 Anton Farygin <rider@altlinux.ru> 5.3.0-alt3
- build process mirgrated to rpm-build-ocaml 1.4

* Wed Jul 01 2020 Anton Farygin <rider@altlinux.ru> 5.3.0-alt2
- added ocaml-ocplib-endian-devel requires to devel package

* Sun Jun 28 2020 Anton Farygin <rider@altlinux.ru> 5.3.0-alt1
- 5.3.0

* Wed Feb 12 2020 Anton Farygin <rider@altlinux.ru> 5.1.1-alt1
- 5.1.1
- fixed License tag

* Wed Jul 31 2019 Anton Farygin <rider@altlinux.ru> 4.2.1-alt1
- 4.2.1

* Wed Mar 13 2019 Anton Farygin <rider@altlinux.ru> 4.1.0-alt4
- rebuilt with dune-1.8

* Mon Jan 21 2019 Anton Farygin <rider@altlinux.ru> 4.1.0-alt3
- rebuilt with ocaml-migrate-parsetree 1.2.0-alt1

* Thu Oct 18 2018 Anton Farygin <rider@altlinux.ru> 4.1.0-alt2
- rebuilt with ocaml-4.07.1

* Wed Sep 05 2018 Anton Farygin <rider@altlinux.ru> 4.1.0-alt1
- 4.1.0

* Fri May 18 2018 Anton Farygin <rider@altlinux.ru> 4.0.1-alt1
- 4.0.1

* Tue Jul 11 2017 Anton Farygin <rider@altlinux.ru> 2.5.2-alt4
- rebuild with ocaml 4.04.2

* Wed May 03 2017 Anton Farygin <rider@altlinux.ru> 2.5.2-alt3
- rebuild with ocaml 4.04.1

* Fri Apr 21 2017 Anton Farygin <rider@altlinux.ru> 2.5.2-alt2
- rebuild in new environment

* Mon Apr 10 2017 Anton Farygin <rider@altlinux.ru> 2.5.2-alt1
- new version from upstream git

* Wed Dec 28 2011 Alexey Shabalin <shaba@altlinux.ru> 1.1.0-alt3
- rebuild with new ocaml

* Mon Sep 08 2008 Veaceslav Grecea <slavutich@altlinux.org> 1.1.0-alt2
- darcs update

* Mon Sep 08 2008 Veaceslav Grecea <slavutich@altlinux.org> 1.1.0-alt1
- Initial build for ALT Linux

* Mon Sep  1 2008 Richard W.M. Jones <rjones@redhat.com> - 1.1.0-1
- Initial RPM release.
