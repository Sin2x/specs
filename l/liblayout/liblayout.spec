Group: System/Libraries
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
BuildRequires: unzip
# END SourceDeps(oneline)
BuildRequires: /proc rpm-build-java
BuildRequires: jpackage-1.8-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name: liblayout
Version: 0.2.10
Release: alt1_20jpp8
Summary: CSS based layouting framework
License: LGPLv2+ and UCD
Source: http://downloads.sourceforge.net/jfreereport/liblayout-%{version}.zip
URL: http://reporting.pentaho.org/
BuildRequires: ant jpackage-utils flute libloader
BuildRequires: librepository pentaho-libxml libfonts sac libbase >= 1.1.3
Requires: jpackage-utils flute libloader >= 1.1.3
Requires: librepository >= 1.1.3 libfonts >= 1.1.3 sac
Requires: pentaho-libxml libbase >= 1.0.0
BuildArch: noarch
Source44: import.info

%description
LibLayout is a layouting framework. It is based on the Cascading StyleSheets
standard. The layouting expects to receive its content as a DOM structure
(although it does not rely on the W3C-DOM API).

%package javadoc
Group: Development/Documentation
Summary: Javadoc for %{name}
Requires: %{name} = %{version}-%{release}
Requires: jpackage-utils
BuildArch: noarch

%description javadoc
Javadoc for %{name}.

%prep
%setup -q -c
find . -name "*.jar" -exec rm -f {} \;
mkdir -p lib
build-jar-repository -s -p lib flute libloader librepository libxml libfonts \
    sac libbase commons-logging-api

%build
ant jar javadoc
for file in README.txt licence-LGPL.txt ChangeLog.txt; do
    tr -d '\r' < $file > $file.new
    mv $file.new $file
done

%install

mkdir -p $RPM_BUILD_ROOT%{_javadir}
cp -p build/lib/%{name}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}.jar

mkdir -p $RPM_BUILD_ROOT%{_javadocdir}/%{name}
cp -rp build/api $RPM_BUILD_ROOT%{_javadocdir}/%{name}

%files
%doc licence-LGPL.txt README.txt ChangeLog.txt
%{_javadir}/*.jar

%files javadoc
%{_javadocdir}/%{name}

%changelog
* Sat Feb 15 2020 Igor Vlasenko <viy@altlinux.ru> 0.2.10-alt1_20jpp8
- fc update

* Mon May 27 2019 Igor Vlasenko <viy@altlinux.ru> 0.2.10-alt1_18jpp8
- new version

* Mon Apr 16 2018 Igor Vlasenko <viy@altlinux.ru> 0.2.10-alt1_15jpp8
- java update

* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 0.2.10-alt1_14jpp8
- fc27 update

* Tue Oct 17 2017 Igor Vlasenko <viy@altlinux.ru> 0.2.10-alt1_13jpp8
- new jpp release

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 0.2.10-alt1_12jpp8
- new fc release

* Tue Feb 02 2016 Igor Vlasenko <viy@altlinux.ru> 0.2.10-alt1_11jpp8
- new version

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 0.2.10-alt1_8jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 0.2.10-alt1_7jpp7
- new release

* Mon Oct 01 2012 Igor Vlasenko <viy@altlinux.ru> 0.2.10-alt1_5jpp7
- new version

