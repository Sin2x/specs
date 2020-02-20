
Name: libvirglrenderer
Version: 0.8.2
Release: alt1

Summary: Virgl Rendering library
Group: System/Libraries
License: MIT

#VCS: git:git://people.freedesktop.org/~airlied/virglrenderer
Source: %name-%version.tar

BuildRequires(pre): meson
BuildRequires: pkgconfig(libdrm) >= 2.4.50
BuildRequires: pkgconfig(gbm) >= 18.0.0
BuildRequires: pkgconfig(epoxy) >= 1.5.4

%description
The virgil3d rendering library is a library used by
qemu to implement 3D GPU support for the virtio GPU.

%package devel
Summary: Virgil3D renderer development files
Group: Development/C

Requires: %name = %version-%release

%description devel
Virgil3D renderer development files, used by
qemu to build against.

%package test-server
Summary: Virgil3D renderer testing server
Group: Emulators

Requires: %name = %version-%release

%description test-server
Virgil3D renderer testing server is a server
that can be used along with the mesa virgl
driver to test virgl rendering without GL.

%prep
%setup

%build
%meson
%meson_build

%install
%meson_install

%files
%doc COPYING
%_libdir/*.so.*

%files devel
%_includedir/virgl
%_libdir/*.so
%_pkgconfigdir/*.pc

%files test-server
%_bindir/virgl_test_server

%changelog
* Thu Feb 20 2020 Alexey Shabalin <shaba@altlinux.org> 0.8.2-alt1
- 0.8.2

* Fri Jan 24 2020 Alexey Shabalin <shaba@altlinux.org> 0.8.1.0.17.g845bc48-alt1
- upstream commit 845bc4889b2398921aee2fd62b883cddd1a1ac19

* Fri Oct 11 2019 Alexey Shabalin <shaba@altlinux.org> 0.8.0.0.34.4ac3a04c-alt1
- upstream commit 4ac3a04cb8a4b0d419bccbb7798b59aa098487a6

* Mon Oct 15 2018 Alexey Shabalin <shaba@altlinux.org> 0.7.0-alt1
- 0.7.0

* Fri Apr 28 2017 Alexey Shabalin <shaba@altlinux.ru> 0.6.0-alt1%ubt
- 0.6.0

* Thu May 19 2016 Alexey Shabalin <shaba@altlinux.ru> 0.5.0-alt1
- 0.5.0

* Thu Dec 17 2015 Alexey Shabalin <shaba@altlinux.ru> 0.3.0-alt0.1.git.e9d3c0c27
- initial build

