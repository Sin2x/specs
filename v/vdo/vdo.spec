%define _unpackaged_files_terminate_build 1

Summary: Management tools for Virtual Data Optimizer
Name: vdo
Version: 6.2.3.114
Release: alt1
Group: System/Base
License: GPLv2
Source: %name-%version.tar
Patch: %name-%version.patch

Url: http://github.com/dm-vdo/vdo
ExclusiveArch: x86_64 aarch64 ppc64le ppc64 s390 s390x

Requires: lvm2

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel
BuildRequires: libdevmapper-devel libdevmapper-event-devel
BuildRequires: libuuid-devel libblkid-devel
BuildRequires: zlib-devel

%description
Virtual Data Optimizer (VDO) is a device mapper target that delivers
block-level deduplication, compression, and thin provisioning.

This package provides the user-space management tools for VDO.

%package support
Summary: Support tools for Virtual Data Optimizer
Group: System/Base
Requires: libuuid >= 2.23

%description support
Virtual Data Optimizer (VDO) is a device mapper target that delivers
block-level deduplication, compression, and thin provisioning.

This package provides the user-space support tools for VDO.

%prep
%setup
%patch -p1

%build
%make

%install
%make install DESTDIR=%buildroot INSTALLOWNER= bindir=%_bindir \
  defaultdocdir=%_defaultdocdir name=%name \
  python3_sitelib=/%python3_sitelibdir mandir=%_mandir \
  unitdir=%_unitdir presetdir=%_presetdir sysconfdir=%_sysconfdir

%post
%post_service vdo

%preun
%preun_service vdo

%files
%_bindir/vdo
%_bindir/vdostats
%_bindir/vdodmeventd
%_bindir/vdodumpconfig
%_bindir/vdoforcerebuild
%_bindir/vdoformat
%_bindir/vdosetuuid
%_bindir/vdo-by-dev
%python3_sitelibdir/*
%_unitdir/vdo.service
%_unitdir/vdo-start-by-dev@.service
%_presetdir/97-vdo.preset
%_sysconfdir/udev/rules.d/69-vdo-start-by-dev.rules
%dir %_defaultdocdir/%name
%doc %_defaultdocdir/%name/COPYING
%_defaultdocdir/%name/examples
%_man8dir/vdo.8*
%_man8dir/vdostats.8*
%_man8dir/vdodmeventd.8*
%_man8dir/vdodumpconfig.8*
%_man8dir/vdoforcerebuild.8*
%_man8dir/vdoformat.8*
%_man8dir/vdosetuuid.8*
%_sysconfdir/bash_completion.d/vdo*

%files support
%_bindir/vdoaudit
%_bindir/vdodebugmetadata
%_bindir/vdodumpblockmap
%_bindir/vdodumpmetadata
%_bindir/vdolistmetadata
%_bindir/vdoreadonly
%_bindir/vdoregenerategeometry
%_man8dir/vdoaudit.8*
%_man8dir/vdodebugmetadata.8*
%_man8dir/vdodumpblockmap.8*
%_man8dir/vdodumpmetadata.8*
%_man8dir/vdolistmetadata.8*
%_man8dir/vdoreadonly.8*
%_man8dir/vdoregenerategeometry.8*

%changelog
* Mon Sep 07 2020 Alexey Shabalin <shaba@altlinux.org> 6.2.3.114-alt1
- 6.2.3.114
- add vdo-support package

* Sat Apr 11 2020 Alexey Shabalin <shaba@altlinux.org> 6.2.2.117-alt1
- 6.2.2.117

* Thu Dec 12 2019 Alexey Shabalin <shaba@altlinux.org> 6.2.2.33-alt1
- 6.2.2.33

* Tue Oct 22 2019 Alexey Shabalin <shaba@altlinux.org> 6.2.2.18-alt1
- 6.2.2.18

* Sun Aug 11 2019 Alexey Shabalin <shaba@altlinux.org> 6.2.1.134-alt1
- 6.2.1.134

* Thu Feb 21 2019 Alexey Shabalin <shaba@altlinux.org> 6.2.0.293-alt1
- initial build for ALT
