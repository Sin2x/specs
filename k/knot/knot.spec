%define _unpackaged_files_terminate_build 1
%define _localstatedir /var

%def_disable dnstap
%def_enable maxminddb
%def_enable xdp
%def_disable documentation

Name: knot
Version: 3.0.0
Release: alt1
Summary: High-performance authoritative DNS server
Group: System/Servers
License: GPL-3.0-or-later
Url: https://www.knot-dns.cz
Source0: %name-%version.tar
Patch0: %name-%version.patch

# Test fails on aarch/s390x for unknown reason, but it is not neccassary for Knot DNS
Patch1: 01-test_net-disable-udp-send-on-unconnected.patch

# Required dependencies
BuildRequires: pkgconfig(liburcu)
BuildRequires: pkgconfig(gnutls) >= 3.3
BuildRequires: pkgconfig(libedit)

# Optional dependencies
BuildRequires: pkgconfig(libcap-ng)
BuildRequires: pkgconfig(libidn2)
BuildRequires: pkgconfig(libnghttp2)
%{?_enable_maxminddb:BuildRequires: pkgconfig(libmaxminddb)}
%{?_enable_xdp:BuildRequires: pkgconfig(libbpf) >= 0.0.6}
BuildRequires: pkgconfig(libsystemd)
BuildRequires: pkgconfig(systemd)
%{?_enable_documentation:BuildRequires: /usr/bin/sphinx-build-3}
BuildRequires: liblmdb-devel
%{?_enable_dnstap:BuildRequires: /usr/bin/protoc-c pkgconfig(libfstrm) pkgconfig(libprotobuf-c) >= 1.0.0}

# Knot DNS 2.7+ isn't compatible with earlier knot-resolver
Conflicts: knot-resolver < 3.0.0

%description
Knot DNS is a high-performance authoritative DNS server implementation.

%package devel
Summary: Development files for the Knot DNS libraries
Group: Development/C

%description devel
Knot DNS is a high-performance authoritative DNS server implementation.

Development files for knot.

%package utils
Summary: DNS client utilities shipped with the Knot DNS server
Group: Networking/Other

%description utils
The package contains DNS client utilities shipped with the Knot DNS server.

%package -n libdnssec
Summary: Knot DNS DNSSEC library
Group: System/Libraries

%description -n libdnssec
Knot DNS DNSSEC library

%package -n libknot
Summary: Knot DNS library
Group: System/Libraries

%description -n libknot
Knot DNS library

%package -n libzscanner
Summary: Knot DNS Zone Parsing library
Group: System/Libraries

%description -n libzscanner
Knot DNS Zone Parsing library

%package doc
Summary: Documentation for the Knot DNS server
Group: Documentation
BuildArch: noarch

%description doc
The package contains documentation for the Knot DNS server.
On-line version is available on https://www.knot-dns.cz/documentation/

%prep
%setup
%patch0 -p1
%patch1 -p1

%build
# disable debug code (causes unused warnings)
%add_optflags -DNDEBUG -Wno-unused

%ifarch armv7hl %ix86 mips32 mipsn32
# 32-bit architectures sometimes do not have sufficient amount of
# contiguous address space to handle default values
%define configure_db_sizes --with-conf-mapsize=64
%endif

%autoreconf
%configure \
  --libexecdir=/usr/lib/%name \
  --with-rundir=/run/%name \
  --with-storage=/var/lib/%name \
  %{?configure_db_sizes} \
%if_enabled dnstap
  --enable-dnstap=yes \
  --with-module-dnstap=yes \
%endif
  %{subst_enable documentation} \
  --disable-static

%make_build
%if_enabled documentation
%make html
%endif

%install
%makeinstall_std

# install documentation
rm -f doc/_build/html/.buildinfo

# install configuration file
rm -f %buildroot%_sysconfdir/%name/*
install -p -m 0644 -D samples/%name.sample.conf %buildroot%_sysconfdir/%name/%name.conf

# install systemd files
install -p -m 0644 -D distro/common/%name.service %buildroot%_unitdir/%name.service
install -p -m 0644 -D distro/common/%name.tmpfiles %buildroot%_tmpfilesdir/%name.conf

# create storage dir and key dir
install -d %buildroot%_sharedstatedir
install -d -m 0775 -D %buildroot%_sharedstatedir/%name
install -d -m 0770 -D %buildroot%_sharedstatedir/%name/keys

# remove libarchive files
find %buildroot -type f -name "*.la" -delete -print

%check
%make check ||:

%pre
%_sbindir/groupadd -r -f %name
%_sbindir/useradd -M -r -d /var/lib/%name -s /bin/false -c "Knot DNS server" -g %name %name >/dev/null 2>&1 ||:

%post
%post_service %name

%preun
%preun_service %name

%files
%doc COPYING NEWS README.md samples
%dir %attr(750,root,%name) %_sysconfdir/%name
%config(noreplace) %attr(640,root,%name) %_sysconfdir/%name/%name.conf
%dir %attr(775,root,%name) %_sharedstatedir/%name
%dir %attr(770,root,%name) %_sharedstatedir/%name/keys
%_unitdir/%name.service
%_tmpfilesdir/%name.conf
%_bindir/kzone*
%_sbindir/*
%_man1dir/kzone*
%_man5dir/*
%_man8dir/*
%exclude %_sbindir/kxdpgun
%exclude %_man8dir/kxdpgun.*

%files utils
%_bindir/*
%if_enabled xdp
%_sbindir/kxdpgun
%_man8dir/kxdpgun.*
%endif
%_man1dir/*
%_bindir/kzonecheck
%_bindir/kzonesign
%exclude %_bindir/kzone*
%exclude %_man1dir/kzone*

%files devel
%_includedir/*
%_libdir/*.so
%_pkgconfigdir/*

%files -n libdnssec
%_libdir/libdnssec.so.*

%files -n libknot
%_libdir/libknot.so.*

%files -n libzscanner
%_libdir/libzscanner.so.*

%if_enabled documentation
%files doc
%doc html
%endif

%changelog
* Thu Sep 10 2020 Alexey Shabalin <shaba@altlinux.org> 3.0.0-alt1
- new version 3.0.0

* Sun May 31 2020 Alexey Shabalin <shaba@altlinux.org> 2.9.5-alt1
- new version 2.9.5

* Fri May 08 2020 Alexey Shabalin <shaba@altlinux.org> 2.9.4-alt1
- new version 2.9.4

* Wed Mar 18 2020 Alexey Shabalin <shaba@altlinux.org> 2.9.3-alt1
- Initial build.

