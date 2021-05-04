Name: zorin-desktop-themes
Version: 3.2.1
Release: alt1
Summary: Zorin OS desktop themes

License: GPL-2.0+
Group: Graphical desktop/GNOME
URL: https://github.com/ZorinOS/zorin-desktop-themes

Source: %name-%version.tar

BuildArch: noarch

#Requires: fonts-zorin-os-core
# +fonts-croscore-config-zorin-os - Map open-source Croscore fonts to MS fonts
# ?fonts-michroma-zorin-os - A rounded-square sans typeface
# +fonts-roboto-mono-zorin-os - Monospaced addition to the Roboto type family
# ?fonts-zorin-os-core - Zorin OS essential fonts

%description
The Zorin OS desktop theme provided in a variety of color combinations.

%define themes ZorinBlue-Dark ZorinBlue-Light ZorinGreen-Dark ZorinGreen-Light ZorinGrey-Dark ZorinGrey-Light ZorinOrange-Dark ZorinOrange-Light ZorinPurple-Dark ZorinPurple-Light ZorinRed-Dark ZorinRed-Light 

%{expand:%(\
    for theme in %{themes}; do \
        echo "%%package -n gtk-theme-$theme";\
        echo -e "Summary: $theme GTK+ theme\nGroup: Graphical desktop/GNOME";\
        echo "Requires: libgtk-engine-murrine";\
        echo "Requires: libgtk+2";\
        echo "Requires: fonts-ttf-google-roboto-mono";\
        echo "Requires: fonts-ttf-google-croscore-arimo";\
        echo "Requires: fonts-ttf-google-croscore-cousine";\
        echo "Requires: fonts-ttf-google-croscore-tinos";\
        if [ "$theme" == "Zorin-95" ]; then echo "Requires: icon-theme-Zorin"; else echo "Requires: icon-theme-$theme"; fi;\
        echo -e "%%description -n gtk-theme-$theme\n$theme GTK+ theme.\n";\
        echo -e "%%files -n gtk-theme-$theme\n%%_datadir/themes/$theme/\n";\
    done\
)}

%prep
%setup

%install
mkdir -p %buildroot%_datadir/themes
cp -a Zorin* %buildroot%_datadir/themes

%changelog
* Tue May 04 2021 Andrey Cherepanov <cas@altlinux.org> 3.2.1-alt1
- New version.

* Mon May 03 2021 Andrey Cherepanov <cas@altlinux.org> 3.2-alt1
- New version.
- Remove deprecated theme Zorin-95.

* Thu Sep 03 2020 Andrey Cherepanov <cas@altlinux.org> 2.1.5-alt1
- New version.

* Wed Apr 01 2020 Andrey Cherepanov <cas@altlinux.org> 2.1.3-alt1
- Initial build in Sisyphus.
