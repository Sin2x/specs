Name:    variety
Version: 0.8.9
Release: alt1

Summary: Wallpaper downloader and manager for Linux systems
License: GPL-3.0
Group:   Other
URL:     https://github.com/varietywalls/variety

Packager: Andrey Cherepanov <cas@altlinux.org>

BuildRequires(pre): rpm-build-python3
BuildRequires(pre): rpm-build-gir
BuildRequires: python3-dev
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-distutils-extra
BuildRequires: python3-module-httplib2
BuildRequires: python3-module-requests
BuildRequires: python3-module-dbus
BuildRequires: python3-module-Pillow
BuildRequires: python3-module-pygobject3-devel
BuildRequires: python3-module-configobj
BuildRequires: python3-module-pycairo-devel
BuildRequires: libgtk+3-gir-devel
BuildRequires: libgexiv2-gir-devel
BuildRequires: libnotify-gir-devel
BuildRequires: libappindicator-gtk3-gir-devel
BuildRequires: intltool

BuildArch: noarch

Source:  %name-%version.tar

# Need for download and convert wallpapers
Requires: python3-module-gexiv2
Requires: python3-module-pycurl

%filter_from_requires /^typelib(AyatanaAppIndicator3)/d
%add_findreq_skiplist %_datadir/%name/scripts/*

%description
Variety is a wallpaper manager for Linux systems. It supports numerous desktops
and wallpaper sources, including local files and online services: Flickr,
Wallhaven, Unsplash, and more.

Where supported, Variety sits as a tray icon to allow easy pausing and
resuming. Otherwise, its desktop entry menu provides a similar set of options.

Variety also includes a range of image effects, such as oil painting and blur,
as well as options to layer quotes and a clock onto the background.

%prep
%setup -n %name-%version
echo "__variety_data_directory__ = \"%_datadir/%name\"" > variety_lib/variety_build_settings.py

%build
%python3_build

%install
%python3_install
rm -f %buildroot%_defaultdocdir/%name/README.md

# Install icons and desktop file
install -Dpm0644 build/share/applications/variety.desktop %buildroot%_desktopdir/%name.desktop
for s in 16 24 32 48 64 128 256;do \
    install -Dpm0644 data/media/variety${s}.png %buildroot%_iconsdir/hicolor/${s}x${s}/apps/%name.png; \
done
install -Dpm0644 data/media/variety.svg %buildroot%_iconsdir/hicolor/scalable/apps/%name.svg

# Install localization files
mkdir -p %buildroot%_datadir/locale
cp -av build/mo/* %buildroot%_datadir/locale
%find_lang %name

%files -f %name.lang
%doc AUTHORS README.md
%_bindir/%name
%python3_sitelibdir/jumble
%python3_sitelibdir/%name
%python3_sitelibdir/variety_lib
%python3_sitelibdir/*.egg-info
%_datadir/%name
%_datadir/metainfo/%name.appdata.xml
%_desktopdir/%name.desktop
%_iconsdir/hicolor/*/apps/%name.png
%_iconsdir/hicolor/scalable/apps/%name.svg

%changelog
* Thu Jun 23 2022 Andrey Cherepanov <cas@altlinux.org> 0.8.9-alt1
- New version.

* Sat Jun 18 2022 Andrey Cherepanov <cas@altlinux.org> 0.8.8-alt1
- New version.

* Mon May 02 2022 Andrey Cherepanov <cas@altlinux.org> 0.8.7-alt1
- New version.

* Mon Apr 25 2022 Andrey Cherepanov <cas@altlinux.org> 0.8.6-alt1
- New version.

* Thu May 20 2021 Andrey Cherepanov <cas@altlinux.org> 0.8.5-alt2
- Add icons, desktop file and localization files.

* Wed May 19 2021 Andrey Cherepanov <cas@altlinux.org> 0.8.5-alt1
- Initial build for Sisyphus
