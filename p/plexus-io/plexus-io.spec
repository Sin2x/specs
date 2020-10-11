Epoch: 0
Group: Development/Java
BuildRequires: /proc rpm-build-java
BuildRequires: jpackage-1.8-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           plexus-io
Summary:        Plexus IO Components
Version:        3.1.1
Release:        alt1_1jpp8
License:        ASL 2.0

URL:            https://github.com/codehaus-plexus/%{name}
Source0:        %{url}/archive/%{name}-%{version}.tar.gz
Source1:        http://www.apache.org/licenses/LICENSE-2.0.txt

BuildArch:      noarch

BuildRequires:  maven-local
BuildRequires:  mvn(com.google.code.findbugs:jsr305)
BuildRequires:  mvn(commons-io:commons-io)
BuildRequires:  mvn(org.codehaus.plexus:plexus-container-default)
BuildRequires:  mvn(org.codehaus.plexus:plexus:pom:)
BuildRequires:  mvn(org.codehaus.plexus:plexus-utils)
Source44: import.info

%description
Plexus IO is a set of plexus components, which are designed for use
in I/O operations.

%package        javadoc
Group: Development/Java
Summary:        Javadoc for %{name}
BuildArch: noarch

%description    javadoc
API documentation for %{name}.


%prep
%setup -q -n plexus-io-plexus-io-%{version}
cp %{SOURCE1} .

%pom_remove_plugin :animal-sniffer-maven-plugin
%pom_remove_plugin :maven-enforcer-plugin

# junit isn't actually used
%pom_remove_dep :junit


%build
%mvn_file  : plexus/io
%mvn_build


%install
%mvn_install


%files -f .mfiles
%doc --no-dereference NOTICE.txt LICENSE-2.0.txt

%files javadoc -f .mfiles-javadoc
%doc --no-dereference NOTICE.txt LICENSE-2.0.txt


%changelog
* Fri Oct 09 2020 Igor Vlasenko <viy@altlinux.ru> 0:3.1.1-alt1_1jpp8
- new version

* Sun May 26 2019 Igor Vlasenko <viy@altlinux.ru> 0:3.0.0-alt1_4jpp8
- new version

* Tue May 15 2018 Igor Vlasenko <viy@altlinux.ru> 0:3.0.0-alt1_2jpp8
- java update

* Tue Nov 14 2017 Igor Vlasenko <viy@altlinux.ru> 0:2.7.1-alt1_3jpp8
- fc27 update

* Wed Nov 01 2017 Igor Vlasenko <viy@altlinux.ru> 0:2.7.1-alt1_2jpp8
- new jpp release

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 0:2.6-alt1_3jpp8
- new fc release

* Mon Feb 01 2016 Igor Vlasenko <viy@altlinux.ru> 0:2.6-alt1_2jpp8
- new version

* Fri Jan 22 2016 Igor Vlasenko <viy@altlinux.ru> 0:2.6-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 0:2.0.5-alt1_8jpp7
- new release

* Mon Aug 25 2014 Igor Vlasenko <viy@altlinux.ru> 0:2.0.5-alt1_6jpp7
- update

* Thu Aug 07 2014 Igor Vlasenko <viy@altlinux.ru> 0:2.0.4-alt3_2jpp7
- rebuild with maven-local

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 0:2.0.4-alt2_2jpp7
- NMU rebuild to move poms and fragments

* Thu Sep 06 2012 Igor Vlasenko <viy@altlinux.ru> 0:2.0.4-alt1_2jpp7
- new version

* Fri Mar 30 2012 Igor Vlasenko <viy@altlinux.ru> 0:2.0.2-alt1_1jpp7
- complete build

* Thu Mar 08 2012 Igor Vlasenko <viy@altlinux.ru> 0:2.0.2-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

