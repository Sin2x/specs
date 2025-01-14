# SPDX-License-Identifier: GPL-2.0-only
%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1

%define kernel_base_version 6.0
%define kernel_source kernel-source-%kernel_base_version
%add_verify_elf_skiplist %_libexecdir/kselftests/*
%add_findreq_skiplist %_datadir/perf-core/tests/*.py

# from hv_kvp_daemon.c
%define kvp_config_loc /var/lib/hyperv
%define kvp_scripts_path /usr/libexec/hypervkvpd

Name: linux-tools
Version: %kernel_base_version
Release: alt1

Summary: Tools from Linux Kernel tree
License: GPL-2.0-only
Group: Development/Tools
URL: http://www.kernel.org/
Requires: perf

BuildRequires(pre): rpm-build-kernel
BuildRequires(pre): rpm-build-python3
BuildRequires: asciidoc
BuildRequires: banner
BuildRequires: binutils-devel
BuildRequires: elfutils-devel
BuildRequires: flex
BuildRequires: libaudit-devel
BuildRequires: libbpf-devel
BuildRequires: libcap-devel
BuildRequires: libcap-ng-devel
BuildRequires: libdebuginfod-devel
BuildRequires: libdw-devel
BuildRequires: libfuse-devel
BuildRequires: libhugetlbfs-devel
BuildRequires: liblzma-devel
BuildRequires: libmnl-devel
BuildRequires: libmount-devel
BuildRequires: libnl-devel
BuildRequires: libpfm-devel
BuildRequires: libpopt-devel
BuildRequires: libprocps-devel
%ifnarch %arm
BuildRequires: libnuma-devel
%endif
BuildRequires: libslang2-devel
BuildRequires: libssl-devel
BuildRequires: libtraceevent-devel
BuildRequires: libtracefs-devel >= 1.3.0
BuildRequires: libuuid-devel
BuildRequires: libzstd-devel
BuildRequires: perl-devel
BuildRequires: rsync
BuildRequires: xmlto

BuildRequires: %kernel_source
BuildRequires: python3-devel
BuildRequires: python3-module-setuptools
BuildRequires: readline-devel
# python3-module-docutils is just for rst2man.py
BuildRequires: python3-module-docutils
# python3 is just for scripts/bpf_helpers_doc.py
BuildRequires: python3

# Sources for hyperv-daemon
Source5: hv_get_dhcp_info.sh
Source6: hv_get_dns_info.sh
Source7: hv_set_ifconfig.sh
Source11: hypervkvpd.init
Source12: hypervvssd.init
Source13: hypervfcopyd.init
Source21: hypervkvpd.service
Source22: hypervvssd.service
Source23: hypervfcopyd.service
Source31: hypervkvpd.rules
Source32: hypervvssd.rules
Source33: hypervfcopyd.rules
Patch1: 0001-libperf-Remove-reference-to-non-uapi-header.patch

%description
Various tools from the Linux Kernel source tree.

%package -n perf
Summary: Performance analysis tools for Linux
Group: Development/Debuggers
Conflicts: linux-tools < 5.8
AutoReq: noperl,nopython
AutoProv: noperl,nopython

%description -n perf
Performance counters for Linux are a new kernel-based subsystem that provide
a framework for all things performance analysis. It covers hardware level
(CPU/PMU, Performance Monitoring Unit) features and software features
(software counters, tracepoints) as well.
This package contains performance analysis tools for Linux

%package -n libperf
Summary: The perf shared library
Group: System/Libraries

%description -n libperf
%summary.

%package -n libperf-devel
Summary: Development files for libperf
Group: Development/C
Requires: libperf = %EVR

%description -n libperf-devel
%summary.

%package -n libperf-devel-checkinstall
Summary: Checkinstall test for libperf
Group: Development/Other
Requires: libperf-devel = %EVR
Requires: rpm-build
BuildArch: noarch

%description -n libperf-devel-checkinstall
%summary.

%package -n python3-module-perf
Summary: Python bindings for apps which will manipulate perf events
Group: Development/Python
Provides: python3-perf

%description -n python3-module-perf
The python3-perf package contains a module that permits applications
written in the Python programming language to use the interface
to manipulate perf events.

# cpupower packages
%package -n cpupower
Summary: Linux kernel tool to examine and tune power saving related features of your processor
Group: System/Kernel and hardware
BuildRequires: libpci-devel
Requires: libcpupower = %version-%release
Provides: cpufrequtils = 009-%release
Obsoletes: cpufrequtils < 009-%release

%description -n cpupower
This package contains the tools/power directory from the kernel source
and the supporting document

%package -n libcpupower
Summary: Library for cpupower
License: GPLv2
Group: System/Libraries

Conflicts: cpupower < %version-%release

%description -n libcpupower
This packages contains some library needed by cpupower.

%package -n libcpupower-devel
Summary: Development files for cpupower
Group: Development/C
Requires: libcpupower = %version-%release
Provides: cpupower-devel = %version-%release
Obsoletes: cpupower-devel < %version-%release

%description -n libcpupower-devel
The lib%name-devel package contains libraries and header files for
developing applications that use %name.

# hyperv-daemon packages
%package -n hyperv-daemons
Summary: HyperV daemons suite
Group: Emulators
Requires: hypervkvpd = %version-%release
Requires: hypervvssd = %version-%release
Requires: hypervfcopyd = %version-%release

%description -n hyperv-daemons
Suite of daemons that are needed when Linux guest
is running on Windows Host with HyperV.

%package -n hypervkvpd
Summary: HyperV key value pair (KVP) daemon
Group: Emulators
Provides: hv_kvp_daemon

%description -n hypervkvpd
Hypervkvpd is an implementation of HyperV key value pair (KVP)
functionality for Linux. The daemon first registers with the
kernel driver. After this is done it collects information
requested by Windows Host about the Linux Guest. It also supports
IP injection functionality on the Guest.


%package -n hypervvssd
Summary: HyperV VSS daemon
Group: Emulators
Provides: hv_vss_daemon

%description -n hypervvssd
Hypervvssd is an implementation of HyperV VSS functionality
for Linux. The daemon is used for host initiated guest snapshot
on HyperV hypervisor. The daemon first registers with the
kernel driver. After this is done it waits for instructions
from Windows Host if to "freeze" or "thaw" the filesystem
on the Linux Guest.

%package -n hypervfcopyd
Summary: HyperV host to guest copy functionality daemon
Group: Emulators
Provides: hv_fcopy_daemon

%description -n hypervfcopyd
Hypervfcopyd is an mplementation of host to guest copy.
functionality for Linux.

%package -n bpftool
Summary: Inspection and simple manipulation of eBPF programs and maps
Group: Development/Tools

%description -n bpftool
This package contains the bpftool, which allows inspection and simple
manipulation of eBPF programs and maps.

%package -n kselftests
Summary: Linux Kernel Selftests
Group: Development/Tools
AutoReq: noperl,nopython,noshebang,nolib,noshell
AutoProv: no

%description -n kselftests
The kernel contains a set of "self tests" under the tools/testing/selftests/
directory. These are intended to be small tests to exercise individual code
paths in the kernel. Tests are intended to be run after building, installing
and booting a kernel.

(This is experimental and internal use only testing package!)

%package -n rtla
Summary: An interface for osnoise/timerlat tracers
Group: Development/Tools
AutoReq: noperl,nopython,noshebang,nolib,noshell
AutoProv: no

%description -n rtla
The rtla(1) is a meta-tool that includes a set of commands that
aims to analyze the real-time properties of Linux. But instead of
testing Linux as a black box, rtla leverages kernel tracing
capabilities to provide precise information about the properties
and root causes of unexpected results.

%prep
%setup -cT
tar -xf %kernel_src/%kernel_source.tar
cd %kernel_source
%autopatch -p1

# This will make perf ask for kernelversion.
touch .git

cd tools

# Avoid conflict with trace-cmd which installs same plug-ins in
# %%_libdir/traceevent/plugins
sed -i 's|\(plugindir[[:blank:]]*=[[:blank:]]*\).*$|\1%_libexecdir/traceevent/plugins|' perf/Makefile.config

# Improve 'Install the audit-libs-python package' help text.
sed -i '/apt-get/ {
		s/python-audit/python3-module-audit/
		s/.(Ubuntu)//
	}
	/yum.install/d
	s/audit-libs-python/python3-module-audit/' perf/scripts/python/Perf-Trace-Util/lib/Perf/Trace/Util.py

# Transient powerpc `make bpf` fix
sed -i '/#include/a typedef struct { __u32 u[4]; } __vector128;' include/uapi/linux/types.h

# Fix `trace/beauty/generated/fsconfig_arrays.c:2:3: error: expected expression before ']' token'.
sed -i 's/*+/*/' perf/trace/beauty/fsconfig.sh

