%define _unpackaged_files_terminate_build 1

%define sdkversion 3.1.420
%define coreversion 3.1.26
%define templatesversion 3.1.27

Name: dotnet-bootstrap-3.1
Version: 3.1.26
Release: alt1

Summary: .NET Core SDK binaries

License: MIT
Url: https://github.com/dotnet
Group: Development/Other

# Update from https://www.microsoft.com/net/download/dotnet-core/3.1

# Source-url: https://download.visualstudio.microsoft.com/download/pr/5424da8c-ce12-46de-a51a-8fa61aefdde6/52a9d6b5718ea40863db96901c780d4b/dotnet-sdk-3.1.420-linux-x64.tar.gz
Source: %name-%version.tar

# Source2-url: https://download.visualstudio.microsoft.com/download/pr/a84bf296-ee6e-4e66-9694-90d3da7af2b4/b00b2efe2432938e5a19c45d3759d80f/dotnet-sdk-3.1.420-linux-arm64.tar.gz
Source2: %name-aarch64-%version.tar

ExclusiveArch: x86_64 aarch64

#Requires: /proc
#BuildPreReq: /proc

%set_verify_elf_method textrel=relaxed
AutoReq: no,lib,shell
AutoProv: no

BuildRequires: libunwind >= 1.1
BuildRequires: liblttng-ust >= 2.8.0
BuildRequires: libcurl
BuildRequires: libkrb5

# for System.Security.Cryptography.Native.OpenSsl.so
# but already required by libkrb5
#Requires: libcrypto10 libssl10

# it is not linked directly (need the same version like in libicu-devel)
# there are icu detection in a version range
Requires: libicu

Provides: dotnet-bootstrap-runtime-3.1 = %coreversion
Provides: dotnet-bootstrap-sdk-3.1 = %sdkversion

%description
This package contains full .NET Core SDK binaries, needed for bootstrap build.

https://github.com/dotnet/core/blob/master/release-notes/download-archives/%version-download.md

%prep
%setup
%ifarch aarch64
rm -rf packs/ host/ shared/
tar xfv %SOURCE2

sed -E -i -e "s@CURL_OPENSSL_3@\x0URL_OPENSSL_3@" shared/Microsoft.NETCore.App/%coreversion/System.Net.Http.Native.so
%endif

%install
mkdir -p %buildroot%_libdir/%name/
cp -a * %buildroot%_libdir/%name/

# due missed lldb (TODO)
rm -f %buildroot%_libdir/%name/shared/Microsoft.NETCore.App/*/libsosplugin.so
%__subst "s|libsosplugin.so|libsos.so|g" %buildroot%_libdir/%name/shared/Microsoft.NETCore.App/*/Microsoft.NETCore.App.deps.json

cd %buildroot%_libdir/%name

# See also https://bugzilla.altlinux.org/show_bug.cgi?id=37413
strip \
	shared/Microsoft.NETCore.App/%coreversion/libmscordbi.so \
	shared/Microsoft.NETCore.App/%coreversion/libmscordaccore.so \
	shared/Microsoft.NETCore.App/%coreversion/libhostpolicy.so \
	shared/Microsoft.NETCore.App/%coreversion/libdbgshim.so \
	shared/Microsoft.NETCore.App/%coreversion/libcoreclrtraceptprovider.so \
	shared/Microsoft.NETCore.App/%coreversion/libcoreclr.so \
	shared/Microsoft.NETCore.App/%coreversion/libclrjit.so \
	shared/Microsoft.NETCore.App/%coreversion/createdump \
	shared/Microsoft.NETCore.App/%coreversion/System.Security.Cryptography.Native.OpenSsl.so \
	shared/Microsoft.NETCore.App/%coreversion/System.Net.Security.Native.so \
	shared/Microsoft.NETCore.App/%coreversion/System.Net.Http.Native.so \
	shared/Microsoft.NETCore.App/%coreversion/System.Native.so \
	shared/Microsoft.NETCore.App/%coreversion/System.IO.Compression.Native.so \
	shared/Microsoft.NETCore.App/%coreversion/System.Globalization.Native.so \
	sdk/%sdkversion/AppHostTemplate/apphost \
%ifarch x86_64
	packs/Microsoft.NETCore.App.Host.linux-x64/%coreversion/runtimes/linux-x64/native/libnethost.so \
	packs/Microsoft.NETCore.App.Host.linux-x64/%coreversion/runtimes/linux-x64/native/apphost \
%endif
%ifarch aarch64
	packs/Microsoft.NETCore.App.Host.linux-arm64/%coreversion/runtimes/linux-arm64/native/libnethost.so \
	packs/Microsoft.NETCore.App.Host.linux-arm64/%coreversion/runtimes/linux-arm64/native/apphost \
