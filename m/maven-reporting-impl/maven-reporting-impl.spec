Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires: unzip
# END SourceDeps(oneline)
BuildRequires: /proc rpm-build-java
BuildRequires: jpackage-1.8-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           maven-reporting-impl
Version:        3.0.0
Release:        alt1_7jpp8
Summary:        Abstract classes to manage report generation
License:        ASL 2.0
URL:            http://maven.apache.org/shared/%{name}
BuildArch:      noarch

Source0:        http://repo1.maven.org/maven2/org/apache/maven/reporting/%{name}/%{version}/%{name}-%{version}-source-release.zip

Patch0:         0001-Remove-dependency-on-junit-addons.patch

BuildRequires:  maven-local
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(org.apache.maven.doxia:doxia-core)
BuildRequires:  mvn(org.apache.maven.doxia:doxia-decoration-model)
BuildRequires:  mvn(org.apache.maven.doxia:doxia-sink-api)
BuildRequires:  mvn(org.apache.maven.doxia:doxia-site-renderer)
BuildRequires:  mvn(org.apache.maven:maven-core)
BuildRequires:  mvn(org.apache.maven:maven-plugin-api)
BuildRequires:  mvn(org.apache.maven.plugin-tools:maven-plugin-annotations)
BuildRequires:  mvn(org.apache.maven.reporting:maven-reporting-api)
BuildRequires:  mvn(org.apache.maven.shared:maven-shared-components:pom:)
BuildRequires:  mvn(org.apache.maven.shared:maven-shared-utils)
BuildRequires:  mvn(org.codehaus.plexus:plexus-utils)
Source44: import.info

%description
Abstract classes to manage report generation, which can be run both:

* as part of a site generation (as a maven-reporting-api's MavenReport),
* or as a direct standalone invocation (as a maven-plugin-api's Mojo).

This is a replacement package for maven-shared-reporting-impl

%package javadoc
Group: Development/Java
Summary:        Javadoc for %{name}
BuildArch: noarch
    
%description javadoc
API documentation for %{name}.

%prep
%setup -q
%patch0 -p1

# integration tests try to download stuff from the internet
# and therefore they don't work in Koji
%pom_remove_plugin :maven-invoker-plugin

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc LICENSE NOTICE

%files javadoc -f .mfiles-javadoc
%doc LICENSE NOTICE

%changelog
* Sat Feb 15 2020 Igor Vlasenko <viy@altlinux.ru> 3.0.0-alt1_7jpp8
- fc update

* Mon May 27 2019 Igor Vlasenko <viy@altlinux.ru> 3.0.0-alt1_5jpp8
- new version

* Thu Nov 23 2017 Igor Vlasenko <viy@altlinux.ru> 3.0.0-alt1_1jpp8
- new version

* Tue Nov 14 2017 Igor Vlasenko <viy@altlinux.ru> 2.4-alt1_4jpp8
- fc27 update

* Sun Oct 22 2017 Igor Vlasenko <viy@altlinux.ru> 2.4-alt1_3jpp8
- new jpp release

* Fri Nov 25 2016 Igor Vlasenko <viy@altlinux.ru> 2.4-alt1_2jpp8
- new version

* Sun Feb 07 2016 Igor Vlasenko <viy@altlinux.ru> 2.3-alt1_2jpp8
- unbootsrap build

* Fri Jan 22 2016 Igor Vlasenko <viy@altlinux.ru> 2.3-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Mon Aug 25 2014 Igor Vlasenko <viy@altlinux.ru> 2.2-alt1_5jpp7
- new release

* Mon Aug 25 2014 Igor Vlasenko <viy@altlinux.ru> 2.2-alt1_0jpp7
- new version