sed -i 's/-s\b/-g/' testing/selftests/size/Makefile
sed -i 's/-std=gnu99/& -g/' testing/selftests/vDSO/Makefile
sed -Ei '\!^CFLAGS!s!(-Wl,-rpath=)\./!\1/usr/lib/kselftests/rseq!' testing/selftests/rseq/Makefile
sed -i 's/-s\b/-g/' testing/selftests/arm64/abi/Makefile testing/selftests/arm64/fp/Makefile
sed -i '/ln -s/s/-s $(DESTDIR)/-s /' tracing/rtla/Makefile

%build
%define optflags_lto %nil
banner build
cd %kernel_source/tools

# Use rst2man from python3-module-docutils
# Sisyphus have rst2man, p10 have rst2man.py, p9 have rst2man.py3.
type rst2man &>/dev/null || {
	rst2man() {
		type rst2man.py3 &>/dev/null 2>&1 && rst2man.py3 "$@" || rst2man.py "$@"
	}; export -f rst2man
}
# Noiseless git stub
git() { exit 1; }; export -f git

export EXTRA_CFLAGS="%optflags" V=1
%define perf_opts \\\
	PERF_VERSION=%version-%release \\\
	JOBS=%__nprocs \\\
	WERROR=0 \\\
	NO_GTK2=1 \\\
	NO_LIBUNWIND=1 \\\
	PYTHON=python3 \\\
	PYTHON_CONFIG=python3-config \\\
	LIBPFM4=1 \\\
	LIBTRACEEVENT_DYNAMIC=1 \\\
	LIBBPF_DYNAMIC=1 \\\
	%nil

