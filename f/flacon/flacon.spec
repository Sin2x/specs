Name: flacon
Version: 9.5.0
Release: alt1

Summary: Audio File Encoder
Summary(ru_RU.UTF-8): Конвертер аудиофайлов
Summary(uk_UA.UTF-8): Кодувальник аудіофайлів
License: LGPLv2.1
Group: Sound

Url: http://%name.github.io/
Packager: Nazarov Denis <nenderus@altlinux.org>

# https://github.com/%name/%name/archive/v%version/%name-%version.tar.gz
Source: %name-%version.tar

BuildRequires: cmake
BuildRequires: libtag-devel
BuildRequires: libuchardet-devel
BuildRequires: qt5-tools-devel

%ifnarch %arm ppc64le
Requires: alacenc
%endif
Requires: faac
Requires: flac
Requires: lame
Requires: mac
Requires: mp3gain
Requires: opus-tools
Requires: sox-base
Requires: ttaenc
Requires: vorbisgain
Requires: vorbis-tools
Requires: wavpack

Provides: %name-qt5 = %version
Obsoletes: %name-qt5

%description
Extracts audio tracks from audio CD image to separate tracks.

%description -l ru_RU.UTF-8
Извлекает аудио треки из CD образа WAV, FLAC, APE в отдельные файлы.

%description -l uk_UA.UTF-8
Витягує доріжки з образу аудіо-CD.

%prep
%setup

%build
%cmake
%cmake_build

%install
%cmake_install

%files
%doc LICENSE README.md
%_bindir/%name
%_desktopdir/%name.desktop
%_miconsdir/%name.png
%_liconsdir/%name.png
%_niconsdir/%name.png
%_iconsdir/hicolor/128x128/apps/%name.png
%_iconsdir/hicolor/256x256/apps/%name.png
%_iconsdir/hicolor/512x512/apps/%name.png
%_iconsdir/hicolor/64x64/apps/%name.png
%_iconsdir/hicolor/scalable/apps/%name.svg
%_datadir/%name
%_datadir/metainfo/com.github.Flacon.metainfo.xml
%_man1dir/%name.1.*

%changelog
* Fri Nov 18 2022 Nazarov Denis <nenderus@altlinux.org> 9.5.0-alt1
- Version 9.5.0

* Sun Oct 02 2022 Nazarov Denis <nenderus@altlinux.org> 9.4.0-alt1
- Version 9.4.0

* Sun Sep 25 2022 Nazarov Denis <nenderus@altlinux.org> 9.3.0-alt1
- Version 9.3.0

* Tue Aug 30 2022 Nazarov Denis <nenderus@altlinux.org> 9.2.0-alt1
- Version 9.2.0

