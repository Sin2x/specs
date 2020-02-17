# coccinelle.spec
Name:		coccinelle
Version:	1.0.8
Release:	alt1
Summary:	Semantic patching for Linux (spatch)

Group:		Development/Kernel
License:	GPL-2.0
Url:		http://coccinelle.lip6.fr/

Source:		%name-%version.tar
Provides:	spatch

BuildRequires:	ocaml >= 3.12.1
BuildRequires:	ocaml-findlib
BuildRequires:	ocaml-ocamldoc
BuildRequires:	ocaml-menhir
BuildRequires:	ocaml-pcre-devel
BuildRequires:	ocaml-num-devel
BuildRequires:	ocaml-parmap-devel
BuildRequires:	rpm-build-python python-devel python-modules-multiprocessing
BuildRequires:	chrpath

# only if vim coccigui is used
%filter_from_requires /^python.*(pida)$/d
# bogus internal name
%filter_from_requires /^python.*(coccinelle)$/d

%description
Coccinelle is a tool to utilize semantic patches for manipulating
C code. It was originally designed to ease maintenance of device
drivers in the Linux kernel.

%prep
%setup -q -n %{name}-%{version}
sed -i '1s:^#!/usr/bin/env python$:#!/usr/bin/python%__python_version:' tools/pycocci

%build
./autogen
%configure
# -unsafe-string
export OCAMLPARAM="safe-string=0,_"
make EXTLIBDIR=`ocamlc -where`/extlib

%install
make DESTDIR=%buildroot install
rm -rf %buildroot%_libdir/coccinelle/ocaml
# relocate python module
install -d %buildroot%python_sitelibdir
mv %buildroot%_libdir/coccinelle/python/coccilib %buildroot%python_sitelibdir/
rm -rf %buildroot%_libdir/coccinelle/python
# delete spgen
rm -rf %buildroot%_bindir/spgen
rm -rf %buildroot%_libdir/coccinelle/spgen
rm -rf %buildroot%_mandir/man1/spgen.*
rm -rf %buildroot%_mandir/man3

# Somebody forgot to install this
install ./tools/pycocci %buildroot%_bindir/pycocci
install ./spatch.opt    %buildroot%_bindir/spatch.opt

%check
export COCCINELLE_HOME=%buildroot%_libdir/coccinelle
export LD_LIBRARY_PATH=.
%buildroot%_bindir/spatch -sp_file demos/simple.cocci demos/simple.c

%files
%doc authors.txt bugs.txt changes.txt copyright.txt credits.txt
%doc license.txt readme.txt
%_bindir/pycocci
%_bindir/spatch
%_bindir/spatch.opt
%_libdir/%name/
%python_sitelibdir/coccilib
%_mandir/man1/*.1*
/usr/share/bash-completion/completions/spatch

%changelog
* Mon Feb 17 2020 Vitaly Chikunov <vt@altlinux.org> 1.0.8-alt1
- Update to 1.0.8.

* Wed Aug 07 2019 Vitaly Chikunov <vt@altlinux.org> 1.0.7.0.217.ged1eb8e0-alt1
- Update to 1.0.7-217-ged1eb8e0.

* Sun Jun 10 2018 Vitaly Chikunov <vt@altlinux.ru> 1.0.6-alt1
- Initial build for ALT.
