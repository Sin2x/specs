%define  modulename ppx_enumerate

Name:    ocaml-%modulename
Version: 0.15.0
Release: alt1

Summary: Generate a list containing all values of a finite type
License: MIT
Group:   Development/ML
URL:     https://github.com/janestreet/ppx_enumerate
BuildRequires: dune
BuildRequires: ocaml-base-devel
BuildRequires: ocaml-ppxlib-devel
Source:  %modulename-%version.tar

%description
%summary

%package devel
Summary: Development files for %name
Group: Development/ML
Requires: %name = %EVR

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

%files devel -f ocaml-files.devel

%changelog
* Tue Jan 04 2022 Anton Farygin <rider@altlinux.ru> 0.15.0-alt1
- 0.15.0

* Tue Dec 08 2020 Anton Farygin <rider@altlinux.ru> 0.14.0-alt2
- migrated to rpm-build-ocaml 1.4
- cleanup for spec and BR

* Wed Jul 29 2020 Mikhail Gordeev <obirvalger@altlinux.org> 0.14.0-alt1
- Initial build for Sisyphus
