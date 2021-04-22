%def_disable static

Name: usbredir
Version: 0.9.0
Release: alt1
Summary: USB network redirection protocol libraries
Group: System/Libraries
License: LGPLv2+
Url: http://gitlab.freedesktop.org/spice/usbredir

Source: %name-%version.tar
Patch0001: 0001-Fix-generated-by-meson-libusbredirhostpc.patch
Patch0002: 0002-Add-local-directory-to-include-search-path-for-meson.patch

BuildRequires(pre): meson
BuildRequires: gcc-c++
BuildRequires: pkgconfig(libusb-1.0) >= 1.0.9
BuildRequires: pkgconfig(glib-2.0) >= 2.44 pkgconfig(gio-unix-2.0) >= 2.44

%description
usbredir is a protocol for redirection USB traffic from a single USB device,
to a different (virtual) machine then the one to which the USB device is
attached. This package contains a number of libraries to help implementing
support for usbredir:

usbredirparser:
A library containing the parser for the usbredir protocol

usbredirhost:
A library implementing the usb-host side of a usbredir connection.
All that an application wishing to implement an usb-host needs to do is:
* Provide a libusb device handle for the device
* Provide write and read callbacks for the actual transport of usbredir data
* Monitor for usbredir and libusb read/write events and call their handlers

%package -n lib%name
Summary: USB network redirection protocol libraries
Group: System/Libraries
License: LGPLv2+

%description -n lib%name
usbredir is a protocol for redirection USB traffic from a single USB device,
to a different (virtual) machine then the one to which the USB device is
attached. This package contains a number of libraries to help implementing
support for usbredir:

usbredirparser:
A library containing the parser for the usbredir protocol

usbredirhost:
A library implementing the usb-host side of a usbredir connection.
All that an application wishing to implement an usb-host needs to do is:
* Provide a libusb device handle for the device
* Provide write and read callbacks for the actual transport of usbredir data
* Monitor for usbredir and libusb read/write events and call their handlers

%package -n lib%name-devel
Summary: Development files for %name
Group: Development/C
Requires: lib%name = %version-%release

%description -n lib%name-devel
The lib%name-devel package contains libraries and header files for
developing applications that use %name.

%package server
Summary: Simple usb-host tcp server
Group: Networking/Other
License: GPLv2+
Requires: lib%name = %version-%release

%description server
A simple usb-host tcp server, using libusbredirhost.

%prep
%setup
%patch0001 -p1
%patch0002 -p1

%build
%meson
%meson_build

%install
%meson_install

%files  -n lib%name
%doc README.md ChangeLog.md
%_libdir/*.so.*

%files  -n lib%name-devel
%doc docs/usb-redirection-protocol.md docs/multi-thread.md
%_includedir/*.h
%_libdir/*.so
%_pkgconfigdir/*.pc

%files server
%_bindir/usbredirect
%_sbindir/usbredirserver
%_man1dir/usbredirect.1*
%_man1dir/usbredirserver.*

%changelog
* Thu Apr 22 2021 Alexey Shabalin <shaba@altlinux.org> 0.9.0-alt1
- new version 0.9.0

* Fri Aug 24 2018 Alexey Shabalin <shaba@altlinux.org> 0.8.0-alt1
- 0.8.0

* Thu Jul 07 2016 Alexey Shabalin <shaba@altlinux.ru> 0.7.1-alt1
- 0.7.1

* Thu Jun 05 2014 Alexey Shabalin <shaba@altlinux.ru> 0.7-alt1
- 0.7

* Mon Feb 18 2013 Alexey Shabalin <shaba@altlinux.ru> 0.6-alt1
- 0.6

* Mon Sep 10 2012 Alexey Shabalin <shaba@altlinux.ru> 0.5-alt1
- 0.5

* Mon Aug 06 2012 Alexey Shabalin <shaba@altlinux.ru> 0.4.3-alt1
- 0.4.3

* Sun Mar 11 2012 Alexey Shabalin <shaba@altlinux.ru> 0.4.2-alt1
- 0.4.2

* Thu Mar 01 2012 Alexey Shabalin <shaba@altlinux.ru> 0.4.1-alt1
- 0.4.1

* Fri Feb 03 2012 Alexey Shabalin <shaba@altlinux.ru> 0.3.3-alt1
- 0.3.3

* Tue Jan 10 2012 Alexey Shabalin <shaba@altlinux.ru> 0.3.2-alt1
- 0.3.2

* Tue Nov 15 2011 Alexey Shabalin <shaba@altlinux.ru> 0.3.1-alt1.git.a897d
- initial build for ALT Linux Sisyphus
