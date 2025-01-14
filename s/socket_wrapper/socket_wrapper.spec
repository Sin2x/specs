Name:           socket_wrapper
Version:        1.3.4
Release:        alt1
Group:          Development/Other
License:        BSD
Summary:        A library passing all socket communications through Unix sockets
Url:            http://cwrap.org/

# git://git.samba.org/socket_wrapper.git
Source0:        %name-%version.tar
Patch0:         %name-%version-alt.patch

BuildRequires:  cmake ctest
BuildRequires:  libcmocka-devel

Requires:       cmake
Requires:       pkgconfig

%description
socket_wrapper aims to help client/server software development teams willing to
gain full functional test coverage. It makes it possible to run several
instances of the full software stack on the same machine and perform locally
functional testing of complex network configurations.

To use it set the following environment variables:

LD_PRELOAD=libsocket_wrapper.so
SOCKET_WRAPPER_DIR=/path/to/swrap_dir

This package doesn't have a devel package because this project is for
development/testing.

%prep
%setup -q
%patch -p1

%build
if test ! -e "obj"; then
mkdir obj
fi

pushd obj
%cmake_insource \
  -DUNIT_TESTING=ON \
  %_builddir/%name-%version

%make VERBOSE=1
popd

%install
pushd obj
%make DESTDIR=%buildroot install
popd

%check
pushd obj
LD_LIBRARY_PATH=$PWD/src ctest -V

LD_PRELOAD=src/libsocket_wrapper.so bash -c '>/dev/null'
LD_PRELOAD=src/libsocket_wrapper_noop.so bash -c '>/dev/null'

popd

%files
%doc AUTHORS README.md CHANGELOG LICENSE
%_libdir/lib%{name}*.so*
%dir %_libdir/cmake/%name
%_libdir/cmake/%name/*.cmake
%_includedir/%name.h
%_pkgconfigdir/%{name}*.pc
%_man1dir/%name.1*

%changelog
* Fri Sep 16 2022 Evgeny Sinelnikov <sin@altlinux.org> 1.3.4-alt1
- Fixed TOCTOU issue with udp auto binding

* Thu Jul 29 2021 Evgeny Sinelnikov <sin@altlinux.org> 1.3.3-alt1
- Update to latest release with support for fd-passing via unix sockets
- Add public libsocket_wrapper_noop library

* Sun Feb 07 2021 Evgeny Sinelnikov <sin@altlinux.org> 1.2.5-alt1
- Update to latest release

* Wed Jan 16 2019 Evgeny Sinelnikov <sin@altlinux.org> 1.2.1-alt1
- Update to latest release
- Disable ubt macros due binary package identity change

* Mon Apr 09 2018 Evgeny Sinelikov <sin@altlinux.org> 1.1.9-alt2
- Add LD_LIBRARY_PATH to libthread_deadlock.so for running tests on e2k

* Mon Jan 29 2018 Evgeny Sinelnikov <sin@altlinux.org> 1.1.9-alt1
- Update to latest release with fixed thread - signal deadlock issue

* Fri Nov 03 2017 Evgeny Sinelnikov <sin@altlinux.org> 1.1.8-alt2
- Disable ipv6 for test_socket_getsockname due girar error with:
  "Address family not supported by protocol"

* Fri Nov 03 2017 Evgeny Sinelnikov <sin@altlinux.org> 1.1.8-alt1
- Initial build for ALT Sisyphus

