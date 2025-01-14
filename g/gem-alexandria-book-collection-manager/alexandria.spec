%define        gemname alexandria-book-collection-manager

Name:          gem-alexandria-book-collection-manager
Version:       0.7.9
Release:       alt1
Summary:       Alexandria is a GNOME application to help you manage your book collection
License:       GPL-2.0+
Group:         Development/Ruby
Url:           https://github.com/mvz/alexandria-book-collection-manager
Vcs:           https://github.com/mvz/alexandria-book-collection-manager.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires(pre): rpm-build-gnome
BuildRequires: GConf
BuildRequires: intltool
BuildRequires: libGConf2-devel
BuildRequires: gem(gettext) >= 3.1 gem(gettext) < 4
BuildRequires: gem(gstreamer) >= 3.5.0 gem(gstreamer) < 3.6
BuildRequires: gem(gtk3) >= 3.5.0 gem(gtk3) < 3.6
BuildRequires: gem(htmlentities) >= 4.3 gem(htmlentities) < 5
BuildRequires: gem(image_size) >= 3.0 gem(image_size) < 4
BuildRequires: gem(marc) >= 1.0 gem(marc) < 1.2
BuildRequires: gem(nokogiri) >= 1.11 gem(nokogiri) < 2
BuildRequires: gem(psych) >= 3.2 gem(psych) < 4.1
BuildRequires: gem(zoom) >= 0.5.0 gem(zoom) < 0.6
BuildRequires: gem(gnome_app_driver) >= 0.3.0 gem(gnome_app_driver) < 0.4
BuildRequires: gem(rake) >= 13.0 gem(rake) < 14
BuildRequires: gem(rspec) >= 3.0 gem(rspec) < 4
BuildRequires: gem(rubocop) >= 1.15.0 gem(rubocop) < 2
BuildRequires: gem(rubocop-i18n) >= 3.0 gem(rubocop-i18n) < 4
BuildRequires: gem(rubocop-performance) >= 1.11.3 gem(rubocop-performance) < 2
BuildRequires: gem(rubocop-rake) >= 0.6.0 gem(rubocop-rake) < 0.7
BuildRequires: gem(rubocop-rspec) >= 2.4.0 gem(rubocop-rspec) < 3
BuildRequires: gem(webmock) >= 3.9 gem(webmock) < 4

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      alexandria
Requires:      gem(gettext) >= 3.1 gem(gettext) < 4
Requires:      gem(gstreamer) >= 3.5.0 gem(gstreamer) < 3.6
Requires:      gem(gtk3) >= 3.5.0 gem(gtk3) < 3.6
Requires:      gem(htmlentities) >= 4.3 gem(htmlentities) < 5
Requires:      gem(image_size) >= 3.0 gem(image_size) < 4
Requires:      gem(marc) >= 1.0 gem(marc) < 1.2
Requires:      gem(nokogiri) >= 1.11 gem(nokogiri) < 2
Requires:      gem(psych) >= 3.2 gem(psych) < 4.1
Requires:      gem(zoom) >= 0.5.0 gem(zoom) < 0.6
Provides:      gem(alexandria-book-collection-manager) = 0.7.9


%description
Alexandria is a GNOME application to help you manage your book
collection.

Alexandria:
* retrieves book information from Amazon (including cover pictures)
* saves data using the YAML format
* features an HIG-compliant user interface
* shows books in different views (standard list or icons list).


%package       -n alexandria
Version:       0.7.9
Release:       alt1
Summary:       Alexandria is a GNOME application to help you manage your book collection executable(s)
Summary(ru_RU.UTF-8): Исполнямка для самоцвета alexandria-book-collection-manager
Group:         Books/Other
BuildArch:     noarch

Requires:      gem(alexandria-book-collection-manager) = 0.7.9
Requires:      /usr/bin/update-desktop-database
Requires:      /usr/sbin/update-menus
Requires:      GConf

%description   -n alexandria
Alexandria is a GNOME application to help you manage your book collection
executable(s).

%description   -n alexandria -l ru_RU.UTF-8
Исполнямка для самоцвета alexandria-book-collection-manager.


%package       -n gem-alexandria-book-collection-manager-doc
Version:       0.7.9
Release:       alt1
Summary:       Alexandria is a GNOME application to help you manage your book collection documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета alexandria-book-collection-manager
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(alexandria-book-collection-manager) = 0.7.9

%description   -n gem-alexandria-book-collection-manager-doc
Alexandria is a GNOME application to help you manage your book collection
documentation files.

%description   -n gem-alexandria-book-collection-manager-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета alexandria-book-collection-manager.


