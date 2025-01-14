%def_disable clang

Name: dtkgui
Version: 5.6.0.2
Release: alt1
Summary: Deepin Toolkit, gui module for DDE look and feel
License: LGPL-3.0
Group: Graphical desktop/Other
Url: https://github.com/linuxdeepin/dtkgui
Packager: Leontiy Volodin <lvol@altlinux.org>

Source: %url/archive/%version/%name-%version.tar.gz
Patch: dtkgui-5.5.17.1-alt-fix-build-ppc64le.patch

%if_enabled clang
BuildRequires(pre): clang-devel
%endif
BuildRequires(pre): rpm-build-ninja
BuildRequires: cmake dtk5-core-devel dtk5-common librsvg-devel libgtest-devel libgmock-devel libqtxdg-devel

%description
Deepin Toolkit, gui module for DDE look and feel.

%package -n libdtk5-gui
Summary: Library for %name
Group: Graphical desktop/Other

%description -n libdtk5-gui
DtkGui is used for DDE look and feel.
This package contains the shared libraries.

%package -n dtk5-gui-devel
Summary: Development package for %name
Group: Graphical desktop/Other

%description -n dtk5-gui-devel
Header files and libraries for %name.

%prep
%setup
# %%ifarch ppc64le
# %%patch -p1
# %%endif
sed -i '/*build-*/d' .gitignore
%if_disabled clang
# fix: XdgIcon crashed in release mode
# 0abaada3ce3a17ccd8f4417321cabe300eed9e37
sed -i 's|XdgIconLoader::instance()->followColorScheme();|return XdgIconLoader::instance()->followColorScheme();|' \
  src/util/private/xdgiconproxyengine.cpp
%endif

%build
%if_enabled clang
export CC="clang"
export CXX="clang++"
export AR="llvm-ar"
export NM="llvm-nm"
export READELF="llvm-readelf"
%endif
export PATH=%_qt5_bindir:$PATH
%cmake \
  -GNinja \
  -DCMAKE_BUILD_TYPE=RelWithDebInfo \
  -DMKSPECS_INSTALL_DIR=%_qt5_archdatadir/mkspecs/modules/ \
  -DCMAKE_INSTALL_LIBDIR=%_libdir \
  -DDTK_VERSION=%version \
  -DVERSION=%version \
  -DLIB_INSTALL_DIR=%_libdir \
  -DBUILD_DOCS=OFF \
#
cmake --build %_cmake__builddir -j%__nprocs

%install
%cmake_install

%files -n libdtk5-gui
%doc README.md
%doc LICENSE
%_libdir/libdtkgui.so.5*
%dir %_libdir/libdtk-5*/
%_libdir/libdtk-5*/DGui/

%files -n dtk5-gui-devel
%_includedir/libdtk-5*/
%_qt5_archdatadir/mkspecs/modules/qt_lib_dtkgui.pri
%dir %_libdir/cmake/DtkGui/
%_libdir/cmake/DtkGui/DtkGuiConfig.cmake
%_pkgconfigdir/dtkgui.pc
%_libdir/libdtkgui.so

%changelog
* Mon Oct 17 2022 Leontiy Volodin <lvol@altlinux.org> 5.6.0.2-alt1
- New version.
- Upstream:
  + use cmake instead qmake.

* Wed Jun 08 2022 Leontiy Volodin <lvol@altlinux.org> 5.5.24-alt1
- New version.
- Upstream:
  + fix: use detected pkg-config to fix cross build.
  + fix: the problem of failure to start again when repairing
  anomalies withdraws.
  + fix: modify the color value of TextWarning under the dark mode.
  + fix: dcc can't start after calling setSingleInstance again.

* Fri Apr 08 2022 Leontiy Volodin <lvol@altlinux.org> 5.5.22-alt1
- New version (5.5.22).

* Tue Feb 08 2022 Leontiy Volodin <lvol@altlinux.org> 5.5.21-alt1
- New version (5.5.21).

* Mon Jul 12 2021 Leontiy Volodin <lvol@altlinux.org> 5.5.17.1-alt1
- New version (5.5.17.1).

* Mon Jun 28 2021 Leontiy Volodin <lvol@altlinux.org> 5.5.2-alt1
- New version (5.5.2) with rpmgs script.

* Thu Apr 08 2021 Leontiy Volodin <lvol@altlinux.org> 5.4.13-alt1
- New version (5.4.13) with rpmgs script.

* Tue Mar 09 2021 Leontiy Volodin <lvol@altlinux.org> 5.4.10-alt1
- New version (5.4.10) with rpmgs script.

* Thu Dec 03 2020 Leontiy Volodin <lvol@altlinux.org> 5.4.0-alt1
- New version (5.4.0) with rpmgs script.

* Wed Oct 28 2020 Leontiy Volodin <lvol@altlinux.org> 5.2.2.18-alt1
- New version (5.2.2.18) with rpmgs script.

* Mon Oct 05 2020 Leontiy Volodin <lvol@altlinux.org> 5.2.2.15-alt1
- New version (5.2.2.15) with rpmgs script.

* Wed Jul 29 2020 Leontiy Volodin <lvol@altlinux.org> 5.2.2.1-alt1
- Initial build for ALT Sisyphus.
