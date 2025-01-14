%define uname   MangoHud
%define srcname %uname-v%version-Source
%define srcpath %uname-v%version

Name: mangohud
Version: 0.6.8
Release: alt1

Summary: A Vulkan overlay layer for monitoring FPS, temperatures, CPU/GPU load and more
License: MIT
Group: Games/Arcade

Url: https://github.com/flightlessmango/MangoHud
# DFSG tarball excludes nonfree nvml.h
Source: https://github.com/flightlessmango/MangoHud/releases/download/v%version/%srcname-DFSG.tar.xz

BuildRequires: gcc-c++ cmake
BuildRequires: meson
BuildRequires: glslang libspdlog-devel
BuildRequires: pkgconfig(dbus-1)
BuildRequires: pkgconfig(gl)
BuildRequires: pkgconfig(vulkan)
BuildRequires: pkgconfig(x11)
BuildRequires: pkgconfig(libdrm)
BuildRequires: python3(mako)

%description
A Vulkan overlay layer for monitoring FPS, temperatures, CPU/GPU load and more.

To enable the MangoHud Vulkan overlay layer, set `MANGOHUD=1` in the shell,
or use the `mangohud` command to launch programs.
See '%_docdir/%name' for configuration details.
%ifarch %ix86 x86_64

The `goverlay` package provides a third-party GUI frontend for MangoHud.
%endif

%prep
%setup -n %srcpath

%build
%meson \
  -Dinclude_doc=true \
  -Duse_system_vulkan=enabled \
  -Duse_system_spdlog=enabled \
  -Dwith_nvml=disabled \
  -Dwith_xnvctrl=disabled
# NVML is nonfree, XNVCtrl is not packaged yet (but could be enabled if it is)

%meson_build

%install
%meson_install

%files
%doc README.md 
%doc LICENSE
%_bindir/%name
%_libdir/%name/
%_datadir/vulkan/implicit_layer.d/%uname.json
%_man1dir/%name.1*
%_datadir/icons/hicolor/scalable/*/*.svg
%_datadir/vulkan/implicit_layer.d/*Mango*.json
%_docdir/%name/%uname.conf.example
%_datadir/metainfo/*.metainfo.xml

%changelog
* Wed Aug 03 2022 Ilya Mashkin <oddity@altlinux.ru> 0.6.8-alt1
- 0.6.8

* Wed Oct 27 2021 Ilya Mashkin <oddity@altlinux.ru> 0.6.6-alt2
- 0.6.6-1

* Wed Oct 20 2021 Ilya Mashkin <oddity@altlinux.ru> 0.6.6-alt1
- 0.6.6

* Sat Aug 28 2021 Ilya Mashkin <oddity@altlinux.ru> 0.6.5-alt1
- 0.6.5

* Wed Apr 21 2021 Michael Shigorin <mike@altlinux.org> 0.6.1-alt1
- initial build for ALT Sisyphus (thx Mageia)

* Wed Dec 30 2020 akien <akien> 0.6.1-1.mga8
+ Revision: 1665672
- Version 0.6.1

* Fri Oct 23 2020 akien <akien> 0.5.1-1.mga8
+ Revision: 1638865
- Version 0.5.1
- Require vulkan-loader lib explicitly

* Thu Jun 11 2020 akien <akien> 0.4.1-1.mga8
+ Revision: 1592504
- Version 0.4.1

* Fri Feb 14 2020 akien <akien> 0.2.0-1.mga8
+ Revision: 1519991
- imported package mangohud