%package       -n gem-alexandria-book-collection-manager-devel
Version:       0.7.9
Release:       alt1
Summary:       Alexandria is a GNOME application to help you manage your book collection development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета alexandria-book-collection-manager
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(alexandria-book-collection-manager) = 0.7.9
Requires:      gem(gnome_app_driver) >= 0.3.0 gem(gnome_app_driver) < 0.4
Requires:      gem(rake) >= 13.0 gem(rake) < 14
Requires:      gem(rspec) >= 3.0 gem(rspec) < 4
Requires:      gem(rubocop) >= 1.15.0 gem(rubocop) < 2
Requires:      gem(rubocop-i18n) >= 3.0.0 gem(rubocop-i18n) < 4
Requires:      gem(rubocop-performance) >= 1.11.3 gem(rubocop-performance) < 2
Requires:      gem(rubocop-rake) >= 0.6.0 gem(rubocop-rake) < 0.7
Requires:      gem(rubocop-rspec) >= 2.4.0 gem(rubocop-rspec) < 3
Requires:      gem(webmock) >= 3.9 gem(webmock) < 4

%description   -n gem-alexandria-book-collection-manager-devel
Alexandria is a GNOME application to help you manage your book collection
development package.

%description   -n gem-alexandria-book-collection-manager-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета alexandria-book-collection-manager.


%prep
%setup

%build
%ruby_build

%install
%ruby_install

%check
%ruby_test

%files
%doc README.md
%ruby_gemspec
%ruby_gemlibdir

%files         -n alexandria
%doc README.md
%_bindir/alexandria

%files         -n gem-alexandria-book-collection-manager-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-alexandria-book-collection-manager-devel
%doc README.md


%changelog
* Fri Mar 11 2022 Pavel Skrylev <majioa@altlinux.org> 0.7.9-alt1
- ^ 0.7.8 -> 0.7.9

* Thu Jul 01 2021 Pavel Skrylev <majioa@altlinux.org> 0.7.8-alt1
- ^ 0.7.7 -> 0.7.8

* Sun Nov 22 2020 Pavel Skrylev <majioa@altlinux.org> 0.7.7-alt1
- ^ 0.7.5 -> 0.7.7

* Mon May 25 2020 Pavel Skrylev <majioa@altlinux.org> 0.7.5-alt1
- ^ 0.7.4 -> 0.7.5
- ! spec syntax
- lost require deps to post script executables

* Wed Mar 04 2020 Pavel Skrylev <majioa@altlinux.org> 0.7.4-alt1
- updated (^) 0.7.3 -> 0.7.4
- fixed (!) spec

* Tue Sep 10 2019 Pavel Skrylev <majioa@altlinux.org> 0.7.3-alt4.1
- fixed (!) spec according to changelog rules, plus some others

* Mon Sep 02 2019 Pavel Skrylev <majioa@altlinux.org> 0.7.3-alt4
- fixed (!) spec

* Wed Apr 03 2019 Pavel Skrylev <majioa@altlinux.org> 0.7.3-alt3
- cleanup spec

* Fri Mar 22 2019 Pavel Skrylev <majioa@altlinux.org> 0.7.3-alt2
- Use setup's dependency detection

* Thu Feb 28 2019 Pavel Skrylev <majioa@altlinux.org> 0.7.3-alt1
- Bump to 0.7.3;
- Use Ruby Policy 2.0.

* Mon May 11 2009 Alexey I. Froloff <raorn@altlinux.org> 0.6.4.1-alt1
- [0.6.4.1]
- Removed all web-based providers (due to missing hpricot)
- Enabled Z39.50 provider (zoom and marc are now available)

* Thu May 29 2008 Vitaly Lipatov <lav@altlinux.ru> 0.6.3-alt2
- fix build, use rake_install macros
- remove unsupported providers (due missed hpricot, marc, zoom modules)

* Thu May 29 2008 Vitaly Lipatov <lav@altlinux.ru> 0.6.3-alt1
- new version 0.6.3 (with rpmrb script)
- note: rake_build/rake_install macroses is broken now

* Wed Jan 16 2008 Vitaly Lipatov <lav@altlinux.ru> 0.6.2-alt2
- remove rubygems requires
- use new rpm-build-ruby

* Tue Jan 08 2008 Vitaly Lipatov <lav@altlinux.ru> 0.6.2-alt1
- new version 0.6.2 (with rpmrb script)

* Sun Sep 10 2006 Vitaly Lipatov <lav@altlinux.ru> 0.6.1-alt0.3
- fix requires
- remove debian menu

* Tue May 23 2006 Vitaly Lipatov <lav@altlinux.ru> 0.6.1-alt0.2
- spec cleanup
- fix requires (bug #9601)

* Sun Oct 16 2005 Vitaly Lipatov <lav@altlinux.ru> 0.6.1-alt0.1
- new version
- add require for ruby-gettext
- still some broken code

* Tue Sep 13 2005 Vitaly Lipatov <lav@altlinux.ru> 0.6.0-alt0.2
- fix scrollkeeper install

* Sat Sep 10 2005 Vitaly Lipatov <lav@altlinux.ru> 0.6.0-alt0.1
- new version

* Wed Aug 24 2005 Vitaly Lipatov <lav@altlinux.ru> 0.5.1-alt0.1
- new version. Ruby hackers, please check this app

* Sat Dec 18 2004 Vitaly Lipatov <lav@altlinux.ru> 0.4.0-alt1
- first build for ALT Linux Sisyphus
