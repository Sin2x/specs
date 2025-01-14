%define _unpackaged_files_terminate_build 1

# LTO causes errors, disable it
%global optflags_lto %nil

%def_enable bootstrap
%def_disable ibmlibs
%set_verify_elf_method no

# stable branches support uses this macro
%define qIF_ver_lt() %if "%(rpmvercmp '%2' '%1')" > "0"

Name: mono
Version: 6.12.0.147
Release: alt2
Summary: Cross-platform, Open Source, .NET development framework

Group: Development/Other
License: MIT
Url: https://www.mono-project.com

# https://github.com/mono/mono.git
Source: %name-%version.tar

# by running the following command:
# sn -k mono.snk
# Dec 2015 ALT
Source2: mono.snk
Source3: monolite.tar.gz
Source4: mono-cert-sync.filetrigger

# External dependencies (git submodules)
Source5:  %name-%version-external-api-doc-tools.tar
Source6:  %name-%version-external-api-doc-tools-external-Lucene.Net.Light.tar
Source7:  %name-%version-external-api-doc-tools-external-SharpZipLib.tar
Source8:  %name-%version-external-api-snapshot.tar
Source9:  %name-%version-external-aspnetwebstack.tar
Source10: %name-%version-external-bdwgc.tar
Source11: %name-%version-external-bdwgc-libatomic_ops.tar
Source12: %name-%version-external-binary-reference-assemblies.tar
Source13: %name-%version-external-bockbuild.tar
Source14: %name-%version-external-boringssl.tar
Source15: %name-%version-external-cecil.tar
Source16: %name-%version-external-cecil-legacy.tar
Source17: %name-%version-external-corefx.tar
Source18: %name-%version-external-corert.tar
Source19: %name-%version-external-helix-binaries.tar
Source20: %name-%version-external-ikdasm.tar
Source21: %name-%version-external-ikvm.tar
Source22: %name-%version-external-illinker-test-assets.tar
Source23: %name-%version-external-linker.tar
Source24: %name-%version-external-linker-external-cecil.tar
Source25: %name-%version-external-llvm-project.tar
Source26: %name-%version-external-Newtonsoft.Json.tar
Source27: %name-%version-external-nuget-buildtasks.tar
Source28: %name-%version-external-nunit-lite.tar
Source29: %name-%version-external-roslyn-binaries.tar
Source30: %name-%version-external-rx.tar
Source31: %name-%version-external-xunit-binaries.tar

Patch1: %name-alt-linking1.patch
Patch2: %name-alt-linking2.patch
Patch3: %name-alt-monodoc-sourcesdir.patch
Patch4: %name-alt-offline-build.patch
Patch5: %name-alt-make-compat.patch
Patch6: %name-alt-cmake-compat.patch

# Patches from Fedora
Patch101: mono-4.2.1-ppc.patch
Patch103: mono-4.2-fix-winforms-trayicon.patch
Patch104: mono-6.6.0-aarch64.patch
Patch108: mono-5.18.0-sharpziplib-parent-path-traversal.patch
# Fix NRE bug in api-doc-tools: https://github.com/mono/api-doc-tools/pull/464
Patch110: 0001-DocumentationEnumerator.cs-Declare-iface-and-ifaceMe.patch
# Replace new Csharp features with old to allow mdoc to build
# https://github.com/mono/api-doc-tools/pull/463
Patch111: 0001-Replace-new-Csharp-features-with-old-ones.patch
# Reenable mdoc build. To be upstreamed after Patch 10 and 11
Patch112: 0001-Reenable-mdoc.exe-build.patch
# fix issue with conflicts between i686 and x86_64 package (#1853724)
Patch113: mono-6.6.0-fix-multi-arch-issue.patch

BuildRequires(pre): rpm-build-mono >= 2.0
BuildRequires(pre): rpm-build-ubt
BuildRequires(pre): rpm-build-python3
BuildRequires: /proc
BuildRequires: gcc-c++
BuildRequires: cmake
BuildRequires: python3
BuildRequires: gettext-devel
BuildRequires: libgdiplus-devel >= 2.10
BuildRequires: pkg-config
BuildRequires: valgrind-devel
BuildRequires: zlib-devel
BuildRequires: perl-Pod-Usage
BuildRequires: /usr/bin/python3 python3(json)

# Yes, mono actually depends on itself, because
# we deleted the bootstrapping binaries. If you
# need to bootstrap mono, comment out this BuildRequires
# and don't delete the binaries in %%prep.

%if_enabled bootstrap
# for bootstrap, use bundled monolite instead of local mono
%else
BuildRequires: %name-devel-full >= 5.0
%endif

# Interfaces of slightly older versions are required, upstream corrects it by modifying 'Requires'
# TODO: on each upgrade disable and recheck it
%filter_from_requires s/^mono(Microsoft\.Build\.Framework) = 15\.1/mono(Microsoft.Build.Framework) = 14.0/
%filter_from_requires s/^mono(Microsoft\.Build\.Tasks\.Core) = 15\.1\.0\.0/mono(Microsoft.Build.Tasks.Core) = 14.0.0.0/
%filter_from_requires s/^mono(Microsoft\.Build\.Utilities\.Core) = 15\.1\.0\.0/mono(Microsoft.Build.Utilities.Core) = 14.0.0.0/
%filter_from_requires s/^mono(Mono\.Cecil) = 0\.10\.0\.0/mono(Mono.Cecil) = 0.11.1.0/
%filter_from_requires s/^mono(System\.Numerics\.Vectors) = 4\.1/mono(System.Numerics.Vectors) = 4.0/
%filter_from_requires /^mono(System\.Buffers) = .*/d
%filter_from_requires /^mono(System\.Runtime\.CompilerServices\.Unsafe) = .*/d
%filter_from_requires /^mono(System\.Runtime\.Loader) = .*/d