%endif
	host/fxr/%coreversion/libhostfxr.so \
	dotnet \
	#

%files
%dir %_libdir/%name/
%dir %_libdir/%name/templates/
%_libdir/%name/templates/%templatesversion/
%dir %_libdir/%name/packs/
%dir %_libdir/%name/packs/Microsoft.AspNetCore.App.Ref
%_libdir/%name/packs/Microsoft.AspNetCore.App.Ref/3.1.10/
%ifarch aarch64
%dir %_libdir/%name/packs/Microsoft.NETCore.App.Host.linux-arm64/
%_libdir/%name/packs/Microsoft.NETCore.App.Host.linux-arm64/%coreversion/
%else
%dir %_libdir/%name/packs/Microsoft.NETCore.App.Host.linux-x64/
%_libdir/%name/packs/Microsoft.NETCore.App.Host.linux-x64/%coreversion/
%endif
%dir %_libdir/%name/packs/Microsoft.NETCore.App.Ref/
%_libdir/%name/packs/Microsoft.NETCore.App.Ref/3.1.0/
%dir %_libdir/%name/packs/NETStandard.Library.Ref/
%_libdir/%name/packs/NETStandard.Library.Ref/2.1.0/
%dir %_libdir/%name/host/
%dir %_libdir/%name/host/fxr/
%_libdir/%name/host/fxr/%coreversion/
%dir %_libdir/%name/sdk/
%_libdir/%name/sdk/%sdkversion/
%dir %_libdir/%name/shared/
%dir %_libdir/%name/shared/Microsoft.NETCore.App/
%_libdir/%name/shared/Microsoft.NETCore.App/%coreversion/
# TODO: drop from bootstrap
#dir %_libdir/%name/shared/Microsoft.AspNetCore.All/
%dir %_libdir/%name/shared/Microsoft.AspNetCore.App/
#_libdir/%name/shared/Microsoft.AspNetCore.All/%coreversion/
%_libdir/%name/shared/Microsoft.AspNetCore.App/%coreversion/
#_libdir/%name/store/
%_libdir/%name/LICENSE.txt
%_libdir/%name/ThirdPartyNotices.txt
%_libdir/%name/dotnet

%changelog
* Fri Aug 05 2022 Vitaly Lipatov <lav@altlinux.ru> 3.1.26-alt1
- .NET Core 3.1.26 and .NET Core SDK 3.1.420 releases
- CVE-2022-30184: .NET Information Disclosure Vulnerability
- CVE-2022-29117: .NET Denial of Service Vulnerability
- CVE-2022-29145: .NET Denial of Service Vulnerability
- CVE-2022-23267: .NET Denial of Service Vulnerability

* Sat Apr 02 2022 Vitaly Lipatov <lav@altlinux.ru> 3.1.23-alt1
- .NET Core 3.1.23 and .NET Core SDK 3.1.417 releases
- CVE-2022-24464 : .NET Denial of Service Vulnerability
- CVE-2022-24512 : .NET Remote Code Execution Vulnerability
- CVE-2020-8927 : .NET Remote Code Execution Vulnerability

* Sat Feb 12 2022 Vitaly Lipatov <lav@altlinux.ru> 3.1.22-alt1
- .NET Core 3.1.22 - December 14, 2021
- CVE-2021-43877: ASP.NET Core Elevation of privilege Vulnerability
- CVE-2021-34485: .NET Core Information Disclosure Vulnerability
- CVE-2021-26423: .NET Core Denial of Service Vulnerability
- CVE-2021-34532: ASP.NET Core Information Disclosure Vulnerability

* Wed Jun 30 2021 Vitaly Lipatov <lav@altlinux.ru> 3.1.16-alt1
- new version 3.1.16 (with rpmrb script)
- .NET Core 3.1.16 and .NET Core SDK 3.1.410
- CVE-2021-31957: ASP.NET Denial of Service Vulnerability
- CVE-2021-31204: .NET Core Elevation of Privilege Vulnerability

* Sat Apr 17 2021 Vitaly Lipatov <lav@altlinux.ru> 3.1.14-alt1
- .NET Core 3.1.14 and .NET Core SDK 3.1.408
- CVE-2021-26701 | .NET Core Remote Code Execution Vulnerability

* Wed Feb 17 2021 Vitaly Lipatov <lav@altlinux.ru> 3.1.12-alt1
- new version (3.1.12) with rpmgs script
- CVE-2021-1721: .NET Core Denial of Service Vulnerability
- CVE-2021-24112: .NET 5 and .NET Core Remote Code Execution Vulnerability

