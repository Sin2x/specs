Group: Development/Other
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
BuildRequires: unzip
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
#

Name:           jline1
Version:        1.0
Release:        alt3_20jpp8
Summary:        Java library for reading and editing user input in console applications
License:        BSD
URL:            http://jline.sourceforge.net/
Source0:        http://download.sourceforge.net/sourceforge/jline/jline-%{version}.zip
Source1:        CatalogManager.properties
Patch1:         jline-0.9.94-crosslink.patch

BuildArch:      noarch

BuildRequires:  maven-local
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)

Requires:       bash sh
# for /bin/stty
Requires:       coreutils
Source44: import.info

# https://bugzilla.redhat.com/show_bug.cgi?id=1022939

%description
JLine is a java library for reading and editing user input in console
applications. It features tab-completion, command history, password
masking, configurable key-bindings, and pass-through handlers to use to
chain to other console applications.

%package        demo
Group: Development/Java
Summary:        Demos for %{name}
Requires:       %{name} = %{version}-%{release}

%description    demo
Demonstrations and samples for %{name}.

%package        javadoc
Group: Development/Java
Summary:        Javadoc for %{name}
BuildArch: noarch

%description    javadoc
Javadoc for %{name}.

%prep
%setup -q -n jline-%{version}
%patch1 -p1

# Make sure upstream hasn't sneaked in any jars we don't know about
find -name '*.class' -exec rm -f '{}' \;
find -name '*.jar' -exec rm -f '{}' \;

# Remove pre-built Windows-only binary artifacts
rm src/src/main/resources/jline/jline*.dll

# Use locally installed DTDs
mkdir build
cp -p %{SOURCE1} build/

%build
# Use locally installed DTDs
export CLASSPATH=%{_builddir}/%{name}-%{version}/build

mv src tmp
mv tmp/* .

%mvn_compat_version : %{version} 1
%mvn_build

%install
%mvn_install

%files -f .mfiles
# there is native code in sources but only for Windows
%dir %{_jnidir}/%{name}
%doc LICENSE.txt src/main/resources/jline/keybindings.properties

%files javadoc -f .mfiles-javadoc
%doc LICENSE.txt

%changelog
* Fri Oct 09 2020 Igor Vlasenko <viy@altlinux.ru> 1.0-alt3_20jpp8
- update

* Sat May 25 2019 Igor Vlasenko <viy@altlinux.ru> 1.0-alt3_18jpp8
- new version

* Tue Feb 05 2019 Igor Vlasenko <viy@altlinux.ru> 1.0-alt3_17jpp8
- fc29 update

* Thu Apr 19 2018 Igor Vlasenko <viy@altlinux.ru> 1.0-alt3_16jpp8
- java update

* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 1.0-alt3_15jpp8
- fc27 update

* Sun Oct 22 2017 Igor Vlasenko <viy@altlinux.ru> 1.0-alt3_14jpp8
- new jpp release

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 1.0-alt3_12jpp8
- new fc release

* Thu Feb 11 2016 Igor Vlasenko <viy@altlinux.ru> 1.0-alt3_11jpp8
- %%_jnidir set to /usr/lib/java

* Wed Feb 03 2016 Igor Vlasenko <viy@altlinux.ru> 1.0-alt2_11jpp8
- manual jni fix

* Wed Feb 03 2016 Igor Vlasenko <viy@altlinux.ru> 1.0-alt1_11jpp8
- java 8 mass update

