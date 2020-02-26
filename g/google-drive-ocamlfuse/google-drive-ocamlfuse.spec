Name: google-drive-ocamlfuse
Version: 0.7.18
Release: alt1
License: BSD-2-Clause
Summary: FUSE filesystem for Google Drive
Url: http://gdfuse.forge.ocamlcore.org
Group: Networking/Remote access
Source: %name-%version.tar
BuildRequires: ocaml ocaml-ocamlbuild
BuildRequires: dune opam
BuildRequires: ocaml-findlib-devel
BuildRequires: ocaml-ocamlfuse-devel
BuildRequires: ocaml-gapi-devel
BuildRequires: ocaml-sqlite3 
BuildRequires: ocaml-cryptokit-devel
BuildRequires: ocaml-extlib-devel
BuildRequires: ocaml-camlidl-devel >= 1.06-alt1
BuildRequires: ocaml-yojson-devel
BuildRequires: ocaml-biniou-devel
BuildRequires: ocaml-easy-format-devel
BuildRequires: ocaml-curl-devel
BuildRequires: ocaml-ocamlnet-devel
BuildRequires: libsqlite3-devel
BuildRequires: libcurl-devel
BuildRequires: zlib-devel
BuildRequires: libfuse-devel
BuildRequires: libgmp-devel

%description
google-drive-ocamlfuse is a FUSE-based file system backed by Google Drive,
written in OCaml. It lets you mount your Google Drive on Linux.

On the first time, just run google-drive-ocamlfuse, which will open a
browser for authentication. If that process succeeds, it will print
"Access token retrieved correctly.". Now run google-drive-ocamlfuse
with an empty directory supplied, which is the mount point for your Google
Drive. You can optionally unmount with fusermount -u mount-point.

Further documentation is available here:

  https://github.com/astrada/google-drive-ocamlfuse/wiki

%prep
%setup

%build
dune build @install

%install
dune install --destdir=%buildroot --libdir=%_libdir/ocaml

%files
%doc README.md doc/ LICENSE
%_bindir/%name

%changelog
* Wed Feb 26 2020 Anton Farygin <rider@altlinux.ru> 0.7.18-alt1
- 0.7.18

* Tue Sep 03 2019 Anton Farygin <rider@altlinux.ru> 0.7.10-alt1
- 0.7.10

* Fri Aug 02 2019 Anton Farygin <rider@altlinux.ru> 0.7.8-alt1
- 0.7.8

* Mon Jul 01 2019 Anton Farygin <rider@altlinux.ru> 0.7.6-alt1
- 0.7.6

* Sun Jun 09 2019 Anton Farygin <rider@altlinux.ru> 0.7.4-alt1
- 0.7.4

* Thu Feb 14 2019 Anton Farygin <rider@altlinux.ru> 0.7.3-alt1
- 0.7.3

* Sun Jan 20 2019 Anton Farygin <rider@altlinux.ru> 0.7.1-alt2
- fixed build with dune-1.6.4

* Tue Dec 11 2018 Anton Farygin <rider@altlinux.ru> 0.7.1-alt1
- 0.7.1

* Mon Oct 29 2018 Anton Farygin <rider@altlinux.ru> 0.7.0-alt1
- 0.7.0

* Thu May 24 2018 Anton Farygin <rider@altlinux.ru> 0.6.25-alt1
- 0.6.25

* Fri Jul 21 2017 Anton Farygin <rider@altlinux.ru> 0.6.20-alt1
- new version

* Thu May 04 2017 Anton Farygin <rider@altlinux.ru> 0.6.19-alt1
- new version

* Mon Apr 24 2017 Anton Farygin <rider@altlinux.ru> 0.6.16-alt1
- first build for ALT
