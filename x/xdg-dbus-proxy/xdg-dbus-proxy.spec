%define ver_major 0.1
%define _libexecdir %_prefix/libexec

%def_enable man
%def_enable check

Name: xdg-dbus-proxy
Version: %ver_major.4
Release: alt1

Summary: D-Bus connections proxy
Group: System/Kernel and hardware
License: LGPLv2.1+
Url: https://github.com/flatpak/%name

Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires(pre): rpm-macros-meson
BuildRequires: meson libgio-devel > 2.40
%{?_enable_man:BuildRequires: xsltproc docbook-style-xsl}
%{?_enable_check:BuildRequires: /proc dbus-tools-gui}

%description
%name is a filtering proxy for D-Bus connections. It was originally part
of the flatpak project, but it has been broken out as a standalone module
to facilitate using it in other contexts.

%prep
%setup
%patch -p1

%build
%meson %{?_disable_man:-Dman=disabled}
%meson_build

%install
%meson_install

%check
%__meson_test

%files
%_bindir/%name
%{?_enable_man:%_man1dir/%name.1.*}
%doc README.md NEWS


%changelog
* Thu May 12 2022 Yuri N. Sedunov <aris@altlinux.org> 0.1.4-alt1
- 0.1.4 (ported to Meson build system)

* Wed Mar 02 2022 Yuri N. Sedunov <aris@altlinux.org> 0.1.3-alt1
- updated to 0.1.3-6-gc38d44a

* Tue Sep 24 2019 Yuri N. Sedunov <aris@altlinux.org> 0.1.2-alt1
- 0.1.2
- removed obsolete patches

* Wed May 29 2019 Yuri N. Sedunov <aris@altlinux.org> 0.1.1-alt1
- first build for Sisyphus



