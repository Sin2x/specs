%define oldname beust-jcommander
Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires: rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           beust-jcommander1.71
Version:        1.71
Release:        alt2_6jpp8
Summary:        Java framework for parsing command line parameters
License:        ASL 2.0
URL:            http://jcommander.org/
BuildArch:      noarch

# ./generate-tarball.sh
Source0:        %{oldname}-%{version}.tar.gz
# Adapted from earlier version that still shipped poms. It uses kobalt for building now
Source1:        %{oldname}.pom
# Cleaned up bundled jars hose licensing cannot be easily verified
Source2:        generate-tarball.sh

Patch0: 0001-ParseValues-NullPointerException-patch.patch 

BuildRequires:  maven-local
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.sonatype.oss:oss-parent:pom:)
BuildRequires:  mvn(org.testng:testng)
Source44: import.info

%description
JCommander is a very small Java framework that makes it trivial to
parse command line parameters (with annotations).

%package javadoc
Group: Development/Java
Summary:        API documentation for %{oldname}
BuildArch: noarch

%description javadoc
This package contains the %{summary}.

%prep
%setup -q -n jcommander-%{version}
%patch0 -p1

chmod -x license.txt
cp -p %SOURCE1 pom.xml
sed -i 's/@VERSION@/%{version}/g' pom.xml

%mvn_compat_version : 1 1.48 %{version}

%build
%mvn_file : %{oldname}
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc license.txt notice.md README.markdown

%files javadoc -f .mfiles-javadoc
%doc license.txt notice.md

%changelog
* Wed May 12 2021 Igor Vlasenko <viy@altlinux.org> 1.71-alt2_6jpp8
- compat build

* Mon May 27 2019 Igor Vlasenko <viy@altlinux.ru> 1.71-alt1_6jpp8
- new version

* Sun Apr 15 2018 Igor Vlasenko <viy@altlinux.ru> 1.71-alt1_3jpp8
- java update

* Sat Nov 18 2017 Igor Vlasenko <viy@altlinux.ru> 1.71-alt1_2jpp8
- new version

* Wed Oct 18 2017 Igor Vlasenko <viy@altlinux.ru> 1.65-alt1_1jpp8
- new jpp release

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 1.47-alt1_3jpp8
- new fc release

* Mon Feb 01 2016 Igor Vlasenko <viy@altlinux.ru> 1.47-alt1_2jpp8
- new version

* Fri Jan 29 2016 Igor Vlasenko <viy@altlinux.ru> 1.47-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 1.30-alt2_4jpp7
- new release

* Tue Aug 05 2014 Igor Vlasenko <viy@altlinux.ru> 1.30-alt2_2.2jpp7
- new version

* Tue Aug 05 2014 Igor Vlasenko <viy@altlinux.ru> 1.30-alt1_2.2jpp7
- new version

* Tue Aug 05 2014 Igor Vlasenko <viy@altlinux.ru> 1.30-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

