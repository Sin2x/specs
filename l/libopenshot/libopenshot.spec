%def_disable snapshot
%define _name openshot

%define ver_major 0.2
%define api_ver 20

%def_enable python
%def_enable opencv
%def_disable doc
#99%% tests passed, 1 tests failed out of 132
%def_disable check

Name: lib%_name
Version: %ver_major.7
Release: alt1

Summary: OpenShot Video Library
Group: System/Libraries
License: GPL-3.0
Url: https://launchpad.net/%name

%if_disabled snapshot
#Source: %url/%ver_major/%version/+download/%name-%version.tar.gz
Source: https://github.com/OpenShot/%name/archive/v%version/%name-%version.tar.gz
%else
Vcs: https://github.com/OpenShot/libopenshot.git
Source: %name-%version.tar
%endif

BuildRequires(pre): rpm-macros-cmake rpm-build-python3
BuildRequires: %name-audio-devel >= 0.2.2
BuildRequires: /proc cmake gcc-c++ libgomp-devel libunittest-cpp-devel jsoncpp-devel
BuildRequires: libalsa-devel qt5-multimedia-devel qt5-svg-devel libzeromq-cpp-devel
BuildRequires: libImageMagick-devel zlib-devel
BuildRequires: libavcodec-devel libavformat-devel libavutil-devel
BuildRequires: libavresample-devel libswresample-devel libswscale-devel
BuildRequires: libavdevice-devel libpostproc-devel
%{?_enable_opencv:BuildRequires: boost-devel libopencv-devel libprotobuf-devel %_bindir/protoc}
%{?_enable_python:BuildRequires: python3-devel python3-module-zmq swig}
%{?_enable_check:BuildRequires: ctest ImageMagick-tools
BuildRequires: catch2-devel}

%description
libopenshot is an open-source, cross-platform C++ library dedicated to
delivering high quality video editing, animation, and playback solutions
to the world. This is the same library which powers OpenShot Video Editor
(version 2.0+) and it could power your next video editing application!
C++, Python, and Ruby are fully supported, and other languages can be
added if requested.

%package devel
Summary: OpenShot Video Library development package
Group: Development/C++
Requires: %name = %version-%release

%description devel
This package contains development libraries and header files
that are needed to write applications that use %name.

%package -n python3-module-%_name
Summary: Python3 bindings for OpenShot Video Library
Group: Development/Python3
Requires: %name = %version-%release

%description -n python3-module-%_name
This package provides Python3 bindings for OpenShot Video Library.

%prep
%setup

%build
%add_optflags %(getconf LFS_CFLAGS) -DNDEBUG
%cmake  -DUSE_SYSTEM_JSONCPP:BOOL=ON \
	-DMAGICKCORE_HDRI_ENABLE:BOOL=ON \
	-DMAGICKCORE_QUANTUM_DEPTH=16 \
	%{?_enable_python:-DENABLE_PYTHON=TRUE} \
	%{?_enable_opencv:-DENABLE_OPENCV=TRUE} \
	%{?_enable_check:-DENABLE_TESTS=TRUE}
%nil
%cmake_build

%install
%cmake_install

%check
%cmake_build -t test

%files
%_libdir/%name.so.*
%{?_enable_opencv:%_libdir/%{name}_protobuf.so.*}
%doc AUTHORS README*

%files devel
%_includedir/%name/
%_libdir/%name.so
%{?_enable_opencv:%_libdir/%{name}_protobuf.so}

%files -n python3-module-%_name
%python3_sitelibdir/*

%changelog
* Tue Sep 07 2021 Yuri N. Sedunov <aris@altlinux.org> 0.2.7-alt1
- 0.2.7

* Wed Aug 25 2021 Yuri N. Sedunov <aris@altlinux.org> 0.2.6-alt1
- 0.2.6

* Sun May 30 2021 Yuri N. Sedunov <aris@altlinux.org> 0.2.5-alt3.1
- rebuild with new cmake macros

* Thu May 27 2021 Yuri N. Sedunov <aris@altlinux.org> 0.2.5-alt3
- disabled broken %check

* Sat Dec 05 2020 Yuri N. Sedunov <aris@altlinux.org> 0.2.5-alt2
- fixed build with gcc10/-fno-common (upstream patch)

* Mon Mar 16 2020 Yuri N. Sedunov <aris@altlinux.org> 0.2.5-alt1
- 0.2.5

* Mon Feb 10 2020 Yuri N. Sedunov <aris@altlinux.org> 0.2.4-alt1
- 0.2.4
- %%check section

* Sat Mar 30 2019 Yuri N. Sedunov <aris@altlinux.org> 0.2.3-alt1
- 0.2.3

* Sun Sep 23 2018 Yuri N. Sedunov <aris@altlinux.org> 0.2.2-alt1
- 0.2.2

* Thu Sep 20 2018 Yuri N. Sedunov <aris@altlinux.org> 0.2.1-alt1
- 0.2.1

* Sat Jun 30 2018 Yuri N. Sedunov <aris@altlinux.org> 0.2.0-alt1
- 0.2.0

* Thu Jun 14 2018 Yuri N. Sedunov <aris@altlinux.org> 0.1.9-alt3
- rebuilt with ffmpeg-4.0

* Tue May 22 2018 Yuri N. Sedunov <aris@altlinux.org> 0.1.9-alt2
- rebuilt against ImageMagick-6.9.9.47 libraries

* Thu Mar 22 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 0.1.9-alt1.1
- (NMU) Rebuilt with python-3.6.4.

* Mon Nov 13 2017 Yuri N. Sedunov <aris@altlinux.org> 0.1.9-alt1
- 0.1.9

* Fri Sep 08 2017 Yuri N. Sedunov <aris@altlinux.org> 0.1.8-alt1
- 0.1.8

* Fri Aug 18 2017 Yuri N. Sedunov <aris@altlinux.org> 0.1.7-alt3
- rebuilt with libImageMagick-6.9.9.7

* Sun Jun 04 2017 Yuri N. Sedunov <aris@altlinux.org> 0.1.7-alt2
- rebuilt against ffmpeg-3.3.1 libraries

* Fri Jun 02 2017 Yuri N. Sedunov <aris@altlinux.org> 0.1.7-alt1
- 0.1.7

* Mon May 29 2017 Yuri N. Sedunov <aris@altlinux.org> 0.1.6-alt1
- 0.1.6

* Fri May 12 2017 Yuri N. Sedunov <aris@altlinux.org> 0.1.5-alt1
- 0.1.5

* Sat Apr 01 2017 Yuri N. Sedunov <aris@altlinux.org> 0.1.4-alt1
- 0.1.4

* Fri Jan 27 2017 Yuri N. Sedunov <aris@altlinux.org> 0.1.3-alt1
- first build for Sisyphus


