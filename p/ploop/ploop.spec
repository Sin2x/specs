%define _libexecdir /usr/libexec
%define _scriptdir %_libexecdir/%name

Name: ploop
Version: 7.0.188
Release: alt1
Group: System/Base
License: GPLv2
Summary: Ploop tools
URL: http://wiki.openvz.org/Ploop
Packager: Viacheslav Dubrovskyi <dubrsl@altlinux.org>
Source: %name-%version.tar

Patch1: %name-%version.patch

ExclusiveArch: x86_64

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-dev python3-module-setuptools
BuildRequires: libxml2-devel libe2fs-devel libuuid-devel libssl-devel libjson-c-devel

%description
This package contains tools to work with ploop devices and images.

%package -n lib%name
Summary: ploop library
Group: System/Libraries
License: LGPLv2.1
Conflicts: vzctl < 4.5
Requires: parted gdisk e2fsprogs lsof

%description -n lib%name
Parallels loopback (ploop) block device API library

%package -n lib%name-devel-static
Summary: Static ploop library
Group: Development/C
License: LGPLv2.1
Requires: lib%name-devel = %version-%release

%description -n lib%name-devel-static
Static version of ploop library

%package -n lib%name-devel
Summary: Headers for development with ploop library
Group: Development/C
License: GPLv2 or LGPLv2.1
Requires: lib%name = %version-%release

%description -n lib%name-devel
Headers of ploop library

%package -n python3-module-%name
Summary: Python bindings for %name
Group: Development/Python
Requires: lib%name = %version-%release
Provides: python3(libploopapi)

%description -n python3-module-%name
python3-module-%name contains Python bindings for %name.

%prep
%setup
%patch1 -p1

%build
export PYTHON=%__python3
%make_build LIBDIR=%_libdir PLOOP_LOG_FILE=%_logdir/%name.log DEBUG=no all

%install
export PYTHON=%__python3
mkdir -p %buildroot%_sbindir
make \
    DESTDIR=%buildroot \
    LIBDIR=%_libdir \
    PLOOP_LOG_FILE=%_logdir/%name.log \
    TMPFILESDIR=%_tmpfilesdir \
    MODULESLOADDIR=%_modulesloaddir \
    install

