Name: rpm-build-ocaml
Version: 1.4.1
Release: alt1
BuildArch: noarch

Summary: RPM helpers to rebuild OCaml packages
License: GPL-2.0-or-later
Group: Development/ML

Source: scripts-%version.tar

# for proper dependencies
BuildPreReq: rpm-build >= 4.0.4-alt81

Requires: %_bindir/ocamlrun
Requires: %_rpmlibdir/ocaml-reqprov
Obsoletes: rpm-build-ocaml4

%description
RPM macros and reqprov helpers to be used in OCaml packages.

%prep
%setup -n scripts-%version

%install
mkdir -p %buildroot%_rpmlibdir
install -pD -m644 ocaml %buildroot%_rpmmacrosdir/ocaml
install -pD -m644 ocaml.env %buildroot%_rpmmacrosdir/ocaml.env
install -p -m755 ocaml.{req,prov}{.files,} ocaml-functions %buildroot%_rpmlibdir/

%files
%_rpmmacrosdir/ocaml
%_rpmmacrosdir/ocaml.env
%_rpmlibdir/ocaml*

%changelog
* Sun Dec 06 2020 Anton Farygin <rider@altlinux.ru> 1.4.1-alt1
- require full version of the ocaml-runtime
- relaxed the text relocations check for 32-bit x86 and armh architectures

* Fri Sep 11 2020 Anton Farygin <rider@altlinux.ru> 1.4-alt1
- %%ocamldir renamed to %%_ocamldir
- added %%dune_build, %%dune_install and %%dune_check
- removed conflict with ocaml4-runtime

* Tue May 16 2017 Anton Farygin <rider@altlinux.ru> 1.3-alt1
- added %%add_ocaml_req_skip macros
- added %%ocamldir

* Tue Apr 18 2017 Anton Farygin <rider@altlinux.ru> 1.2-alt1
- added stublibs path to search shared libraries in cmxi archives
- resolve .so path for avoid requires to devel packages in runtime ocaml libraries

* Thu Feb 16 2017 Anton Farygin <rider@altlinux.ru> 1.1.1-alt2
- added temporaty conflict with ocaml4-runtime

* Tue Apr 08 2008 Alexey Tourbin <at@altlinux.ru> 1.1.1-alt1
- ocaml.req: check "ccopt" libaray paths when resolving "cclib" dependencies

* Fri Apr 04 2008 Alexey Tourbin <at@altlinux.ru> 1.1-alt2
- added dependency on %_rpmlibdir/ocaml-reqprov

* Thu Apr 03 2008 Alexey Tourbin <at@altlinux.ru> 1.1-alt1
- major revision, implemented new types of dependencies:
  + ocaml-cmi(Unit) = V-hash - for bytecode units;
  + ocaml-cmx(Unit) = V-hash - for native units;
  + ocaml-dll(name) - for stub libraries (dll*.so);
  where V - major.minor of ocaml, hash - part of CRC

* Mon Jan 21 2007 Alex V. Myltsev <avm@altlinux.ru> 1-alt1
- Initial build for Sisyphus.

