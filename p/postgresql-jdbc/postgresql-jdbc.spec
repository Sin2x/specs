Epoch: 0
Group: Databases
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
BuildRequires: /proc rpm-build-java
BuildRequires: jpackage-1.8-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
# Copyright (c) 2000-2005, JPackage Project
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
#
# 1. Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
# 2. Redistributions in binary form must reproduce the above copyright
#    notice, this list of conditions and the following disclaimer in the
#    documentation and/or other materials provided with the
#    distribution.
# 3. Neither the name of the JPackage Project nor the names of its
#    contributors may be used to endorse or promote products derived
#    from this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
# A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
# OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
# SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
# LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
# DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
# THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.


# Configuration for rpmbuild, might be specified by options
# like e.g. 'rpmbuild --define "runselftest 0"'.

# =============================================================================
# IMPORTANT NOTE: This spec file is maintained on two places -- in native
# Fedora repo [1] and in pgjdbc upstream [2].  Please, keep that in sync
# (manual effort!) so both Fedora and Upstream can benefit from automatic
# packaging CI, this is now done in [3] Copr project.
# [1] https://src.fedoraproject.org/rpms/postgresql-jdbc
# [2] https://github.com/pgjdbc/pgjdbc/tree/master/packaging/rpm
# [3] https://copr.fedorainfracloud.org/coprs/g/pgjdbc/pgjdbc-travis/
# ============================================================================

%{!?runselftest:%global runselftest 0}

%global section		devel
%global source_path	pgjdbc/src/main/java/org/postgresql

Summary:	JDBC driver for PostgreSQL
Name:		postgresql-jdbc
Version:  42.2.16
Release:	alt1_1jpp8
License:	BSD
URL:		http://jdbc.postgresql.org/

Source0:	https://repo1.maven.org/maven2/org/postgresql/postgresql/%{version}/postgresql-%{version}-jdbc-src.tar.gz
Provides:	pgjdbc = %version-%release

BuildArch:	noarch
BuildRequires:	maven-local
BuildRequires:	maven-javadoc-plugin
BuildRequires:	java-comment-preprocessor
BuildRequires:	maven-enforcer-plugin
BuildRequires:	maven-plugin-bundle
BuildRequires:	classloader-leak-test-framework

BuildRequires:	mvn(com.ongres.scram:client)
BuildRequires:	mvn(org.apache.maven.plugins:maven-clean-plugin)
BuildRequires:	mvn(org.apache.maven.surefire:surefire-junit-platform)
BuildRequires:	mvn(org.junit.jupiter:junit-jupiter-api)
BuildRequires:	mvn(org.junit.jupiter:junit-jupiter-engine)
BuildRequires:	mvn(org.junit.jupiter:junit-jupiter-params)
BuildRequires:	mvn(org.junit.vintage:junit-vintage-engine)

%if %runselftest
BuildRequires:	postgresql-contrib
BuildRequires:	postgresql-test-rpm-macros
%endif

# gettext is only needed if we try to update translations
#BuildRequires:	gettext

Obsoletes:	%{name}-parent-poms < 42.2.2-2
Source44: import.info

%description
PostgreSQL is an advanced Object-Relational database management
system. The postgresql-jdbc package includes the .jar files needed for
Java programs to access a PostgreSQL database.


%package javadoc
Group: Development/Java
Summary:	API docs for %{name}
BuildArch: noarch

%description javadoc
This package contains the API Documentation for %{name}.


%prep
%setup -c -q

mv postgresql-%{version}-jdbc-src/* .

# remove any binary libs
find -type f \( -name "*.jar" -or -name "*.class" \) | xargs rm -f

# Build parent POMs in the same Maven call.
%pom_xpath_remove "pom:plugin[pom:artifactId = 'maven-shade-plugin']"

# compat symlink: requested by dtardon (libreoffice), reverts part of
# 0af97ce32de877 commit.
%mvn_file org.postgresql:postgresql %{name}/postgresql %{name} postgresql

# For compat reasons, make Maven artifact available under older coordinates.
%mvn_alias org.postgresql:postgresql postgresql:postgresql


%build
# Ideally we would run "sh update-translations.sh" here, but that results
# in inserting the build timestamp into the generated messages_*.class
# files, which makes rpmdiff complain about multilib conflicts if the
# different platforms don't build in the same minute.  For now, rely on
# upstream to have updated the translations files before packaging.

# Include PostgreSQL testing methods and variables.
%if %runselftest
%postgresql_tests_init

PGTESTS_LOCALE=C.UTF-8

cat <<EOF > build.local.properties
server=localhost
port=$PGTESTS_PORT
database=test
username=test
password=test
privilegedUser=$PGTESTS_ADMIN
privilegedPassword=$PGTESTS_ADMINPASS
preparethreshold=5
loglevel=0
protocolVersion=0
EOF

# Start the local PG cluster.
%postgresql_tests_start
%else
# -f is equal to -Dmaven.test.skip=true
opts="-f"
%endif

%mvn_build $opts --xmvn-javadoc


%install
%mvn_install


%files -f .mfiles
%doc --no-dereference LICENSE
%doc README.md


%files javadoc -f .mfiles-javadoc
%doc --no-dereference LICENSE


%changelog
* Fri Oct 09 2020 Igor Vlasenko <viy@altlinux.ru> 0:42.2.16-alt1_1jpp8
- new version

* Wed Jun 19 2019 Igor Vlasenko <viy@altlinux.ru> 0:42.2.5-alt1_2jpp8
- new version

* Sat Jun 02 2018 Igor Vlasenko <viy@altlinux.ru> 0:42.2.2-alt1_4jpp8
- fc28+ update

* Wed May 16 2018 Igor Vlasenko <viy@altlinux.ru> 0:42.2.1-alt1_2jpp8
- java fc28 update

* Wed Nov 22 2017 Igor Vlasenko <viy@altlinux.ru> 0:42.1.4-alt1_1jpp8
- new version

* Sat Nov 04 2017 Igor Vlasenko <viy@altlinux.ru> 0:9.4.1212-alt1_4jpp8
- new version

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 0:9.4.1200-alt1_3jpp8
- new fc release

* Tue Feb 02 2016 Igor Vlasenko <viy@altlinux.ru> 0:9.4.1200-alt1_2jpp8
- new version

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 0:9.2.1002-alt1_4jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 0:9.2.1002-alt1_2jpp7
- new release

* Wed Feb 13 2013 Igor Vlasenko <viy@altlinux.ru> 0:9.2.1002-alt1_1jpp7
- fc update

* Mon Aug 20 2012 Igor Vlasenko <viy@altlinux.ru> 0:9.1.902-alt1_1jpp7
- new version

* Wed Sep 14 2011 Igor Vlasenko <viy@altlinux.ru> 0:9.1.901-alt1_1jpp6
- update to new release by jppimport

* Sat Mar 12 2011 Igor Vlasenko <viy@altlinux.ru> 0:9.0.801-alt1_1jpp6
- new jpp release

* Sun Feb 21 2010 Igor Vlasenko <viy@altlinux.ru> 0:8.3.604-alt1_1jpp5
- new jpackage release

* Fri Nov 02 2007 Igor Vlasenko <viy@altlinux.ru> 0:8.1.407-alt1_2jpp1.7
- converted from JPackage by jppimport script