* Thu Jan 28 2021 Vitaly Lipatov <lav@altlinux.ru> 3.1.11-alt1
- new version (3.1.11) with rpmgs script
- .NET Core 3.1.11 - January 12, 2021
- CVE-2021-1723: ASP.NET Core Denial of Service Vulnerability
- CVE-2020-1045: Microsoft ASP.NET Core Security Feature Bypass Vulnerability
- CVE-2020-1597: NET Core Remote Code Execution Vulnerability

* Sun Aug 02 2020 Vitaly Lipatov <lav@altlinux.ru> 3.1.6-alt1
- new version 3.1.6 (with rpmrb script) (ALT bug 38744)
- .NET Core 3.1.6 - July 14, 2020
- CVE-2020-1108: .NET Core Denial of Service Vulnerability
- CVE-2020-1147: NET Core Remote Code Execution Vulnerability

* Mon Dec 16 2019 Vitaly Lipatov <lav@altlinux.ru> 3.1.0-alt1
- new version (3.1.0) with rpmgs script
- .NET Core 3.1.0 - December 3, 2019

* Fri Nov 08 2019 Gleb F-Malinovskiy <glebfm@altlinux.org> 3.0.0-alt1.qa1
- Dropped hack for ld-linux path on aarch64.

* Sat Oct 05 2019 Vitaly Lipatov <lav@altlinux.ru> 3.0.0-alt1
- new version (3.0.0) with rpmgs script
- .NET Core 3.0.0 - September 23, 2019

* Wed Mar 13 2019 Vitaly Lipatov <lav@altlinux.ru> 2.1.9-alt1
- new version 2.1.9 (with rpmrb script)
- includes .NET Core 2.1.9, ASP.NET Core 2.1.9 and .NET Core SDK 2.1.505
- CVE-2019-0657: .NET Core NuGet Tampering Vulnerability

* Tue Dec 04 2018 Vitaly Lipatov <lav@altlinux.ru> 2.1.6-alt1
- new version 2.1.6 (with rpmrb script)
- includes .NET Core 2.1.6, ASP.NET Core 2.1.6 and .NET Core SDK 2.1.500

* Fri Oct 12 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 2.1.5-alt1
- NMU: new version (2.1.5) (based on changes by lav@)
- includes .NET Core 2.1.5, ASP.NET Core 2.1.5 and .NET Core SDK 2.1.403

* Sat Sep 15 2018 Vitaly Lipatov <lav@altlinux.ru> 2.1.4-alt1
- new version (2.1.4) with rpmgs script
- includes .NET Core 2.1.4, ASP.NET Core 2.1.4 and .NET Core SDK 2.1.402

* Mon Sep 03 2018 Vitaly Lipatov <lav@altlinux.ru> 2.1.3-alt1
- new version (2.1.3) with rpmgs script
- includes .NET Core 2.1.3, ASP.NET Core 2.1.3 and .NET Core SDK 2.1.401

* Mon Feb 05 2018 Vitaly Lipatov <lav@altlinux.ru> 2.0.5-alt1
- new version (2.0.5) with rpmgs script
- CVE-2018-0764, CVE-2018-0786

* Thu Nov 23 2017 Vitaly Lipatov <lav@altlinux.ru> 2.0.3-alt1
- new version (2.0.3) with rpmgs script

* Sun Aug 27 2017 Vitaly Lipatov <lav@altlinux.ru> 2.0.0-alt3
- new version (2.0.0) with rpmgs script

* Fri Jul 14 2017 Vitaly Lipatov <lav@altlinux.ru> 2.0.0-alt2.preview2
- enable autoreq for libs, shell
- fix buildreqs to correct generated requires

* Fri Jul 14 2017 Vitaly Lipatov <lav@altlinux.ru> 2.0.0-alt1.preview2
- add provides with .NET Core runtime/SDK versions

* Thu Jul 13 2017 Vitaly Lipatov <lav@altlinux.ru> 2.0.0-alt0.preview2
- .NET Core Runtime 2.0.0 Preview 2 build 25407-01
- .NET Core SDK 2.0.0 Preview 2 build 006497

* Thu May 11 2017 Vitaly Lipatov <lav@altlinux.ru> 2.0.0-alt0.preview1.005977
- .NET Core Runtime 2.0.0 Preview 1 build 002111
- .NET Core SDK 2.0.0 Preview 1 build 005977

* Fri Apr 28 2017 Vitaly Lipatov <lav@altlinux.ru> 1.1.1-alt1
- new version (1.1.1) with rpmgs script (SDK 1.0.3)

* Fri Apr 14 2017 Vitaly Lipatov <lav@altlinux.ru> 1.0.4-alt1
- initial release for ALT Sisyphus
