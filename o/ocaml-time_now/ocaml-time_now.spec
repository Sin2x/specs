%set_verify_elf_method textrel=relaxed
%define  modulename time_now

Name:    ocaml-%modulename
Version: 0.14.0
Release: alt4
Summary: Reports the current time
License: MIT
Group:   Development/ML
URL:     https://github.com/janestreet/time_now
BuildRequires: dune ocaml-jane-street-headers-devel ocaml-jst-config-devel
BuildRequires: ocaml-ppx_base-devel ocaml-ppx_optcomp-devel
BuildPreReq: rpm-build-ocaml >= 1.1

Source:  %modulename-%version.tar

%description
%summary

%package devel
Summary: Development files for %name
Group: Development/ML
Requires: %name = %EVR
Requires: ocaml-jane-street-headers-devel
Requires: ocaml-ppx_sexp_conv-devel
Requires: ocaml-ppx_compare-devel
Requires: ocaml-ppx_enumerate-devel
Requires: ocaml-ppx_hash-devel
%description devel
The %name-devel package contains libraries and signature files for
developing applications that use %name.

%prep
%setup -n %modulename-%version

%build
%dune_build -p %modulename

%install
%dune_install

%check
%dune_check

%files -f ocaml-files.runtime
%dir %_libdir/ocaml/%modulename

%files devel -f ocaml-files.devel

%changelog
* Wed Sep 23 2020 Anton Farygin <rider@altlinux.ru> 0.14.0-alt4
- changed runtime to devel requires for devel package

* Fri Sep 18 2020 Anton Farygin <rider@altlinux.ru> 0.14.0-alt3
- added runtime requires from dune-package

* Thu Sep 17 2020 Anton Farygin <rider@altlinux.ru> 0.14.0-alt2
- removed rpm-build-ocaml dependency for runtime package
- migrated to rpm-build-ocaml 1.4
- cleanup build requires
- added ocaml-jane-street-headers-devel dependency to devel package

* Thu Jul 30 2020 Mikhail Gordeev <obirvalger@altlinux.org> 0.14.0-alt1
- Initial build for Sisyphus
