Group: Graphical desktop/Other
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-cmake rpm-macros-fedora-compat
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%define autorelease 2

%global __provides_exclude_from ^%{_libdir}/fcitx5/.*\\.so$

Name:       fcitx5-hangul
Version:    5.0.10
Release:    alt1_%autorelease
Summary:    Hangul Wrapper for Fcitx5
# data/symbol.txt is licensed under BSE license
License:    LGPLv2+ and BSD
URL:        https://github.com/fcitx/fcitx5-hangul
Source:     https://download.fcitx-im.org/fcitx5/%{name}/%{name}-%{version}.tar.xz
Source1:    https://download.fcitx-im.org/fcitx5/%{name}/%{name}-%{version}.tar.xz.sig
Source2:    https://pgp.key-server.io/download/0x8E8B898CBF2412F9

BuildRequires:  gnupg2
BuildRequires:  ctest cmake
BuildRequires:  extra-cmake-modules
BuildRequires:  gcc-c++
BuildRequires:  ninja-build python3-module-ninja_syntax
BuildRequires:  cmake(Fcitx5Core)
BuildRequires:  pkgconfig(libhangul) >= 0.0.12
BuildRequires:  gettext gettext-tools
BuildRequires:  /usr/bin/appstream-util
Requires:       icon-theme-hicolor
Requires:       fcitx5-data
Source44: import.info

%description
%{summary}.

%prep
%setup -q


%build
%{fedora_v2_cmake} -GNinja
%fedora_v2_cmake_build

%install
%fedora_v2_cmake_install

# convert symlinked icons to copied icons, this will help co-existing with
# fcitx4
for iconfile in $(find %{buildroot}%{_datadir}/icons -type l)
do
  origicon=$(readlink -f ${iconfile})
  rm -f ${iconfile}
  cp ${origicon} ${iconfile}
done 
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.metainfo.xml
%find_lang %{name}

%files -f %{name}.lang
%doc --no-dereference LICENSES/LGPL-2.1-or-later.txt
%doc README.md 
%{_libdir}/fcitx5/hangul.so
%{_datadir}/fcitx5/addon/hangul.conf
%{_datadir}/fcitx5/hangul
%{_datadir}/fcitx5/inputmethod/hangul.conf
%{_datadir}/icons/hicolor/*/apps/*.png
%{_metainfodir}/org.fcitx.Fcitx5.Addon.Hangul.metainfo.xml

%changelog
* Fri Sep 16 2022 Igor Vlasenko <viy@altlinux.org> 5.0.10-alt1_2
- new version

