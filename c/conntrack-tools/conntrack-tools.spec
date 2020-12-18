Name: conntrack-tools
Version: 1.4.6
Release: alt2
Summary: Tool to manipulate netfilter connection tracking table
Group: System/Kernel and hardware
License: GPLv2
Url: http://netfilter.org
Source0: http://netfilter.org/projects/conntrack-tools/files/%name-%version.tar

BuildRequires: flex libnetfilter_conntrack-devel libmnl-devel
BuildRequires: libnetfilter_cttimeout-devel libnetfilter_cthelper-devel libnetfilter_queue-devel
BuildRequires: libsystemd-devel
BuildRequires: libtirpc-devel

%description
%name  is  used to search, list, inspect and maintain the netfilter
connection tracking subsystem of the Linux kernel.
Using conntrack , you can dump a list of all (or a filtered selection  of)
currently  tracked  connections, delete connections from the state table,
and even add new ones.
In  addition,  you  can  also  monitor connection tracking events, e.g.
show an event message (one line) per newly established connection.

%prep
%setup

%build
%autoreconf -fisv
%configure --enable-systemd
%make

%install
make install DESTDIR=%buildroot
rm -f %buildroot%_libdir/conntrack-tools/*.la

%files
%doc COPYING AUTHORS
%_sbindir/conntrack
%_sbindir/nfct
%_sbindir/conntrackd
%_libdir/%name/*.so
%_man8dir/*
%_man5dir/*

%changelog
* Fri Dec 18 2020 Anton Farygin <rider@altlinux.ru> 1.4.6-alt2
- added libtirpc to BuildRequires against glibc-2.32

* Tue Apr 14 2020 Anton Farygin <rider@altlinux.ru> 1.4.6-alt1
- 1.4.6
- cleanup spec

* Fri Jun 14 2019 Anton Farygin <rider@altlinux.ru> 1.4.5-alt2
- removed ubt macros

* Tue May 22 2018 Anton Farygin <rider@altlinux.ru> 1.4.5-alt1
- 1.4.5

* Mon Mar 27 2017 Anton Farygin <rider@altlinux.ru> 1.4.4-alt1
- new version

* Mon Jun 24 2013 Anton Farygin <rider@altlinux.ru> 1.4.1-alt1
- new version

* Mon Dec 03 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.15-alt1.1
- Fixed build with glibc 2.16

* Sat Oct 30 2010 Anton Farygin <rider@altlinux.ru> 0.9.15-alt1
- New version

* Mon May 05 2008 Avramenko Andrew <liks@altlinux.ru> 0.9.6-alt1
- NMU: New version (Fix build with a new libnetfilter_conntrack)

* Mon Jun 18 2007 Eugene Ostapets <eostapets@altlinux.ru> 0.9.3-alt0.1
- first build