* Mon May 16 2022 Nazarov Denis <nenderus@altlinux.org> 9.0.0-alt1.1
- Add require on alacenc except %arm and ppc64le (ALT #42737)

* Sat Apr 30 2022 Nazarov Denis <nenderus@altlinux.org> 9.0.0-alt1
- Version 9.0.0

* Wed Feb 02 2022 Nazarov Denis <nenderus@altlinux.org> 8.3.0-alt1
- Version 8.3.0

* Tue Dec 21 2021 Nazarov Denis <nenderus@altlinux.org> 8.2.0-alt1
- Version 8.2.0

* Fri Nov 26 2021 Nazarov Denis <nenderus@altlinux.org> 8.1.0-alt1
- Version 8.1.0

* Sun Nov 14 2021 Nazarov Denis <nenderus@altlinux.org> 8.0.0-alt1
- Version 8.0.0

* Sun Apr 25 2021 Nazarov Denis <nenderus@altlinux.org> 7.0.1-alt1
- Version 7.0.1

* Wed Mar 10 2021 Nazarov Denis <nenderus@altlinux.org> 6.1.0-alt2
- Fix build

* Fri Jun 26 2020 Nazarov Denis <nenderus@altlinux.org> 6.1.0-alt1
- Version 6.1.0

* Wed Jun 03 2020 Nazarov Denis <nenderus@altlinux.org> 6.0.0-alt2
- Add requires on all needs packages (ALT #38570)

* Sat May 30 2020 Nazarov Denis <nenderus@altlinux.org> 6.0.0-alt1
- Version 6.0.0

* Sat Oct 12 2019 Nazarov Denis <nenderus@altlinux.org> 5.5.1-alt1
- Version 5.5.1

* Wed May 01 2019 Nazarov Denis <nenderus@altlinux.org> 5.4.0-alt1
- Version 5.4.0

* Sun Apr 07 2019 Nazarov Denis <nenderus@altlinux.org> 5.2.0-alt1
- Version 5.2.0

* Wed Jan 30 2019 Nazarov Denis <nenderus@altlinux.org> 5.1.0-alt1
- Version 5.1.0

* Mon Jan 21 2019 Nazarov Denis <nenderus@altlinux.org> 5.0.0-alt2
- Add files in project

* Wed Jan 16 2019 Nazarov Denis <nenderus@altlinux.org> 5.0.0-alt1
- Version 5.0.0
  Remove %ubt macro

* Fri May 04 2018 Nazarov Denis <nenderus@altlinux.org> 4.1.0-alt1%ubt
- Version 4.1.0

* Fri Jan 05 2018 Nazarov Denis <nenderus@altlinux.org> 4.0.0-alt1%ubt
- Version 4.0.0

* Sun Sep 10 2017 Nazarov Denis <nenderus@altlinux.org> 3.1.1-alt1%ubt
- Version 3.1.1

* Sun Jul 30 2017 Nazarov Denis <nenderus@altlinux.org> 3.0.0-alt1%ubt
- Version 3.0.0

* Thu Jan 05 2017 Nazarov Denis <nenderus@altlinux.org> 2.1.1-alt0.M80P.1
- Build for branch p8

* Tue Jan 03 2017 Nazarov Denis <nenderus@altlinux.org> 2.1.1-alt1
- Versiob 2.1.1

* Sat Oct 08 2016 Nazarov Denis <nenderus@altlinux.org> 2.1.0-alt0.M70P.1
- Build for branch p7

* Sat Oct 08 2016 Nazarov Denis <nenderus@altlinux.org> 2.1.0-alt0.M70T.1
- Build for branch t7

* Thu Oct 06 2016 Nazarov Denis <nenderus@altlinux.org> 2.1.0-alt0.M80P.1
- Build for branch p8

* Wed Oct 05 2016 Nazarov Denis <nenderus@altlinux.org> 2.1.0-alt1
- Version 2.1.0

* Wed Feb 17 2016 Nazarov Denis <nenderus@altlinux.org> 2.0.1-alt0.M70P.1
- Build for branch p7

* Sun Feb 14 2016 Nazarov Denis <nenderus@altlinux.org> 2.0.1-alt0.M70T.1
- Build for branch t7

* Mon Feb 01 2016 Nazarov Denis <nenderus@altlinux.org> 2.0.1-alt1
- Version 2.0.1

* Sun Jan 24 2016 Nazarov Denis <nenderus@altlinux.org> 1.2.0-alt2
- Fix man file

* Wed Sep 23 2015 Nazarov Denis <nenderus@altlinux.org> 1.2.0-alt0.M70P.1
- Build for branch p7

* Sun Sep 20 2015 Nazarov Denis <nenderus@altlinux.org> 1.2.0-alt0.M70T.1
- Build for branch t7

* Sat Sep 19 2015 Nazarov Denis <nenderus@altlinux.org> 1.2.0-alt1
- Version 1.2.0

* Tue Sep 09 2014 Andrey Cherepanov <cas@altlinux.org> 1.0.1-alt0.M70P.1
- Backport new version to p7 branch (ALT #30297)

* Wed Aug 27 2014 Nazarov Denis <nenderus@altlinux.org> 1.0.1-alt0.M70T.1
- Build for branch t7

* Tue Aug 26 2014 Nazarov Denis <nenderus@altlinux.org> 1.0.1-alt1
- Version 1.0.1

* Wed Aug 06 2014 Nazarov Denis <nenderus@altlinux.org> 1.0.0-alt0.M70T.1
- Build for branch t7

* Tue Aug 05 2014 Nazarov Denis <nenderus@altlinux.org> 1.0.0-alt1
- Version 1.0.0

* Sun Mar 23 2014 Nazarov Denis <nenderus@altlinux.org> 0.9.4-alt0.M70T.1
- Build for branch t7

* Sun Mar 16 2014 Nazarov Denis <nenderus@altlinux.org> 0.9.4-alt1
- Version 0.9.4

* Thu Jan 16 2014 Nazarov Denis <nenderus@altlinux.org> 0.9.3-alt0.M70T.1
- Build for branch t7

* Thu Jan 16 2014 Nazarov Denis <nenderus@altlinux.org> 0.9.3-alt1
- Version 0.9.3

* Sun Oct 27 2013 Nazarov Denis <nenderus@altlinux.org> 0.9.2-alt0.M70P.1
- Build for branch p7

* Sun Oct 27 2013 Nazarov Denis <nenderus@altlinux.org> 0.9.2-alt0.M70T.1
- Build for branch t7

* Sun Oct 27 2013 Nazarov Denis <nenderus@altlinux.org> 0.9.2-alt1
- Version 0.9.2

* Thu Oct 17 2013 Nazarov Denis <nenderus@altlinux.org> 0.9.1-alt0.M60P.1
- Build for branch p6

* Wed Oct 16 2013 Nazarov Denis <nenderus@altlinux.org> 0.9.1-alt0.M60T.1
- Build for branch t6

* Wed Oct 16 2013 Nazarov Denis <nenderus@altlinux.org> 0.9.1-alt0.M70P.1
- Build for branch p7

* Tue Oct 15 2013 Nazarov Denis <nenderus@altlinux.org> 0.9.1-alt0.M70T.1
- Build for branch t7

* Tue Oct 15 2013 Nazarov Denis <nenderus@altlinux.org> 0.9.1-alt1
- Version 0.9.1 (ALT #29478)

* Sat May 25 2013 Nazarov Denis <nenderus@altlinux.org> 0.8.0-alt1
- Version 0.8.0

* Thu Aug 23 2012 Nazarov Denis <nenderus@altlinux.org> 0.7.2-alt0.M60P.1
- Build for branch p6

* Mon Aug 20 2012 Nazarov Denis <nenderus@altlinux.org> 0.7.2-alt0.M60T.1
- Build for branch t6

* Mon Aug 20 2012 Nazarov Denis <nenderus@altlinux.org> 0.7.2-alt1
- Version 0.7.2

* Wed Aug 08 2012 Nazarov Denis <nenderus@altlinux.org> 0.7.1-alt0.M60T.1
- Build for branch t6

* Wed Aug 08 2012 Nazarov Denis <nenderus@altlinux.org> 0.7.1-alt1
- Version 0.7.1

* Mon Feb 20 2012 Nazarov Denis <nenderus@altlinux.org> 0.6.1-alt0.M60T.1
- Build for branch t6

* Mon Feb 20 2012 Nazarov Denis <nenderus@altlinux.org> 0.6.1-alt1
- Version 0.6.1

* Sat Dec 10 2011 Nazarov Denis <nenderus@altlinux.org> 0.6.0-alt0.M60T.1
- Build for branch t6

* Sat Dec 10 2011 Nazarov Denis <nenderus@altlinux.org> 0.6.0-alt1
- Version 0.6.0

* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.5.7-alt1.1
- Rebuild with Python-2.7

* Fri May 27 2011 Nazarov Denis <nenderus@altlinux.org> 0.5.7-alt0.M60T.1
- Build for branch t6

* Mon May 09 2011 Nazarov Denis <nenderus@altlinux.org> 0.5.7-alt1
- Version 0.5.7

* Sun Feb 13 2011 Nazarov Denis <nenderus@altlinux.org> 0.5.6-alt0.M41.1
- Build for branch 4.1

* Sun Feb 13 2011 Nazarov Denis <nenderus@altlinux.org> 0.5.6-alt0.M51.1
- Build for branch 5.1

* Sun Feb 13 2011 Nazarov Denis <nenderus@altlinux.org> 0.5.6-alt1
- Version 0.5.6

* Fri Feb 11 2011 Nazarov Denis <nenderus@altlinux.org> 0.5.5-alt0.M51.1
- Build for branch 5.1

* Fri Feb 11 2011 Nazarov Denis <nenderus@altlinux.org> 0.5.5-alt1
- Version 0.5.5

* Sat Jan 29 2011 Nazarov Denis <nenderus@altlinux.org> 0.5.4-alt0.M51.1
- Build for branch 5.1

* Sat Jan 29 2011 Nazarov Denis <nenderus@altlinux.org> 0.5.4-alt1
- Version 0.5.4

* Fri Nov 26 2010 Nazarov Denis <nenderus@altlinux.org> 0.5.3-alt0.M51.1
- Build for branch 5.1

* Fri Nov 26 2010 Nazarov Denis <nenderus@altlinux.org> 0.5.3-alt1
- Version 0.5.3

* Sun Oct 31 2010 Nazarov Denis <nenderus@altlinux.org> 0.5.2-alt0.M51.1
- Build for branch 5.1

* Fri Oct 29 2010 Nazarov Denis <nenderus@altlinux.org> 0.5.2-alt1
- Version 0.5.2

* Wed Oct 20 2010 Motsyo Gennadi <drool@altlinux.ru> 0.5.1-alt0.M41.1
- build for M41

* Tue Oct 19 2010 Nazarov Denis <nenderus@altlinux.org> 0.5.1-alt0.M51.1
- Build for branch 5.1

* Mon Oct 18 2010 Nazarov Denis <nenderus@altlinux.org> 0.5.1-alt1
- Version 0.5.1

* Mon Oct 04 2010 Nazarov Denis <nenderus@altlinux.org> 0.5-alt0.M51.1
- Build for branch 5.1

* Mon Oct 04 2010 Nazarov Denis <nenderus@altlinux.org> 0.5-alt1
- Version 0.5

* Thu Aug 19 2010 Nazarov Denis <nenderus@altlinux.org> 0.4.7-alt0.M51.1
- Build for branch 5.1

* Thu Aug 19 2010 Nazarov Denis <nenderus@altlinux.org> 0.4.7-alt1
- Version 0.4.7

* Sun Aug 08 2010 Nazarov Denis <nenderus@altlinux.org> 0.4.5-alt0.M51.1
- Build for branch 5.1

* Sun Aug 08 2010 Nazarov Denis <nenderus@altlinux.org> 0.4.5-alt1
- Version 0.4.5

* Sun Aug 01 2010 Nazarov Denis <nenderus@altlinux.org> 0.4.4-alt0.M51.1
- Build for branch 5.1

* Sun Aug 01 2010 Nazarov Denis <nenderus@altlinux.org> 0.4.4-alt1
- Version 0.4.4

* Sat Jul 24 2010 Nazarov Denis <nenderus@altlinux.org> 0.4.3-alt0.M51.1
- Build for branch 5.1

* Sat Jul 24 2010 Nazarov Denis <nenderus@altlinux.org> 0.4.3-alt1
- Version 0.4.3

* Sun Jun 13 2010 Nazarov Denis <nenderus@altlinux.org> 0.4.2-alt0.M51.1
- Build for branch 5.1

* Sun Jun 13 2010 Nazarov Denis <nenderus@altlinux.org> 0.4.2-alt1
- Version 0.4.2

* Mon May 31 2010 Nazarov Denis <nenderus@altlinux.org> 0.4.1-alt0.M51.1
- Build for branch 5.1

* Mon May 31 2010 Nazarov Denis <nenderus@altlinux.org> 0.4.1-alt1
- Version 0.4.1

* Fri May 28 2010 Nazarov Denis <nenderus@altlinux.org> 0.4-alt0.M51.1
- Build for branch 5.1

* Fri May 28 2010 Nazarov Denis <nenderus@altlinux.org> 0.4-alt1
- Version 0.4

* Wed May 12 2010 Nazarov Denis <nenderus@altlinux.org> 0.3.1-alt1.M51.3
- Build for branch 5.1

* Fri Apr 30 2010 Nazarov Denis <nenderus@altlinux.org> 0.3.1-alt2.2
- Fix desktop-file

* Tue Apr 27 2010 Nazarov Denis <nenderus@altlinux.org> 0.3.1-alt1.M51.2
- Build for branch 5.1

* Tue Apr 27 2010 Nazarov Denis <nenderus@altlinux.org> 0.3.1-alt2.1
- Cleanup spec-file

* Mon Apr 26 2010 Nazarov Denis <nenderus@altlinux.org> 0.3.1-alt1.M51.1
- First build for branch 5.1

* Mon Apr 12 2010 Nazarov Denis <nenderus@altlinux.org> 0.3.1-alt2
- Fix requires, buildarch and icons

* Fri Apr 9 2010 Nazarov Denis <nenderus@altlinux.org> 0.3.1-alt1
- First build for ALT Linux 5.0 (p5)
