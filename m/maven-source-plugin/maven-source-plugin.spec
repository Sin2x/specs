Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires: unzip
# END SourceDeps(oneline)
BuildRequires: /proc rpm-build-java
BuildRequires: jpackage-1.8-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           maven-source-plugin
Summary:        Plugin creating source JAR
Version:        3.1.0
Release:        alt1_2jpp8
License:        ASL 2.0

URL:            http://maven.apache.org/plugins/maven-source-plugin/
Source0:        http://repo1.maven.org/maven2/org/apache/maven/plugins/%{name}/%{version}/%{name}-%{version}-source-release.zip

BuildArch:      noarch

BuildRequires:  maven-local
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(org.apache.maven:maven-archiver)
BuildRequires:  mvn(org.apache.maven:maven-compat)
BuildRequires:  mvn(org.apache.maven:maven-core)
BuildRequires:  mvn(org.apache.maven:maven-model)
BuildRequires:  mvn(org.apache.maven:maven-plugin-api)
BuildRequires:  mvn(org.apache.maven.plugins:maven-plugin-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-plugins:pom:)
BuildRequires:  mvn(org.apache.maven.plugin-testing:maven-plugin-testing-harness)
BuildRequires:  mvn(org.apache.maven.plugin-tools:maven-plugin-annotations)
BuildRequires:  mvn(org.codehaus.plexus:plexus-archiver)
Source44: import.info

%description
The Maven Source Plugin creates a JAR archive of the
source files of the current project.


%package        javadoc
Group: Development/Java
Summary:        Javadoc for %{name}
BuildArch: noarch

%description    javadoc
API documentation for %{name}.


%prep
%setup -q


%build
%mvn_file : %{name}
%mvn_build


%install
%mvn_install


%files -f .mfiles
%doc --no-dereference LICENSE NOTICE

%files javadoc -f .mfiles-javadoc
%doc --no-dereference LICENSE NOTICE


%changelog
* Fri Oct 09 2020 Igor Vlasenko <viy@altlinux.ru> 3.1.0-alt1_2jpp8
- new version

* Sun May 26 2019 Igor Vlasenko <viy@altlinux.ru> 3.0.1-alt1_6jpp8
- new version

* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 3.0.1-alt1_3jpp8
- fc27 update

* Sun Oct 22 2017 Igor Vlasenko <viy@altlinux.ru> 3.0.1-alt1_2jpp8
- new jpp release

* Fri Dec 16 2016 Igor Vlasenko <viy@altlinux.ru> 3.0.1-alt1_1jpp8
- new version

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 2.4-alt1_4jpp8
- new fc release

* Mon Feb 01 2016 Igor Vlasenko <viy@altlinux.ru> 2.4-alt1_3jpp8
- new version

* Tue Jan 26 2016 Igor Vlasenko <viy@altlinux.ru> 2.4-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 2.2.1-alt1_6jpp7
- new release

* Mon Aug 25 2014 Igor Vlasenko <viy@altlinux.ru> 2.2.1-alt1_5jpp7
- new version

* Thu Aug 07 2014 Igor Vlasenko <viy@altlinux.ru> 2.1.2-alt3_8jpp7
- rebuild with maven-local

* Fri Jul 18 2014 Igor Vlasenko <viy@altlinux.ru> 2.1.2-alt2_8jpp7
- fixed build

* Mon Oct 01 2012 Igor Vlasenko <viy@altlinux.ru> 2.1.2-alt1_8jpp7
- new fc release

* Mon Mar 26 2012 Igor Vlasenko <viy@altlinux.ru> 2.1.2-alt1_7jpp7
- complete build

* Thu Mar 08 2012 Igor Vlasenko <viy@altlinux.ru> 2.1.2-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

