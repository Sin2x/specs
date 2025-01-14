%define _runtimedir /run

Name: lldpd
Version: 1.0.15
Release: alt1
Summary: Link Layer Discovery Protocol Daemon
Source: %name-%version.tar
Group: Networking/Other
License: ISC
Url: https://lldpd.github.io/
Vcs: https://github.com/lldpd/lldpd.git

Source1: lldpd.init
Source2: lldpd.sysconfig
Source3: lldpd.all.chroot
Source4: lldpd.conf.chroot
Source5: lldpd.service
Source6: lldpd.tmpfiles

Patch11: lldpd-alt-release.patch
Patch12: lldpd-fix-build-system-libevent.patch

%def_enable cdp
%def_enable fdp
%def_enable edp
%def_enable sonmp
%def_enable lldpmed
%def_enable dot1
%def_enable dot3

%def_with snmp
%def_with xml
%def_with readline
%def_without seccomp

BuildRequires: libssl-devel
BuildRequires: doxygen
BuildRequires: libevent-devel
BuildRequires: libcap-devel

Provides: bash-completion-lldpd = %EVR
Obsoletes: bash-completion-lldpd < %EVR
Provides: zsh-completion-lldpd = %EVR
Obsoletes: zsh-completion-lldpd < %EVR

%{?_with_readline:BuildRequires: libreadline-devel}
%{?_with_snmp:BuildRequires: libnet-snmp-devel}
%{?_with_xml:BuildRequires: libxml2-devel}
%{?_with_seccomp:BuildRequires: libseccomp-devel}

%description
LLDP (Link Layer Discovery Protocol) (also known as 802.1ab) is an
industry standard protocol designed to supplant proprietary Link-Layer
protocols such as Extreme's EDP (Extreme Discovery Protocol) and CDP
(Cisco Discovery Protocol). The goal of LLDP is to provide an
inter-vendor compatible mechanism to deliver Link-Layer notifications
to adjacent network devices.

lldpd is a lldp daemon for GNU/Linux and implements both reception and
sending. It supports both LLDP and LLDP-MED (contributed by Michael
Hanig). It also implements an SNMP subagent for net-snmp to get local
and remote LLDP information. The LLDP MIB is partially implemented but
the most useful tables are here.

lldpd supports bridge, vlan and bonding. bonding need to be done on
real physical devices, not on bridges, vlans, etc. However, vlans can
be mapped on the bonding device. You can bridge vlan but not add vlans
on bridges. More complex setups may give false results.

%package devel
Group: Development/C
Summary: Link Layer Discovery Protocol Daemon

%description devel
Header files for LLDP Daemon

%prep
%setup
%patch11 -p1
%patch12 -p1

%build
%autoreconf
%configure \
    --enable-pie \
    --disable-static \
    %{subst_enable cdp} \
    %{subst_enable fdp} \
    %{subst_enable edp} \
    %{subst_enable sonmp} \
    %{subst_enable lldpmed} \
    %{subst_enable dot1} \
    %{subst_enable dot3} \
    %{subst_with readline} \
    %{subst_with snmp} \
    %{subst_with xml} \
    %{subst_with seccomp} \
    --with-privsep-user=_lldpd \
    --with-privsep-group=_lldpd \
    --with-privsep-chroot=%_runtimedir/%name \
    --with-systemdsystemunitdir=%_unitdir \
    --without-embedded-libevent \
    --with-lldpd-ctl-socket=%_runtimedir/%name/%name.socket \
    --with-lldpd-pid-file=%_runtimedir/%name.pid

%make

%install
%make_install DESTDIR=%buildroot install
mv %buildroot%_datadir/doc/lldpd %buildroot%_datadir/doc/%name-%version
install -m755 -D %SOURCE1 %buildroot%_initdir/%name  
install -m644 -D %SOURCE2 %buildroot%_sysconfdir/sysconfig/%name
install -m750 -D %SOURCE3 %buildroot%_sysconfdir/chroot.d/%name.all
install -m750 -D %SOURCE4 %buildroot%_sysconfdir/chroot.d/%name.conf
install -m644 -D %SOURCE5 %buildroot%_unitdir/%name.service
install -m644 -D %SOURCE6 %buildroot%_tmpfilesdir/%name.conf
install -d -m 0755 %buildroot%_sharedstatedir/%name

