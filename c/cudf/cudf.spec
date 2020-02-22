%set_verify_elf_method textrel=relaxed

Summary: CUDF (Common Upgradeability Description Format) tools and libraries
Name: cudf
Version: 0.9
Release: alt7
# https://scm.gforge.inria.fr/anonscm/git/cudf/cudf.git
Source: %name-%version.tar
Url: http://www.mancoosi.org/cudf/
License: LGPLv3
Group: Development/ML
BuildRequires: ocaml ocaml-findlib ocaml-extlib-devel perl-podlators ocaml-ocamlbuild libncurses-devel glib2-devel ocaml-ounit

%description
CUDF (for Common Upgradeability Description Format) is a format for describing
upgrade scenarios in package-based Free and Open Source Software distribution.

libCUDF is a library to manipulate so called CUDF documents. A CUDF document
describe an upgrade problem, as faced by package managers in popular
package-based GNU/Linux distributions.

%package tools
Summary: CUDF (Common Upgradeability Description Format) command-line tools
Group: System/Configuration/Packaging

%description tools
CUDF (for Common Upgradeability Description Format) is a format for describing
upgrade scenarios in package-based Free and Open Source Software distribution.

libCUDF is a library to manipulate so called CUDF documents. A CUDF document
describe an upgrade problem, as faced by package managers in popular
package-based GNU/Linux distributions.

This package contains command line tools to manipulate CUDF and related
documents. In particular it contains cudf-check, which enables checking of
document properties such as installation consistency and matching of problems
with their solutions.

%package devel
Summary: CUDF (Common Upgradeability Description Format) C development stuff
Group: Development/ML

%description devel
CUDF (for Common Upgradeability Description Format) is a format for describing
upgrade scenarios in package-based Free and Open Source Software distribution.

libCUDF is a library to manipulate so called CUDF documents. A CUDF document
describe an upgrade problem, as faced by package managers in popular
package-based GNU/Linux distributions.

This package contains the development stuff needed to use libCUDF in your C
programs.

%package -n ocaml-%name-devel
Summary: CUDF (Common Upgradeability Description Format) OCaml development stuff
Group: Development/ML

%description -n ocaml-%name-devel
CUDF (for Common Upgradeability Description Format) is a format for describing
upgrade scenarios in package-based Free and Open Source Software distribution.

libCUDF is a library to manipulate so called CUDF documents. A CUDF document
describe an upgrade problem, as faced by package managers in popular
package-based GNU/Linux distributions.

This package contains the development stuff needed to use libCUDF in your OCaml
programs.

%prep
%setup

%build
sed -i 's,oUnit,ounit2,' _tags
make all c-lib
which /usr/bin/ocamlopt > /dev/null && make opt c-lib-opt

%install
make install				\
    DESTDIR="$RPM_BUILD_ROOT"		\
    LIBDIR="%_libdir"			\
    OCAMLLIBDIR="%_libdir/ocaml"

%check
make test

%files tools
%_bindir/cudf-check
%_bindir/cudf-parse-822

%files devel
%_includedir/cudf.h
%_libdir/*.a
%_libdir/pkgconfig/cudf.pc

%files -n ocaml-%name-devel
%_libdir/ocaml/cudf

%changelog
* Sat Feb 22 2020 Anton Farygin <rider@altlinux.ru> 0.9-alt7
- fixed build with new environment: oUnit now is ounit2

* Wed Jul 31 2019 Anton Farygin <rider@altlinux.ru> 0.9-alt6
- rebuilt with ocaml-4.08

* Thu Oct 18 2018 Anton Farygin <rider@altlinux.ru> 0.9-alt5
- rebuilt with ocaml-4.07.1

* Thu Sep 06 2018 Anton Farygin <rider@altlinux.ru> 0.9-alt4
- rebuilt with ocaml 4.07

* Sun May 20 2018 Anton Farygin <rider@altlinux.ru> 0.9-alt3
- rebuilt for ocaml 4.06.1

* Tue Jul 11 2017 Anton Farygin <rider@altlinux.ru> 0.9-alt2
- rebuild with ocaml 4.04.2

* Mon May 15 2017 Anton Farygin <rider@altlinux.ru> 0.9-alt1
- first build for ALT
