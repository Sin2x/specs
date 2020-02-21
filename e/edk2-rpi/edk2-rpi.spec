%define TOOL_CHAIN_TAG GCC49
%define openssl_ver 1.1.1d

# More subpackages to come once licensing issues are fixed
Name: edk2-rpi
Version: 20191122
Release: alt2
Summary: UEFI Firmware for Raspberry PI 3 and 4

#Vcs-Git: https://github.com/tianocore/edk2.git
Source: %name-%version.tar

Source2: openssl.tar
Source3: berkeley-softfloat-3.tar
Source4: Logo.bmp
Source5: edk2-platforms.tar
Source6: edk2-non-osi.tar

# https://github.com/raspberrypi/firmware/tree/master/boot
Source7: bcm2710-rpi-3-b.dtb
Source8: bcm2710-rpi-3-b-plus.dtb
Source9: bcm2711-rpi-4-b.dtb

Patch1: %name-%version.patch

# Upstream patchs for Raspberry Pi 4
Patch2: 0020-EmbeddedPkg-NonCoherentDmaLib-implement-support-for-.patch
Patch3: 0021-EmbeddedPkg-implement-EDK2-IoMmu-protocol-wrapping-D.patch

License: BSD-2-Clause and OpenSSL
Group: Emulators
Url: http://www.tianocore.org
ExclusiveArch: aarch64
BuildArch: noarch

Provides: edk2-ovmf-aarch64 = %EVR

BuildRequires: iasl nasm gcc-c++
BuildRequires: python3-devel python3-modules-sqlite3
BuildRequires: libuuid-devel
BuildRequires: bc
BuildRequires: raspberrypi-firmware
# build MarkDown
BuildRequires: pandoc

%description
EFI Development Kit II
UEFI Firmware for Raspberry PI 3 and 4

%prep
%setup -q
%patch1 -p1
%patch2 -p1
%patch3 -p1

