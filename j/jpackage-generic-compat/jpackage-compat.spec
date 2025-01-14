Name: jpackage-generic-compat
Version: 0.42
Release: alt1

Summary: ALT to JPackage build compatibility adaptor.
Group: Development/Java
License: GPLv2+ or Apache-2.0 or ALT-Public-Domain
Url: http://www.sisyphus.ru/packages/viy/srpms

BuildArch: noarch

%define jpackage_common_requires \
Requires(pre): rpm-build-java \
Requires: /proc \
Requires: java-stub-javadoc

Requires: java-devel java-headless java
#Requires: java-javadoc
%jpackage_common_requires

%description
JPackage compatibility package. The main goal is to provide all nessssary
symlinks, Requires and BuildRequires for ALTLinux to create a build environment
compatible with JPackage.org.


%package -n jpackage-1.8-compat
Summary: JPackage build environment with java-1.8.0.
Group: Development/Java

# does not work
#Requires(pre): java-devel >= 0:1.8.0 java >= 0:1.8.0
#Requires(pre): java-javadoc >= 0:1.8.0
# does work
Requires(pre): java-1.8.0-openjdk-devel
#Requires(pre): java-1.8.0-openjdk-javadoc-zip
# hack
Conflicts: java-devel > 1.8.99 java > 1.8.99 java-headless > 1.8.99
#java-javadoc > 1.8.99

#Requires: jpackage-generic-compat
%jpackage_common_requires
Obsoletes: jpackage-1.7-compat < %version
Obsoletes: jpackage-1.7.0-compat < %version

%description -n jpackage-1.8-compat
JPackage compatibility package. the main goal is to provide all nessssary symlinks,
Requires and BuildRequires for ALT to be build compatible with JPackage.
Provides JPackage build environment with java-1.8.0.

%package -n jpackage-11-compat
Summary: JPackage build environment with java-11.
Group: Development/Java
Obsoletes: jpackage-9-compat < %version
Obsoletes: jpackage-10-compat < %version
Provides: jpackage-default = %version-%release
Provides: jpackage-11 = %version-%release

Requires(pre): java-11-devel >= 11 java-11
#Requires(pre): java-11-openjdk-javadoc-zip
# hack
Conflicts: java-devel > 11.99 java > 11.99 java-headless > 11.99 java-javadoc > 11.99
Conflicts: maven-local-openjdk8
Conflicts: maven-local-openjdk17
Conflicts: maven-openjdk8
Conflicts: maven-openjdk17
#Requires: jpackage-generic-compat
%jpackage_common_requires

%description -n jpackage-11-compat
JPackage compatibility package. the main goal is to provide all nessssary symlinks,
Requires and BuildRequires for ALT to be build compatible with JPackage.
Provides JPackage build environment with java-11.

%prep

%build

%install
install -d $RPM_BUILD_ROOT%_datadir

%files -n jpackage-generic-compat
%files -n jpackage-1.8-compat
%files -n jpackage-11-compat

%changelog
* Sun Jun 12 2022 Igor Vlasenko <viy@altlinux.org> 0.42-alt1
- added jpackage-11 provides

* Thu Jun 09 2022 Igor Vlasenko <viy@altlinux.org> 0.41-alt1
- added Conflicts for maven-openjdkXX

* Wed Jun 08 2022 Igor Vlasenko <viy@altlinux.org> 0.40-alt1
- added Conflicts for maven-local-openjdkXX

* Wed Sep 01 2021 Igor Vlasenko <viy@altlinux.org> 0.39-alt1
- restored jpackage-generic-compat dependency on latest jvm

* Thu Aug 26 2021 Igor Vlasenko <viy@altlinux.org> 0.38-alt1
- jpackage-generic-compat no more common

* Sat Aug 14 2021 Igor Vlasenko <viy@altlinux.org> 0.37-alt1
- dropped jpackage-compat

* Fri Jul 02 2021 Igor Vlasenko <viy@altlinux.org> 0.36-alt1
- dropped requires on unzip

* Tue Jun 22 2021 Igor Vlasenko <viy@altlinux.org> 0.35-alt1
- added jpackage-default
- removed unused jpackage-9,10-compat

* Fri Jun 18 2021 Igor Vlasenko <viy@altlinux.org> 0.34-alt1
- dropped requires on jpackage-utils

