Name: paexec
Version: 1.1.3
Release: alt3

Summary: paexec distributes tasks over network or CPUs

License: MIT
Group: Networking/Other
Url: http://paexec.sourceforge.net/

# Source-url: https://prdownloads.sourceforge.net/paexec/paexec/paexec-%version/paexec-%version.tar.gz
Source: %name-%version.tar

Packager: Aleksey Cheusov <cheusov@altlinux.org>

BuildRequires: %_bindir/pod2man
BuildRequires: mk-configure >= 0.34.2-alt4
BuildRequires: rpm-macros-mk-configure
BuildRequires: runawk

Requires: runawk

%description
Small program that processes a list of tasks in parallel
on different CPUs, computers in a network or whatever else.

%package examples
Summary: Examples for paexec
Group: Documentation
BuildArch: noarch
Requires: %name = %version-%release

%description examples
Small program that processes a list of tasks in parallel
on different CPUs, computers in a network or whatever else.

This package contains examples for PAEXEC.

%prep
%setup

%build
%mkc_env
%mkcmake_configure
%mkcmake_build

# NB: the test might be a bit stressy, disabled so far
#%%check
#%%mkc_env
#%%mkcmake test

%install
%mkc_env
%mkcmake_install

%files
%doc doc/NEWS README doc/LICENSE doc/TODO presentation/paexec.pdf
%_bindir/*
%_man1dir/*

%files examples
%doc examples

%changelog
* Fri May 22 2020 Aleksey Cheusov <cheusov@altlinux.ru> 1.1.3-alt3
- 1.1.3-alt3:
  + fix build failure on Sisyphus with gcc9
  + fix hasher warnings and build-time dependencies

* Fri May 22 2020 Aleksey Cheusov <cheusov@altlinux.ru> 1.1.3-alt2
- 1.1.3-alt2: use rpm macro provided by mk-configure

* Sat May 16 2020 Aleksey Cheusov <cheusov@altlinux.ru> 1.1.3-alt1
- 1.1.3

* Sun Mar 03 2019 Vitaly Lipatov <lav@altlinux.ru> 1.1.1-alt1
- new version (1.1.1) with rpmgs script

* Sat Nov 29 2014 Aleksey Cheusov <cheusov@altlinux.org> 1.0.1-alt1
- 1.0.1

* Sat Aug 31 2013 Michael Shigorin <mike@altlinux.org> 0.19.1-alt2
- rebuilt for Sisyphus (thanks upstream; closes: #29308)

* Sat Aug 31 2013 Aleksey Cheusov <vle@gmx.net> 0.19.1-alt1
- 0.19.1

* Sun Mar 10 2013 Michael Shigorin <mike@altlinux.org> 0.18.0-alt1
- 0.18.0

* Mon Nov 07 2011 Michael Shigorin <mike@altlinux.org> 0.16.1-alt1
- NMU: 0.16.1 built with:
  + mk-configure 0.21.2
  + libmaa 1.3.1
  + runawk
- spec cleanup

* Thu Apr 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.14.0-alt2
- Rebuilt with libmaa 1.3.0

* Tue Jun 15 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.14.0-alt1
- Initial build for Sisyphus

