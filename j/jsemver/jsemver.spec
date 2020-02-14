Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
BuildRequires: /proc rpm-build-java
BuildRequires: jpackage-1.8-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           jsemver
Version:        0.9.0
Release:        alt1_11jpp8
Summary:        A Java implementation of the Semantic Versioning Specification

License:        MIT
URL:            https://github.com/zafarkhaja/jsemver
Source0:        https://github.com/zafarkhaja/jsemver/archive/%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  maven-local
BuildRequires:  maven-compiler-plugin >= 3.2
BuildRequires:  maven-javadoc-plugin >= 2.10.2
BuildRequires:  junit >= 4.12
BuildRequires:  mvn(org.sonatype.oss:oss-parent:pom:)
Source44: import.info

%description
JSemVer (formerly Java SemVer) is a Java implementation of
version 2.0.0 of the Semantic Versioning Specification

%package javadoc
Group: Development/Java
Summary:        Javadocs for %{name}
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}

%prep
%setup -q
find -name \*.jar -delete
find -name \*.class -delete

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%dir %{_javadir}/%{name}
%dir %{_mavenpomdir}/%{name}
%doc CHANGELOG.md
%doc README.md
%doc --no-dereference LICENSE

%files javadoc -f .mfiles-javadoc
%doc --no-dereference LICENSE


%changelog
* Wed Jan 29 2020 Igor Vlasenko <viy@altlinux.ru> 0.9.0-alt1_11jpp8
- fc update

* Sun May 26 2019 Igor Vlasenko <viy@altlinux.ru> 0.9.0-alt1_9jpp8
- new version

* Tue Feb 05 2019 Igor Vlasenko <viy@altlinux.ru> 0.9.0-alt1_8jpp8
- fc29 update

* Thu Apr 19 2018 Igor Vlasenko <viy@altlinux.ru> 0.9.0-alt1_7jpp8
- java update

* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 0.9.0-alt1_6jpp8
- fc27 update

* Sun Oct 22 2017 Igor Vlasenko <viy@altlinux.ru> 0.9.0-alt1_5jpp8
- new jpp release

* Tue Dec 06 2016 Igor Vlasenko <viy@altlinux.ru> 0.9.0-alt1_3jpp8
- new version

