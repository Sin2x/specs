%define        gemname iconv

Name:          gem-iconv
Version:       1.0.8.1
Release:       alt0.1
Summary:       iconv wrapper, used to be ext/iconv
License:       BSD-2-Clause or Ruby
Group:         Development/Ruby
Url:           https://github.com/nurse/iconv
Vcs:           https://github.com/ruby/iconv.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Obsoletes:     ruby-iconv < %EVR
Provides:      ruby-iconv = %EVR
Provides:      gem(iconv) = 1.0.8.1

%ruby_use_gem_version iconv:1.0.8.1

%description
Iconv is a wrapper class for the UNIX 95 iconv() function family, which
translates string between various encoding systems.


%package       -n gem-iconv-doc
Version:       1.0.8.1
Release:       alt0.1
Summary:       iconv wrapper, used to be ext/iconv documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета iconv
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(iconv) = 1.0.8.1

%description   -n gem-iconv-doc
iconv wrapper, used to be ext/iconv documentation files.

Iconv is a wrapper class for the UNIX 95 iconv() function family, which
translates string between various encoding systems.

%description   -n gem-iconv-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета iconv.


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
%ruby_gemextdir

%files         -n gem-iconv-doc
%doc README.md
%ruby_gemdocdir


%changelog
* Wed Sep 21 2022 Pavel Skrylev <majioa@altlinux.org> 1.0.8.1-alt0.1
- ^ 1.0.8 -> 1.0.8[1]

* Wed Apr 01 2020 Pavel Skrylev <majioa@altlinux.org> 1.0.8-alt2
- ! spec tags

* Tue Apr 16 2019 Pavel Skrylev <majioa@altlinux.org> 1.0.8-alt1
- > Ruby Policy 2.0
- ^ 1.0.5 -> 1.0.8

* Fri Mar 30 2018 Andrey Cherepanov <cas@altlinux.org> 1.0.5-alt1.2
- Rebuild with Ruby 2.5.1

* Tue Mar 13 2018 Andrey Cherepanov <cas@altlinux.org> 1.0.5-alt1.1
- Rebuild with Ruby 2.5.0

* Mon Dec 25 2017 Andrey Cherepanov <cas@altlinux.org> 1.0.5-alt1
- New version.

* Mon Sep 25 2017 Andrey Cherepanov <cas@altlinux.org> 1.0.4-alt2.2
- Rebuild with Ruby 2.4.2

* Tue Sep 05 2017 Andrey Cherepanov <cas@altlinux.org> 1.0.4-alt2.1
- Rebuild with Ruby 2.4.1

* Sat Mar 11 2017 Andrey Cherepanov <cas@altlinux.org> 1.0.4-alt2
- Rebuild with new %%ruby_sitearchdir location

* Fri Sep 23 2016 Andrey Cherepanov <cas@altlinux.org> 1.0.4-alt1
- new version 1.0.4

* Fri Mar 21 2014 Led <led@altlinux.ru> 1.0-alt1
- initial build
