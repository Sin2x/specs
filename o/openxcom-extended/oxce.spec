%define alias oxce
Name: openxcom-extended
Version: 7.0_2021.05.18
Release: alt1
Summary: OpenXcom Extended is an open-source clone of the original X-COM
License: GPLv3+
Group: Games/Strategy
Url: http://openxcom.org/

Source: https://github.com/SupSuper/OpenXcom/%name-%version.tar
Source2: openxcom16.png
Source3: openxcom32.png
Patch0: openxcom.desktop-to-oxce.patch
Patch1: openxcom-man6.patch

BuildRequires: cmake gcc-c++ libSDL_gfx-devel libSDL_image-devel libSDL_mixer-devel libyaml-cpp0-devel zlib-devel doxygen /usr/bin/git libGLU-devel libglvnd-devel pkgconfig(sdl)

# Recommends
Requires: zenity

%description
OpenXcom Extended (OXCE) is an open-source clone of the popular
UFO: Enemy Unknown (X-Com: UFO Defense in USA) videogame by Microprose,
licensed under the GPL and written in C++ / SDL.

OpenXcom Extended is a game engine required to run properly
some OpenXcom.org mods such as Pirates!, Area 51 or X-Files.

%prep
%setup -n %name-%version
%patch0
%patch1 -p1

sed -i 's,DATADIR}/openxcom",DATADIR}/%name",g' src/CMakeLists.txt

%build
cmake --debug-output -D CMAKE_INSTALL_PREFIX="/usr" -D CMAKE_CXX_FLAGS="%optflags" -D CMAKE_C_FLAGS="%optflags" CMakeLists.txt
%make_build VERBOSE=1


%install
%makeinstall_std

mv %buildroot%_desktopdir/{openxcom,%name}.desktop
sed -i s,openxcom,%name,g %buildroot%_desktopdir/%name.desktop

install -pm 644 -D %{SOURCE3} %buildroot%_niconsdir/%name.png
install -pm 644 -D %{SOURCE2} %buildroot%_miconsdir/%name.png
#rm -f %buildroot%_iconsdir/hicolor/*/apps/openxcom*
mv %buildroot%_liconsdir/{openxcom,%{name}}.png
mv %buildroot%_iconsdir/hicolor/128x128/apps/{openxcom,%{name}}.png
mv %buildroot%_iconsdir/hicolor/scalable/apps/{openxcom,%{name}}.svg
mv %buildroot%_bindir/{openxcom,%{name}}
ln -s %{name} %buildroot%_bindir/%alias
mv %buildroot%_man6dir/{openxcom.6,%{name}.6}

%files
%doc CHANGELOG.txt README.* LICENSE.txt
%_bindir/%name
%_bindir/%alias
%_datadir/%name
%_man6dir/*
%_iconsdir/hicolor/*/apps/%name.*
%_desktopdir/%name.desktop

%changelog
* Thu May 20 2021 Igor Vlasenko <viy@altlinux.org> 7.0_2021.05.18-alt1
- nightly 2021.05.18

* Wed Sep 02 2020 Igor Vlasenko <viy@altlinux.ru> 6.6_2020.09.01-alt1
- nightly 2020.09.01

