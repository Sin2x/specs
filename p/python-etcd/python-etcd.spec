%global modname etcd
%global srcname python-%{modname}
%global __ospython %{_bindir}/python3
%global python3_sitelib %(%{__ospython} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())")

Name:           %{srcname}
Version:        0.4.5
Release:        alt1
Summary:        A python client library for etcd
Group:          System/Libraries
License:        MIT
URL:            http://pypi.python.org/pypi/%{srcname}
Source0:        %{name}-%{version}.tar

BuildArch:      noarch

# See https://bugzilla.redhat.com/1393497
# Also https://fedoraproject.org/wiki/Packaging:Guidelines#Noarch_with_Unported_Dependencies
ExclusiveArch:  noarch %{ix86} x86_64 %{arm} aarch64 ppc64le s390x

BuildRequires:  python3-dev
BuildRequires:  python3-module-setuptools
BuildRequires:  python3-module-dns
BuildRequires:  python3-module-mock
BuildRequires:  python3-module-nose
BuildRequires:  python3-module-urllib3
BuildRequires:  python3-module-OpenSSL

%description
Client library for interacting with an etcd service, providing Python
access to the full etcd REST API.  Includes authentication, accessing
and manipulating shared content, managing cluster members, and leader
election.

%package -n python3-module-%{modname}
Summary:        %summary
Group:          System/Libraries
Requires:       python3-module-dns
Requires:       python3-module-urllib3
Obsoletes:      python3-module-python-etcd
Provides:       python3-module-python-etcd
%{?python_provide:%python_provide python3-etcd}

%description -n python3-module-%{modname}
Client library for interacting with an etcd service, providing Python
access to the full etcd REST API.  Includes authentication, accessing
and manipulating shared content, managing cluster members, and leader
election.

%prep
%setup -n %name-%version

%build
%{__ospython} setup.py build

%install
%{__rm} -rf %{buildroot}
%{__ospython} setup.py install --root %{buildroot} -O1 --skip-build

%check
nosetests-3 src/etcd/tests/unit/

# This seems to require a newer python3-mock than what's currently available
# in F23, and even Rawhide.  If I let it download mock-1.3.0 from the Python
# Package Index (pypi) then tests pass.
#%%{__python3} setup.py test

%files -n python3-module-%{modname}
%doc README.rst
%doc LICENSE.txt
%{python3_sitelib}/*

%changelog
* Fri Oct 07 2022 Ilfat Aminov <aminov@altlinux.org> 0.4.5-alt1
- initial build for alt sisyphus

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.5-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.5-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.4.5-22
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.5-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.5-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.4.5-19
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.5-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.4.5-17
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.4.5-16
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.5-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.5-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Sep 20 2018 Matthew Barnes <mbarnes@redhat.com> - 0.4.5-13
- Remove python2 subpackage (rhbz#1630954).

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.5-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.4.5-11
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.5-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Jan 16 2018 Iryna Shcherbina <ishcherb@redhat.com> - 0.4.5-9
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Mon Dec 18 2017 Steve Milner <smilner@redhat.com> - 0.4.5-8
- Fix naming per rhbz#1526788.

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jun 19 2017 Matthew Barnes <mbarnes@redhat.com> - 0.4.5-6
- I'm told etcd works on s390x too; add it to ExclusiveArch.

* Mon Jun 19 2017 Steve Milner <smilner@redhat.com> - 0.4.5-5
- Remove requirements on etcd for build and install

* Mon Jun 19 2017 Matthew Barnes <mbarnes@redhat.com> - 0.4.5-4
- Last change didn't help and we were in compliance with Packaging
  Guidelines before the change, so revert.  The fact that it still
  randomly gets built on ppc64 seems to be a Fedora infrastructure
  issue.

* Wed Jun 14 2017 Matthew Barnes <mbarnes@redhat.com> - 0.4.5-3
- Try excluding ppc64 directly, since ExclusiveArch doesn't.

* Wed Apr 12 2017 Matthew Barnes <mbarnes@redhat.com> - 0.4.5-2
- Add missing requires python[3]-urllib3 (rhbz#1440546).
- Patch from Oleg Gashev <oleg@gashev.net>

* Thu Mar  2 2017 Steve Milner <smilner@redhat.com> - 0.4.5-1
- Update to 0.4.5

* Fri Feb 17 2017 Matthew Barnes <mbarnes@redhat.com> - 0.4.4-1
- Update to 0.4.4

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.4.3-6
- Rebuild for Python 3.6

* Fri Nov 18 2016 Steve Milner <smilner@redhat.com> - 0.4.3-5
- Running unittests only.

* Wed Nov 16 2016 Steve Milner <smilner@redhat.com> - 0.4.3-4
- Added noarch to the list to build.
- Fixed provides (see rhbz#1374240)
- Disabled the new auth module (see https://github.com/jplana/python-etcd/issues/210)

* Wed Nov 09 2016 Matthew Barnes <mbarnes@redhat.com> - 0.4.3-3
- etcd now excludes ppc64; follow suit.
  related: #1393497

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.3-2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Mon Feb 22 2016 Matthew Barnes <mbarnes@redhat.com> - 0.4.3-1
- Initial packaging.
