# SPDX-License-Identifier: GPL-2.0-only
%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1

Name:     rteval
Version:  2.14.0.28
Release:  alt6

Summary:  Evaluate the performance of a realtime Linux kernel
License:  GPL-2.0-or-later
Group:    System/Kernel and hardware
Url:      https://wiki.linuxfoundation.org/realtime/documentation/howto/tools/rteval
# OldUrl: https://rt.wiki.kernel.org/index.php/Rteval
Vcs:      https://git.kernel.org/pub/scm/linux/kernel/git/clrkwllms/rteval.git
# Also:   https://git.kernel.org/pub/scm/linux/kernel/git/jkacur/rteval.git

Source:   %name-%version.tar
# armh: No linux-rt-tests due to no cyclictest due to no libnuma.
ExcludeArch: armh
BuildRequires: python-module-ethtool
BuildRequires: python-module-libxml2
BuildRequires: python-module-lxml
BuildRequires: python-modules-dmidecode
BuildRequires: python-module-setuptools

# hackbench and cyclictest
Requires: linux-rt-tests
# taskset
Requires: schedutils
# --loaddir=
Requires: kernel-source-4.9
# something to build the kernel
Requires: gcc gcc-c++ make binutils util-linux e2fsprogs bc perl flex
Requires: lzma-utils libelf-devel
#
Requires: python-modules-dmidecode
# sos contains python module for --sysreport
Requires: sos

%description
Rteval is a python program written to evaluate the performance of a
realtime Linux kernel on a particular hardware platform. The program
unpacks source code for two loads: hackbench and a Linux kernel
compile, then loops running hackbench and a parallel build of the
Linux kernel. While the loads are running, the cyclictest program is
run to measure realtime performance under load. When the specified run
duration is met, the loads are stopped and cyclictest outputs measured
timer latency values in histogram format, which is analyzed by
rteval. Rteval then writes an XML file to disk with information about
the system (gotten through DMI tables), the raw histogram data
collected during the run and the statistical analysis of the run.

%prep
%setup
sed -i 's/\bpython\b/python2/g' Makefile

%build
%python_build

%install
%python_install --install-lib=%python_sitelibdir
# relocate rteval as it's for root only
mv %buildroot%_bindir %buildroot%_sbindir
egrep -lr '^#!/usr/bin/python\b' %buildroot | xargs sed -i '1s,python,python2,'

%check
# vm-run --mem=4G --overlay=tmpfs:/usr/src/RPM/BUILD make runit

%files
%doc COPYING README doc/rteval.txt
%_sysconfdir/rteval.conf
%_sbindir/rteval
%python_sitelibdir/rteval*
%_datadir/rteval
%_man8dir/*

%changelog
* Sat Oct 17 2020 Vitaly Chikunov <vt@altlinux.org> 2.14.0.28-alt6
- Update to latest John Kacur patches.
- spec: Fix Beekeeper rebuild and minor spec changes.

* Thu Dec 05 2019 Vitaly Chikunov <vt@altlinux.org> 2.14.0.27.g5ed68ae-alt5
- Remove --numa mode leaving only --smp for cyclictest.

* Wed Dec 04 2019 Vitaly Chikunov <vt@altlinux.org> 2.14.0.27.g5ed68ae-alt4
- Minor changes (fix tabs in python code, log cyclictest cmd).

* Sat Nov 30 2019 Vitaly Chikunov <vt@altlinux.org> 2.14.0.27.g5ed68ae-alt3
- Change hashbang python to python2.

* Wed Sep 18 2019 Vitaly Chikunov <vt@altlinux.org> 2.14.0.27.g5ed68ae-alt2
- Add more Requires to streamline user experience.
- Relocate rteval to /usr/sbin

* Tue Sep 17 2019 Vitaly Chikunov <vt@altlinux.org> 2.14.0.27.g5ed68ae-alt1
- Initial build of v2.14-27-g5ed68ae.