* Tue Jun 15 2021 Igor Vlasenko <viy@altlinux.org> 0.33-alt1
- dropped requires on zip

* Tue Jun 15 2021 Igor Vlasenko <viy@altlinux.org> 0.32-alt1
- dropped requires on docbook-style-xsl

* Thu Jun 10 2021 Igor Vlasenko <viy@altlinux.org> 0.31-alt1
- cleaned up obsolete subpackages

* Thu Jul 11 2019 Igor Vlasenko <viy@altlinux.ru> 0.30-alt1
- java 11 support

* Thu Apr 12 2018 Igor Vlasenko <viy@altlinux.ru> 0.29-alt1
- cleaned up BuildRequires.

* Thu Apr 05 2018 Igor Vlasenko <viy@altlinux.ru> 0.28-alt1
- made noarch; removed java7 environment

* Thu Feb 01 2018 Igor Vlasenko <viy@altlinux.ru> 0.27-alt1
- removed java 5/6 support

* Thu Jan 21 2016 Igor Vlasenko <viy@altlinux.ru> 0.26-alt1
- selected java8 as default

* Thu Jan 21 2016 Igor Vlasenko <viy@altlinux.ru> 0.25-alt1
- preparation for java-1.8.0
- TODO: set upper limits for java-1.8.0 when it will be released

* Mon Mar 11 2013 Igor Vlasenko <viy@altlinux.ru> 0.24-alt1
- efficient arch hack (using arch-dependent provides)

* Sun Mar 10 2013 Igor Vlasenko <viy@altlinux.ru> 0.23-alt1
- package is arch specific due to arm support

* Tue Mar 05 2013 Igor Vlasenko <viy@altlinux.ru> 0.22-alt1
- arm support (thanks to sbolshakov@)

* Thu Jan 17 2013 Igor Vlasenko <viy@altlinux.ru> 0.21-alt1
- moved compat symlink into docbook-style-xsl

* Thu Oct 04 2012 Igor Vlasenko <viy@altlinux.ru> 0.20-alt1
- dropped jpackage-*-core

* Sun Sep 30 2012 Igor Vlasenko <viy@altlinux.ru> 0.19-alt1
- dropped ant-antlr from greneric environment

* Wed Mar 14 2012 Igor Vlasenko <viy@altlinux.ru> 0.18-alt1
- selected java7 as default

* Mon Apr 11 2011 Igor Vlasenko <viy@altlinux.ru> 0.17-alt2
- fixed misprint thanks to manowar@

* Wed Mar 09 2011 Igor Vlasenko <viy@altlinux.ru> 0.17-alt1
- added jpackage-1.5.0-core/jpackage-1.6-core subpackages

* Tue Oct 26 2010 Igor Vlasenko <viy@altlinux.ru> 0.16-alt5.6
- restored java6 defaults

* Tue Oct 26 2010 Igor Vlasenko <viy@altlinux.ru> 0.16-alt5.5
- temporary selected java5 as default

* Sat Sep 18 2010 Igor Vlasenko <viy@altlinux.ru> 0.16-alt5.4
- restored java6 defaults

* Sat Sep 18 2010 Igor Vlasenko <viy@altlinux.ru> 0.16-alt5.3
- temporary selected java5 as default

* Thu Sep 16 2010 Igor Vlasenko <viy@altlinux.ru> 0.16-alt5.2
- restored java6 defaults

* Thu Sep 16 2010 Igor Vlasenko <viy@altlinux.ru> 0.16-alt5.1
- temporary selected java5 as default

* Fri Jul 30 2010 Igor Vlasenko <viy@altlinux.ru> 0.16-alt5
- selected java6 as default

* Sun May 30 2010 Igor Vlasenko <viy@altlinux.ru> 0.16-alt4
- restored java5 defaults

* Fri May 21 2010 Igor Vlasenko <viy@altlinux.ru> 0.16-alt3
- temporary selected java6 as default

* Tue May 18 2010 Igor Vlasenko <viy@altlinux.ru> 0.16-alt2
- restored java5 defaults

* Mon May 17 2010 Igor Vlasenko <viy@altlinux.ru> 0.16-alt1
- removed obsolete jpackage-1.4.2-compat subpackage
- added jpackage-1.5.0-compat subpackage
- temporary switched default compiler to java6

* Mon May 10 2010 Igor Vlasenko <viy@altlinux.ru> 0.15-alt6
- restored java5 defaults