%define install_opts \\\
	DESTDIR=%buildroot \\\
	prefix=%_prefix \\\
	%nil

### Build perf
make -C lib/perf \
     %perf_opts
make -C perf \
     %perf_opts \
     VF=1 \
     all \
     man \
     python

### build bpf tools
# runqslower does not build with: `Couldn't find kernel BTF; set VMLINUX_BTF to specify its location.`
sed -i /^all:/s/runqslower// bpf/Makefile
sed -i /^install:/s/runqslower_install// bpf/Makefile
%make_build bpf
%make_build -C bpf/bpftool doc

# Build cpupower
%make_build cpupower CPUFREQ_BENCH=false

%ifarch %ix86
  %make_build -C power/cpupower/debug/i386 centrino-decode powernow-k8-decode
%endif

%ifarch x86_64
  %make_build -C power/cpupower/debug/x86_64 centrino-decode powernow-k8-decode
  %make_build intel-speed-select
%endif

%ifarch %ix86 x86_64
  %make_build x86_energy_perf_policy
  %make_build turbostat
%endif

### Build hyperv daemons
%ifarch %ix86 x86_64
  make hv
%endif

# acpi cannot make in parrallel.
make acpi

%make_build ASFLAGS=-g VERSION=%version \
	bootconfig \
	cgroup \
	firmware \
	freefall \
	gpio \
	iio \
	leds \
	selftests \
	tmon \
	tracing \
	vm \

%install
banner install
cd %kernel_source/tools

export EXTRA_CFLAGS="%optflags" V=1