%description
The Mono runtime implements a JIT engine for the ECMA CLI
virtual machine (as well as a byte code interpreter, the
class loader, the garbage collector, threading system and
metadata access libraries.

%package core
Summary: The Mono CIL runtime, suitable for running .NET code
Group: Development/Other
Requires: /proc
Requires: ca-certificates
Conflicts: mono4-core < %EVR
Conflicts: mono < 3.0
Conflicts: mono-mscorlib  < 3.0
Conflicts: monodis < 3.0
Conflicts: libmono < 3.0
Obsoletes: mono4-core
Provides: mono4-core = %EVR

%description core
This package contains the core of the Mono runtime including its
Virtual Machine, Just-in-time compiler, C# compiler, security
tools and libraries (corlib, XML, System.Security, ZipLib,
I18N, Cairo and Mono.*).

%package winfx
Summary: Mono implementation of core WinFX APIs
Group: Development/Other
Requires: %name-core = %EVR
Conflicts: mono4-winfx < %EVR
Obsoletes: mono4-winfx
Provides: mono4-winfx = %EVR

%description winfx
Open source implementation of core WinFX APIs

%package mvc
Summary: Mono implementation of ASP.NET MVC
Group: Development/Other
Requires: %name-dyndata = %EVR
Conflicts: mono4-mvc < %EVR
Obsoletes: mono4-mvc
Provides: mono4-mvc = %EVR

%description mvc
This is the Mono implementation of ASP.NET MVC

%package mvc-devel
Summary: Development files for  ASP.NET MVC
Group: Development/Other
Requires: %name-core = %EVR
Conflicts: mono4-mvc-devel < %EVR
Obsoletes: mono4-mvc-devel
Provides: mono4-mvc-devel = %EVR


%description mvc-devel
This is the Mono implementation of ASP.NET MVC

%package dyndata
Summary: Dynamic data dll for both web and mvc
Group: Development/Other
Requires: %name-core = %EVR
Conflicts: mono4-dyndata < %EVR
Obsoletes: mono4-dyndata
Provides: mono4-dyndata = %EVR

%description dyndata
This is dll needed for implementation of ASP.NET MVC and for web services too

%package full
Summary: full runtime virtual package
Group: Development/Other
Requires: %name-dyndata = %EVR
Requires: %name-data = %EVR
Requires: %name-mvc = %EVR
Requires: %name-extras = %EVR
Requires: %name-winfx = %EVR
Requires: %name-locale-extras = %EVR
Requires: %name-reactive = %EVR
Requires: %name-reactive-winforms = %EVR
Requires: %name-wcf = %EVR
Requires: %name-winforms = %EVR
Requires: %name-data-oracle = %EVR
Requires: %name-data-sqlite = %EVR
%if_enabled ibmlibs
Requires: %name-ibm-data-db2 = %EVR
%endif
Requires: %name-monodoc = %EVR
Requires: %name-mono2-compat = %EVR
Conflicts: mono4-full < %EVR
Obsoletes: mono4-full
Provides: mono4-full = %EVR

%description full
Virtual package containing all non-devel packages from mono

%package devel-full
Summary: full development virtual package
Group:Development/Other
Requires: %name-devel = %EVR
Requires: %name-full = %EVR
Requires: %name-reactive-devel = %EVR
Requires: %name-web-devel = %EVR
Requires: %name-mvc-devel = %EVR
Requires: %name-monodoc-devel = %EVR
Requires: %name-mono2-compat-devel = %EVR
Conflicts: mono4-devel-full < %EVR
Obsoletes: mono4-devel-full
Provides: mono4-devel-full = %EVR
%qIF_ver_lt %ubt_id S1
Conflicts: %name-nunit-devel < %EVR
Obsoletes: %name-nunit-devel
Provides: %name-nunit-devel = %EVR
%endif

%description devel-full
Virtual package containing all devel packages from mono

%package devel
Summary: Development tools for Mono
Group: Development/Other
Requires: %name-core = %EVR
Requires: pkg-config
Requires: glib2-devel
Conflicts: mono4-devel < %EVR
Obsoletes: mono4-devel
Provides: mono4-devel = %EVR
%qIF_ver_lt %ubt_id S1
Conflicts: mono-mcs < %EVR
Provides: mono-mcs = %EVR
Obsoletes: mono-mcs
Requires: rpm-build-mono
%endif

%description devel
This package completes the Mono developer toolchain with the mono profiler,
assembler and other various tools.

%package locale-extras
Summary: Extra locale information for Mono
Group: Development/Other
Requires: %name-core = %EVR
Conflicts: mono4-locale-extras < %EVR
Obsoletes: mono4-locale-extras
Provides: mono4-locale-extras = %EVR

%description locale-extras
This package contains assemblies to support I18N applications for
non-latin alphabets.

%package extras
Summary: Provides the infrastructure for running and building daemons and services with Mono as well as various stub assemblies
Group: Development/Other
Requires: %name-core = %EVR
Conflicts: mono4-extras < %EVR
Obsoletes: mono4-extras
Provides: mono4-extras = %EVR

%description extras
This package provides the library and application to run services
and daemons with Mono. It also includes stubs for the following
assemblies: Microsoft.Vsa,
System.Configuration.Install, System.Management, System.Messaging.

%package reactive
License: MIT and Apache-2.0
Summary: Reactive Extensions for Mono core libraries
Group: Development/Other
Requires: %name-core = %EVR
Conflicts: mono4-reactive < %EVR
Obsoletes: mono4-reactive
Provides: mono4-reactive = %EVR

%description reactive
Reactive Extensions for Mono, this packages don't depend on
desktop-specific features.

%package reactive-winforms
License: MIT and Apache-2.0
Summary: Reactive Extensions for Mono desktop-specific libraries
Group: Development/Other
Requires: %name-core = %EVR
Requires: %name-reactive = %EVR
Conflicts: mono4-reactive-winforms < %EVR
Obsoletes: mono4-reactive-winforms
Provides: mono4-reactive-winforms = %EVR

%description reactive-winforms
Reactive Extensions for Mono, desktop-specific packages (winforms,
windows threading).

%package reactive-devel
Summary: Development files for system.web
Group: Development/Other
Requires: %name-core = %EVR
Requires: %name-reactive = %EVR
Requires: pkg-config
Conflicts: mono4-reactive-devel < %EVR
Obsoletes: mono4-reactive-devel
Provides: mono4-reactive-devel = %EVR

%description reactive-devel
This package provides the .pc file for %name-rx

%package winforms
Summary: Windows Forms implementation for Mono
Group: Development/Other
Requires: %name-core = %EVR
Conflicts: mono4-winforms < %EVR
Obsoletes: mono4-winforms
Provides: mono4-winforms = %EVR

%description winforms
This package provides a fully managed implementation of
System.Windows.Forms, the default graphical toolkit for .NET
applications.

%package wcf
Summary: Mono implementation of Windows Communication Foundation
Group: Development/Other
Requires: %name-core = %EVR
Conflicts: mono4-wcf < %EVR
Obsoletes: mono4-wcf
Provides: mono4-wcf = %EVR

%description wcf
This package provides an implementation of WCF, the Windows Communication
Foundation.

%package web
Summary: ASP.NET, Remoting, and Web Services for Mono
Group: Development/Other
Requires: %name-dyndata = %EVR
Conflicts: mono4-web < %EVR
Obsoletes: mono4-web
Provides: mono4-web = %EVR

%description web
This package provides the ASP.NET libraries and runtime for
development of web application, web services and remoting support.

%package web-devel
Summary: Development files for system.web
Group: Development/Other
Requires: %name-core = %EVR
Requires: %name-web = %EVR
Requires: pkg-config
Conflicts: mono4-web-devel < %EVR
Obsoletes: mono4-web-devel
Provides: mono4-web-devel = %EVR

%description web-devel
This package provides the .pc file for %name-web

%package data
Summary: Database connectivity for Mono
Group: Development/Other
Requires: %name-core = %EVR
Conflicts: mono4-data < %EVR
Obsoletes: mono4-data
Provides: mono4-data = %EVR

%description data
This package provides a Mono assembly to facilitate data access
and manipulation with databases, LDAP compatible directory servers
and/or XML data exchange. Beyond the ADO.NET, Novell.LDAP and
System.DirectoryServices assemblies, it also includes a command
line sql application as well as the Microsoft SQL Server and ODBC
data providers.

%package data-sqlite
Summary: sqlite database connectivity for Mono
Group: Development/Other
Requires: %name-core = %EVR
Conflicts: mono4-data-sqlite < %EVR
Obsoletes: mono4-data-sqlite
Provides: mono4-data-sqlite = %EVR

%description data-sqlite
This package contains the ADO.NET Data provider for the sqlite
database.

%package data-oracle
Summary: Oracle database connectivity for Mono
Group: Development/Other
Requires: %name-core = %EVR
Conflicts: mono4-data-oracle < %EVR
Obsoletes: mono4-data-oracle
Provides: mono4-data-oracle = %EVR

%description data-oracle
This package contains the ADO.NET Data provider for the Oracle
database.

%if_enabled ibmlibs
%package   ibm-data-db2
Summary: IBM DB2 database connectivity for Mono
Group: Development/Other
Requires: %name-core = %EVR
Conflicts: mono4-ibm-data-db2 < %EVR
Obsoletes: mono4-ibm-data-db2
Provides: mono4-ibm-data-db2 = %EVR

%description ibm-data-db2
This package contains the ADO.NET Data provider for the IBM DB2
Universal database.
%endif

%package monodoc
Summary: The %name documentation system
Group: Documentation
Requires: %name-core = %EVR
Conflicts: mono4-monodoc < %EVR
Obsoletes: mono4-monodoc
Provides: mono4-monodoc = %EVR
%qIF_ver_lt %ubt_id S1
Conflicts: monodoc < %EVR
Provides: monodoc = %EVR
Obsoletes: monodoc
%endif

%description monodoc
monodoc is the documentation package for the mono .NET environment

%package  monodoc-devel
Summary: .pc file for monodoc
Group: Documentation
Requires: %name-core = %EVR
Requires: %name-monodoc = %EVR
Requires: pkg-config
Conflicts: mono4-monodoc-devel < %EVR
Obsoletes: mono4-monodoc-devel
Provides: mono4-monodoc-devel = %EVR
%qIF_ver_lt %ubt_id S1
Conflicts: monodoc-devel < %EVR
Provides: monodoc-devel = %EVR
Obsoletes: monodoc-devel
%endif

%description monodoc-devel
Development file for monodoc

%package mono2-compat
Summary:        A Library for embedding Mono in your Application
Requires:       %name-core = %EVR
Group:          Development/Other

%description mono2-compat
The Mono Project is an open development initiative that is working to
develop an open source, Unix version of the .NET development platform.
Its objective is to enable Unix developers to build and deploy
cross-platform .NET applications. The project will implement various
technologies that have been submitted to the ECMA for standardization.

A Library for embedding Mono in your Application.

%package mono2-compat-devel
Summary:        Development files for libmono
Group:          Development/Other
Requires:       %name-mono2-compat = %EVR
Requires:       %name-core = %EVR

%description mono2-compat-devel
The Mono Project is an open development initiative that is working to
develop an open source, Unix version of the .NET development platform.
Its objective is to enable Unix developers to build and deploy
cross-platform .NET applications. The project will implement various
technologies that have been submitted to the ECMA for standardization.

Development files for libmono.

%define gac_dll() \
%_monogacdir/%1 \
%_monodir/4.5/%1.dll \
%nil

%define mono_bin() \
%_bindir/%1 \
%_monodir/4.5/%1.exe \
%_monodir/4.5/%1.exe.mdb \
%nil

%ifnarch ppc64le
%define dll_so() \
%_monodir/4.5/%1.dll \
%_monodir/4.5/%1.dll.so \
%nil
%else
%define dll_so() \
%_monodir/4.5/%1.dll \
%nil
%endif

%prep
%setup -a5 -a6 -a7 -a8 -a9 -a10 -a11 -a12 -a13 -a14 -a15 -a16 -a17 -a18 -a19 -a20 -a21 -a22 -a23 -a24 -a25 -a26 -a27 -a28 -a29 -a30 -a31
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1

%ifarch ppc64le
%patch101 -p1
%endif
%patch103 -p1
%patch104 -p1
%patch108 -p1
pushd external/api-doc-tools
%patch110 -p1
%patch111 -p1
popd
%patch112 -p1
%patch113 -p1

%if_enabled bootstrap
mkdir -p mcs/class/lib/monolite-linux
pushd mcs/class/lib/monolite-linux
tar xzf %SOURCE3
monolitename="$(tar tzf %SOURCE3 | head -n 1 | sed -e 's:/$::')"
if [ -n "$monolitename" ] ; then
    mv "$monolitename" "$(echo "$monolitename" | sed -e 's:monolite-linux-::' -e 's:-latest::')"
fi
popd
%endif

# fix imports, otherwise dependencies on devel packages are created
find . -type f -iname '*.cs' -print0 | xargs -0 \
    sed -i \
        -e 's:"libgdk-x11-2.0.so":"libgdk-x11-2.0.so.0":g' \
        -e 's:"libgdk_pixbuf-2.0.so":"libgdk_pixbuf-2.0.so.0":g' \
        -e 's:"libgobject-2.0.so":"libgobject-2.0.so.0":g' \
        -e 's:"libgtk-x11-2.0.so":"libgtk-x11-2.0.so.0":g' \
        -e 's:"libgmodule-2.0.so":"libgmodule-2.0.so.0":g' \
        -e 's:"libglib-2.0.so":"libglib-2.0.so.0":g'

# don't build mono-helix-client which requires the helix-binaries to build
sed -i 's|mono-helix-client||g' mcs/tools/Makefile

# Remove hardcoded lib directory for libMonoPosixHelper.so from the config
sed -i 's|$mono_libdir/||g' data/config.in

%build
export LD_LIBRARY_PATH=$(pwd)/mono/native/.libs

%add_optflags -fno-strict-aliasing

NOCONFIGURE=yes sh ./autogen.sh
%configure \
	--disable-rpath \
	--with-csc=mcs \
	--with-moonlight=no \
	--with-spectre-mitigation=yes \
	--enable-dynamic-btls \
	%nil

%make

%install
export LD_LIBRARY_PATH=$(pwd)/mono/native/.libs

%makeinstall_std

rm -fv %buildroot%_bindir/mono-heapviz

# copy the mono.snk key into /etc/pki/mono
mkdir -p %buildroot%_sysconfdir/pki/mono
install -p -m0644 %SOURCE2 %buildroot%_sysconfdir/pki/mono/

# C5 is not installed, see commit 0af35dd5

# remove Windows-only stuff
rm -rfv %buildroot%_monodir/*/Mono.Security.Win32*
rm -fv %buildroot%_libdir/libMonoSupportW.*
# remove libgc cruft
rm -rfv %buildroot%_datadir/libgc-mono
# remove stuff that we don't package*
rm -fv %buildroot%_man1dir/cilc.1*
rm -fv %buildroot%_man1dir/mdb2ppdb.1*
rm -fv %buildroot%_monodir/*/browsercaps-updater.*
rm -fv %buildroot%_monodir/*/culevel.*

rm -fv %buildroot%_monodir/*/mscorlib.dll.so
rm -fv %buildroot%_monodir/*/mcs.exe.so
rm -rfv %buildroot%_bindir/mono-configuration-crypto
rm -rfv %buildroot%_mandir/man?/mono-configuration-crypto*

%if_disabled ibmlibs
rm -rfv %buildroot%_monogacdir/IBM.Data.DB2
rm -fv %buildroot%_monodir/*/IBM.Data.DB2.dll
%endif

rm -fv %buildroot%_monodir/4.5/mono-shlib-cop.exe.config
rm -fv %buildroot%_monodir/4.5/sqlmetal.exe.config
rm -fv %buildroot%_monodir/4.5/xbuild.exe.config

rm -fv %buildroot%_libdir/libmono-2.0.a
rm -fv %buildroot%_libdir/libmono-2.0.la
rm -fv %buildroot%_libdir/libmonoboehm-2.0.a
rm -fv %buildroot%_libdir/libmonosgen-2.0.a
rm -rfv %buildroot%_libdir/mono/lldb
rm -rfv %buildroot%_datadir/mono-2.0/mono/profiler

mkdir -p  %buildroot%_sysconfdir/mono-2.0/
mkdir -p  %buildroot%_sysconfdir/mono-4.5/
mkdir -p  %buildroot%_sysconfdir/mono-4.0/

# install file trigger
install -pD -m755 %SOURCE4 %buildroot%_rpmlibdir/mono-cert-sync.filetrigger

%qIF_ver_lt %ubt_id S1
ln -s mcs %buildroot%_bindir/gmcs
%endif

%find_lang mcs

# drop python2-base requires
for i in %_bindir/mono-gdb.py %_bindir/mono-sgen-gdb.py ; do
    sed -i "1i#!/usr/bin/python3" %buildroot$i
done

%files core -f mcs.lang
%doc .github/CONTRIBUTING.md LICENSE COPYING.LIB NEWS README.md PATENTS.TXT
%_rpmlibdir/mono-cert-sync.filetrigger
%_sysconfdir/mono-4.5/
%_sysconfdir/mono-4.0/
%dir %_sysconfdir/mono/4.5/
%dir %_monodir
%dir %_monodir/4.5
%dir %_monodir/4.0
%_bindir/mono
%_bindir/mono-gdb.py
%ifnarch aarch64
%_bindir/mono-boehm
%endif
%_bindir/mono-service2
%_bindir/mono-sgen
%_bindir/mono-sgen-gdb.py
%mono_bin cert-sync
%mono_bin certmgr
%mono_bin chktrust
%mono_bin gacutil
%mono_bin ikdasm
%mono_bin lc
%_bindir/gacutil2
%mono_bin mozroots
%mono_bin setreg
%mono_bin sn
%_bindir/mono-hang-watchdog
#_bindir/mono-heapviz
%_bindir/mprof-report
%_man1dir/certmgr.1*
%_man1dir/chktrust.1*
%_man1dir/gacutil.1*
%_man1dir/mono.1*
%_man1dir/mozroots.1*
%_man1dir/setreg.1*
%_man1dir/sn.1*
%_man5dir/mono-config.5*
%_man1dir/lc.1*
%_man1dir/mprof-report.1*
%_man1dir/cert-sync.1*
%_libdir/libMonoPosixHelper.so*
%_libdir/*profiler*.so*
%_libdir/libmono-btls-shared.so*
%_libdir/libikvm-native.so*
%_libdir/libmono-native.so*
%_monodir/4.0/Mono.Posix.dll
%_monodir/4.0/mscorlib.dll

%dir %_monodir/gac
%gac_dll Commons.Xml.Relaxng
%gac_dll ICSharpCode.SharpZipLib
%_monogacdir/Mono.Cecil
%gac_dll cscompmgd
%gac_dll System.Drawing
%gac_dll Mono.Posix
%gac_dll Mono.Security
%gac_dll System
%gac_dll System.Configuration
%gac_dll System.Core
%gac_dll System.Security
%gac_dll System.Xml
%gac_dll System.Reflection.Context
%gac_dll System.Runtime.Serialization
%gac_dll System.Net
%gac_dll System.Xml.Linq
%dir %_sysconfdir/mono
%dir %_sysconfdir/mono/mconfig
%config (noreplace) %_sysconfdir/mono/config
%config (noreplace) %_sysconfdir/mono/4.5/settings.map
%config (noreplace) %_sysconfdir/mono/4.0/DefaultWsdlHelpGenerator.aspx
%config (noreplace) %_sysconfdir/mono/4.5/DefaultWsdlHelpGenerator.aspx
%config (noreplace) %_sysconfdir/mono/4.5/machine.config
%config (noreplace) %_sysconfdir/mono/4.5/web.config
%config (noreplace) %_sysconfdir/mono/4.0/machine.config
%config (noreplace) %_sysconfdir/mono/4.0/web.config
%config (noreplace) %_sysconfdir/mono/4.0/settings.map
%dir %_sysconfdir/mono/4.0
%dir %_monodir/4.5/Facades

%_monodir/4.5/mscorlib.dll
%_monodir/4.5/mscorlib.dll.mdb
%_monodir/4.5/System.Memory.dll
%gac_dll Microsoft.CSharp
%gac_dll System.Dynamic
%gac_dll System.ComponentModel.Composition
%gac_dll System.Numerics

%dir %_monodir/mono-configuration-crypto/
%dir %_monodir/mono-configuration-crypto/4.5/
%_monodir/mono-configuration-crypto/4.5/*
%gac_dll Mono.Cairo
%gac_dll Mono.Management
%gac_dll Mono.Parallel
%gac_dll Mono.Simd
%gac_dll Mono.Tasklets
%gac_dll CustomMarshalers
%gac_dll I18N.West
%gac_dll I18N
%gac_dll System.Json
%gac_dll System.Json.Microsoft
%_monodir/4.5/Facades/*.dll
%_monodir/4.5/Facades/*.dll.mdb
%gac_dll System.IO.Compression
%gac_dll System.IO.Compression.FileSystem
%gac_dll System.Net.Http
%gac_dll System.Net.Http.WebRequest
%gac_dll System.Threading.Tasks.Dataflow
%gac_dll System.Numerics.Vectors
%gac_dll System.ServiceModel.Internals
%exclude %_monodir/4.5/System.Runtime.Caching.dll
%exclude %_monodir/4.5/System.Xaml.dll
%exclude %_monogacdir/System.Runtime.Caching/*
%exclude %_monogacdir/System.Xaml/*
%exclude %_sysconfdir/mono/4.0/Browsers/Compat.browser
%dir %_monodir/gac/Mono.Btls.Interface
%_monodir/gac/Mono.Btls.Interface/*
%_monodir/4.5/Mono.Btls.Interface.dll
%dll_so System.Collections.Immutable
%dll_so System.Reflection.Metadata

%dir %_monodir/msbuild
%dir %_monodir/msbuild/Current
%dir %_monodir/msbuild/Current/bin
%dir %_monodir/msbuild/Current/bin/Roslyn
%_monodir/msbuild/Current/bin/Roslyn/System.Collections.Immutable.dll
%_monodir/msbuild/Current/bin/Roslyn/System.Memory.dll
%_monodir/msbuild/Current/bin/Roslyn/System.Reflection.Metadata.dll

%_libdir/libmonosgen-2.0.so*
%ifnarch aarch64
%_libdir/libmonoboehm-2.0.so*
%endif
%_monodir/2.0-api
%_monodir/3.5-api
%_monodir/4.0-api
%_monodir/4.5-api
%_monodir/4.5.1-api
%_monodir/4.5.2-api
%_monodir/4.6-api
%_monodir/4.6.1-api
%_monodir/4.6.2-api
%_monodir/4.7-api
%_monodir/4.7.1-api
%_monodir/4.7.2-api
%_monodir/4.8-api

# data
%exclude %_monodir/*-api/Mono.Data.Tds.dll
%exclude %_monodir/*-api/Novell.Directory.Ldap.dll
%exclude %_monodir/*-api/System.Data.dll
%exclude %_monodir/*-api/System.Data.Linq.dll
%exclude %_monodir/*-api/System.Data.DataSetExtensions.dll
%exclude %_monodir/*-api/System.Data.Entity.dll
%exclude %_monodir/*-api/System.Data.Services.dll
%exclude %_monodir/*-api/System.Data.Services.Client.dll
%exclude %_monodir/*-api/System.DirectoryServices.dll
%exclude %_monodir/*-api/System.DirectoryServices.Protocols.dll
%exclude %_monodir/*-api/System.EnterpriseServices.dll
%exclude %_monodir/*-api/System.Runtime.DurableInstancing.dll
%exclude %_monodir/*-api/System.Transactions.dll
%exclude %_monodir/*-api/WebMatrix.Data.dll
%exclude %_monodir/*/Facades/netstandard.dll
%exclude %_monodir/*/Facades/System.Data.Common.dll

# data-oracle
%exclude %_monodir/*-api/System.Data.OracleClient.dll

# data-sqlite
%exclude %_monodir/*-api/Mono.Data.Sqlite.dll
%exclude %_monodir/*/Facades/System.Data.SqlClient.dll

# devel
%exclude %_monodir/*-api/Microsoft.VisualBasic.dll
%exclude %_monodir/*-api/Microsoft.Build.Engine.dll
%exclude %_monodir/*-api/Microsoft.Build.Framework.dll
%exclude %_monodir/*-api/Microsoft.Build.Tasks.dll
%exclude %_monodir/*-api/Microsoft.Build.Tasks.v3.5.dll
%exclude %_monodir/*-api/Microsoft.Build.Tasks.v4.0.dll
%exclude %_monodir/*-api/Microsoft.Build.Utilities.dll
%exclude %_monodir/*-api/Microsoft.Build.Utilities.v3.5.dll
%exclude %_monodir/*-api/Microsoft.Build.Utilities.v4.0.dll
%exclude %_monodir/*-api/Microsoft.Build.dll
%exclude %_monodir/*-api/Microsoft.VisualC.dll
%exclude %_monodir/*-api/Mono.C5.dll
%exclude %_monodir/*-api/Mono.CSharp.dll
%exclude %_monodir/*-api/Mono.CodeContracts.dll
%exclude %_monodir/*-api/Mono.CompilerServices.SymbolWriter.dll
%exclude %_monodir/*-api/Mono.Debugger.Soft.dll
%exclude %_monodir/*-api/PEAPI.dll
%exclude %_monodir/*-api/SMDiagnostics.dll
%exclude %_monodir/*/Facades/System.Runtime.CompilerServices.VisualC.dll
%exclude %_monodir/*-api/System.Deployment.dll

# dyndata
%exclude %_monodir/*-api/System.Web.DynamicData.dll

# extras
%exclude %_monodir/*-api/Mono.Messaging.RabbitMQ.dll
%exclude %_monodir/*-api/Mono.Messaging.dll
%exclude %_monodir/*-api/RabbitMQ.Client.dll
%exclude %_monodir/*-api/System.Configuration.Install.dll
%exclude %_monodir/*-api/System.Management.dll
%exclude %_monodir/*-api/System.Messaging.dll
%exclude %_monodir/*-api/System.Runtime.Caching.dll
%exclude %_monodir/*-api/System.ServiceProcess.dll
%exclude %_monodir/*-api/System.Xaml.dll
%exclude %_monodir/*/Facades/System.ServiceProcess.ServiceController.dll*

# ibm-data-db2
%if_enabled ibmlibs
%exclude %_monodir/*-api/IBM.Data.DB2.dll
%endif

# locale-extras
%exclude %_monodir/*-api/I18N.CJK.dll
%exclude %_monodir/*-api/I18N.MidEast.dll
%exclude %_monodir/*-api/I18N.Other.dll
%exclude %_monodir/*-api/I18N.Rare.dll

# mvc
%exclude %_monodir/*-api/System.Web.Extensions.dll
%exclude %_monodir/*-api/System.Web.Extensions.Design.dll
%exclude %_monodir/*-api/System.Web.Mvc.dll

# reactive
%exclude %_monodir/*-api/System.Reactive.Core.dll
%exclude %_monodir/*-api/System.Reactive.Debugger.dll
%exclude %_monodir/*-api/System.Reactive.Experimental.dll
%exclude %_monodir/*-api/System.Reactive.Interfaces.dll
%exclude %_monodir/*-api/System.Reactive.Linq.dll
%exclude %_monodir/*-api/System.Reactive.Observable.Aliases.dll
%exclude %_monodir/*-api/System.Reactive.PlatformServices.dll
%exclude %_monodir/*-api/System.Reactive.Providers.dll
%exclude %_monodir/*-api/System.Reactive.Runtime.Remoting.dll

# reactive-winforms
%exclude %_monodir/*-api/System.Reactive.Windows.Forms.dll
%exclude %_monodir/*-api/System.Reactive.Windows.Threading.dll

# wcf
%exclude %_monodir/*-api/System.IdentityModel.dll
%exclude %_monodir/*-api/System.IdentityModel.Selectors.dll
%exclude %_monodir/*-api/System.ServiceModel.dll
%exclude %_monodir/*-api/System.ServiceModel.Activation.dll
%exclude %_monodir/*-api/System.ServiceModel.Discovery.dll
%exclude %_monodir/*-api/System.ServiceModel.Routing.dll
%exclude %_monodir/*-api/System.ServiceModel.Web.dll
%exclude %_monodir/*-api/System.Xml.Serialization.dll
%exclude %_monodir/*/Facades/System.ServiceModel.Duplex.dll
%exclude %_monodir/*/Facades/System.ServiceModel.Http.dll
%exclude %_monodir/*/Facades/System.ServiceModel.NetTcp.dll
%exclude %_monodir/*/Facades/System.ServiceModel.Primitives.dll
%exclude %_monodir/*/Facades/System.ServiceModel.Security.dll

# web
%exclude %_monodir/*-api/Microsoft.Web.Infrastructure.dll
%exclude %_monodir/*-api/Mono.Http.dll
%exclude %_monodir/*-api/System.ComponentModel.DataAnnotations.dll
%exclude %_monodir/*-api/System.Net.Http.Formatting.dll
%exclude %_monodir/*-api/System.Runtime.Remoting.dll
%exclude %_monodir/*-api/System.Runtime.Serialization.Formatters.Soap.dll
%exclude %_monodir/*-api/System.Web.dll
%exclude %_monodir/*-api/System.Web.Abstractions.dll
%exclude %_monodir/*-api/System.Web.ApplicationServices.dll
%exclude %_monodir/*-api/System.Web.Http.dll
%exclude %_monodir/*-api/System.Web.Http.SelfHost.dll
%exclude %_monodir/*-api/System.Web.Http.WebHost.dll
%exclude %_monodir/*-api/System.Web.Mobile.dll
%exclude %_monodir/*-api/System.Web.Razor.dll
%exclude %_monodir/*-api/System.Web.RegularExpressions.dll
%exclude %_monodir/*-api/System.Web.Routing.dll
%exclude %_monodir/*-api/System.Web.Services.dll
%exclude %_monodir/*-api/System.Web.WebPages.dll
%exclude %_monodir/*-api/System.Web.WebPages.Deployment.dll
%exclude %_monodir/*-api/System.Web.WebPages.Razor.dll
%exclude %_monodir/*-api/System.Workflow.Activities.dll
%exclude %_monodir/*-api/System.Workflow.ComponentModel.dll
%exclude %_monodir/*-api/System.Workflow.Runtime.dll
%exclude %_monodir/*/Facades/System.ComponentModel.Annotations.dll

# winforms
%exclude %_monodir/*-api/Accessibility.dll
%exclude %_monodir/*-api/Mono.WebBrowser.dll
%exclude %_monodir/*-api/System.Design.dll
%exclude %_monodir/*-api/System.Drawing.Design.dll
%exclude %_monodir/*-api/System.Windows.Forms.dll
%exclude %_monodir/*-api/System.Windows.Forms.DataVisualization.dll

# winfx
%exclude %_monodir/*-api/WindowsBase.dll

%files dyndata
%gac_dll System.Web.DynamicData

%_monodir/*-api/System.Web.DynamicData.dll

%files full

%files devel-full

%files devel
%qIF_ver_lt %ubt_id S1
%_bindir/gmcs
%endif
%_sysconfdir/pki/mono/
%_bindir/mono-test-install
%mono_bin mono-api-info
%mono_bin aprofutil
%mono_bin illinkanalyzer
%_bindir/mono-package-runtime
%_bindir/sgen-grep-binprot
%_bindir/csi
%mono_bin pdb2mdb
%mono_bin csharp
%_bindir/csc
%_bindir/dmcs
%mono_bin mcs
%mono_bin ccrewrite
%_man1dir/ccrewrite.1*
%_man1dir/mcs.1*
%_man1dir/csharp.1*
%_man1dir/pdb2mdb.1*
%_monodir/4.5/csc.*
%_monodir/4.5/mono-api-diff.exe
%_monodir/4.5/mono-api-diff.exe.mdb
%_monodir/4.5/csi.*
%_bindir/vbc
%_monodir/4.5/vbc.*
%_monodir/4.5/VBCSCompiler.*
%_monodir/4.5/mono-symbolicate.exe
%_monodir/4.5/mono-symbolicate.exe.mdb
%_monodir/4.5/Microsoft.CodeAnalysis.CSharp.Scripting.dll
%_monodir/4.5/Microsoft.CodeAnalysis.Scripting.dll
%_monodir/4.5/Microsoft.CodeAnalysis.VisualBasic.dll
%_monodir/4.5/System.Runtime.CompilerServices.Unsafe.dll
%_monodir/4.5/System.Threading.Tasks.Extensions.dll
%_monodir/msbuild/Current/bin/Roslyn/*
%exclude %_monodir/msbuild/Current/bin/Roslyn/System.Collections.Immutable.dll
%exclude %_monodir/msbuild/Current/bin/Roslyn/System.Memory.dll
%exclude %_monodir/msbuild/Current/bin/Roslyn/System.Reflection.Metadata.dll
%_bindir/mono-symbolicate
%mono_bin xbuild
%_monodir/4.5/xbuild.rsp
%mono_bin genxs
%_monodir/4.5/ictool*
%_monodir/4.5/mod*
%mono_bin al
%_bindir/al2
%mono_bin caspol
%mono_bin cert2spc
%mono_bin dtd2rng
%mono_bin dtd2xsd
%mono_bin ilasm
%mono_bin installvst
%_monodir/4.5/installutil*
%mono_bin macpack
%mono_bin mkbundle
%mono_bin makecert
%mono_bin mono-cil-strip
%_bindir/mono-find-provides
%_bindir/mono-find-requires
%_bindir/monodis
%_bindir/monolinker
%mono_bin mono-shlib-cop
%mono_bin mono-xmltool
%mono_bin monop
%_bindir/monop2
%mono_bin permview
%_bindir/peverify
%mono_bin resgen
%_bindir/resgen2
%mono_bin sgen
%mono_bin secutil
%mono_bin signcode
%mono_bin cccheck
%mono_bin crlupdate
%mono_bin mdbrebase
%_libexecdir/mono-source-libs/
%_bindir/pedump
%_man1dir/resgen.1*
%_man1dir/al.1*
%_man1dir/cert2spc.1*
%_man1dir/dtd2xsd.1*
%_man1dir/genxs.1*
%_man1dir/ilasm.1*
%_man1dir/macpack.1*
%_man1dir/makecert.1*
%_man1dir/mkbundle.1*
%_man1dir/mono-cil-strip.1*
%_man1dir/monodis.1*
%_man1dir/monolinker.1*
%_man1dir/mono-profilers.1*
%_man1dir/mono-shlib-cop.1*
%_man1dir/mono-xmltool.1*
%_man1dir/monop.1*
%_man1dir/permview.1*
%_man1dir/secutil.1*
%_man1dir/sgen.1*
%_man1dir/signcode.1*
%_man1dir/xbuild.1*
%_man1dir/mono-api-info.1*
%_man1dir/aprofutil.1*
%_man1dir/cccheck.1*
%_man1dir/crlupdate.1*
%_man1dir/illinkanalyzer.1*
%gac_dll PEAPI
%gac_dll Microsoft.Build
%gac_dll Microsoft.Build.Engine
%gac_dll Microsoft.Build.Framework
%_monogacdir/Microsoft.Build.Tasks.Core
%gac_dll Microsoft.Build.Tasks.v4.0
%gac_dll Microsoft.Build.Utilities.v4.0
%_monogacdir/Microsoft.Build.Utilities.Core
%_monogacdir/Microsoft.Build.Tasks.v12.0
%_monogacdir/Microsoft.Build.Utilities.v12.0
%gac_dll Microsoft.VisualC
%gac_dll Mono.CSharp
%gac_dll Mono.CodeContracts
%gac_dll Mono.CompilerServices.SymbolWriter
%gac_dll Mono.Debugger.Soft
%gac_dll Mono.Profiler.Log
%gac_dll Mono.XBuild.Tasks
%gac_dll System.Windows
%gac_dll SMDiagnostics
%gac_dll System.Deployment
%dll_so Microsoft.CodeAnalysis
%dll_so Microsoft.CodeAnalysis.CSharp
%_monodir/4.5/Microsoft.Common.tasks
%_monodir/4.5/MSBuild/Microsoft.Build*
%_monodir/4.5/Microsoft.Build.xsd
%_monodir/4.5/Microsoft.CSharp.targets
%_monodir/4.5/Microsoft.Common.targets
%_monodir/4.5/Microsoft.VisualBasic.targets
%_monodir/xbuild/
%_monodir/xbuild-frameworks/
%_libdir/libMonoPosixHelper.a
%_libdir/*profiler*.a
%_libdir/libikvm-native.a
%_libdir/libmono-native.a
%_pkgconfigdir/dotnet.pc
%_pkgconfigdir/mono-cairo.pc
%_pkgconfigdir/mono.pc
%_pkgconfigdir/monosgen-2.pc
%_pkgconfigdir/cecil.pc
%_pkgconfigdir/dotnet35.pc
%_pkgconfigdir/mono-lineeditor.pc
%_pkgconfigdir/mono-options.pc
%_pkgconfigdir/wcf.pc
%_pkgconfigdir/xbuild12.pc

%_monodir/*-api/Microsoft.VisualBasic.dll
%_monodir/*-api/Microsoft.Build.Engine.dll
%_monodir/*-api/Microsoft.Build.Framework.dll
%_monodir/*-api/Microsoft.Build.Tasks.dll
%_monodir/*-api/Microsoft.Build.Tasks.v3.5.dll
%_monodir/*-api/Microsoft.Build.Tasks.v4.0.dll
%_monodir/*-api/Microsoft.Build.Utilities.dll
%_monodir/*-api/Microsoft.Build.Utilities.v3.5.dll
%_monodir/*-api/Microsoft.Build.Utilities.v4.0.dll
%_monodir/*-api/Microsoft.Build.dll
%_monodir/*-api/Microsoft.VisualC.dll
%_monodir/*-api/Mono.C5.dll
%_monodir/*-api/Mono.CSharp.dll
%_monodir/*-api/Mono.CodeContracts.dll
%_monodir/*-api/Mono.CompilerServices.SymbolWriter.dll
%_monodir/*-api/Mono.Debugger.Soft.dll
%_monodir/*-api/PEAPI.dll
%_monodir/*-api/SMDiagnostics.dll
%_monodir/*/Facades/System.Runtime.CompilerServices.VisualC.dll
%_monodir/*-api/System.Deployment.dll

%files locale-extras
%gac_dll I18N.CJK
%gac_dll I18N.MidEast
%gac_dll I18N.Other
%gac_dll I18N.Rare

%_monodir/*-api/I18N.CJK.dll
%_monodir/*-api/I18N.MidEast.dll
%_monodir/*-api/I18N.Other.dll
%_monodir/*-api/I18N.Rare.dll

%files extras
%mono_bin mono-service
%_monogacdir/mono-service
%gac_dll System.Configuration.Install
%gac_dll System.Management
%gac_dll System.Messaging
%gac_dll System.ServiceProcess
%gac_dll System.Runtime.Caching
%gac_dll System.Xaml
%gac_dll Mono.Messaging.RabbitMQ
%gac_dll Mono.Messaging
%gac_dll RabbitMQ.Client
%_monodir/4.5/RabbitMQ.Client.Apigen*
%_man1dir/mono-service.1*

%_monodir/*-api/Mono.Messaging.RabbitMQ.dll
%_monodir/*-api/Mono.Messaging.dll
%_monodir/*-api/RabbitMQ.Client.dll
%_monodir/*-api/System.Configuration.Install.dll
%_monodir/*-api/System.Management.dll
%_monodir/*-api/System.Messaging.dll
%_monodir/*-api/System.Runtime.Caching.dll
%_monodir/*-api/System.ServiceProcess.dll
%_monodir/*-api/System.Xaml.dll
%_monodir/*/Facades/System.ServiceProcess.ServiceController.dll*

%files reactive
%gac_dll System.Reactive.Core
%gac_dll System.Reactive.Debugger
%gac_dll System.Reactive.Experimental
%gac_dll System.Reactive.Interfaces
%gac_dll System.Reactive.Linq
%gac_dll System.Reactive.Observable.Aliases
%gac_dll System.Reactive.PlatformServices
%gac_dll System.Reactive.Providers
%gac_dll System.Reactive.Runtime.Remoting

%_monodir/*-api/System.Reactive.Core.dll
%_monodir/*-api/System.Reactive.Debugger.dll
%_monodir/*-api/System.Reactive.Experimental.dll
%_monodir/*-api/System.Reactive.Interfaces.dll
%_monodir/*-api/System.Reactive.Linq.dll
%_monodir/*-api/System.Reactive.Observable.Aliases.dll
%_monodir/*-api/System.Reactive.PlatformServices.dll
%_monodir/*-api/System.Reactive.Providers.dll
%_monodir/*-api/System.Reactive.Runtime.Remoting.dll

%files reactive-winforms
%gac_dll System.Reactive.Windows.Forms
%gac_dll System.Reactive.Windows.Threading

%_monodir/*-api/System.Reactive.Windows.Forms.dll
%_monodir/*-api/System.Reactive.Windows.Threading.dll

%files reactive-devel
%_pkgconfigdir/reactive.pc

%files wcf
%gac_dll System.IdentityModel
%gac_dll System.IdentityModel.Selectors
%gac_dll System.ServiceModel
%gac_dll System.ServiceModel.Activation
%gac_dll System.ServiceModel.Discovery
%gac_dll System.ServiceModel.Routing
%gac_dll System.ServiceModel.Web
%gac_dll System.Xml.Serialization

%_monodir/*-api/System.IdentityModel.dll
%_monodir/*-api/System.IdentityModel.Selectors.dll
%_monodir/*-api/System.ServiceModel.dll
%_monodir/*-api/System.ServiceModel.Activation.dll
%_monodir/*-api/System.ServiceModel.Discovery.dll
%_monodir/*-api/System.ServiceModel.Routing.dll
%_monodir/*-api/System.ServiceModel.Web.dll
%_monodir/*-api/System.Xml.Serialization.dll
%_monodir/*/Facades/System.ServiceModel.Duplex.dll
%_monodir/*/Facades/System.ServiceModel.Http.dll
%_monodir/*/Facades/System.ServiceModel.NetTcp.dll
%_monodir/*/Facades/System.ServiceModel.Primitives.dll
%_monodir/*/Facades/System.ServiceModel.Security.dll

%files web
%mono_bin disco
%mono_bin httpcfg
%mono_bin mconfig
%mono_bin soapsuds
%mono_bin svcutil
%mono_bin wsdl
%_bindir/wsdl2
%mono_bin xsd
%mono_bin mono-api-html
%gac_dll Microsoft.Web.Infrastructure
%gac_dll Mono.Http
%gac_dll System.ComponentModel.DataAnnotations
%gac_dll System.Net.Http.Formatting
%gac_dll System.Runtime.Remoting
%gac_dll System.Runtime.Serialization.Formatters.Soap
%gac_dll System.Web
%gac_dll System.Web.Abstractions
%gac_dll System.Web.Routing
%gac_dll System.Web.Services
%gac_dll System.Web.ApplicationServices
%gac_dll System.Web.Http
%gac_dll System.Web.Http.SelfHost
%gac_dll System.Web.Http.WebHost
%gac_dll System.Web.Razor
%gac_dll System.Web.WebPages
%gac_dll System.Web.WebPages.Deployment
%gac_dll System.Web.WebPages.Razor
%gac_dll System.Web.Mobile
%gac_dll System.Web.RegularExpressions
%gac_dll System.Workflow.Activities
%gac_dll System.Workflow.ComponentModel
%gac_dll System.Workflow.Runtime

%_monodir/*-api/Microsoft.Web.Infrastructure.dll
%_monodir/*-api/Mono.Http.dll
%_monodir/*-api/System.ComponentModel.DataAnnotations.dll
%_monodir/*-api/System.Net.Http.Formatting.dll
%_monodir/*-api/System.Runtime.Remoting.dll
%_monodir/*-api/System.Runtime.Serialization.Formatters.Soap.dll
%_monodir/*-api/System.Web.dll
%_monodir/*-api/System.Web.Abstractions.dll
%_monodir/*-api/System.Web.ApplicationServices.dll
%_monodir/*-api/System.Web.Http.dll
%_monodir/*-api/System.Web.Http.SelfHost.dll
%_monodir/*-api/System.Web.Http.WebHost.dll
%_monodir/*-api/System.Web.Mobile.dll
%_monodir/*-api/System.Web.Razor.dll
%_monodir/*-api/System.Web.RegularExpressions.dll
%_monodir/*-api/System.Web.Routing.dll
%_monodir/*-api/System.Web.Services.dll
%_monodir/*-api/System.Web.WebPages.dll
%_monodir/*-api/System.Web.WebPages.Deployment.dll
%_monodir/*-api/System.Web.WebPages.Razor.dll
%_monodir/*-api/System.Workflow.Activities.dll
%_monodir/*-api/System.Workflow.ComponentModel.dll
%_monodir/*-api/System.Workflow.Runtime.dll
%_monodir/*/Facades/System.ComponentModel.Annotations.dll

%_man1dir/disco.1*
%_man1dir/httpcfg.1*
%_man1dir/mconfig.1*
%_man1dir/soapsuds.1*
%_man1dir/wsdl.1*
%_man1dir/xsd.1*
%config (noreplace) %_sysconfdir/mono/browscap.ini
%config (noreplace) %_sysconfdir/mono/2.0/Browsers/Compat.browser
%config (noreplace) %_sysconfdir/mono/4.0/Browsers/Compat.browser
%config (noreplace) %_sysconfdir/mono/4.5/Browsers/Compat.browser
%config (noreplace) %_sysconfdir/mono/2.0/DefaultWsdlHelpGenerator.aspx
%config (noreplace) %_sysconfdir/mono/mconfig/config.xml

%files web-devel
%_pkgconfigdir/aspnetwebstack.pc

%files winforms
%gac_dll Accessibility
%gac_dll Mono.WebBrowser
%gac_dll System.Design
%gac_dll System.Drawing.Design
%gac_dll System.Windows.Forms
%gac_dll System.Windows.Forms.DataVisualization

%_monodir/*-api/Accessibility.dll
%_monodir/*-api/Mono.WebBrowser.dll
%_monodir/*-api/System.Design.dll
%_monodir/*-api/System.Drawing.Design.dll
%_monodir/*-api/System.Windows.Forms.dll
%_monodir/*-api/System.Windows.Forms.DataVisualization.dll

%files mvc
%gac_dll System.Web.Extensions
%gac_dll System.Web.Extensions.Design
%gac_dll System.Web.Mvc

%_monodir/*-api/System.Web.Extensions.dll
%_monodir/*-api/System.Web.Extensions.Design.dll
%_monodir/*-api/System.Web.Mvc.dll

%files mvc-devel
%_pkgconfigdir/system.web.extensions.design_1.0.pc
%_pkgconfigdir/system.web.extensions_1.0.pc
%_pkgconfigdir/system.web.mvc.pc
%_pkgconfigdir/system.web.mvc2.pc
%_pkgconfigdir/system.web.mvc3.pc

%files winfx
%gac_dll WindowsBase
%_monodir/*-api/WindowsBase.dll

%files data
%mono_bin sqlsharp
%mono_bin sqlmetal
%gac_dll System.Data
%gac_dll System.Data.DataSetExtensions
%gac_dll System.Data.Entity
%gac_dll System.Data.Linq
%gac_dll System.Data.Services
%gac_dll System.Data.Services.Client
%gac_dll System.DirectoryServices
%gac_dll System.DirectoryServices.Protocols
%gac_dll System.EnterpriseServices
%gac_dll System.Runtime.DurableInstancing
%gac_dll System.Transactions
%gac_dll Mono.Data.Tds
%gac_dll Novell.Directory.Ldap
%gac_dll WebMatrix.Data
%_man1dir/sqlsharp.1*

%_monodir/*-api/Mono.Data.Tds.dll
%_monodir/*-api/Novell.Directory.Ldap.dll
%_monodir/*-api/System.Data.dll
%_monodir/*-api/System.Data.Linq.dll
%_monodir/*-api/System.Data.DataSetExtensions.dll
%_monodir/*-api/System.Data.Entity.dll
%_monodir/*-api/System.Data.Services.dll
%_monodir/*-api/System.Data.Services.Client.dll
%_monodir/*-api/System.DirectoryServices.dll
%_monodir/*-api/System.DirectoryServices.Protocols.dll
%_monodir/*-api/System.EnterpriseServices.dll
%_monodir/*-api/System.Runtime.DurableInstancing.dll
%_monodir/*-api/System.Transactions.dll
%_monodir/*-api/WebMatrix.Data.dll
%_monodir/*/Facades/netstandard.dll
%_monodir/*/Facades/System.Data.Common.dll

%files data-sqlite
%gac_dll Mono.Data.Sqlite

%_monodir/*-api/Mono.Data.Sqlite.dll
%_monodir/*/Facades/System.Data.SqlClient.dll

%files data-oracle
%gac_dll System.Data.OracleClient

%_monodir/*-api/System.Data.OracleClient.dll

%if_enabled ibmlibs
%files  ibm-data-db2
%gac_dll IBM.Data.DB2

%_monodir/*-api/IBM.Data.DB2.dll
%endif

%files monodoc
%_monogacdir/monodoc
%_monodir/monodoc/*
%ifnarch  ppc
%_datadir/monodoc
%endif
%mono_bin mdoc
%_bindir/mod
%_bindir/mdoc-*
%_bindir/mdass*
%_bindir/mdval*
%_bindir/monodoc*
%_man1dir/monodocer.1*
%_man5dir/mdoc.5*
%_man1dir/mdoc-*
%_man1dir/mdoc.1.*
%_man1dir/mdassembler*
%_man1dir/monodocs2html.1*
%_man1dir/mdvalidater.1*
%_man1dir/mono-symbolicate.1*

%files  monodoc-devel
%_pkgconfigdir/monodoc.pc

%files mono2-compat
%_sysconfdir/mono-2.0/
%dir %_sysconfdir/mono/2.0
%config (noreplace) %_sysconfdir/mono/2.0/machine.config
%config (noreplace) %_sysconfdir/mono/2.0/settings.map
%config (noreplace) %_sysconfdir/mono/2.0/web.config
%_libdir/libmono-2.0.so*

%files mono2-compat-devel
%_includedir/mono-2.0
%_datadir/mono-2.0
%_pkgconfigdir/mono-2.pc

%changelog
* Mon Aug 30 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 6.12.0.147-alt2
- Disabled LTO.

* Wed Aug 04 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 6.12.0.147-alt1
- Updated to upstream version 6.12.0.147.
- Reverted some changes and patches from Fedora.

* Wed Jul 28 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 6.12.0.122-alt3
- Replaced %%post with updated filetrigger: if CA certificates are installed
  in same transaction with mono, certificates are not prepared for use during %%post.
  If mono filetrigger runs before CA certificates filetrigger,
  it still may fail.

* Wed Jun 23 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 6.12.0.122-alt2
- Fixed dependencies issues introduced by rpm-build (Closes: #40273).

* Tue Apr 27 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 6.12.0.122-alt1
- Updated to upstream version 6.12.0.122 (Closes: #39899).
- Imported changes and patches from Fedora.

* Wed Nov 18 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 5.20.1.19-alt8
- Repackaged some libraries (Closes: #39254).

* Wed Nov 11 2020 Vitaly Lipatov <lav@altlinux.ru> 5.20.1.19-alt7
- move mono-test-install to mono-devel package (it uses pkg-config file from it)
- use python3 during build, don't require python2-base in mono-core

* Fri Aug 07 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 5.20.1.19-alt6
- Fixed build with new cmake.

* Tue Jul 07 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 5.20.1.19-alt5
- Fixed build with new make.

* Thu Jan 23 2020 Vitaly Lipatov <lav@altlinux.ru> 5.20.1.19-alt4
- drop sqlite require from mono-data-sqlite
- use python3 for internal build scripts
- disable mono-heapviz packing (uses obsoleted python PIL module)

* Fri Jul 05 2019 Aleksei Nikiforov <darktemplar@altlinux.org> 5.20.1.19-alt3
- Moved *.so libraries out of devel subpackages (Closes: #36979)
- Switched to mcs compiler

* Tue May 28 2019 Aleksei Nikiforov <darktemplar@altlinux.org> 5.20.1.19-alt2
- Rebuilt with patch from upstream pull request #12864.

* Mon Apr 15 2019 Aleksei Nikiforov <darktemplar@altlinux.org> 5.20.1.19-alt1
- Updated to upstream version 5.20.1.19.

* Thu Jan 24 2019 Aleksei Nikiforov <darktemplar@altlinux.org> 5.18.0.240-alt1
- Updated to upstream version 5.18.0.240.

* Mon Oct 08 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 5.14.0.177-alt1
- Updated to upstream version 5.14.0.177.

* Wed May 16 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 5.10.0.157-alt4
- Updated interpackage dependencies.

* Mon Apr 16 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 5.10.0.157-alt3
- Fixed build on some architectures.

* Fri Apr 06 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 5.10.0.157-alt2
- Updated interpackage dependencies.

* Fri Mar 16 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 5.10.0.157-alt1
- Updated to upstream version 5.10.0.157.

* Mon Sep 25 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 5.0.1.1-alt8
- Updated provides.
- Fixed monodoc directory.

* Mon Sep 18 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 5.0.1.1-alt7
- Added file trigger to run cert-sync tool on certificates update.

* Fri Sep 01 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 5.0.1.1-alt6
- Rebuilt with support of %%ubt macro.

* Fri Jul 28 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 5.0.1.1-alt5
- Fixed unresolved symbols
- Added post-install action for mono-core to import certificates

* Wed Jul 26 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 5.0.1.1-alt4
- Installed msbuild config files

* Mon Jul 24 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 5.0.1.1-alt3
- Fixed circular dependency between mono-core and mono-devel
- Packaged mono-2 parts

* Mon Jul 24 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 5.0.1.1-alt2
- Updated package metadata

* Wed Jul 19 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 5.0.1.1-alt1
- Updated to stable upstream release version 5.0.1.1

* Tue Nov 22 2016 Denis Medvedev <nbr@altlinux.org> 4.6.2.7-alt4
- fix libraries for profiler

* Mon Nov 21 2016 Denis Medvedev <nbr@altlinux.org> 4.6.2.7-alt3
- fix for profiler-iomap

* Fri Nov 18 2016 Denis Medvedev <nbr@altlinux.org> 4.6.2.7-alt2
- fix place of monoPosixHelper for x86_64

* Thu Oct 06 2016 Denis Medvedev <nbr@altlinux.org> 4.6.2.7-alt1
- new version.

* Sun Jul 17 2016 Denis Medvedev <nbr@altlinux.org> 4.3.1.1-alt9
- Moved library libMonoPosixHelper to arch-depended dir (fixes #32246).

* Sun Jan 24 2016 Denis Medvedev <nbr@altlinux.org> 4.3.1.1-alt8
- Removing remains of mono2

* Tue Jan 19 2016 Denis Medvedev <nbr@altlinux.org> 4.3.1.1-alt7
- rpm-build-mono4 integration

* Mon Jan 18 2016 Denis Medvedev <nbr@altlinux.org> 4.3.1.1-alt6
- Added missing mono4-data to mono4-full

* Fri Jan 15 2016 Denis Medvedev <nbr@altlinux.org> 4.3.1.1-alt4
- Fixed dependence on mono4-full

* Thu Jan 14 2016 Denis Medvedev <nbr@altlinux.org> 4.3.1.1-alt3
- Virtual packages mono4-full and mono4-devel added

* Sun Dec 27 2015 Denis Medvedev <nbr@altlinux.org> 4.3.1.1-alt2
- Self compile

* Mon Dec 07 2015 Denis Medvedev <nbr@altlinux.org> 4.3.1.1-alt1
- Initial build of 4.* version (based on Fedora core spec)


:
