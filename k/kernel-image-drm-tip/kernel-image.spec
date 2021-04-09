# SPDX-License-Identifier: GPL-2.0-only
# spec is based on kernel-image-un-def
%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1

Name: kernel-image-drm-tip
%define kernel_source_version	5.11
%define kernel_base_version	5.12
%define kernel_sublevel .0
%define kernel_extra_version	+rc6.20210409
Version: %kernel_base_version%kernel_sublevel%kernel_extra_version
Release: alt1

%define krelease	%release
%define flavour		%( s='%name'; printf %%s "${s#kernel-image-}" )
%define base_flavour	%( s='%flavour'; printf %%s "${s%%%%-*}" )
%define sub_flavour	%( s='%flavour'; printf %%s "${s#*-}" )

%define kgcc_version	%__gcc_version_base

%define kversion	%kernel_base_version%kernel_sublevel%kernel_extra_version
%define modules_dir	/lib/modules/%kversion-%flavour-%krelease

%define kheaders_dir	%_prefix/include/linux-%kversion-%flavour
%define kbuild_dir	%_prefix/src/linux-%kversion-%flavour-%krelease

%brp_strip_none /boot/*
%add_verify_elf_skiplist %modules_dir/*

Summary: The drm-tip Linux kernel (bleeding edge of kernel graphics)
License: GPL-2.0-only
Group: System/Kernel and hardware
Url: https://drm.pages.freedesktop.org/maintainer-tools/drm-tip.html
Vcs: http://cgit.freedesktop.org/drm-tip
Packager: Kernel Maintainers Team <kernel@packages.altlinux.org>

Patch0: %name-%version-%release.patch

ExclusiveOS: Linux
ExclusiveArch: x86_64
%define arch_dir x86

BuildRequires(pre): rpm-build-kernel
BuildRequires: dev86
BuildRequires: flex
BuildRequires: libdb4-devel
BuildRequires: gcc%kgcc_version gcc%kgcc_version-c++
BuildRequires: gcc%kgcc_version-plugin-devel libgmp-devel libmpc-devel
BuildRequires: kernel-source-%kernel_source_version = 1.0.0
BuildRequires: kmod
BuildRequires: lzma-utils zlib-devel
BuildRequires: libelf-devel
BuildRequires: bc
BuildRequires: rsync
BuildRequires: openssl-devel openssl
BuildRequires: dwarves >= 1.16
BuildRequires: banner
# To import .config
BuildRequires: kernel-headers-modules-un-def
# For check
%{?!_without_check:%{?!_disable_check:BuildRequires: rpm-build-vm-run}}

Requires: coreutils
Requires: bootloader-utils
Requires: kmod

%description
  ******   ******   *     *           *******  ***  ******
  *     *  *     *  **   **              *      *   *     *
  *     *  *     *  * * * *              *      *   *     *
  *     *  ******   *  *  *  *******     *      *   ******
  *     *  *   *    *     *              *      *   *
  *     *  *    *   *     *              *      *   *
  ******   *     *  *     *              *     ***  *

drm-tip is the combined bleeding edge of kernel graphics.

THIS IS HIGHLY EXPERIMENTAL AND SHOULD BE USED FOR TESTING ONLY!

How to file i915 bugs:
  https://gitlab.freedesktop.org/drm/intel/-/wikis/How-to-file-i915-bugs

%package -n kernel-headers-%flavour
Summary: Header files for the %flavour Linux kernel
Group: Development/Kernel
Requires: kernel-headers-common
AutoReqProv: nocpp

%description -n kernel-headers-%flavour
This package makes Linux kernel headers corresponding to the Linux
kernel package %name-%version-%release.

%package -n kernel-headers-modules-%flavour
Summary: Headers and files needed for building modules for %flavour kernel
Group: Development/Kernel
Requires: gcc%kgcc_version
Requires: libelf-devel
AutoReqProv: nocpp

%description -n kernel-headers-modules-%flavour
This package contains header files, Makefiles and other parts of the
Linux kernel build system which are needed to build kernel modules for
the Linux kernel package %name-%version-%release.

%prep
%setup -cT -n kernel-image-%flavour-%kversion-%krelease
rm -rf kernel-source-%kernel_source_version
tar -xf %kernel_src/kernel-source-%kernel_source_version.tar
%setup -D -T -n kernel-image-%flavour-%kversion-%krelease/kernel-source-%kernel_source_version
%patch0 -p1

subst 's/EXTRAVERSION[[:space:]]*=.*/EXTRAVERSION = %kernel_extra_version-%flavour-%krelease/g' Makefile

