%define _unpackaged_files_terminate_build 1

Name: fido2
Version: 1.10.0
Release: alt1

Summary: Command-line tools to communicate with a FIDO device over USB.
License: BSD-2-Clause
Group: System/Configuration/Hardware
Url: https://github.com/Yubico/libfido2

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-cmake
BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: pkg-config
BuildRequires: libssl-devel
BuildRequires: libudev-devel
BuildRequires: libcbor-devel
BuildRequires: zlib-devel

Requires: lib%name = %EVR

%description
Provides command-line tools to communicate with a FIDO device over USB,
and to verify attestation and assertion signatures.

Supports the FIDO U2F (CTAP 1) and FIDO2 (CTAP 2) protocols.


%package -n lib%name
Summary: Library functionality to communicate with a FIDO device over USB.
Group: System/Libraries

%description -n lib%name
Provides library functionality to communicate with a FIDO device over USB,
and to verify attestation and assertion signatures.

Supports the FIDO U2F (CTAP 1) and FIDO2 (CTAP 2) protocols.


%package -n lib%name-devel
Summary: Development header files for lib%name.
Group: Development/Other
Requires: lib%name = %EVR

%description -n lib%name-devel
Provides development header files for lib%name.


%prep
%setup

%build
%cmake -DBUILD_STATIC_LIBS=OFF
%cmake_build

%install
%cmake_install

%files
%doc LICENSE NEWS
%_bindir/*
%_man1dir/*

%files -n lib%name
%doc LICENSE NEWS
%_libdir/libfido2*

%files -n lib%name-devel
%doc LICENSE NEWS
%_includedir/*
%_libdir/pkgconfig/lib%name.pc
%_man3dir/*

%changelog
* Sat Jul 23 2022 Anton Zhukharev <ancieg@altlinux.org> 1.10.0-alt1
- initial build for Sisyphus
