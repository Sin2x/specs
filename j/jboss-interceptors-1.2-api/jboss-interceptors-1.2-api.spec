Group: Development/Java
BuildRequires: /proc rpm-build-java
BuildRequires: jpackage-11-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
# %%version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define version 1.0.1
%global namedreltag .Final
%global namedversion %{version}%{?namedreltag}
%global oname jboss-interceptors-api_1.2_spec

Name:          jboss-interceptors-1.2-api
Version:       1.0.1
Release:       alt1_2jpp11
Summary:       Java EE Interceptors 1.2 API
License:       CDDL or GPLv2 with exceptions
URL:           https://github.com/jboss/jboss-interceptors-api_spec
Source0:       %{url}/archive/%{oname}-%{namedversion}.tar.gz

BuildRequires: maven-local
BuildRequires: mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires: mvn(org.apache.maven.plugins:maven-source-plugin)
BuildRequires: mvn(org.jboss:jboss-parent:pom:)

BuildArch:     noarch
Source44: import.info

%description
The Java EE  Interceptors 1.2 API classes from JSR 318.

%package javadoc
Group: Development/Java
Summary:       Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q -n jboss-interceptors-api_spec-%{oname}-%{namedversion}

# Fix incorrect-fsf-address
sed -i "s,59,51,;s,Temple Place,Franklin Street,;s,Suite 330,Fifth Floor,;s,02111-1307,02110-1301," LICENSE

%mvn_file :%{oname} %{name}

%build

%mvn_build -- -Dmaven.compile.source=1.8 -Dmaven.compile.target=1.8 -Dmaven.javadoc.source=1.8

%install
%mvn_install

%files -f .mfiles
%doc README
%doc --no-dereference LICENSE

%files javadoc -f .mfiles-javadoc
%doc --no-dereference LICENSE

%changelog
* Thu Apr 29 2021 Igor Vlasenko <viy@altlinux.org> 1.0.1-alt1_2jpp11
- new version

* Sat May 25 2019 Igor Vlasenko <viy@altlinux.ru> 1.0.0-alt1_10jpp8
- new version

* Tue Feb 05 2019 Igor Vlasenko <viy@altlinux.ru> 1.0.0-alt1_9jpp8
- fc29 update

* Thu Apr 19 2018 Igor Vlasenko <viy@altlinux.ru> 1.0.0-alt1_8jpp8
- java update

* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 1.0.0-alt1_7jpp8
- fc27 update

* Sun Oct 22 2017 Igor Vlasenko <viy@altlinux.ru> 1.0.0-alt1_6jpp8
- new jpp release

* Fri Dec 16 2016 Igor Vlasenko <viy@altlinux.ru> 1.0.0-alt1_5jpp8
- new fc release

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 1.0.0-alt1_4jpp8
- new fc release

* Mon Feb 01 2016 Igor Vlasenko <viy@altlinux.ru> 1.0.0-alt1_3jpp8
- new version

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 1.0.0-alt1_0.3.Alpha3jpp7
- new release

* Mon Jul 21 2014 Igor Vlasenko <viy@altlinux.ru> 1.0.0-alt1_0.1.Alpha3jpp7
- new version

