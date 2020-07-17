# Based on https://github.com/iovisor/bpftrace/blob/master/INSTALL.md

Name:		bpftrace
Version:	0.11.0
Release:	alt1
Summary:	High-level tracing language for Linux eBPF
Group:		Development/Debuggers
License:	Apache-2.0
URL:		https://github.com/iovisor/bpftrace
Vcs:		https://github.com/iovisor/bpftrace.git
Source:		%name-%version.tar
ExclusiveArch:	x86_64 aarch64

%define clang_version 9.0

BuildRequires(pre): rpm-macros-cmake
BuildRequires: cmake
BuildRequires: flex
BuildRequires: libstdc++-devel
BuildRequires: clang%clang_version-devel
BuildRequires:  llvm%clang_version-devel
BuildRequires:  llvm%clang_version-devel-static
BuildRequires: clang%clang_version-devel-static
BuildRequires:   lld%clang_version
BuildRequires: libbcc-devel
BuildRequires: libelf-devel
BuildRequires: binutils-devel
BuildRequires: /proc
# Assuming 'kernel' dependency will bring un-def kernel
%{?!_without_check:%{?!_disable_check:BuildRequires: rpm-build-vm kernel-headers-modules-un-def}}

%description
BPFtrace is a high-level tracing language for Linux enhanced Berkeley Packet
Filter (eBPF) available in recent Linux kernels (4.x). BPFtrace uses LLVM as a
backend to compile scripts to BPF-bytecode and makes use of BCC for interacting
with the Linux BPF system, as well as existing Linux tracing capabilities:
kernel dynamic tracing (kprobes), user-level dynamic tracing (uprobes), and
tracepoints. The BPFtrace language is inspired by awk and C, and predecessor
tracers such as DTrace and SystemTap.

See http://www.brendangregg.com/ebpf.html#bpftrace
    http://www.brendangregg.com/BPF/bpftrace-cheat-sheet.html

%prep
%setup

%build
%remove_optflags -frecord-gcc-switches
export CC=clang
export CXX=clang++
export LDFLAGS="-fuse-ld=lld $LDFLAGS"
export Clang_DIR=/usr/share/cmake/Modules/clang
# -DBUILD_TESTING:BOOL=ON will require googletest and try to clone it from github
%cmake \
	-DCMAKE_BUILD_TYPE=RelWithDebInfo \
	-DBUILD_TESTING:BOOL=OFF \
	-DBUILD_SHARED_LIBS:BOOL=OFF \
	-DLLVM_DIR=$(llvm-config --cmakedir) \
	-DOFFLINE_BUILDS:BOOL=ON \
	-DALLOW_UNSAFE_PROBE:BOOL=ON \

%cmake_build bpftrace

%install
%set_verify_elf_method relaxed
%cmake_install install/strip DESTDIR=%buildroot
find %buildroot%_datadir/%name/tools -name '*.bt' | xargs chmod a+x

%check
BUILD/src/bpftrace --version	 # not requires root
vm-run BUILD/src/bpftrace --info # should be fast enough even w/o kvm
[ -w /dev/kvm ] && vm-run BUILD/src/bpftrace -l '*_sleep_*'
if [ -w /dev/kvm ]; then
	# Great run-time tests

	# Some fail due to no BUILD_TESTING
	.gear/delete-blocks syscalls:	tests/runtime/*
	.gear/delete-blocks testprogs	tests/runtime/*
	.gear/delete-blocks uprobe	tests/runtime/*
	.gear/delete-blocks usdt	tests/runtime/usdt
	.gear/delete-blocks vfs_read	tests/runtime/*     # TIMEOUT
	.gear/delete-blocks hardware	tests/runtime/probe # TIMEOUT
	.gear/delete-blocks k.*_order	tests/runtime/probe # TIMEOUT
	.gear/delete-blocks watchpoint:	tests/runtime/watchpoint
	.gear/delete-blocks string_args	tests/runtime/other
	.gear/delete-blocks interval_order tests/runtime/probe
	.gear/delete-blocks tracepoint_order tests/runtime/probe
	.gear/delete-blocks uint64_t	tests/runtime/signed_ints
	.gear/delete-blocks tracepoint:random:random_read tests/runtime/variable
%ifarch x86_64
	sed -i s/python/python3/	tests/runtime/json-output
%else
	# TIMEOUT on aarch64
	.gear/delete-blocks python	tests/runtime/json-output
%endif
	export BPFTRACE_RUNTIME_TEST_EXECUTABLE=$PWD/BUILD/src/
	vm-run --sbin tests/runtime-tests.sh
fi

%files
%doc LICENSE README.md CONTRIBUTING-TOOLS.md
%doc docs/reference_guide.md docs/tutorial_one_liners.md
%_bindir/*
%_datadir/%name
%_man8dir/*

%changelog
* Fri Jul 17 2020 Vitaly Chikunov <vt@altlinux.org> 0.11.0-alt1
- Update to v0.11.0.

* Sat Jul 04 2020 Vitaly Chikunov <vt@altlinux.org> 0.10.0-alt2
- Fix build with libbcc-devel-0.15.0.

* Wed Apr 15 2020 Vitaly Chikunov <vt@altlinux.org> 0.10.0-alt1
- Update to v0.10.0 released at 2020-04-12. New features: kfuncs,
  C++ Symbol demangling, if-else control flow.

* Sat Mar 28 2020 Vitaly Chikunov <vt@altlinux.org> 0.9.4-alt2
- spec: Rework BuildRequires.

* Sat Mar 14 2020 Vitaly Chikunov <vt@altlinux.org> 0.9.4-alt1
- Update to v0.9.4.
- Update license tag from ASL 2.0 to Apache-2.0.
- Add %%check with some tests.

* Fri May 17 2019 Vitaly Chikunov <vt@altlinux.org> 0.9.0.0.169.ga4bf870-alt1
- First import v0.9-169-ga4bf870.
