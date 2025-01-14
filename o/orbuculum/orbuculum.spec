Name: orbuculum
Version: 2.0.0
Release: alt1

Summary: Cortex-M code instrumentation for the masses
License: BSD-3-Clause
Group: Development/Other
Url: https://github.com/orbcode/orbuculum

Source: %name-%version-%release.tar

BuildRequires: binutils-devel libczmq-devel libncurses-devel libusb-devel

%description
Orbuculum is a set of tools for decoding and presenting output flows
from the Debug pins of a CORTEX-M CPU.

%prep
%setup
sed -ri '/^CFLAGS=/ s,$,%optflags,' Makefile

%build
make VERBOSE=1 VERSION=%version-%release

%install
%make_install DESTDIR=%buildroot INSTALL_ROOT=%prefix/ install

%files
%doc CHANGES* CONTRIBUTORS COPYING README* Docs Support
%_bindir/*
%_datadir/orbcode

%changelog
* Fri Aug 19 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.0.0-alt1
- 2.0.0 released

* Fri Nov 19 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.12-alt2
- V1.12-120-gce9ff2c

* Thu Jan 21 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.12-alt1
- initial