%files
/sbin/*
%_sbindir/*
%_man8dir/*
%_logrotatedir/%name
%_modulesloaddir/%name.conf
%_sysconfdir/bash_completion.d/ploop

%files -n lib%name
%_libdir/lib%name.so.*
%_lockdir/%name
%_tmpfilesdir/*
%dir %_scriptdir
%_scriptdir/*
%dir %_scriptdir-test
%_scriptdir-test/*

%files -n lib%name-devel-static
%_libdir/libploop.a

%files -n lib%name-devel
%_libdir/lib%name.so
%_includedir/%name
%_pkgconfigdir/%name.pc

%files -n python3-module-%name
%python3_sitelibdir/*

%changelog
* Fri Mar 20 2020 Andrew A. Vasilyev <andy@altlinux.org> 7.0.188-alt1
- 7.0.188

* Tue Mar 10 2020 Andrew A. Vasilyev <andy@altlinux.org> 7.0.187-alt1
- 7.0.187

* Wed Feb 26 2020 Andrew A. Vasilyev <andy@altlinux.org> 7.0.184-alt1
- 7.0.184

* Wed Feb 19 2020 Andrew A. Vasilyev <andy@altlinux.org> 7.0.183-alt1
- 7.0.183

* Fri Feb 14 2020 Andrew A. Vasilyev <andy@altlinux.org> 7.0.182-alt1
- 7.0.182

* Tue Feb 11 2020 Andrew A. Vasilyev <andy@altlinux.org> 7.0.181-alt1
- 7.0.181

* Mon Feb 10 2020 Andrew A. Vasilyev <andy@altlinux.org> 7.0.179-alt1
- 7.0.179

* Fri Feb 07 2020 Andrew A. Vasilyev <andy@altlinux.org> 7.0.178-alt1
- 7.0.178

* Wed Feb 05 2020 Andrew A. Vasilyev <andy@altlinux.org> 7.0.177-alt1
- 7.0.177

* Mon Feb 03 2020 Andrew A. Vasilyev <andy@altlinux.org> 7.0.176-alt1
- 7.0.176

* Thu Jan 30 2020 Andrew A. Vasilyev <andy@altlinux.org> 7.0.175-alt1
- 7.0.175

* Wed Jan 29 2020 Andrew A. Vasilyev <andy@altlinux.org> 7.0.174-alt1
- 7.0.174

* Tue Jan 28 2020 Andrew A. Vasilyev <andy@altlinux.org> 7.0.173-alt1
- 7.0.173

* Mon Jan 27 2020 Andrew A. Vasilyev <andy@altlinux.org> 7.0.172-alt1
- 7.0.172

* Mon Jan 27 2020 Andrew A. Vasilyev <andy@altlinux.org> 7.0.171-alt1
- 7.0.171

* Thu Jan 23 2020 Andrew A. Vasilyev <andy@altlinux.org> 7.0.170-alt1
- 7.0.170

* Wed Jan 22 2020 Andrew A. Vasilyev <andy@altlinux.org> 7.0.169-alt1
- 7.0.169

* Tue Jan 21 2020 Andrew A. Vasilyev <andy@altlinux.org> 7.0.168-alt1
- 7.0.168

* Fri Jan 10 2020 Andrew A. Vasilyev <andy@altlinux.org> 7.0.167-alt1
- 7.0.167

* Fri Dec 20 2019 Andrew A. Vasilyev <andy@altlinux.org> 7.0.166-alt1
- 7.0.166

* Thu Dec 19 2019 Andrew A. Vasilyev <andy@altlinux.org> 7.0.165-alt1
- 7.0.165

* Thu Dec 05 2019 Andrew A. Vasilyev <andy@altlinux.org> 7.0.163-alt7
- build only for x86_64
- fix License

* Wed Dec 04 2019 Andrew A. Vasilyev <andy@altlinux.org> 7.0.163-alt6
- reduce the changes from upstream

* Thu Oct 31 2019 Andrew A. Vasilyev <andy@altlinux.org> 7.0.163-alt5
- make python3 convertion closer to upstream style

* Wed Oct 30 2019 Andrew A. Vasilyev <andy@altlinux.org> 7.0.163-alt4
- fix compilation warnings on snprintf/strncpy calls

* Fri Oct 25 2019 Andrew A. Vasilyev <andy@altlinux.org> 7.0.163-alt3
- enable ELF verify

* Thu Oct 17 2019 Andrew A. Vasilyev <andy@altlinux.org> 7.0.163-alt2
- convert to python3

* Mon Sep 30 2019 Andrew A. Vasilyev <andy@altlinux.org> 7.0.163-alt1
- 7.0.163

* Fri Sep 20 2019 Andrew A. Vasilyev <andy@altlinux.org> 7.0.162-alt2
- fix e4defrag command line arguments

* Fri Sep 20 2019 Andrew A. Vasilyev <andy@altlinux.org> 7.0.162-alt1
- 7.0.162

* Wed Sep 18 2019 Andrew A. Vasilyev <andy@altlinux.org> 7.0.161-alt1
- 7.0.161

* Fri Aug 16 2019 Andrew A. Vasilyev <andy@altlinux.org> 7.0.160-alt1
- 7.0.160

* Sun Nov 04 2018 Alexey Shabalin <shaba@altlinux.org> 7.0.132-alt1
- 7.0.132

* Mon Feb 26 2018 Alexey Shabalin <shaba@altlinux.ru> 7.0.126-alt1
- 7.0.126

* Fri Feb 09 2018 Alexey Shabalin <shaba@altlinux.ru> 7.0.124-alt1
- Updated to 7.0.124
- add python package

* Fri Jul 28 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 1.15-alt2
- Fixed build with new toolchain

* Sun May 01 2016 Gleb F-Malinovskiy <glebfm@altlinux.org> 1.15-alt1
- Updated to 1.15.

* Tue Sep 22 2015 Terechkov Evgenii <evg@altlinux.org> 1.14.1-alt1
- New version
- Add pkg-config support

* Tue Sep 22 2015 Terechkov Evgenii <evg@altlinux.org> 1.14-alt1
- New version

* Tue Apr 21 2015 Terechkov Evgenii <evg@altlinux.org> 1.13.2-alt1
- New version

* Thu Apr 16 2015 Terechkov Evgenii <evg@altlinux.org> 1.13-alt1
- New version

* Sat Jan  3 2015 Terechkov Evgenii <evg@altlinux.org> 1.12.2-alt1
- New version

* Fri Sep  5 2014 Terechkov Evgenii <evg@altlinux.org> 1.12.1-alt1
- New version

* Thu Jul 31 2014 Terechkov Evgenii <evg@altlinux.org> 1.12-alt1
- New version

* Tue Jul  1 2014 Evgenii Terechkov <evg@altlinux.org> 1.11-alt1
- New version

* Sat Dec 28 2013 Slava Dubrovskiy <dubrsl@altlinux.org> 1.10-alt1
- New version

* Sun Oct 20 2013 Slava Dubrovskiy <dubrsl@altlinux.org> 1.9-alt1
- New version

* Mon Aug 05 2013 Slava Dubrovskiy <dubrsl@altlinux.org> 1.8-alt1
- New version

* Tue Jan 29 2013 Slava Dubrovskiy <dubrsl@altlinux.org> 1.6-alt1
- New version

* Thu Jun 14 2012 Slava Dubrovskiy <dubrsl@altlinux.org> 1.4-alt1
- New version

* Wed Apr 18 2012 Slava Dubrovskiy <dubrsl@altlinux.org> 1.2-alt1
- New version

* Sat Mar 24 2012 Slava Dubrovskiy <dubrsl@altlinux.org> 1.1-alt1
- Update to bb3948d45daf3e30d0e05f20d1442376237ac49d

* Tue Mar 13 2012 Slava Dubrovskiy <dubrsl@altlinux.org> 1.0-alt1
- build for ALT

* Tue Mar 13 2012 Kir Kolyshkin <kir@openvz.org> 1.0-1
- initial version
