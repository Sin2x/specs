%def_enable snapshot

%define ver_major 0.4
%define beta %nil
%define pypi_name blueprintcompiler
%def_disable docs
%def_enable check

Name: blueprint-compiler
Version: %ver_major.0
Release: alt1%beta

Summary: A markup language for GTK user interface files
Group: Development/GNOME and GTK+
License: GPL-3.0
Url: https://gitlab.gnome.org/jwestman/blueprint-compiler

%if_disabled snapshot
Source: %url/-/archive/v%version/%name-%version%beta.tar.bz2
%else
Vcs: https://gitlab.gnome.org/jwestman/blueprint-compiler.git
Source: %name-%version%beta.tar
%endif

BuildArch: noarch

BuildRequires(pre): rpm-macros-meson rpm-build-python3 rpm-build-gir
BuildRequires: meson
%{?_enable_check:BuildRequires: python3-module-pygobject3}

%description
%summary
See also https://jwestman.pages.gitlab.gnome.org/blueprint-compiler/

%prep
%setup -n %name-%version%beta

%build
%meson \
    %{?_enable_docs:-Ddocs=true}
%nil
%meson_build

%install
%meson_install
%find_lang %name

%check
%__meson_test

%files -f %name.lang
%_bindir/%name
%python3_sitelibdir_noarch/%pypi_name/
%_datadir/pkgconfig/%name.pc
%doc NEWS* README*

%changelog
* Mon Oct 03 2022 Yuri N. Sedunov <aris@altlinux.org> 0.4.0-alt1
- first build for Sisyphus