### Install perf
# Note: perf's Makefile cannot set `mandir=%%_mandir` properly.
make -C perf \
     %perf_opts \
     %install_opts \
     install \
     install-man \
     install-python_ext

make -C lib/perf \
     %perf_opts \
     %install_opts \
     install \
     install_headers

rm -rf %buildroot%_libexecdir/perf

# These already in libtraceevent package.
rm -rf %buildroot%_libexecdir/traceevent

install -d -m 0755 %buildroot%_docdir/perf
install -m 0644 ../COPYING %buildroot%_docdir/perf/
install -m 0644 perf/{CREDITS,design.txt,Documentation/examples.txt,Documentation/tips.txt} %buildroot%_docdir/perf/

rm %buildroot/%_docdir/perf-tip/tips.txt
rmdir %buildroot/%_docdir/perf-tip

find %buildroot%_sysconfdir/bash_completion.d \
	%buildroot%_datadir/perf-core \
	%buildroot%_libexecdir/perf* \
	%buildroot%_docdir \
	-name bin -prune -o -type f \
	| xargs chmod a-x

### Install bpf tools
make %install_opts \
	bpf_install
# Previous does not install docs, thus
make -C bpf/bpftool \
	%install_opts \
	mandir=%_mandir \
	doc-install

# Provided by man-pages
rm -f %buildroot/%_man7dir/bpf-helpers.*

