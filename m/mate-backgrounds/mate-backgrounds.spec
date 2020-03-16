Name: mate-backgrounds
Version: 1.24.1
Release: alt1
Epoch: 1
Summary: MATE Desktop backgrounds
License: GPLv2+
Group: Graphical desktop/MATE
Url: http://mate-desktop.org/
Packager: Valery Inozemtsev <shrek@altlinux.ru>

Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildArch: noarch
BuildRequires: mate-common glib2-devel

%description
Backgrounds for MATE Desktop

%prep
%setup -q
%patch -p1

%build
%autoreconf
%configure

%make_build

%install
%make DESTDIR=%buildroot install

%find_lang %name --with-gnome --all-name

%files -f %name.lang
%doc AUTHORS COPYING README
%_datadir/mate-background-properties
%_datadir/backgrounds/mate

%changelog
* Mon Mar 16 2020 Valery Inozemtsev <shrek@altlinux.ru> 1:1.24.1-alt1
- 1.24.1

* Wed Feb 26 2020 Valery Inozemtsev <shrek@altlinux.ru> 1:1.24.0-alt1
- 1.24.0

* Wed Mar 06 2019 Valery Inozemtsev <shrek@altlinux.ru> 1:1.22.0-alt1
- 1.22.0

* Tue Mar 13 2018 Valery Inozemtsev <shrek@altlinux.ru> 1:1.20.0-alt1
- initial build from git.mate-desktop.org

* Mon Feb 19 2018 Vladimir D. Seleznev <vseleznv@altlinux.org> 1.20.0-alt1_1
- new fc release
