Epoch: 1
Group: Security/Networking
# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/protoc /usr/bin/protoc-c binutils-devel libdw-devel libsensors3-devel libunwind-devel zlib-devel
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
# %%name is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define name kismet
%global _version        2020-09-R4

## {Local macros...
%global cfgdir          %_sysconfdir/%name
%global _rpmversion     0.0.%(echo %_version | tr - .)
## ...local macros}

%{!?apply:%global  apply(p:n:b:) %patch%%{-n:%%{-n*}} %%{-p:-p%%{-p*}} %%{-b:-b%%{-b*}} \
%nil}

Summary:        WLAN detector, sniffer and IDS
Name:           kismet
Version:        %_rpmversion
Release:        alt1_2
License:        GPLv2+
URL:            http://www.kismetwireless.net/
Source0:        http://www.kismetwireless.net/code/%{name}-%_version.tar.xz

Patch0:         kismet-include.patch
Patch1:         kismet-install.patch

BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  libncurses++-devel libncurses-devel libncursesw-devel libtic-devel libtinfo-devel diffutils
BuildRequires:  libpcap-devel libpcre-devel libpcrecpp-devel
BuildRequires:  libssl-devel libcap-devel libnl-devel
BuildRequires:  libbluez-devel
BuildRequires:  libmicrohttpd-devel libprotobuf-devel libprotobuf-c-devel
BuildRequires:  libnm-devel libnm-gir-devel libusb-devel
BuildRequires:  libsqlite3-devel
Source44: import.info

%description
Kismet is an 802.11 layer2 wireless network detector, sniffer, and
intrusion detection system. Kismet will work with any wireless card
which supports raw monitoring (rfmon) mode, and can sniff 802.11b,
802.11a, and 802.11g traffic.

Kismet identifies networks by passively collecting packets and detecting
standard named networks, detecting (and given time, decloaking) hidden
networks, and infering the presence of nonbeaconing networks via data
traffic.

%prep
%setup -qn %{name}-%{_version}

%patch0 -p0
%patch1 -p0

sed -i 's!\$(prefix)/lib/!%{_libdir}/!g' plugin-*/Makefile


# set our 'kismet' user, disable GPS and log into %%logdir by
# default
sed -i \
    -e '\!^ouifile=/etc/manuf!d' \
    -e '\!^ouifile=/usr/share/wireshark/wireshark/manuf!d' \
    conf/kismet.conf

%build

export ac_cv_lib_uClibcpp_main=no # we do not want to build against uClibc++, even when available
export LDFLAGS='-Wl,--as-needed'
%configure \
           --sysconfdir=%cfgdir \
           CXXFLAGS="$RPM_OPT_FLAGS -D__STDC_FORMAT_MACROS" \
           --disable-python-tools

%make_build

sed -i s/2019-08-GIT/%{version}-%{release}%{?dist}/g packaging/kismet.pc

%install
BIN=$RPM_BUILD_ROOT/bin ETC=$RPM_BUILD_ROOT/etc %makeinstall_std

%files
%doc CHANGELOG README* docs/
%dir %attr(0755,root,root) %cfgdir
%config(noreplace) %cfgdir/*
%{_bindir}/kismet*
%{_datadir}/kismet
%{_libdir}/pkgconfig/kismet.pc

%changelog
* Sun Nov 22 2020 Igor Vlasenko <viy@altlinux.ru> 1:0.0.2020.09.R4-alt1_2
- picked up from orphaned to fix unmets in autoimports

* Thu Feb 14 2019 Andrey Bychkov <mrdrew@altlinux.org> 2014.02.R1-alt2
- no return statement in the non-void function fixed (according g++8)

* Tue Jan 23 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 2014.02.R1-alt1
- Updated to upstream version 2014.02.R1.

* Mon Apr 15 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 2010.07.R1-alt1.1.qa1
- NMU: rebuilt for debuginfo.

* Tue Dec 07 2010 Igor Vlasenko <viy@altlinux.ru> 2010.07.R1-alt1.1
- rebuild with new openssl and/or boost by request of git.alt administrator

* Sat Jul 17 2010 Andrey Rahmatullin <wrar@altlinux.org> 2010.07.R1-alt1
- 2010-07-R1

* Tue Jan 12 2010 Andrey Rahmatullin <wrar@altlinux.ru> 2010.01.R1-alt1
- 2010-01-R1
- package plugin README file

* Fri Dec 02 2009 Andrey Rahmatullin <wrar@altlinux.ru> 2009.11.R1-alt1
- 2009-11-R1

* Sun Aug 23 2009 Andrey Rahmatullin <wrar@altlinux.ru> 2009.06.R1-alt1
- 2009-06-R1 Newcore (closes: #15590)
- drop initscript and all related stuff, server should be run by user
  now (closes: #21186)
- implement control(8) support for kismet_capture (raorn@)
- package bundled plugins into -plugins subpackage
- leave only proper path to the wireshark manuf file in the default
  config (RH)

* Tue Aug 11 2009 Ilya Mashkin <oddity@altlinux.ru> 2008.05.R1-alt3
- fix build in current environment

* Sat Feb 21 2009 Ilya Mashkin <oddity@altlinux.ru> 2008.05.R1-alt2
- fix build
- update requires (fix #18831)
- fix init script (fix #18832)

* Mon Jun 02 2008 Pavlov Konstantin <thresh@altlinux.ru> 2008.05.R1-alt1
- 2008-05-R1 release.

* Fri Oct 19 2007 Pavlov Konstantin <thresh@altlinux.ru> 2007.10.R1-alt1
- 2007.10.R1 version.

* Sun Jan 21 2007 Pavlov Konstantin <thresh@altlinux.ru> 2007.01.R1b-alt4
- Added fix for enable building on x86_64.

* Sun Jan 21 2007 Pavlov Konstantin <thresh@altlinux.ru> 2007.01.R1b-alt3
- Specfile fixes here and there.
- Removed wget and diffutils from build requres.
- Replaced linux-libc-headers with glibc-kernheaders.
- Introduced gpsmap package.
- Packed some scripts from extra/ to kismet-common package.

* Sat Jan 20 2007 Pavlov Konstantin <thresh@altlinux.ru> 2007.01.R1b-alt2
- Added daemonization patch.
- Fixed kismet init script to work with daemonization.

* Sat Jan 20 2007 Pavlov Konstantin <thresh@altlinux.ru> 2007.01.R1b-alt1
- 2007-01-R1b version.

* Sat Jan 20 2007 Pavlov Konstantin <thresh@altlinux.ru> 2006.04.R1-alt2
- Merged patches into source tree.
- Removed unneeded SOURCE1.

* Fri Nov 17 2006 Pavlov Konstantin <thresh@altlinux.ru> 2006.04.R1-alt1
- Added init-script.
- Changed pid dir.
- Removed *.conf files from common package.

* Mon Aug 28 2006 Pavlov Konstantin <thresh@altlinux.ru> 2006.04.R1-alt0.2
- Initial packaging for ALT Linux.
- main package is virtual, that requires:
  + kismet-server, the server side of kismet.
  + kismet-client, the client user interface of kismet.
  + kismet-drone, the remote drone for kismet.
- The spec file is based on Mandriva/FC's one, good man who made it is
  + Enrico Scholz <enrico.scholz@informatik.tu-chemnitz.de>

