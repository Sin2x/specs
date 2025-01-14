Name: nvidia-modprobe
Version: 510.60.02
Release: alt1

Group: System/Configuration/Hardware
Summary: Helper to load kernel module and create device files
Url: ftp://download.nvidia.com/XFree86/nvidia-modprobe/
License: GPL-2.0-or-later

Source: %name-%version.tar
Patch1: alt-cflags.patch

BuildRequires: glibc-devel

%description
 The nvidia-modprobe utility is used by user-space NVIDIA driver components
to make sure the NVIDIA kernel module is loaded and that the NVIDIA
character device files are present.  These facilities are normally provided
by Linux distribution configuration systems such as udev.  When possible,
it is recommended to  use  your  Linux distribution's  native  mechanisms
for  managing kernel module loading and device file creation.  This utility
is provided as a fallback to work out-of-the-box in a distribution-independent way.

%prep
%setup -q
%patch1 -p1 -b .flags

%build
%make_build NV_VERBOSE=1 OUTPUTDIR=BUILD STRIP_CMD=true NV_KEEP_UNSTRIPPED_BINARIES=1 PREFIX=%prefix CC=gcc LOCAL_CFLAGS="%optflags"
cp -ar BUILD/nvidia-modprobe.unstripped BUILD/nvidia-modprobe

%install
make install NV_VERBOSE=1 OUTPUTDIR=BUILD STRIP_CMD=true NV_KEEP_UNSTRIPPED_BINARIES=1 PREFIX=%buildroot/%prefix bindir=%buildroot/%_bindir mandir=%buildroot/%_man1dir
#install -m 0755 nvidia-modprobe %buildroot/%_bindir

%files
%doc COPYING
%attr(4710,root,wheel) %_bindir/%name
%_man1dir/%name.*


%changelog
* Fri Apr 08 2022 Sergey V Turchin <zerg@altlinux.org> 510.60.02-alt1
- new version

* Wed Nov 24 2021 Sergey V Turchin <zerg@altlinux.org> 470.86-alt2
- make SUID

* Mon Nov 22 2021 Sergey V Turchin <zerg@altlinux.org> 470.86-alt1
- initial build

