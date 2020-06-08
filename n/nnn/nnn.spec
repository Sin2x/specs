Name: nnn
Version: 3.2
Release: alt1

Summary: A full-featured terminal file manager.
License: BSD-2-Clause and BSD-3-Clause
Group: Editors

Packager: Andrew A. Vasilyev <andy@altlinux.org>

Source: %name-%version.tar
Patch: %name-%version.patch

BuildRequires(pre): rpm-build-licenses
BuildRequires: libreadline-devel libncurses-devel libncursesw-devel

%description
nnn (or n^3) is a full-featured terminal file manager. It's tiny and nearly 0-config with an incredible performance.

%prep
%setup
%patch -p1

%build
%make_build

%install
%make_install DESTDIR=%buildroot PREFIX=/usr install

%files
%doc LICENSE README.md
%_bindir/*
%_man1dir/*

%changelog
* Mon Jun 08 2020 Andrew A. Vasilyev <andy@altlinux.org> 3.2-alt1
- Initial build fot ALT.

