%def_without check

Name: crtools-ovz
Version: 3.15.1.27
Release: alt1

Summary: Utility to checkpoint/restore tasks for OpenVZ containers
License: GPL-2.0-only
Group: System/Configuration/Other
Url: http://criu.org

Packager: Andrew A. Vasilyev <andy@altlinux.org>

# VCS: https://src.openvz.org/scm/ovz/criu.git
Source: criu-%version.tar

Provides: criu-ovz = %EVR
Conflicts: crtools
ExclusiveArch: x86_64

BuildRequires: libnet2-devel
BuildRequires: libprotobuf-c-devel %_bindir/protoc-c
BuildRequires: libprotobuf-devel protobuf-compiler
BuildRequires: asciidoc xmlto %_bindir/a2x
BuildRequires: libnftables-devel
BuildRequires: libgnutls-devel
BuildRequires: glibc-devel
BuildRequires: libnl-devel
BuildRequires: libcap-devel
BuildRequires: python3-base
# BuildRequires: libselinux-devel
BuildRequires(pre): rpm-build-python3

%if_with check
BuildRequires: rpm-build-vm-run
BuildRequires: vzkernel
BuildRequires: libaio-devel
BuildRequires: python-module-future python3-module-yaml python3-module-protobuf
BuildRequires: libbsd-devel
BuildRequires: iproute2 iptables iputils openvswitch
%endif

Requires: nftables util-linux ipset

%description
An utility to checkpoint/restore tasks for OpenVZ containers.

%prep
%setup -n criu-%version

%build
export CFLAGS="%optflags -fcommon"
export PYTHON=python3
%make_build \
	PREFIX=%prefix V=1 all docs

%install
export PYTHON=python3
%makeinstall_std \
	PREFIX=%prefix LIBDIR=%_libdir LIBEXECDIR=%_libexecdir SYSTEMDUNITDIR=%_unitdir

mv %buildroot%_sbindir/criu{,-ovz}
ln -s criu-ovz %buildroot%_sbindir/criu
ln -s criu-ovz %buildroot%_sbindir/crtools
ln -s criu.8 %buildroot%_man8dir/crtools.8

find %buildroot -name 'lib*.a' -delete

rm -f %buildroot%_bindir/crit
rm -rf %buildroot%python3_sitelibdir_noarch
rm -f %buildroot%_man1dir/crit.1*
rm -f %buildroot%_libdir/libcriu.so.2*
rm -f %buildroot%_libdir/libcompel.so.1*
rm -rf %buildroot%_includedir/criu
rm -rf %buildroot%_includedir/compel
rm -f %buildroot%_libdir/*.so
rm -f %buildroot%_pkgconfigdir/criu.pc

%check
vm-run --kvm=cond make test || :

%files
%doc README.md COPYING CREDITS
%_sbindir/criu
%_sbindir/criu-ovz
%_sbindir/crtools
%_bindir/compel
%_libexecdir/criu
%_libexecdir/compel
%_man1dir/compel.1*
%_man8dir/criu.8*
%_man8dir/crtools.8*

%changelog
* Tue Apr 13 2021 Andrew A. Vasilyev <andy@altlinux.org> 3.15.1.27-alt1
- 3.15.1.27

* Thu Apr 08 2021 Andrew A. Vasilyev <andy@altlinux.org> 3.15.1.26-alt1
- 3.15.1.26

* Mon Mar 08 2021 Andrew A. Vasilyev <andy@altlinux.org> 3.15.1.23-alt1
- 3.15.1.23

* Fri Feb 19 2021 Andrew A. Vasilyev <andy@altlinux.org> 3.15.1.22-alt1
- 3.15.1.22

* Mon Feb 01 2021 Andrew A. Vasilyev <andy@altlinux.org> 3.15.1.15-alt1
- 3.15.1.15

* Sat Jan 02 2021 Andrew A. Vasilyev <andy@altlinux.org> 3.15.0.15-alt1
- 3.15.0.15

* Fri Dec 25 2020 Andrew A. Vasilyev <andy@altlinux.org> 3.15.0.14-alt1
- 3.15.0.14

* Tue Dec 08 2020 Andrew A. Vasilyev <andy@altlinux.org> 3.15.0.9-alt1
- 3.15.0.9

* Mon Nov 09 2020 Andrew A. Vasilyev <andy@altlinux.org> 3.12.5.52-alt1
- 3.12.5.52
- cherry-picked commit 86a386a0171eb553d5d3bcb5db92ff13b1f60ad4
  from criu real upstream: "Update test_bit() and test_and_set_bit()
  implementation with recent version from the Linux kernel to fix the warning."

* Fri Oct 30 2020 Andrew A. Vasilyev <andy@altlinux.org> 3.12.5.50-alt1
- 3.12.5.50

* Mon Oct 12 2020 Andrew A. Vasilyev <andy@altlinux.org> 3.12.5.46-alt1
- 3.12.5.46

* Mon Oct 05 2020 Andrew A. Vasilyev <andy@altlinux.org> 3.12.5.44-alt1
- 3.12.5.44

* Fri Oct 02 2020 Andrew A. Vasilyev <andy@altlinux.org> 3.12.5.43-alt1
- 3.12.5.43

* Wed Sep 30 2020 Andrew A. Vasilyev <andy@altlinux.org> 3.12.5.41-alt1
- 3.12.5.41
- remove all extra packages not needed for OpenVZ

* Mon Sep 14 2020 Andrew A. Vasilyev <andy@altlinux.org> 3.12.5.40-alt1
- 3.12.5.40

* Fri Sep 11 2020 Andrew A. Vasilyev <andy@altlinux.org> 3.12.5.38-alt1
- Initial build for ALT from Virtuozzo fork of criu, spec based on crtool.

