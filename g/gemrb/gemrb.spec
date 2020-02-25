# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-mageia-compat
BuildRequires: gcc-c++ libSDL-devel perl(Digest/MD5.pm) python-devel
# END SourceDeps(oneline)
%filter_from_requires /^python...._\?GemRB./d
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%define _cmake_skip_rpath %{nil}

Name:          gemrb
Version:       0.8.5
Release:       alt3_1
Summary:       Port of the original Infinity (Game) Engine
Group:         Games/Adventure
License:       GPLv2+
URL:           http://www.gemrb.org
Source0:       http://downloads.sourceforge.net/gemrb/%{name}-%{version}.tar.gz

BuildRequires: ccmake cmake ctest
BuildRequires: pkgconfig(gl)
BuildRequires: pkgconfig(glew)
BuildRequires: pkgconfig(libpng)
BuildRequires: pkgconfig(libvlc)
BuildRequires: pkgconfig(openal)
BuildRequires: pkgconfig(python2)
BuildRequires: pkgconfig(sdl2)
BuildRequires: pkgconfig(SDL2_mixer)
BuildRequires: pkgconfig(SDL2_ttf)
BuildRequires: pkgconfig(vorbis)
BuildRequires: pkgconfig(zlib)
Source44: import.info

%description
GemRB (Game Engine Made with pre-Rendered Background) is a portable
open-source implementation of Bioware's Infinity Engine.

It was written to support pseudo-3D role playing games based on the
Dungeons & Dragons ruleset (Baldur's Gate and Icewind Dale series,
Planescape: Torment).

This is not a game, but the engine. You need data installed somewhere, and
point gemrb the the relevant directory. More details and a list of
supported games can be found at www.gemrb.org

%prep
%setup -q


%build
%{mageia_cmake} \
	-DCMAKE_SKIP_INSTALL_RPATH:BOOL=OFF -DCMAKE_SKIP_RPATH:BOOL=OFF \
	-DLAYOUT=fhs \
       -DLIB_DIR=%{_libdir}/%{name} \
       -DSDL_BACKEND=SDL2 \
       -DOPENGL_BACKEND=OpenGL

%mageia_cmake_build

%install
%mageia_cmake_install

rm -f %{buildroot}%{_sysconfdir}/gemrb/GemRB.cfg.noinstall.sample
rm -f %{buildroot}%{_docdir}/%{name}/INSTALL

sed -i 1s,python,python2, %buildroot%_bindir/extend2da.py

%files
%doc AUTHORS COPYING NEWS README
%doc %{_docdir}/%{name}/en/
%{_bindir}/%{name}
%{_bindir}/extend2da.py
%{_datadir}/%{name}/
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png
%{_iconsdir}/hicolor/scalable/apps/%{name}.svg
%{_libdir}/%{name}/libgemrb_core.so*
%{_libdir}/%{name}/plugins/
%{_mandir}/man6/%{name}.6*
%{_sysconfdir}/%{name}/GemRB.cfg.sample


%changelog
* Tue Feb 25 2020 Igor Vlasenko <viy@altlinux.ru> 0.8.5-alt3_1
- fixed build

* Mon Jan 13 2020 Igor Vlasenko <viy@altlinux.ru> 0.8.5-alt2_1
- fixed build

* Tue Sep 18 2018 Igor Vlasenko <viy@altlinux.ru> 0.8.5-alt1_1
- update by mgaimport

* Thu Feb 22 2018 Igor Vlasenko <viy@altlinux.ru> 0.8.4-alt2_3
- mga update

* Sat Nov 25 2017 Igor Vlasenko <viy@altlinux.ru> 0.8.4-alt2_2
- fixed build

* Fri Dec 16 2016 Igor Vlasenko <viy@altlinux.ru> 0.8.4-alt2_1
- to Sisyphus

* Mon Jun 13 2016 Igor Vlasenko <viy@altlinux.ru> 0.8.4-alt1_1
- converted for ALT Linux by srpmconvert tools