%build
KernelVer=%kversion-%flavour-%krelease

echo "Building Kernel $KernelVer"

cp /usr/src/linux-*-un-def-*/.config .config
%make_build olddefconfig
%make_build bzImage
%make_build modules

echo "Kernel built $KernelVer"

%install
KernelVer=%kversion-%flavour-%krelease

install -Dp -m644 System.map %buildroot/boot/System.map-$KernelVer
install -Dp -m644 arch/x86/boot/bzImage %buildroot/boot/vmlinuz-$KernelVer
install -Dp -m644 .config %buildroot/boot/config-$KernelVer

%make_build modules_install INSTALL_MOD_PATH=%buildroot

mkdir -p %buildroot%kbuild_dir
cp -a include %buildroot%kbuild_dir
cp -a --parents arch/x86/include %buildroot%kbuild_dir
cp -a --parents {Module.symvers,.config,System.map,Makefile,arch/x86/Makefile} \
	%buildroot%kbuild_dir

# Install files required for building external modules (in addition to headers)
KbuildFiles="
	scripts/mod/modpost
	scripts/mkmakefile
	scripts/link-vmlinux.sh
	scripts/mod/mk_elfconfig
	scripts/kconfig/conf
	scripts/mkcompile_h
	scripts/makelst
	scripts/Makefile.*
	scripts/Makefile
	scripts/Kbuild.include
	scripts/kallsyms
	scripts/genksyms/genksyms
	scripts/basic/fixdep
	scripts/extract-ikconfig
	scripts/conmakehash
	scripts/checkversion.pl
	scripts/checkincludes.pl
	scripts/bin2c
	scripts/gcc-version.sh
	scripts/gcc-goto.sh
	scripts/module.lds
	scripts/recordmcount.pl
	scripts/recordmcount.h
	scripts/recordmcount.c
	scripts/recordmcount
	scripts/gcc-x86_*-has-stack-protector.sh
	scripts/subarch.include
	scripts/depmod.sh
	scripts/ld-version.sh
	tools/objtool/objtool
"
for f in $KbuildFiles; do
	[ -e "$f" ] || continue
	[ -x "$f" ] && mode=755 || mode=644
	install -Dp -m$mode "$f" %buildroot%kbuild_dir/"$f"
done

# Fix symlinks to kernel sources in /lib/modules
rm -f %buildroot%modules_dir/{build,source}
ln -s %kbuild_dir %buildroot%modules_dir/build

# Provide kernel headers for userspace
%make_build headers_install INSTALL_HDR_PATH=%buildroot%kheaders_dir

mkdir %buildroot%modules_dir/{extra,updates}

%check
vm-run 'banner `uname -r`'

%files
%doc README integration-manifest LICENSES/preferred/GPL-2.0 LICENSES/exceptions/Linux-syscall-note
/boot/vmlinuz-%kversion-%flavour-%krelease
/boot/System.map-%kversion-%flavour-%krelease
/boot/config-%kversion-%flavour-%krelease
%dir %modules_dir
%dir %modules_dir/extra
%dir %modules_dir/updates
%modules_dir/kernel
%modules_dir/modules.*

%files -n kernel-headers-%flavour
%kheaders_dir

%files -n kernel-headers-modules-%flavour
%kbuild_dir
%dir %modules_dir
%modules_dir/build

%changelog
* Fri Apr 09 2021 Kernel Pony <kernelpony@altlinux.org> 5.12.0+rc6.20210409-alt1
- drm-tip v5.12-rc6-1293-gcaf1e8d36f0b (2021y-04m-09d-06h-44m-06s).
