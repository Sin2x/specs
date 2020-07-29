Name: kmscube
Version: 0.0.20200331
Release: alt1

Summary: Bare metal graphics demo using DRM/KMS 
License: X11
Group: Graphics
Url: https://gitlab.freedesktop.org/mesa/kmscube

Source: %name-%version.tar

BuildRequires: libdrm-devel libgbm-devel libEGL-devel libGLES-devel meson

%description
kmscube is a little demonstration program for how to drive bare metal graphics
without a compositor like X11, wayland or similar, using DRM/KMS (kernel mode
setting), GBM (graphics buffer manager) and EGL for rendering content using
OpenGL or OpenGL ES.

%prep
%setup

%build
%meson
%meson_build

%install
%meson_install

%files
%_bindir/kmscube
%_bindir/texturator

%changelog
* Wed Jul 29 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.0.20200331-alt1
- updated up to 4660a7d

* Tue Aug 06 2019 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.0.20190720-alt1
- updated up to f632b23

* Thu Dec 13 2018 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.0.20181211-alt1
- initial
