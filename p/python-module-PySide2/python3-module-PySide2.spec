Name: python-module-PySide2
Version: 5.15.0
Release: alt5

Summary: Python bindings for the Qt 5 cross-platform application and UI framework
Group: Development/Python
License: BSD-3-Clause and GPL-2.0 and GPL-3.0 and LGPL-3.0
URL: https://wiki.qt.io/Qt_for_Python

%filter_from_requires /python-base/d
%filter_from_requires /^python2.7(signature_bootstrap)/d

# Download from https://download.qt.io/official_releases/QtForPython/pyside2/PySide2-$version-src/
Source: pyside-setup-everywhere-src-%version.tar
Patch1: pyside2-link-with-python.patch

BuildRequires(pre): rpm-build-python
BuildRequires(pre): cmake
BuildRequires: gcc-c++
BuildRequires: clang-devel
BuildRequires: llvm-devel
BuildRequires: libxml2-devel
BuildRequires: libxslt-devel
BuildRequires: python-devel
BuildRequires: python-module-setuptools
BuildRequires: python-module-sphinx
BuildRequires: qt5-base-devel
BuildRequires: qt5-xmlpatterns-devel
BuildRequires: qt5-x11extras-devel
BuildRequires: qt5-charts-devel
BuildRequires: qt5-datavis3d-devel
BuildRequires: qt5-remoteobjects-devel
BuildRequires: qt5-script-devel
BuildRequires: qt5-multimedia-devel
BuildRequires: qt5-xmlpatterns-devel
BuildRequires: qt5-tools-devel
BuildRequires: qt5-multimedia-devel
BuildRequires: qt5-scxml-devel
BuildRequires: qt5-sensors-devel
BuildRequires: qt5-speech-devel
BuildRequires: qt5-svg-devel
BuildRequires: qt5-webengine-devel
BuildRequires: qt5-websockets-devel
BuildRequires: qt5-3d-devel
BuildRequires: qt5-tools-devel
BuildRequires: qt5-tools-devel-static
BuildRequires: qt5-scxml
BuildRequires: qt5-declarative-devel

%description
PySide2 is the official Python module from the Qt for Python project,
which provides access to the complete Qt 5.13+ framework.

The name Shiboken2 and PySide2 make reference to the Qt 5 compatibility,
since the previous versions (without the 2) refer to Qt 4.

%package devel
Summary: Development files related to %name
Group: Development/Python
Conflicts: python3-module-PySide2-devel

%description devel
%{summary}.

%package -n pyside2-tools-python2
Summary: PySide2 tools for the Qt 5 framework
Group: Development/Python
Conflicts: pyside2-tools
 
%description -n pyside2-tools-python2
PySide2 provides Python bindings for the Qt5 cross-platform application
and UI framework.

This package ships the following accompanying tools:
* pyside2-rcc - PySide2 resource compiler
* pyside2-uic - Python User Interface Compiler for PySide2
* pyside2-lupdate - update Qt Linguist translation files for PySide2

The name Shiboken2 and PySide2 make reference to the Qt 5 compatibility, since
the previous versions (without the 2) refer to Qt 4.

%package -n shiboken2-python2
Summary: Python/C++ bindings generator for PySide2
Group: Development/Python
Conflicts: shiboken2

%description -n shiboken2-python2
Shiboken is the Python binding generator that Qt for Python uses to create the
PySide module, in other words, is the system we use to expose the Qt C++ API to
Python.

The name Shiboken2 and PySide2 make reference to the Qt 5 compatibility, since
the previous versions (without the 2) refer to Qt 4.

%package -n python-module-shiboken2
Summary: Python/C++ bindings libraries for PySide2
Group: Development/Python

%description -n python-module-shiboken2
Shiboken is the Python binding generator that Qt for Python uses to create the
PySide module, in other words, is the system we use to expose the Qt C++ API to
Python.

The name Shiboken2 and PySide2 make reference to the Qt 5 compatibility, since
the previous versions (without the 2) refer to Qt 4.

%package -n python-module-shiboken2-devel
Summary: Python/C++ bindings helper module for PySide2
Group: Development/Python
Requires: shiboken2-python2
Requires: python-module-shiboken2
Conflicts: python3-module-shiboken2-devel
 
%description -n python-module-shiboken2-devel
Shiboken is the Python binding generator that Qt for Python uses to create the
PySide module, in other words, is the system we use to expose the Qt C++ API to
Python.

The name Shiboken2 and PySide2 make reference to the Qt 5 compatibility, since
the previous versions (without the 2) refer to Qt 4.

%prep
%setup -n pyside-setup-everywhere-src-%version
%patch1 -p2

%build
export CXX=g++
%cmake -DUSE_PYTHON_VERSION=2
%cmake_build

%install
%cmakeinstall_std

# Generate egg-info manually and install since we're performing a cmake build.
%__python setup.py egg_info
for name in PySide2 shiboken2 shiboken2_generator; do
  mkdir -p %buildroot%python_sitelibdir/$name-%version-py%_python_version.egg-info
  cp -p $name.egg-info/{PKG-INFO,not-zip-safe,top_level.txt} \
        %buildroot%python_sitelibdir/$name-%version-py%_python_version.egg-info/
done


# Remove pkgconfig files
rm -f %buildroot%_libdir/pkgconfig/*.pc

# Remove pkgconfig files
rm -f %buildroot%_libdir/pkgconfig/*.pc

%files
%doc README.md
%_libdir/libpyside2*.so.*
%python_sitelibdir/PySide2
%python_sitelibdir/PySide2*.egg-info

%files devel
%doc examples
%_datadir/PySide2/
%_includedir/PySide2/
%_libdir/libpyside2*.so
%_libdir/cmake/PySide2*

%files -n pyside2-tools-python2
%doc README.pyside2.md
%_bindir/pyside2-*
%_man1dir/pyside2-*
 
%files -n shiboken2-python2
%doc README.shiboken2-generator.md
%_bindir/shiboken2
 
%files -n python-module-shiboken2
%doc README.shiboken2.md
%_libdir/libshiboken2*.so.*
%python_sitelibdir/shiboken2/
%python_sitelibdir/shiboken2-*.egg-info/
 
%files -n python-module-shiboken2-devel
%doc README.shiboken2.md
%_includedir/shiboken2/
%_libdir/cmake/Shiboken2-%version/
%_libdir/libshiboken2*.so
%python_sitelibdir/shiboken2_generator/
%python_sitelibdir/shiboken2_generator-*.egg-info/

%changelog
* Fri Apr 02 2021 Grigory Ustinov <grenka@altlinux.org> 5.15.0-alt5
- Fixed BuildRequires

* Fri Feb 12 2021 Sergey V Turchin <zerg@altlinux.org> 5.15.0-alt4
- merge with p9

* Wed Feb 03 2021 Andrey Cherepanov <cas@altlinux.org> 5.15.0-alt3
- Remove pkgconfig files to prevent duplicate pkgconfig provides.

* Thu Jan 21 2021 Andrey Cherepanov <cas@altlinux.org> 5.12.6-alt1.1.p9
- FTBFS: build with llvm7.0.
- Remove pkgconfig files.

* Wed Sep 16 2020 Sergey V Turchin <zerg@altlinux.org> 5.15.0-alt2
- update requires

* Tue Aug 11 2020 Sergey V Turchin <zerg@altlinux.org> 5.15.0-alt1
- new version

* Thu May 14 2020 Andrey Cherepanov <cas@altlinux.org> 5.12.6-alt1
- Initial build in Sisyphus for Python2.
