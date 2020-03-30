# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-python3 rpm-macros-fedora-compat
BuildRequires: waf
# END SourceDeps(oneline)
BuildRequires: libnumpy-devel
BuildRequires: gcc-c++
Group: System/Libraries
%add_optflags %optflags_shared
%define oldname lilv
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
# %%oldname and %%version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define name lilv
%define version 0.24.6
%{!?_pkgdocdir: %global _pkgdocdir %{_docdir}/%{oldname}-%{version}}
%global maj 0

Name:       liblilv
Version:    0.24.6
Release:    alt1_2
Summary:    An LV2 Resource Description Framework Library

License:    MIT
URL:        http://drobilla.net/software/lilv/
Source0:    http://download.drobilla.net/%{oldname}-%{version}.tar.bz2
BuildRequires:  doxygen
BuildRequires:  graphviz libgraphviz
BuildRequires:  libsord-devel >= 0.14.0
BuildRequires:  libsratom-devel >= 0.4.4
BuildRequires:  lv2-devel >= 1.16.0
BuildRequires:  python3
BuildRequires:  python3-devel
BuildRequires:  swig
BuildRequires:  libserd-devel >= 0.30.0
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  libsndfile-devel >= 1.0.0
Source44: import.info
Provides: lilv = %{version}-%{release}

%description
%{oldname} is a library to make the use of LV2 plugins as simple as possible
for applications. Lilv is the successor to SLV2, rewritten to be significantly
faster and have minimal dependencies.

%package devel
Group: Development/Other
Summary:    Development libraries and headers for %{oldname}
Requires:   %{name} = %{version}-%{release}
Provides: lilv-devel = %{version}-%{release}

%description devel
%{oldname} is a lightweight C library for Resource Description Syntax which
supports reading and writing Turtle and NTriples.

This package contains the headers and development libraries for %{oldname}.

%package -n python3-module-lilv
Group: System/Libraries
%{?python_provide:%python_provide python3-%{oldname}}
Summary:    Python bindings for %{oldname}
Requires:   %{name} = %{version}-%{release}

%description -n python3-module-lilv
%{oldname} is a lightweight C library for Resource Description Syntax which
supports reading and writing Turtle and NTriples.

This package contains the python libraries for %{oldname}.

%prep
%setup -n %{oldname}-%{version} -q 
# we'll run ld config
sed -i -e 's|bld.add_post_fun(autowaf.run_ldconfig)||' wscript
# for packagers sake, build the tests with debug symbols
sed -i -e "s|'-ftest-coverage'\]|\
 '-ftest-coverage' \] + '%{optflags}'.split(' ')|" wscript

%build

export LINKFLAGS="%{__global_ldflags}"
python3 waf configure -v --prefix=%{_prefix} \
 --libdir=%{_libdir} --configdir=%{_sysconfdir} --mandir=%{_mandir} \
 --docdir=%{_docdir}/%{oldname} \
 --docs --test --dyn-manifest \
 --default-lv2-path=%{_libdir}/lv2
python3 waf -v build %{?_smp_mflags}

%install
python3 waf -v install --destdir=%{buildroot}
chmod +x %{buildroot}%{_libdir}/lib%{oldname}-0.so.*

%check
./build/test/lilv_test

%files
%doc AUTHORS NEWS README.md
%doc --no-dereference COPYING
%exclude %{_docdir}/%{oldname}/%{oldname}-%{maj}/
%{_libdir}/lib%{oldname}-%{maj}.so.*
%{_bindir}/lilv-bench
%{_bindir}/lv2info
%{_bindir}/lv2ls
%{_bindir}/lv2bench
%{_bindir}/lv2apply
%{_sysconfdir}/bash_completion.d/lilv
%{_mandir}/man1/*

%files devel
%{_libdir}/lib%{oldname}-%{maj}.so
%{_libdir}/pkgconfig/%{oldname}-%{maj}.pc
%{_includedir}/%{oldname}-%{maj}/
%{_docdir}/%{oldname}/%{oldname}-%{maj}/
%{_mandir}/man3/*

%files -n python3-module-lilv
%{python3_sitelibdir_noarch}/%{oldname}.*
%{python3_sitelibdir_noarch}/__pycache__/*

%changelog
* Mon Mar 30 2020 Igor Vlasenko <viy@altlinux.ru> 0.24.6-alt1_2
- update

* Wed Nov 20 2019 Igor Vlasenko <viy@altlinux.ru> 0.24.4-alt1_7
- update to new release by fcimport

* Sat Feb 16 2019 Igor Vlasenko <viy@altlinux.ru> 0.24.4-alt1_5
- update to new release by fcimport

* Sat Feb 09 2019 Igor Vlasenko <viy@altlinux.ru> 0.24.4-alt1_3
- update to new release by fcimport

* Mon May 07 2018 Igor Vlasenko <viy@altlinux.ru> 0.24.2-alt2_7
- update to new release by fcimport

* Tue Jan 16 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 0.24.2-alt2_4
- Updated build dependencies.

* Wed Oct 11 2017 Igor Vlasenko <viy@altlinux.ru> 0.24.2-alt1_4
- update to new release by fcimport

* Thu Mar 16 2017 Igor Vlasenko <viy@altlinux.ru> 0.20.0-alt1_7
- update to new release by fcimport

* Wed Sep 21 2016 Igor Vlasenko <viy@altlinux.ru> 0.20.0-alt1_6
- update to new release by fcimport

* Mon Feb 15 2016 Igor Vlasenko <viy@altlinux.ru> 0.20.0-alt1_5
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 0.20.0-alt1_4
- update to new release by fcimport

* Wed Aug 27 2014 Igor Vlasenko <viy@altlinux.ru> 0.20.0-alt1_2
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 0.18.0-alt1_3
- update to new release by fcimport

* Thu Jun 05 2014 Igor Vlasenko <viy@altlinux.ru> 0.18.0-alt1_2
- converted for ALT Linux by srpmconvert tools

* Tue Dec 03 2013 Igor Vlasenko <viy@altlinux.ru> 0.16.0-alt1_3
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 0.16.0-alt1_2
- update to new release by fcimport

* Fri May 31 2013 Igor Vlasenko <viy@altlinux.ru> 0.16.0-alt1_1
- update to new release by fcimport

* Tue Mar 26 2013 Igor Vlasenko <viy@altlinux.ru> 0.14.4-alt1_2
- fc import