%pre
groupadd -r -f _lldpd >/dev/null 2>&1 ||:
useradd -M -r -g _lldpd -s /dev/null -c "LLDP Daemon" \
        -s /bin/false -d %_sharedstatedir/%name _lldpd  >/dev/null 2>&1 ||:

%post
%post_service %name

%preun
%preun_service %name

%files
%_unitdir/*
%_tmpfilesdir/%name.conf
%_initdir/*
%config(noreplace) %_sysconfdir/sysconfig/%name
%_sysconfdir/chroot.d/*
%dir %_sysconfdir/lldpd.d
%config(noreplace) %_sysconfdir/lldpd.d/*
%_sbindir/*
%_libdir/liblldpctl.so.*
%_datadir/doc/%name-%version/
%_datadir/bash-completion/completions/*
%_datadir/zsh/site-functions/*
%dir %attr(0775, root, _lldpd) %_sharedstatedir/%name
%_man8dir/*

%files devel
%_includedir/*
%_libdir/liblldpctl.so
%_pkgconfigdir/*

%changelog
* Thu Sep 29 2022 Alexey Shabalin <shaba@altlinux.org> 1.0.15-alt1
- new version 1.0.15

* Fri Jun 03 2022 Alexey Shabalin <shaba@altlinux.org> 1.0.14-alt1
- new version 1.0.14

* Thu Dec 02 2021 Alexey Shabalin <shaba@altlinux.org> 1.0.13-alt1
- new version 1.0.13 (Fixes: CVE-2021-43612)
- migrate /var/run -> /run

* Sun Oct 31 2021 Alexey Shabalin <shaba@altlinux.org> 1.0.12-alt2
- disable build static lib

* Mon Aug 23 2021 Alexey Shabalin <shaba@altlinux.org> 1.0.12-alt1
- new version 1.0.12

* Thu Feb 18 2021 Alexey Shabalin <shaba@altlinux.org> 1.0.8-alt2
- disable seccomp

* Tue Feb 16 2021 Alexey Shabalin <shaba@altlinux.org> 1.0.8-alt1
- new version 1.0.8 (Fixes: CVE-2020-27827)
- enable seccomp for x86_64

* Tue Jul 21 2020 Alexey Shabalin <shaba@altlinux.org> 1.0.5-alt1
- new version 1.0.5

* Fri Oct 04 2019 Alexey Shabalin <shaba@altlinux.org> 1.0.4-alt1
- new version 1.0.4
- merge complitions subpackages with main package

* Tue Jan 22 2019 Alexey Shabalin <shaba@altlinux.org> 1.0.3-alt1
- 1.0.3

* Fri Apr 13 2018 Alexey Shabalin <shaba@altlinux.ru> 1.0.1-alt1
- 1.0.1

* Sat Mar 24 2018 Alexey Shabalin <shaba@altlinux.ru> 0.9.9-alt2
- add tmpfiles for chroot dir
- move chroot dir from /var/lib/lldpd to /var/ran/lldpd

* Sat Mar 24 2018 Alexey Shabalin <shaba@altlinux.ru> 0.9.9-alt1
- add ubt suffix to release

* Sat Mar 24 2018 Alexey Shabalin <shaba@altlinux.ru> 0.9.9-alt1
- 0.9.9
- add modified systemd unit

* Wed Mar 21 2018 Igor Vlasenko <viy@altlinux.ru> 0.9.5-alt1.1
- NMU: added URL

* Sun Oct 23 2016 Afanasov Dmitry <ender@altlinux.org> 0.9.5-alt1
- 0.9.5
- switch from json-c to jannson: json-c too old
- disable seccomp

* Tue Dec 22 2015 Afanasov Dmitry <ender@altlinux.org> 0.7.19-alt1
- 0.7.19

* Wed Aug 26 2015 Afanasov Dmitry <ender@altlinux.org> 0.7.15-alt1
- 0.7.15
- add json output and seccomp support
- build bash and zsh completions in a separate packages

* Mon Dec 02 2013 Afanasov Dmitry <ender@altlinux.org> 0.7.6-alt1
- new version (upstream commit 5f7d1c)

* Thu Nov 28 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.1-alt2.1
- Fixed build

* Fri Nov 02 2012 Afanasov Dmitry <ender@altlinux.org> 0.6.1-alt2
- add init scripts

* Wed Oct 31 2012 Afanasov Dmitry <ender@altlinux.org> 0.6.1-alt1
- first build

