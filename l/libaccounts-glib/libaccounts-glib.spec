# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-python3
# END SourceDeps(oneline)
%filter_from_requires /dbus-test-runner/d
%add_optflags %optflags_shared
Group: System/Libraries
%add_optflags %optflags_shared
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           libaccounts-glib
Version:        1.25
Release:        alt1_2
Summary:        Accounts framework for Linux and POSIX based platforms
License:        LGPLv2

# workaround for GitLab bug that puts commit hash into tarball root directory name
# https://gitlab.com/gitlab-org/gitlab/-/issues/214535
%global ver_str VERSION_%{version}

URL:            https://gitlab.com/accounts-sso/libaccounts-glib
Source0:        %{url}/-/archive/%{ver_str}/%{name}-%{ver_str}.tar.gz

BuildRequires:  gcc
BuildRequires:  meson >= 0.48.0
BuildRequires:  python3-devel
BuildRequires:  python3-module-pygobject3
BuildRequires:  vala vala-tools

BuildRequires:  pkgconfig(gio-2.0) >= 2.26
BuildRequires:  pkgconfig(gio-unix-2.0)
BuildRequires:  pkgconfig(glib-2.0) >= 2.26
BuildRequires:  pkgconfig(gobject-2.0) >= 2.35.1
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(sqlite3) >= 3.7.0

# dependencies for building docs
BuildRequires:  gtk-doc gtk-doc-mkpdf

# dependencies for tests
BuildRequires:  pkgconfig(check)
Source44: import.info

# package contains python3-gobject overrides

%description
%{summary}.


%package devel
Group: Development/C
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}

%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%package docs
Group: System/Libraries
Summary:        Documentation for %{name}
BuildArch:      noarch

%description docs
The %{name}-docs package contains documentation for %{name}.


%prep
%setup -q -n %{name}-%{ver_str}



%build
%meson
%meson_build


%install
%meson_install

# create data directories
mkdir -p %{buildroot}%{_datadir}/accounts/{applications,providers,services,service_types}


%check
# some tests fail without either dbus-test-runner (not packaged) or X11 session
%meson_test || :


%files
%doc --no-dereference COPYING
%doc README.md NEWS

%{_bindir}/ag-backup
%{_bindir}/ag-tool

%{_libdir}/libaccounts-glib.so.0
%{_libdir}/libaccounts-glib.so.%{version}
%{_libdir}/girepository-1.0/Accounts-1.0.typelib

%dir %{_datadir}/xml/accounts/schema/dtd
%{_datadir}/xml/accounts/schema/dtd/accounts-*.dtd

%dir %{_datadir}/xml/
%dir %{_datadir}/xml/accounts/
%dir %{_datadir}/xml/accounts/schema/
%dir %{_datadir}/accounts/
%dir %{_datadir}/accounts/applications/
%dir %{_datadir}/accounts/providers/
%dir %{_datadir}/accounts/services/
%dir %{_datadir}/accounts/service_types/

%{python3_sitelibdir}/gi/overrides/Accounts.py
%{python3_sitelibdir}/gi/overrides/__pycache__/*


%files devel
%{_includedir}/libaccounts-glib/

%{_libdir}/libaccounts-glib.so
%{_libdir}/pkgconfig/libaccounts-glib.pc

%{_datadir}/dbus-1/interfaces/*.xml
%{_datadir}/gettext/its/accounts-*.its
%{_datadir}/gettext/its/accounts-*.loc
%{_datadir}/gir-1.0/Accounts-1.0.gir
%{_datadir}/vala/vapi/libaccounts-glib.deps
%{_datadir}/vala/vapi/libaccounts-glib.vapi


%files docs
%doc %{_datadir}/gtk-doc/html/libaccounts-glib/


%changelog
* Thu Jun 25 2020 Igor Vlasenko <viy@altlinux.ru> 1.25-alt1_2
- update to new release by fcimport

* Fri Apr 17 2020 Igor Vlasenko <viy@altlinux.ru> 1.24-alt1_1
- update to new release by fcimport

* Sat Dec 07 2019 Igor Vlasenko <viy@altlinux.ru> 1.23-alt1_8
- fixed build

* Thu Oct 18 2018 Igor Vlasenko <viy@altlinux.ru> 1.23-alt1_6
- dropped req: dbus-test-runner

* Wed Sep 27 2017 Igor Vlasenko <viy@altlinux.ru> 1.23-alt1_4
- update to new release by fcimport

* Thu Mar 16 2017 Igor Vlasenko <viy@altlinux.ru> 1.23-alt1_2
- update to new release by fcimport

* Mon Dec 19 2016 Igor Vlasenko <viy@altlinux.ru> 1.23-alt1_1
- update to new release by fcimport

* Tue Mar 29 2016 Igor Vlasenko <viy@altlinux.ru> 1.21-alt1_1
- update to new release by fcimport

* Mon Oct 19 2015 Igor Vlasenko <viy@altlinux.ru> 1.18-alt1_3
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 1.18-alt1_2
- update to new release by fcimport

* Tue Apr 07 2015 Igor Vlasenko <viy@altlinux.ru> 1.18-alt1_1
- update to new release by fcimport

* Wed Aug 27 2014 Igor Vlasenko <viy@altlinux.ru> 1.16-alt1_4
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 1.16-alt1_2
- update to new release by fcimport

* Wed Mar 05 2014 Igor Vlasenko <viy@altlinux.ru> 1.16-alt1_1
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 1.8-alt1_2
- update to new release by fcimport

* Sat Jun 01 2013 Igor Vlasenko <viy@altlinux.ru> 1.8-alt1_1
- new fc release

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 0.45-alt3_5
- update to new release by fcimport

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 0.45-alt3_4
- update to new release by fcimport

* Wed Jun 13 2012 Igor Vlasenko <viy@altlinux.ru> 0.45-alt3_3
- fixed build

* Wed Feb 01 2012 Igor Vlasenko <viy@altlinux.ru> 0.45-alt2_3
- update to new release by fcimport

* Fri Dec 23 2011 Igor Vlasenko <viy@altlinux.ru> 0.45-alt2_2
- spec cleanup thanks to ldv@

* Sat Dec 17 2011 Igor Vlasenko <viy@altlinux.ru> 0.45-alt1_2
- initial import by fcimport

