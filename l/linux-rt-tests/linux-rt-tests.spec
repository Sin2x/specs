# SPDX-License-Identifier: GPL-2.0-only
%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1

# rt-tests is taken by perl tests for RT
Name:     linux-rt-tests
Version:  1.9
Release:  alt1

Summary:  Programs that test various rt-linux features
License:  GPL-2.0-or-later
Group:    System/Kernel and hardware
Url:      https://wiki.linuxfoundation.org/realtime/documentation/howto/tools/rt-tests
Vcs:      git://git.kernel.org/pub/scm/utils/rt-tests/rt-tests.git

Source: %name-%version.tar
# No libnuma, no cyclictest.
ExcludeArch: armh
BuildRequires(pre): rpm-build-python3
BuildRequires: libnuma-devel

%description
rt-tests is a test suite, that contains programs (such as cyclictest,
hwlatdetect, hackbench) to test various Real Time Linux features.

%prep
%setup
%ifarch aarch64
  # src/oslat/oslat.c:72:4: error: #error Need frc() for this platform.
  sed -i '/oslat\.[c8]/d' Makefile
%endif

%build
%make_build CFLAGS="%optflags" prefix=/usr

%install
%makeinstall_std prefix=/usr

%files
%doc COPYING MAINTAINERS README.markdown src/hwlatdetect/hwlat.txt
%_bindir/*
#%_sbindir/hwlatdetect
%python3_sitelibdir_noarch/*.py
%_man8dir/*.8*

%changelog
* Wed Sep 23 2020 Vitaly Chikunov <vt@altlinux.org> 1.9-alt1
- Update to v1.9 (2020-09-18).

* Fri Mar 27 2020 Vitaly Chikunov <vt@altlinux.org> 1.8-alt1
- Update version to v1.8.

* Fri Mar 06 2020 Vitaly Chikunov <vt@altlinux.org> 1.7.0.11.gf240656-alt1
- Update to v1.7-11-gf240656.

* Wed Dec 04 2019 Vitaly Chikunov <vt@altlinux.org> 1.5-alt4
- Return of the --numa option (for rteval).

* Sun Sep 15 2019 Vitaly Chikunov <vt@altlinux.org> 1.5-alt3
- Make it compile on other arches.

* Sun Sep 08 2019 Vitaly Chikunov <vt@altlinux.org> 1.5-alt2
- Add hwlatdetect (required python3).

* Fri Sep 06 2019 Vitaly Chikunov <vt@altlinux.org> 1.5-alt1
- First build of rt-tests.