* Sat May 08 2010 Igor Vlasenko <viy@altlinux.ru> 0.15-alt5
- temporary switched default compiler to java6

* Sun Feb 21 2010 Igor Vlasenko <viy@altlinux.ru> 0.15-alt4
- restored java5 defaults

* Sun Feb 21 2010 Igor Vlasenko <viy@altlinux.ru> 0.15-alt3
- temporary switched default compiler to java6

* Mon Oct 05 2009 Igor Vlasenko <viy@altlinux.ru> 0.15-alt2
- tambourine dance around /usr/share/xml/docbook/xsl-stylesheets 
  auto dependency // does not resolved in hasher :(

* Sun Oct 04 2009 Igor Vlasenko <viy@altlinux.ru> 0.15-alt1
- added requires: on rpm-build-java

* Mon Jun 15 2009 Igor Vlasenko <viy@altlinux.ru> 0.14-alt1
- added /usr/share/sgml/docbook/xsl-stylesheets symlink
  TODO: move it to  docbook-style-xsl someday

* Wed Feb 25 2009 Igor Vlasenko <viy@altlinux.ru> 0.13-alt1
- added ant-nodeps to generic environment

* Sun Aug 10 2008 Igor Vlasenko <viy@altlinux.ru> 0.12-alt3
- Added Requires: /proc

* Fri Aug 01 2008 Igor Vlasenko <viy@altlinux.ru> 0.12-alt2
- java-devel is now Required(pre).

* Thu Jul 24 2008 Igor Vlasenko <viy@altlinux.ru> 0.12-alt1
- added jpackage-1.4.2-compat
- added Provides: jpackage-compat (for default compiler choice)

* Wed Jun 25 2008 Igor Vlasenko <viy@altlinux.ru> 0.11-alt1
- removed jpackage-1.4-compat (provides by jpackage-1.5-compat)

* Mon Apr 28 2008 Igor Vlasenko <viy@altlinux.ru> 0.10-alt1
- added gnu-crypto-sasl-jdk1.4 to jpackage-1.4-compat

* Fri Nov 30 2007 Igor Vlasenko <viy@altlinux.ru> 0.09-alt1
- consolidated jpackage-*-compat's into one spec
- added zip to environment
- added jpackage-1.6-compat 

* Tue Jul 03 2007 Igor Vlasenko <viy@altlinux.ru> 0.08-alt1
- added 'generic' subpackage
- removed hack for ant-apache-bcf

* Tue Jul 03 2007 Igor Vlasenko <viy@altlinux.ru> 0.07-alt2
- added hack for ant-apache-bcf
- removed hack for ant-apache-resolver

* Fri Jun 08 2007 Igor Vlasenko <viy@altlinux.ru> 0.07-alt1
- added java-javadoc dependency

* Thu May 24 2007 Igor Vlasenko <viy@altlinux.ru> 0.06-alt3
- added hack for ant-apache-resolver (and company)

* Wed May 23 2007 Igor Vlasenko <viy@altlinux.ru> 0.06-alt2
- Requires: ant-trax

* Tue May 22 2007 Igor Vlasenko <viy@altlinux.ru> 0.06-alt1
- Requires: ant-junit ant-antlr
- removed xerces-j/xni hack

* Sat May 19 2007 Igor Vlasenko <viy@altlinux.ru> 0.05-alt2
- removed ant hack (thanks to damir@ for fix)
- added xerces-j/xni hack (waiting for Eugene (eostapets@) to fix)

* Wed May 09 2007 Igor Vlasenko <viy@altlinux.ru> 0.05-alt1
- added quick hack around ant compatibility

* Fri Apr 27 2007 Igor Vlasenko <viy@altlinux.ru> 0.04-alt2
- added explicit /proc

* Fri Apr 27 2007 Igor Vlasenko <viy@altlinux.ru> 0.04-alt1
- added requires: ant

* Sat Apr 21 2007 Igor Vlasenko <viy@altlinux.ru> 0.03-alt1
- removed fake xerces-j2 (moved to jpackage-1.5-compat)
- changed dependencies to get java-1.4

* Sat Apr 21 2007 Igor Vlasenko <viy@altlinux.ru> 0.02-alt1
- added conflict to java-devel 1.6

* Sat Mar 24 2007 Igor Vlasenko <viy@altlinux.ru> 0.01-alt1
- initial build.