### Install cpupower
%make %install_opts libdir=%_libdir mandir=%_mandir CPUFREQ_BENCH=false cpupower_install
rm -f %buildroot%_libdir/*.{a,la}
%find_lang cpupower
mv cpupower.lang ../../

%ifarch %ix86
  pushd power/cpupower/debug/i386
  install -m755 centrino-decode %buildroot%_bindir/centrino-decode
  install -m755 powernow-k8-decode %buildroot%_bindir/powernow-k8-decode
  popd
%endif

%ifarch x86_64
  pushd power/cpupower/debug/x86_64
  install -m755 centrino-decode %buildroot%_bindir/centrino-decode
  install -m755 powernow-k8-decode %buildroot%_bindir/powernow-k8-decode
  popd
  make %install_opts intel-speed-select_install
%endif

%ifarch %ix86 x86_64
  make %install_opts x86_energy_perf_policy_install
  make %install_opts turbostat_install
%endif

### Install hyperv daemons
%ifarch %ix86 x86_64
mkdir -p %buildroot%_sbindir
install -p -m 0755 hv/hv_kvp_daemon %buildroot%_sbindir/hypervkvpd
install -p -m 0755 hv/hv_vss_daemon %buildroot%_sbindir/hypervvssd
install -p -m 0755 hv/hv_fcopy_daemon %buildroot%_sbindir/hypervfcopyd

mkdir -p %buildroot%kvp_scripts_path
mkdir -p %buildroot%kvp_config_loc
# Shell scripts for the KVP daemon
install -p -m 0755 %SOURCE5 %buildroot%kvp_scripts_path/hv_get_dhcp_info
install -p -m 0755 %SOURCE6 %buildroot%kvp_scripts_path/hv_get_dns_info
install -p -m 0755 %SOURCE7 %buildroot%kvp_scripts_path/hv_set_ifconfig

# SysV init scripts
mkdir -p %buildroot%_initdir
install -p -m 0755 %SOURCE11 %buildroot%_initdir/hypervkvpd
install -p -m 0755 %SOURCE12 %buildroot%_initdir/hypervvssd
install -p -m 0755 %SOURCE13 %buildroot%_initdir/hypervfcopyd

# Systemd unit file
mkdir -p %buildroot%_unitdir
install -p -m 0644 %SOURCE21 %buildroot%_unitdir/hypervkvpd.service
install -p -m 0644 %SOURCE22 %buildroot%_unitdir/hypervvssd.service
install -p -m 0644 %SOURCE23 %buildroot%_unitdir/hypervfcopyd.service

# udev rules
mkdir -p %buildroot%_udevrulesdir
install -p -m 0644 %SOURCE31 %buildroot%_udevrulesdir/hypervkvpd.rules
install -p -m 0644 %SOURCE32 %buildroot%_udevrulesdir/hypervvssd.rules
install -p -m 0644 %SOURCE33 %buildroot%_udevrulesdir/hypervfcopyd.rules

# Directory for pool files
mkdir -p %buildroot%_sharedstatedir/hyperv
%endif

make %install_opts mandir=%_mandir acpi_install
# Rename them to not conflict with acpica and pmtools
mv %buildroot%_sbindir/acpidbg    %buildroot%_sbindir/acpidbg-linux
mv %buildroot%_sbindir/acpidump   %buildroot%_sbindir/acpidump-linux
mv %buildroot%_sbindir/ec         %buildroot%_sbindir/ec-linux
mv %buildroot%_man8dir/acpidump.8 %buildroot%_man8dir/acpidump-linux.8

make %install_opts bootconfig_install
make %install_opts freefall_install
make %install_opts gpio_install
make %install_opts iio_install
make %install_opts vm_install
make %install_opts tracing_install STRIP=true
install -p -m755 cgroup/cgroup_event_listener	%buildroot%_bindir
install -p -m755 firmware/ihex2fw		%buildroot%_bindir
install -p -m755 kvm/kvm_stat/kvm_stat		%buildroot%_bindir
install -p -m755 leds/get_led_device_info.sh	%buildroot%_bindir
install -p -m755 leds/led_hw_brightness_mon	%buildroot%_bindir
install -p -m755 leds/uledmon			%buildroot%_bindir
install -p -m755 thermal/tmon/tmon		%buildroot%_bindir
install -p -m755 thermal/tmon/tmon.8		%buildroot%_man8dir

pushd testing/selftests
mkdir -p %buildroot%_libexecdir/kselftests
./kselftest_install.sh %buildroot%_libexecdir/kselftests
popd

%add_debuginfo_skiplist %_prefix/libexec/perf-core/dlfilters/dlfilter-test-api-v0.so

%check
banner check
cd %kernel_source/tools

# Simplistic tests
ldd %buildroot%_bindir/perf | sort -V
%buildroot%_bindir/perf --version | grep -Fw %version
%buildroot%_bindir/perf version --build-options
# To run more comprehensive test run: perf test

make -C bootconfig test

%pre -n libperf-devel-checkinstall
set -euxo pipefail
cd /tmp
cc %_docdir/libperf/examples/counting.c `pkg-config --libs libperf`
cc %_docdir/libperf/examples/sampling.c `pkg-config --libs libperf`
# Cannot run due to kernel.perf_event_paranoid=4

%post -n hypervkvpd
# auto enable service for Hyper-V guest
if [ $1 -eq 1 ]; then
    board_vendor=
    product_name=
    [ -r /sys/class/dmi/id/board_vendor ] && board_vendor="`cat /sys/class/dmi/id/board_vendor`"
    [ -r /sys/class/dmi/id/product_name ] && board_vendor="`cat /sys/class/dmi/id/product_name`"

    if test "${board_vendor}" = "Microsoft Corporation" -a "${product_name}" = "Virtual Machine"; then
	echo "Enabling hypervkvpd on '${product_name}' from '${board_vendor}'"
	chkconfig hypervkvpd on
    fi
fi
%post_service hypervkvpd

%preun -n hypervkvpd
%preun_service hypervkvpd

%post -n hypervvssd
if [ $1 -eq 1 ]; then
    board_vendor=
    product_name=
    [ -r /sys/class/dmi/id/board_vendor ] && board_vendor="`cat /sys/class/dmi/id/board_vendor`"
    [ -r /sys/class/dmi/id/product_name ] && board_vendor="`cat /sys/class/dmi/id/product_name`"

    if test "${board_vendor}" = "Microsoft Corporation" -a "${product_name}" = "Virtual Machine"; then
	echo "Enabling hypervvssd on '${product_name}' from '${board_vendor}'"
	chkconfig hypervvssd on
    fi
fi
%post_service hypervvssd

%preun -n hypervvssd
%preun_service hypervvssd

%post -n hypervfcopyd
%post_service hypervfcopyd

%preun -n hypervfcopyd
%preun_service hypervfcopyd

%files
%doc kernel-source-%version/COPYING
%_sbindir/acpidbg-linux
%_sbindir/acpidump-linux
%_sbindir/ec-linux
%_man8dir/acpidump-linux.*
%_bindir/cgroup_event_listener
%_bindir/ihex2fw
%_sbindir/freefall
%_bindir/lsgpio
%_bindir/gpio-hammer
%_bindir/gpio-event-mon
%_bindir/gpio-watch
%_bindir/iio_event_monitor
%_bindir/lsiio
%_bindir/iio_generic_buffer
%_bindir/kvm_stat
%_bindir/get_led_device_info.sh
%_bindir/led_hw_brightness_mon
%_bindir/uledmon
%_bindir/tmon
%_man8dir/tmon.*
%_sbindir/page-types
%_sbindir/slabinfo
%_sbindir/page_owner_sort
%_bindir/bootconfig
%_sbindir/pfrut
%_man8dir/pfrut.*

%files -n perf
%_bindir/perf
%_bindir/trace
%_man1dir/perf*
%_sysconfdir/bash_completion.d/perf
%_prefix/libexec/perf-core
%_datadir/perf-core
%doc %_docdir/perf

%files -n libperf
%doc kernel-source-%version/COPYING
%_libdir/libperf.so.*

%files -n libperf-devel
%doc kernel-source-%version/COPYING
%_includedir/perf
%_libdir/libperf.so
%_pkgconfigdir/libperf.pc
%_docdir/libperf
%_man3dir/libperf.*
%_man7dir/libperf*.*

%files -n libperf-devel-checkinstall

%files -n python3-module-perf
%python3_sitelibdir/perf*

# files cpupower
%files -n cpupower -f cpupower.lang
%_bindir/cpupower
%ifarch x86_64
%_bindir/intel-speed-select
%endif
%_man1dir/cpupower*
%_datadir/bash-completion/completions/cpupower
%ifarch %ix86 x86_64
%_man8dir/turbostat*
%_man8dir/x86_energy_perf_policy*
%_bindir/centrino-decode
%_bindir/powernow-k8-decode
%_bindir/x86_energy_perf_policy
%_bindir/turbostat
%endif

%files -n libcpupower
%_libdir/libcpupower.so.*

%files -n libcpupower-devel
%_libdir/libcpupower.so
%_includedir/cpu*.h

# files hyperv daemons
%ifarch %ix86 x86_64
%files -n hyperv-daemons
# the base package does not contain any files.

%files -n hypervkvpd
%_sbindir/hypervkvpd
%dir %kvp_config_loc
%dir %kvp_scripts_path
%kvp_scripts_path/*
%_initdir/hypervkvpd
%_unitdir/hypervkvpd.service
%_udevrulesdir/hypervkvpd.rules

%files -n hypervvssd
%_sbindir/hypervvssd
%_initdir/hypervvssd
%_unitdir/hypervvssd.service
%_udevrulesdir/hypervvssd.rules

%files -n hypervfcopyd
%_sbindir/hypervfcopyd
%_initdir/hypervfcopyd
%_unitdir/hypervfcopyd.service
%_udevrulesdir/hypervfcopyd.rules
%endif

%files -n bpftool
%_bindir/bpf_asm
%_bindir/bpf_dbg
%_bindir/bpf_jit_disasm
%_sbindir/bpftool
%_datadir/bash-completion/completions/bpftool
%_man8dir/bpftool*

%files -n kselftests
%_libexecdir/kselftests

%files -n rtla
%_bindir/osnoise
%_bindir/rtla
%_bindir/timerlat
%_sbindir/latency-collector
%_man1dir/rtla*

%changelog
* Sat Oct 08 2022 Vitaly Chikunov <vt@altlinux.org> 6.0-alt1
- Update to v6.0 (2022-10-02).

* Mon Aug 15 2022 Vitaly Chikunov <vt@altlinux.org> 5.19-alt2
- perf: Fix `version` output, enable debuginfod support, build with dynamic
  linking to libbpf and libtraceevent. Package libperf and libperf-devel.

* Mon Aug 01 2022 Vitaly Chikunov <vt@altlinux.org> 5.19-alt1
- Update to v5.19 (2022-07-31).
- Do not package objtool and fixdep (use kernel-headers-modules).

* Mon May 23 2022 Vitaly Chikunov <vt@altlinux.org> 5.18-alt1
- Update to v5.18 (2022-05-22).

* Sat Apr 16 2022 Vitaly Chikunov <vt@altlinux.org> 5.17-alt2
- spec: Fix rebuild with new rst2man.

* Wed Mar 23 2022 Vitaly Chikunov <vt@altlinux.org> 5.17-alt1
- Updated to v5.17 (2022-03-20).
- Package RTLA tools.

* Mon Jan 10 2022 Vitaly Chikunov <vt@altlinux.org> 5.16-alt1
- Updated to v5.16 (2022-01-09).
- Enable PMU event selection using libpfm4 syntax (--pfm-events).

* Tue Nov 02 2021 Vitaly Chikunov <vt@altlinux.org> 5.15-alt1
- Update to v5.15 (2021-10-31).

* Sun Sep 19 2021 Vitaly Chikunov <vt@altlinux.org> 5.14-alt2
- Package bootconfig tool (closes: #40956).

* Tue Aug 31 2021 Vitaly Chikunov <vt@altlinux.org> 5.14-alt1
- Update to v5.14 (2021-08-29).

* Wed Jun 30 2021 Vitaly Chikunov <vt@altlinux.org> 5.13-alt1
- Update to v5.13 (2021-06-27).

* Fri Apr 30 2021 Vitaly Chikunov <vt@altlinux.org> 5.12-alt2
- Build kselftests.

* Tue Apr 27 2021 Vitaly Chikunov <vt@altlinux.org> 5.12-alt1
- Update to v5.12 (2021-04-25).

* Wed Feb 17 2021 Vitaly Chikunov <vt@altlinux.org> 5.11-alt1
- Update to v5.11 (2021-02-14).

* Mon Dec 21 2020 Vitaly Chikunov <vt@altlinux.org> 5.10-alt1
- Update to v5.10 (2020-12-13).

* Thu Nov 12 2020 Vitaly Chikunov <vt@altlinux.org> 5.9-alt3
- spec: Fix make acpi race appeared on armh.

* Wed Nov 11 2020 Vitaly Chikunov <vt@altlinux.org> 5.9-alt2
- spec: Fix 'rst2man.py: command not found' in p9.

* Mon Oct 12 2020 Vitaly Chikunov <vt@altlinux.org> 5.9-alt1
- Update to v5.9 (2020-10-11).

* Thu Aug 06 2020 Vitaly Chikunov <vt@altlinux.org> 5.8-alt1
- Update to v5.8.
- spec: Switch to python3.
- spec: Move perf into separate package.
- spec: Build more tools (into linux-tools).
- spec: Remove kernel version suffix from perf name.
- spec: Pack /usr/libexec/perf-core.
- spec: Enable libzstd.
- spec: Add simple %%check section.

* Fri Oct 25 2019 Alexey Shabalin <shaba@altlinux.org> 5.3-alt3
- fixed typo alternatives for perf

* Thu Oct 24 2019 Alexey Shabalin <shaba@altlinux.org> 5.3-alt2
- move bash completions for bpftool to /usr/share
- package bash completions for cpupower

* Wed Oct 23 2019 Alexey Shabalin <shaba@altlinux.org> 5.3-alt1
- Update for 5.3
- fixed sysvinit scripts

* Tue May 21 2019 Vitaly Chikunov <vt@altlinux.org> 5.1-alt1
- Add /usr/lib/perf to perf
- Clean up .spec (fix warnings, remove duplicated files)
- Build and provide bpftool
- Use kernel-source-5.1
- Simplify linux-tools-alt.patch
- Switch from libunwind to libdw

* Thu Jan 24 2019 Igor Vlasenko <viy@altlinux.ru> 4.19-alt1.1
- rebuild with new perl 5.28.1

* Wed Nov 21 2018 Alexey Shabalin <shaba@altlinux.org> 4.19-alt1
- Update for kernel-4.19

* Mon Feb 19 2018 Sergey Bolshakov <sbolshakov@altlinux.ru> 4.15-alt2
- fixed spec for non-x86 arches

* Wed Feb 07 2018 Alexey Shabalin <shaba@altlinux.ru> 4.15-alt1
- Update for kernel-4.15
- absorb cpupower package
- absorb hyperv-daemons package

* Fri Dec 15 2017 Igor Vlasenko <viy@altlinux.ru> 4.12-alt2.1
- rebuild with new perl 5.26.1

* Wed Aug  2 2017 Terechkov Evgenii <evg@altlinux.org> 4.12-alt2
- Build exclusively for x86_64 for now, waiting for upstream fix...

* Thu Jul 13 2017 Terechkov Evgenii <evg@altlinux.org> 4.12-alt1
- Update for kernel-4.12

* Wed Mar 29 2017 Terechkov Evgenii <evg@altlinux.org> 4.10-alt1
- Update for kernel-4.10
- Fix minor repocop warning about python-dev

* Wed Feb  8 2017 Terechkov Evgenii <evg@altlinux.org> 4.9-alt4
- Add python-module-perf subpackage

* Wed Feb  8 2017 Terechkov Evgenii <evg@altlinux.org> 4.9-alt3
- Add patch2 to linking python

* Wed Feb  8 2017 Terechkov Evgenii <evg@altlinux.org> 4.9-alt2
- Build with python support

* Mon Feb 06 2017 Igor Vlasenko <viy@altlinux.ru> 4.9-alt1.1
- rebuild with new perl 5.24.1

* Fri Feb  3 2017 Terechkov Evgenii <evg@altlinux.org> 4.9-alt1
- Update for kernel-4.9

* Wed Oct 19 2016 Terechkov Evgenii <evg@altlinux.org> 4.7-alt1
- Clone package from linux-tools-4.4
- TODO: build with python support

* Thu Jan 28 2016 Terechkov Evgenii <evg@altlinux.org> 4.4-alt1
- Clone package from linux-tools-4.3

* Wed Nov 25 2015 Igor Vlasenko <viy@altlinux.ru> 4.3-alt1.1
- rebuild with new perl 5.22.0

* Wed Nov  4 2015 Terechkov Evgenii <evg@altlinux.org> 4.3-alt1
- Clone package from linux-tools-4.2

* Sat Oct 10 2015 Terechkov Evgenii <evg@altlinux.org> 4.2-alt1
- Clone package from linux-tools-4.1

* Fri Oct  2 2015 Terechkov Evgenii <evg@altlinux.org> 4.1-alt1
- Clone package from linux-tools-4.0

* Mon Jul 13 2015 Terechkov Evgenii <evg@altlinux.org> 4.0-alt2
- Return bin/trace (hardlink to bin/perf) for convience
- Additional alternatives (man1dir/bash_completion/trace)

* Sun Jul 12 2015 Terechkov Evgenii <evg@altlinux.org> 4.0-alt1
- Clone package from linux-tools-3.14
- Rediffed patches

* Sun Jul 12 2015 Terechkov Evgenii <evg@altlinux.org> 3.14-alt4
- Add tools-perf-install.patch from Debian

* Sun Jul 12 2015 Terechkov Evgenii <evg@altlinux.org> 3.14-alt3
- Add basic alternatives support
- Make different kernel versions non-conflicting

* Sun Jul 12 2015 Terechkov Evgenii <evg@altlinux.org> 3.14-alt2
- Add tool-perf-version.patch from Debian

* Sat Jul 11 2015 Terechkov Evgenii <evg@altlinux.org> 3.14-alt1
- Initial build for ALT Linux
