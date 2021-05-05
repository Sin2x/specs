# vim: set ft=spec: -*- rpm-spec -*-
%define _unpackaged_files_terminate_build 1

%def_with    check

Name: breezy
Version: 3.2.0
Release: alt1

Summary: Breezy is a fork of decentralized revision control system Bazaar
License: GPL-2.0-or-later
Group: Development/Other

Url: https://github.com/breezy-team/breezy.git
Packager: Anatoly Kitaykin <cetus@altlinux.ru>

Source: %name-%version.tar

#Patch0: %name-%version-alt.patch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel
BuildRequires: python3-module-six
BuildRequires: python3-module-Cython
BuildRequires: python3-module-configobj

%if_with check

BuildRequires: python3-module-docutils
BuildRequires: python3-module-paramiko
BuildRequires: python3-module-testtools
BuildRequires: python3-module-subunit
BuildRequires: python3-module-dulwich
BuildRequires: python3-module-subunit

%endif

%add_python3_req_skip lazr

Conflicts: %name-doc < %version-%release
Conflicts: bzr-git-remote

%description
Breezy (or brz) is a distributed version control system that is powerful, friendly, and scalable.
Breezy is a fork of the Bazaar version control system.
By default, Breezy provides support for both the Bazaar and Git file formats.

%package -n python3-module-breezy-tests
Summary: Tools for testing Bazaar
Group: Development/Other
#BuildArch: noarch

Requires: %name = %version-%release
Provides: brz-selftest = %version-%release

%description -n python3-module-breezy-tests
This package contain tools and test suites for testing Bazaar.

%package doc
Summary: %name documentation and examples
Group: Development/Other
BuildArch: noarch

Conflicts: %name < %version

%description doc
Bazaar is a decentralized revision control system. This
package contain documentation and examples for using Bazaar.

%prep
%setup
#patch0 -p1

%build
%add_optflags -fno-strict-aliasing

%python3_build

%install

%python3_install --install-data=%_datadir

%define breezy_docdir %_docdir/%name-%version

install -dm0755 %buildroot%breezy_docdir
install -m0644 BRANCH.TODO INSTALL NEWS README.rst README_BDIST_RPM TODO %buildroot%breezy_docdir
cp -a doc contrib %buildroot%breezy_docdir
# Hack! Need a subst in setup.py
cp -a breezy/locale %buildroot%_datadir
%find_lang %name

%check
%python3_build check

%files -f %name.lang
%_bindir/*
%_man1dir/*

%python3_sitelibdir/*
%exclude %python3_sitelibdir/breezy/tests
%exclude %python3_sitelibdir/breezy/git/tests
%exclude %python3_sitelibdir/breezy/plugins/*/tests
%exclude %python3_sitelibdir/breezy/util/tests

%breezy_docdir
%exclude %breezy_docdir/doc
%exclude %breezy_docdir/contrib

%files -n python3-module-breezy-tests
%python3_sitelibdir/breezy/tests
%python3_sitelibdir/breezy/git/tests
%python3_sitelibdir/breezy/plugins/*/tests
%python3_sitelibdir/breezy/util/tests

%files doc
%dir %breezy_docdir
%breezy_docdir/doc
%breezy_docdir/contrib

%changelog
* Wed May 05 2021 Anatoly Kitaikin <cetus@altlinux.org> 3.2.0-alt1
- Release 3.2.0

* Tue Feb 02 2021 Anatoly Kitaykin <cetus@altlinux.org> 3.1.0.8-alt1
- Release 3.1.0-8 (debian)

* Fri Jul 10 2020 Anatoly Kitaikin <cetus@altlinux.org> 3.1.0-alt1
- Release 3.1.0

* Mon Jan 13 2020 Anatoly Kitaykin <cetus@altlinux.org> 3.0.2-alt1
- Release 3.0.2
- Check enabled

* Mon Aug 12 2019 Anatoly Kitaikin <cetus@altlinux.org> 3.0.1-alt3
- Git plugin path fix

* Tue Jul 09 2019 Anatoly Kitaikin <cetus@altlinux.org> 3.0.1-alt2
- Rebuilt with python3

* Wed Jun 19 2019 Anatoly Kitaykin <cetus@altlinux.org> 3.0.1-alt1
- Release 3.0.1

* Fri Apr 26 2019 Anatoly Kitaykin <cetus@altlinux.org> 3.0.0-alt1
- Initial build
