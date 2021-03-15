%def_with check
%define  modulename luv
Name:    ocaml-%modulename
Version: 0.5.7
Release: alt2
Summary: Binding to libuv for ocaml: cross-platform asynchronous I/O
License: MIT
Group:   Development/ML
URL:     https://github.com/aantron/luv
Source:  %name-%version.tar
Patch0: %name-%version-%release.patch

BuildRequires: dune
BuildRequires: libuv-devel >= 1.41.0-alt2
BuildRequires: ocaml-base-devel
BuildRequires: ocaml-result-devel
BuildRequires: ocaml-alcotest-devel
BuildRequires: ocaml-ctypes-devel
BuildPreReq: rpm-build-ocaml >= 1.4


%description
%name is a binding to libuv, the cross-platform C library that does asynchronous
I/O in Node.js and runs its main loop.

Besides asynchronous I/O, libuv also supports multiprocessing and
multithreading. Multiple event loops can be run in different threads. libuv also
exposes a lot of other functionality, amounting to a full OS API, and an
alternative to the standard module Unix.

%package devel
Summary: Development files for %name
Group: Development/ML
Requires: %name = %EVR

%description devel
The %name-devel package contains libraries and signature files for
developing applications that use %name.

%prep
%setup
%patch0 -p1

%build
export LUV_USE_SYSTEM_LIBUV=yes
%dune_build -p %modulename

%install
%dune_install %modulename

%check
export LUV_USE_SYSTEM_LIBUV=yes
export TRAVIS=true
%dune_check

%files -f ocaml-files.runtime
%doc README.md

%files devel -f ocaml-files.devel

%changelog
* Fri Mar 12 2021 Anton Farygin <rider@altlinux.org> 0.5.7-alt2
- libuv-1.41.0-alt2 was built without assertions and this change made it
  possible to enable tests
- added patches from upstream with fixes for testing on non-x86 architectures

* Thu Mar 11 2021 Anton Farygin <rider@altlinux.org> 0.5.7-alt1
- first build for ALT
