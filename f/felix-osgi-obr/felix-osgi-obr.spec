Epoch: 1
Group: Development/Java
BuildRequires: /proc rpm-build-java
BuildRequires: jpackage-1.8-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%global bundle org.osgi.service.obr

Name:           felix-osgi-obr
Version:        1.0.2
Release:        alt2_24jpp8
Summary:        Felix OSGi OBR Service API
License:        ASL 2.0
URL:            http://felix.apache.org/site/apache-felix-osgi-bundle-repository.html
BuildArch:      noarch

Source0:        http://www.apache.org/dist/felix/org.osgi.service.obr-%{version}-project.tar.gz

BuildRequires:  maven-local
BuildRequires:  mvn(org.apache.felix:felix:pom:)
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.osgi:osgi.core)
Source44: import.info

%description
OSGi OBR Service API.

%package javadoc
Group: Development/Java
Summary:        Javadoc for %{name}
BuildArch: noarch

%description javadoc
API documentation for %{name}.

%prep
%setup -q -n %{bundle}-%{version}

# Use latest OSGi implementation
%pom_change_dep :org.osgi.core org.osgi:osgi.core

%mvn_file ":{*}" felix/@1

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc --no-dereference LICENSE NOTICE

%files javadoc -f .mfiles-javadoc
%doc --no-dereference LICENSE NOTICE

%changelog
* Fri Oct 09 2020 Igor Vlasenko <viy@altlinux.ru> 1:1.0.2-alt2_24jpp8
- update

* Sat May 25 2019 Igor Vlasenko <viy@altlinux.ru> 1:1.0.2-alt2_22jpp8
- new version

* Tue Feb 05 2019 Igor Vlasenko <viy@altlinux.ru> 1:1.0.2-alt2_21jpp8
- fc29 update

* Thu Apr 19 2018 Igor Vlasenko <viy@altlinux.ru> 1:1.0.2-alt2_20jpp8
- java update

* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 1:1.0.2-alt2_19jpp8
- fc27 update

* Sun Oct 22 2017 Igor Vlasenko <viy@altlinux.ru> 1:1.0.2-alt2_18jpp8
- new jpp release

* Fri Dec 16 2016 Igor Vlasenko <viy@altlinux.ru> 1:1.0.2-alt2_17jpp8
- new fc release

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 1:1.0.2-alt2_16jpp8
- new fc release

* Tue Feb 02 2016 Igor Vlasenko <viy@altlinux.ru> 1:1.0.2-alt2_15jpp8
- new version

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 1:1.0.2-alt2_11jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 1:1.0.2-alt2_9jpp7
- new release

* Fri Jul 11 2014 Igor Vlasenko <viy@altlinux.ru> 1:1.0.2-alt2_6jpp7
- NMU rebuild to move _mavenpomdir and _mavendepmapfragdir

* Thu Aug 23 2012 Igor Vlasenko <viy@altlinux.ru> 1:1.0.2-alt1_6jpp7
- new release

* Wed Apr 04 2012 Igor Vlasenko <viy@altlinux.ru> 1:1.0.2-alt1_5jpp7
- fc package

