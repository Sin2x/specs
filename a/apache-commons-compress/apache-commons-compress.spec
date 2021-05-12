Epoch: 0
Group: Development/Java
BuildRequires: /proc rpm-build-java
BuildRequires: jpackage-1.8-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%global base_name       compress
%global short_name      commons-%{base_name}

Name:           apache-%{short_name}
Version:        1.19
Release:        alt1_2jpp8
Summary:        Java API for working with compressed files and archivers
License:        ASL 2.0
URL:            http://commons.apache.org/proper/commons-compress/
BuildArch:      noarch

Source0:        http://archive.apache.org/dist/commons/compress/source/%{short_name}-%{version}-src.tar.gz

Patch0:         0001-Remove-Brotli-compressor.patch
Patch1:         0002-Remove-ZSTD-compressor.patch
Patch2:         0003-Avoid-use-of-internal-Mockito-API.patch

BuildRequires:  maven-local
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(org.apache.commons:commons-parent:pom:)
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-antrun-plugin)
BuildRequires:  mvn(org.mockito:mockito-core)
BuildRequires:  mvn(org.osgi:osgi.core)
BuildRequires:  mvn(org.tukaani:xz)
Source44: import.info

%description
The Apache Commons Compress library defines an API for working with
ar, cpio, Unix dump, tar, zip, gzip, XZ, Pack200 and bzip2 files.
In version 1.14 read-only support for Brotli decompression has been added,
but it has been removed form this package.

%package javadoc
Group: Development/Java
Summary:        API documentation for %{name}
BuildArch: noarch

%description javadoc
This package provides %{summary}.

%prep
%setup -q -n %{short_name}-%{version}-src

# Unavailable Google Brotli library (org.brotli.dec)
%patch0 -p1
%pom_remove_dep org.brotli:dec
rm -r src/{main,test}/java/org/apache/commons/compress/compressors/brotli

# Unavailable ZSTD JNI library
%patch1 -p1
%pom_remove_dep :zstd-jni
rm -r src/{main,test}/java/org/apache/commons/compress/compressors/zstandard
rm src/test/java/org/apache/commons/compress/compressors/DetectCompressorTestCase.java

# Avoid using internal Mockito APIs
%patch2 -p1

# remove osgi tests, we don't have deps for them
%pom_remove_dep org.ops4j.pax.exam:::test
%pom_remove_dep :org.apache.felix.framework::test
%pom_remove_dep :javax.inject::test
%pom_remove_dep :slf4j-api::test
rm src/test/java/org/apache/commons/compress/OsgiITest.java

# use osgi-core instead of felix-osgi-core
%pom_change_dep :org.osgi.core org.osgi:osgi.core

# Remove test that requires powermock
%pom_remove_dep org.powermock:
%pom_add_dep org.mockito:mockito-core::test
rm src/test/java/org/apache/commons/compress/compressors/z/ZCompressorInputStreamTest.java

%build
%mvn_file  : %{short_name} %{name}
%mvn_alias : commons:
%mvn_build -- -Dcommons.osgi.symbolicName=org.apache.commons.compress

%install
%mvn_install

%files -f .mfiles
%doc LICENSE.txt NOTICE.txt

%files javadoc -f .mfiles-javadoc
%doc LICENSE.txt NOTICE.txt

%changelog
* Wed May 12 2021 Igor Vlasenko <viy@altlinux.org> 0:1.19-alt1_2jpp8
- new version

* Fri Oct 09 2020 Igor Vlasenko <viy@altlinux.ru> 0:1.18-alt1_6jpp8
- update

* Fri May 24 2019 Igor Vlasenko <viy@altlinux.ru> 0:1.18-alt1_4jpp8
- new version

* Tue May 15 2018 Igor Vlasenko <viy@altlinux.ru> 0:1.16.1-alt1_1jpp8
- java update

* Thu Nov 23 2017 Igor Vlasenko <viy@altlinux.ru> 0:1.15-alt1_1jpp8
- new version

* Fri Nov 10 2017 Igor Vlasenko <viy@altlinux.ru> 0:1.14-alt1_2jpp8
- new version

* Wed Nov 01 2017 Igor Vlasenko <viy@altlinux.ru> 0:1.13-alt1_2jpp8
- new jpp release

* Fri Dec 16 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.12-alt1_1jpp8
- new version

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.10-alt3_0.3.svn1684406jpp8
- new fc release

* Wed Feb 03 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.10-alt3_0.2.svn1684406jpp8
- new version

* Fri Jan 22 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.10-alt2jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Sat Aug 23 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.5-alt1_1jpp7
- new version

* Thu Aug 21 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.4.1-alt3_2jpp7
- added maven-local BR:

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.4.1-alt2_2jpp7
- NMU rebuild to move poms and fragments

* Sun Sep 09 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.4.1-alt1_2jpp7
- new version

* Fri Dec 10 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.1-alt1_0.r831574.6jpp6
- new version

