%define sover 0.14

%def_with devel

%if_with devel
%define _unpackaged_files_terminate_build 1

Name: hiredis
%else
Name: hiredis%sover
%endif
Version: 0.14.1
Release: alt1
Summary: The official C client for Redis
Group: System/Libraries
License: BSD-3-Clause
Url: https://github.com/redis/hiredis

# https://github.com/redis/hiredis.git
Source: hiredis-%version.tar

BuildRequires: gcc-c++ libevent-devel libev-devel glib2-devel

%description
Hiredis is a minimalistic C client library for the Redis database.

%package -n libhiredis%sover
Summary: The official C client for Redis
License: BSD
Group: System/Libraries

%description -n libhiredis%sover
Hiredis is a minimalistic C client library for the Redis database.

%if_with devel
%package -n libhiredis-devel
Summary: Header files and libraries for hiredis C development
Group: Development/C
Requires: libhiredis%sover = %EVR

Provides: hiredis-devel = %EVR
Obsoletes: hiredis-devel

# Those pkgs included the example & test executables, too:
Conflicts: libhiredis0.12 <= 0.12-alt1
Conflicts: libhiredis <= 0.12-alt1
Conflicts: libhiredis0.11
Conflicts: libhiredis0.10

%description -n libhiredis-devel
The hiredis-devel package contains the header files and
libraries to develop applications using a Redis database.

%package -n libhiredis-devel-static
Summary: Static libraries for hiredis C development
Group: Development/C
Requires: libhiredis-devel = %EVR

%description -n libhiredis-devel-static
The hiredis-devel package contains static libraries
to develop applications using a Redis database.
%endif

%prep
%setup -n hiredis-%version

%build
%make_build \
	OPTIMIZATION= \
	DEBUG_FLAGS= \
	CFLAGS="%optflags" \
	CXXFLAGS="%optflags" \
	%nil

%make examples \
	OPTIMIZATION= \
	DEBUG_FLAGS= \
	CFLAGS="%optflags" \
	CXXFLAGS="%optflags" \
	%nil

%make hiredis-test \
	OPTIMIZATION= \
	DEBUG_FLAGS= \
	CFLAGS="%optflags" \
	CXXFLAGS="%optflags" \
	%nil

%install
%make install \
	PREFIX=%buildroot%_prefix \
	LIBRARY_PATH=%_lib \
	LIB_SUFFIX=%_libsuff \
	%nil

mkdir -p %buildroot%_bindir/
cp examples/hiredis-example* %buildroot%_bindir/
cp hiredis-test %buildroot%_bindir/

%files -n libhiredis%sover
%doc COPYING CHANGELOG.md
%_libdir/*.so.%{sover}

%if_with devel
%files -n libhiredis-devel
%doc README.md
%_bindir/hiredis-example*
%_bindir/hiredis-test
%_includedir/hiredis
%_libdir/*.so
%_libdir/pkgconfig/hiredis.pc

%files -n libhiredis-devel-static
%_libdir/*.a
%endif

%changelog
* Tue Oct 27 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 0.14.1-alt1
- Updated to upstream version 0.14.1 (Fixes: CVE-2020-7105).

* Thu Feb 28 2019 Mikhail Gordeev <obirvalger@altlinux.org> 0.13.3-alt3.1
- Rebuild with new libevent2

* Mon Oct 30 2017 Ivan Zakharyaschev <imz@altlinux.org> 0.13.3-alt3
- Added to devel subpkg: Conflicts: libhiredis* <= 0.12-alt1
  (which included the example & test executables, too)

* Mon Oct 16 2017 Mikhail Gordeev <obirvalger@altlinux.org> 0.13.3-alt2
- (ALT #34016) Move example files to devel package

* Wed Sep 13 2017 Mikhail Gordeev <obirvalger@altlinux.org> 0.13.3-alt1
- Version 0.13.3

* Mon Sep 08 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.11.0-alt1.git20140529
- Version 0.11.0

* Fri May 18 2012 Anatoly Lyutin <vostok@altlinux.org> 0.10.1-alt2
- rename to libhiredis (closes: #27301)

* Thu Apr 19 2012 Anatoly Lyutin <vostok@altlinux.org> 0.10.1-alt1
- initial build for ALT Linux