# cleanup
find . -name '*.efi' -print0 | xargs -0 rm -f
rm -rf BaseTools/Bin \
	UefiCpuPkg/ResetVector/Vtf0/Bin/*.raw \
	EdkCompatibilityPkg/Other \
	AppPkg \
	DuetPkg/BootSector/bin \
	StdLib/LibC/Main/Ia32/ftol2.obj \
	BeagleBoardPkg/Debugger_scripts/rvi_dummy.axf \
	BaseTools/Source/Python/*/*.pyd \
	BaseTools/Source/Python/UPT/Dll/sqlite3.dll \
	Vlv2TbltDevicePkg/GenBiosId \
	Vlv2TbltDevicePkg/*.exe \
	ArmPkg/Library/GccLto/liblto-*.a

# Ensure old shell and binary packages are not used
rm -rf EdkShellBinPkg
rm -rf EdkShellPkg
rm -rf FatBinPkg
rm -rf ShellBinPkg

# add openssl
mkdir -p CryptoPkg/Library/OpensslLib/openssl
tar -xf %SOURCE2 --strip-components 1 --directory CryptoPkg/Library/OpensslLib/openssl

# add /berkeley-softfloat-3
mkdir -p ArmPkg/Library/ArmSoftFloatLib/berkeley-softfloat-3
tar -xf %SOURCE3 --strip-components 1 --directory ArmPkg/Library/ArmSoftFloatLib/berkeley-softfloat-3

# add /edk2-platforms
tar -xf %SOURCE5

# add /edk2-non-osi
tar -xf %SOURCE6

# Install ALT Logo
cp -f %SOURCE4 edk2-non-osi/Platform/RaspberryPi/Drivers/LogoDxe/

# Update dtb
cp -f %SOURCE7 edk2-non-osi/Platform/RaspberryPi/RPi3/DeviceTree/bcm2710-rpi-3-b.dtb
cp -f %SOURCE8 edk2-non-osi/Platform/RaspberryPi/RPi3/DeviceTree/bcm2710-rpi-3-b-plus.dtb
cp -f %SOURCE9 edk2-non-osi/Platform/RaspberryPi/RPi4/DeviceTree/bcm2711-rpi-4-b.dtb

%build
source ./edksetup.sh

# compiler
CC_FLAGS="-t %TOOL_CHAIN_TAG"

# common features
#CC_FLAGS="${CC_FLAGS} --cmd-len=65536 -b DEBUG --hash"
CC_FLAGS="${CC_FLAGS} -b RELEASE"
#CC_FLAGS="${CC_FLAGS} -b DEBUG --hash"
CC_FLAGS="${CC_FLAGS} --cmd-len=65536"
CC_FLAGS="${CC_FLAGS} -D NETWORK_IP6_ENABLE"
CC_FLAGS="${CC_FLAGS} -D TPM2_ENABLE"

# ovmf features
OVMF_FLAGS="${CC_FLAGS}"
OVMF_FLAGS="${OVMF_FLAGS} -D NETWORK_TLS_ENABLE"
OVMF_FLAGS="${OVMF_FLAGS} -D NETWORK_HTTP_BOOT_ENABLE"
OVMF_FLAGS="${OVMF_FLAGS} -D NETWORK_IP6_ENABLE"
OVMF_FLAGS="${OVMF_FLAGS} -D FD_SIZE_2MB"

# ovmf + secure boot features
OVMF_SB_FLAGS="${OVMF_FLAGS}"
OVMF_SB_FLAGS="${OVMF_SB_FLAGS} -D SECURE_BOOT_ENABLE"
OVMF_SB_FLAGS="${OVMF_SB_FLAGS} -D SMM_REQUIRE"
OVMF_SB_FLAGS="${OVMF_SB_FLAGS} -D EXCLUDE_SHELL_FROM_FD"

# arm firmware features
#ARM_FLAGS="-t %TOOL_CHAIN_TAG -b DEBUG --cmd-len=65536"
ARM_FLAGS="${CC_FLAGS}"
ARM_FLAGS="${ARM_FLAGS} -D DEBUG_PRINT_ERROR_LEVEL=0x8040004F"


unset MAKEFLAGS

# prepare
#cp /usr/share/seabios/bios-csm.bin OvmfPkg/Csm/Csm16/Csm16.bin
#cp /usr/share/seabios/bios-csm.bin corebootPkg/Csm/Csm16/Csm16.bin
%make_build \
	 -C BaseTools


#(cd UefiCpuPkg/ResetVector/Vtf0; python Build.py)

#mkdir -p FatBinPkg/EnhancedFatDxe/{X64,Ia32}
#source ./edksetup.sh

mkdir -p out

# build Raspberry Pi 3 firmware
export PACKAGES_PATH=$PWD:$PWD/edk2-platforms:$PWD/edk2-non-osi
build ${ARM_FLAGS} -a AARCH64 -p edk2-platforms/Platform/RaspberryPi/RPi3/RPi3.dsc
mv Build/RPi3/RELEASE_GCC49/FV/RPI_EFI.fd out/RPi3_EFI.fd
rm -r Build/RPi3

# build Raspberry Pi 4 firmware without ACPI
export PACKAGES_PATH=$PWD:$PWD/edk2-platforms:$PWD/edk2-non-osi
build ${ARM_FLAGS} -a AARCH64 -p edk2-platforms/Platform/RaspberryPi/RPi4/RPi4.dsc \
  -D ACPI_BASIC_MODE_ENABLE=0 -D PL011_ENABLE=1
mv Build/RPi4/RELEASE_GCC49/FV/RPI_EFI.fd out/RPi4_EFI.fd
rm -fr Build/RPi4

# build Raspberry Pi 4 firmware with ACPI
export PACKAGES_PATH=$PWD:$PWD/edk2-platforms:$PWD/edk2-non-osi
build ${ARM_FLAGS} -a AARCH64 -p edk2-platforms/Platform/RaspberryPi/RPi4/RPi4.dsc \
  -D ACPI_BASIC_MODE_ENABLE=1 -D PL011_ENABLE=1
mv Build/RPi4/RELEASE_GCC49/FV/RPI_EFI.fd out/RPi4_EFI_ACPI.fd
rm -fr Build/RPi4

%install
mkdir -p %buildroot%_datadir/edk2-rpi
cp -a out/*.fd %buildroot%_datadir/edk2-rpi/

mkdir -p out/docs/RPi3
pandoc -f markdown -t plain edk2-platforms/Platform/RaspberryPi/RPi3/Readme.md -o out/docs/RPi3/Readme.txt
pandoc -f markdown -t plain edk2-platforms/Platform/RaspberryPi/RPi3/Systems.md -o out/docs/RPi3/Systems.txt
mkdir -p out/docs/RPi3/DeviceTree
cp edk2-non-osi/Platform/RaspberryPi/RPi3/DeviceTree/License.txt out/docs/RPi3/DeviceTree
mkdir -p out/docs/RPi3/TrustedFirmware/
cp edk2-non-osi/Platform/RaspberryPi/RPi3/TrustedFirmware/License.txt out/docs/RPi3/TrustedFirmware/
mkdir -p out/docs/RPi4
pandoc -f markdown -t plain edk2-platforms/Platform/RaspberryPi/RPi4/Readme.md -o out/docs/RPi4/Readme.txt
mkdir -p out/docs/RPi4/DeviceTree
cp edk2-non-osi/Platform/RaspberryPi/RPi4/DeviceTree/License.txt out/docs/RPi4/DeviceTree
mkdir -p out/docs/RPi4/TrustedFirmware/
cp edk2-non-osi/Platform/RaspberryPi/RPi4/TrustedFirmware/License.txt out/docs/RPi4/TrustedFirmware/

%files
%doc out/docs/{RPi3,RPi4}
%_datadir/edk2-rpi

%changelog
* Wed Feb 19 2020 Anton Midyukov <antohami@altlinux.org> 20191122-alt2
- Build two variants for rpi4: with ACPI and without ACPI.
- Update edk2-platforms (2020-02-19)
- Update dtb (2020-02-19)

* Thu Jan 23 2020 Anton Midyukov <antohami@altlinux.org> 20191122-alt1
- edk2-stable201911
- build as edk2-rpi package (for Raspberry Pi 3 and 4)

* Wed Jul 31 2019 Alexey Shabalin <shaba@altlinux.org> 20190501-alt2
- build as edk2-aarch64 package

* Wed Jun 19 2019 Alexey Shabalin <shaba@altlinux.org> 20190501-alt1
- edk2-stable201905 (Fixes: CVE-2018-12182)

* Tue Apr 02 2019 Alexey Shabalin <shaba@altlinux.org> 20190308-alt1
- edk2-stable201903 (Fixes: CVE-2018-12178, CVE-2018-12180, CVE-2018-12181, CVE-2018-3630)

* Tue Dec 11 2018 Alexey Shabalin <shaba@altlinux.org> 20181113-alt1
- edk2-stable201811

* Wed Dec 13 2017 Alexey Shabalin <shaba@altlinux.ru> 20170720-alt3%ubt
- snapshot of UDK2017 branch

* Mon Sep 18 2017 Sergey Bolshakov <sbolshakov@altlinux.ru> 20170720-alt2%ubt
- added efi-shell subpackage

* Fri Sep 01 2017 Alexey Shabalin <shaba@altlinux.ru> 20170720-alt1%ubt
- snapshot of UDK2017 branch

* Thu Jan 12 2017 Alexey Shabalin <shaba@altlinux.ru> 20161227-alt1
- UDK2017 branch

* Wed May 25 2016 Alexey Shabalin <shaba@altlinux.ru> 20160518-alt1
- master snapshot 855743f7177459bea95798e59b6b18dab867710c

* Mon Dec 28 2015 Alexey Shabalin <shaba@altlinux.ru> 20151225-alt1.svn19549
- build from branche UDK2015

* Wed Jun 24 2015 Alexey Shabalin <shaba@altlinux.ru> 20150616svn17642-alt2
- buils ovmf as noarch

* Wed Jun 17 2015 Alexey Shabalin <shaba@altlinux.ru> 20150616svn17642-alt1
- svn snapshot r17642
- add ovmf package

* Mon Oct 06 2014 Alexey Shabalin <shaba@altlinux.ru> 20140722svn2674-alt1
- svn snapshot r2674

* Fri Aug 09 2013 Alexey Shabalin <shaba@altlinux.ru> 0.1-alt1.svn2594
- initial build
