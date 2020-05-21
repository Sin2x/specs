Name: volk
Version: 2.3.0
Release: alt1
Summary: Vector-Optimized Library of Kernels
License: GPLv3
Group: Development/C++
Url: http://libvolk.org/

Source: %name-%version.tar

%description
VOLK:
- is the Vector-Optimized Library of Kernels;
- is a free library, currently offered under the GPLv3 license;
- provides an abstraction of optimized math routines targetting several SIMD processors.

%package -n lib%name
Group: Development/C++
Summary: Vector-Optimized Library of Kernels
BuildRequires(pre): rpm-macros-cmake
BuildRequires: gcc-c++ cmake
BuildRequires: liborc-devel orc
BuildRequires: boost-filesystem-devel

%description -n lib%name
VOLK:
- is the Vector-Optimized Library of Kernels;
- is a free library, currently offered under the GPLv3 license;
- provides an abstraction of optimized math routines targetting several SIMD processors.

%package -n lib%name-devel
Summary: Vector-Optimized Library of Kernels
Group: Development/C++
Requires: lib%name = %version-%release

%description -n lib%name-devel
VOLK:
- is the Vector-Optimized Library of Kernels;
- is a free library, currently offered under the GPLv3 license;
- provides an abstraction of optimized math routines targetting several SIMD processors.

%package -n python3-module-%name
Summary: The Python 3 bindings for VOLK
Group: Development/Python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel
BuildRequires: python3-module-six
BuildRequires: python3-module-mako
Requires: lib%name = %version

%description -n python3-module-%name
Python 3 module for VOLK.

%prep
%setup

%build
%cmake \
	-DGR_PYTHON_DIR=%python3_sitelibdir \
	-DPYTHON_EXECUTABLE=%__python3

%cmake_build

%install
%cmakeinstall_std

%files
%_bindir/*
%doc COPYING README.md

%files -n lib%name
%_libdir/lib%name.so.*

%files -n lib%name-devel
%_includedir/*
%_libdir/*.so
%_pkgconfigdir/*
%_libdir/cmake/%name

%files -n python3-module-%name
%python3_sitelibdir/*

%changelog
* Thu May 21 2020 Anton Midyukov <antohami@altlinux.org> 2.3.0-alt1
- new version 2.3.0

* Fri Nov 22 2019 Anton Midyukov <antohami@altlinux.org> 2.0.0-alt1
- new version 2.0.0

* Thu May 31 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 1.4-alt1.1
- NMU: rebuilt with boost-1.67.0

* Sun Apr 22 2018 Anton Midyukov <antohami@altlinux.org> 1.4-alt1
- new version 1.4

* Fri Aug 11 2017 Anton Midyukov <antohami@altlinux.org> 1.3-alt1
- New version 1.3

* Tue Mar 25 2016 Dmitry Derjavin <dd@altlinux.org> 1.2.1-alt1
- Initial ALT Linux build.
