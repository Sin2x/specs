# use no more than system_memory/2000 build procs (see https://bugzilla.altlinux.org/show_bug.cgi?id=35112)
%_tune_parallel_build_by_procsize 2000

%def_with python

Name: ledger
Version: 3.2.1
Release: alt1

Summary: Ledger is a highly flexible, double-entry accounting system

License: BSD-3-Clause
Group: Office
Url: http://www.ledger-cli.org/

Packager: Vitaly Lipatov <lav@altlinux.ru>

# Source-url: https://github.com/ledger/ledger/archive/v%version.tar.gz
Source: %name-%version.tar

Patch: 69e6b89cf8d2820d28174e7ffaea1c59a0f84d3f.patch

Requires: libledger = %EVR

BuildRequires(pre): rpm-macros-cmake
BuildRequires(pre): rpm-macros-intro

BuildRequires: cmake gcc-c++
BuildRequires: boost-filesystem-devel
%if_with python
BuildRequires: boost-python3-devel
%endif
BuildRequires: libedit-devel libicu-devel libmpfr-devel libutfcpp-devel libssl-devel

%description
Ledger is an accounting program which is invoked from the command-line
using a textual ledger file.  To start using Ledger, you will need to
create such a file containing your financial transactions.
See the documentation (ledger.pdf, or ledger.info) for full documentation
on creating a ledger file and using Ledger to generate reports.

A sample has been provided in the file "sample.dat":
$ ledger -f %_docdir/%name-%version/sample.dat reg

%package -n libledger
Summary: Libraries for ledger accounting system
Group: System/Libraries

%description -n libledger
Ledger is an accounting program which is invoked from the command-line
using a textual ledger file.  To start using Ledger, you will need to
create such a file containing your financial transactions.  A sample
has been provided in the file "sample.dat".  See the documentation
(ledger.pdf, or ledger.info) for full documentation on creating a
ledger file and using Ledger to generate reports.

This package contains libraries for ledger to use.

%package -n libledger-devel
Summary: Development files for ledger accounting system
Group: Development/C
Requires: libledger = %version-%release

%description -n libledger-devel
Ledger is an accounting program which is invoked from the command-line
using a textual ledger file.  To start using Ledger, you will need to
create such a file containing your financial transactions.  A sample
has been provided in the file "sample.dat".  See the documentation
(ledger.pdf, or ledger.info) for full documentation on creating a
ledger file and using Ledger to generate reports.

This package contains files needed for developing programs using
ledger facilities.

%package -n python3-module-%name
Summary: Python bindings for ledger
Group: Development/Python3
Requires: libledger = %EVR

%description -n python3-module-%name
Ledger is an accounting program which is invoked from the command-line
using a textual ledger file.  To start using Ledger, you will need to
create such a file containing your financial transactions.  A sample
has been provided in the file "sample.dat".  See the documentation
(ledger.pdf, or ledger.info) for full documentation on creating a
ledger file and using Ledger to generate reports.

This package contains python bindings for some of ledger
functionality.

%package -n emacs-ledger
Summary: Emacs mode for ledger accounting system
Group: Editors
Requires: ledger = %EVR

%description -n emacs-ledger
Ledger is an accounting program which is invoked from the command-line
using a textual ledger file.  To start using Ledger, you will need to
create such a file containing your financial transactions.  A sample
has been provided in the file "sample.dat".  See the documentation
(ledger.pdf, or ledger.info) for full documentation on creating a
ledger file and using Ledger to generate reports.

This package contains emacs libraries to ease use of ledger.

%prep
%setup
%patch -p1

%build
%cmake -DUSE_PYTHON=yes
# 15.08.2015: disabled due ledger3.info install bug
# -DBUILD_DOCS=yes
%cmake_build

%install
%cmake_install

%files
%doc LICENSE.md README.md
%doc test/input/sample.dat
%_bindir/%name
%_man1dir/*

%files -n libledger
%_libdir/libledger.so.3

%files -n libledger-devel
%_includedir/%name/
%_libdir/libledger.so

%if_with python
%files -n python3-module-ledger
%python3_sitelibdir/*
%endif

#%files -n emacs-ledger
#%_emacslispdir/*

%changelog
* Fri Aug 13 2021 Vitaly Lipatov <lav@altlinux.ru> 3.2.1-alt1
- new version 3.2.1 (with rpmrb script)
- fix build with boost-1.76

* Tue Apr 27 2021 Arseny Maslennikov <arseny@altlinux.org> 3.1.aed3709-alt5.1
- NMU: spec: adapted to new cmake macros.

* Mon Dec 16 2019 Aleksei Nikiforov <darktemplar@altlinux.org> 3.1.aed3709-alt5
- Rebuilt with boost-1.71.0

* Thu Dec 12 2019 Grigory Ustinov <grenka@altlinux.org> 3.1.aed3709-alt4
- NMU: Fix license.

* Mon Jul 30 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 3.1.aed3709-alt3
- NMU: rebuilt with boost-1.67.0

* Thu May 31 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 3.1.aed3709-alt2.1
- NMU: rebuilt with boost-1.67.0

* Mon Apr 30 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 3.1.aed3709-alt2
- (NMU) Rebuilt with python-3.6.4.

* Wed Feb 10 2016 Gleb F-Malinovskiy <glebfm@altlinux.org> 3.1.aed3709-alt1.1
- Rebuilt with libicuuc.so.56.

* Sat Aug 15 2015 Vitaly Lipatov <lav@altlinux.ru> 3.1.aed3709-alt1
- new version 3.1 (with rpmrb script)

* Sat Jan 03 2015 Ivan A. Melnikov <iv@altlinux.org> 3.0.2-alt1.1
- rebuild with boost 1.57.0

* Wed Sep 24 2014 Vitaly Lipatov <lav@altlinux.ru> 3.0.2-alt1
- new version 3.0.2 (with rpmrb script)

* Fri Feb 07 2014 Vitaly Lipatov <lav@altlinux.ru> 2.6.3-alt1
- new version 2.6.3 (with rpmrb script)
- cleanup spec, remove emacs subpackage

* Fri Feb 29 2008 Alexey Voinov <voins@altlinux.ru> 2.6.0.90-alt1
- initial build
