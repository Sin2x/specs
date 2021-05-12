Epoch: 0
Group: Development/Java
BuildRequires: /proc rpm-build-java
BuildRequires: jpackage-1.8-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           plexus-build-api
Version:        0.0.7
Release:        alt3_27jpp8
Summary:        Plexus Build API
License:        ASL 2.0
URL:            https://github.com/sonatype/sisu-build-api
BuildArch:      noarch

#Fetched from https://github.com/sonatype/sisu-build-api/tarball/plexus-build-api-0.0.7
Source0:        sonatype-sisu-build-api-plexus-build-api-0.0.7-0-g883ea67.tar.gz
Source1:        http://www.apache.org/licenses/LICENSE-2.0.txt

# Forwarded upstream: https://github.com/sonatype/sisu-build-api/pull/2
Patch0:         %{name}-migration-to-component-metadata.patch

# Port to plexus-utils 3.3.0 (implement a dummy method)
Patch1:         %{name}-utils-3.3.0.patch

BuildRequires:  maven-local
BuildRequires:  mvn(org.codehaus.plexus:plexus-component-metadata)
BuildRequires:  mvn(org.codehaus.plexus:plexus-container-default)
BuildRequires:  mvn(org.codehaus.plexus:plexus-utils) >= 3.3.0
Source44: import.info

%description
Plexus Build API

%package javadoc
Group: Development/Java
Summary:        Javadoc for %{name}
BuildArch: noarch

%description javadoc
API documentation for %{name}.

%prep
%setup -q -n sonatype-sisu-build-api-f1f8849
cp -p %{SOURCE1} .

%patch0 -p1
%patch1 -p1

# remove unnecessary dependency on parent POM
%pom_remove_parent

%mvn_file : plexus/%{name}

%pom_xpath_remove "pom:build/pom:plugins/pom:plugin[pom:artifactId='maven-compiler-plugin']/pom:configuration"

%build
%mvn_build -- -Dmaven.compiler.source=1.6 -Dmaven.compiler.target=1.6

%install
%mvn_install

%files -f .mfiles
%doc LICENSE-2.0.txt

%files javadoc -f .mfiles-javadoc
%doc LICENSE-2.0.txt

%changelog
* Wed May 12 2021 Igor Vlasenko <viy@altlinux.org> 0:0.0.7-alt3_27jpp8
- fc update

* Tue Mar 31 2020 Igor Vlasenko <viy@altlinux.ru> 0:0.0.7-alt3_23jpp8
- fc update

* Sun May 26 2019 Igor Vlasenko <viy@altlinux.ru> 0:0.0.7-alt3_22jpp8
- new version

* Tue May 08 2018 Igor Vlasenko <viy@altlinux.ru> 0:0.0.7-alt3_20jpp8
- java update

* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 0:0.0.7-alt3_18jpp8
- fc27 update

* Sun Oct 22 2017 Igor Vlasenko <viy@altlinux.ru> 0:0.0.7-alt3_17jpp8
- new jpp release

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 0:0.0.7-alt3_16jpp8
- new fc release

* Wed Feb 03 2016 Igor Vlasenko <viy@altlinux.ru> 0:0.0.7-alt3_15jpp8
- new version

* Fri Jan 22 2016 Igor Vlasenko <viy@altlinux.ru> 0:0.0.7-alt2jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 0:0.0.7-alt1_9jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 0:0.0.7-alt1_8jpp7
- new release

* Mon Oct 01 2012 Igor Vlasenko <viy@altlinux.ru> 0:0.0.7-alt1_4jpp7
- new fc release

* Tue Mar 20 2012 Igor Vlasenko <viy@altlinux.ru> 0:0.0.7-alt1_3jpp7
- fc version

* Tue Feb 22 2011 Igor Vlasenko <viy@altlinux.ru> 0:0.0.4-alt2_2jpp6
- added maven2-plugin-resources dep

* Wed Jan 26 2011 Igor Vlasenko <viy@altlinux.ru> 0:0.0.4-alt1_2jpp6
- new jpp release

* Wed Jan 26 2011 Igor Vlasenko <viy@altlinux.ru> 0:0.0.4-alt0.1jpp
- bootstrap

