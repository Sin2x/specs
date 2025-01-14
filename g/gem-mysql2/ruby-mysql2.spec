%define        gemname mysql2

Name:          gem-mysql2
Version:       0.5.4.2
Release:       alt0.1
Summary:       A modern, simple and very fast Mysql library for Ruby - binding to libmysql
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/brianmario/mysql2
Vcs:           https://github.com/brianmario/mysql2.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: libmysqlclient-devel

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency rake-compiler >= 1.1.2,rake-compiler < 2
%ruby_use_gem_dependency rake-compiler-dock >= 1.2.1,rake-compiler-dock < 2
Obsoletes:     ruby-mysql2 < %EVR
Provides:      ruby-mysql2 = %EVR
Provides:      gem(mysql2) = 0.5.4.2

%ruby_use_gem_version mysql2:0.5.4.2

%description
The Mysql2 gem is meant to serve the extremely common use-case of connecting,
querying and iterating on results. Some database libraries out there serve as
direct 1:1 mappings of the already complex C APIs available. This one is
not.

It also forces the use of UTF-8 [or binary] for the connection [and all strings
in 1.9, unless Encoding.default_internal is set then it will convert from UTF-8
to that encoding] and uses encoding-aware MySQL API calls where it can.


%package       -n gem-mysql2-doc
Version:       0.5.4.2
Release:       alt0.1
Summary:       A modern, simple and very fast Mysql library for Ruby - binding to libmysql documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета mysql2
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(mysql2) = 0.5.4.2

%description   -n gem-mysql2-doc
A modern, simple and very fast Mysql library for Ruby - binding to libmysql
documentation files.

The Mysql2 gem is meant to serve the extremely common use-case of connecting,
querying and iterating on results. Some database libraries out there serve as
direct 1:1 mappings of the already complex C APIs available. This one is
not.

It also forces the use of UTF-8 [or binary] for the connection [and all strings
in 1.9, unless Encoding.default_internal is set then it will convert from UTF-8
to that encoding] and uses encoding-aware MySQL API calls where it can.

%description   -n gem-mysql2-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета mysql2.


%package       -n gem-mysql2-devel
Version:       0.5.4.2
Release:       alt0.1
Summary:       A modern, simple and very fast Mysql library for Ruby - binding to libmysql development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета mysql2
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(mysql2) = 0.5.4.2
Requires:      libmysqlclient-devel

%description   -n gem-mysql2-devel
A modern, simple and very fast Mysql library for Ruby - binding to libmysql
development package.

The Mysql2 gem is meant to serve the extremely common use-case of connecting,
querying and iterating on results. Some database libraries out there serve as
direct 1:1 mappings of the already complex C APIs available. This one is
not.

It also forces the use of UTF-8 [or binary] for the connection [and all strings
in 1.9, unless Encoding.default_internal is set then it will convert from UTF-8
to that encoding] and uses encoding-aware MySQL API calls where it can.

%description   -n gem-mysql2-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета mysql2.


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

%files         -n gem-mysql2-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-mysql2-devel
%doc README.md
%ruby_includedir/*


%changelog
* Wed Sep 21 2022 Pavel Skrylev <majioa@altlinux.org> 0.5.4.2-alt0.1
- ^ 0.5.4[1] -> 0.5.4[2]

* Fri Jul 01 2022 Pavel Skrylev <majioa@altlinux.org> 0.5.4.1-alt1
- ^ 0.5.4 -> 0.5.4[1]

* Wed May 18 2022 Pavel Skrylev <majioa@altlinux.org> 0.5.4-alt1
- ^ 0.5.3 -> 0.5.4

* Wed Apr 01 2020 Pavel Skrylev <majioa@altlinux.org> 0.5.3-alt1
- ^ 0.5.2 -> 0.5.3
- ! spec tags and syntax

* Tue Apr 16 2019 Pavel Skrylev <majioa@altlinux.org> 0.5.2-alt2
- > Ruby Policy 2.0

* Thu Jul 26 2018 Andrey Cherepanov <cas@altlinux.org> 0.5.2-alt1.1
- Rebuild with new Ruby autorequirements.

* Sun Jul 08 2018 Andrey Cherepanov <cas@altlinux.org> 0.5.2-alt1
- New version.
- Package as gem.

* Wed Apr 11 2018 Andrey Cherepanov <cas@altlinux.org> 0.5.1-alt1
- New version.

* Fri Mar 30 2018 Andrey Cherepanov <cas@altlinux.org> 0.5.0-alt1.1
- Rebuild with Ruby 2.5.1

* Wed Mar 21 2018 Andrey Cherepanov <cas@altlinux.org> 0.5.0-alt1
- New version.

* Tue Mar 13 2018 Andrey Cherepanov <cas@altlinux.org> 0.4.10-alt1.1
- Rebuild with Ruby 2.5.0

* Wed Nov 15 2017 Andrey Cherepanov <cas@altlinux.org> 0.4.10-alt1
- New version.

* Mon Sep 25 2017 Andrey Cherepanov <cas@altlinux.org> 0.4.9-alt1.2
- Rebuild with Ruby 2.4.2

* Tue Sep 05 2017 Andrey Cherepanov <cas@altlinux.org> 0.4.9-alt1.1
- Rebuild with Ruby 2.4.1

* Mon Aug 14 2017 Andrey Cherepanov <cas@altlinux.org> 0.4.9-alt1
- New version

* Tue Jul 11 2017 Andrey Cherepanov <cas@altlinux.org> 0.4.8-alt1
- New version

* Wed Jul 05 2017 Andrey Cherepanov <cas@altlinux.org> 0.4.7-alt1
- New version

* Thu May 04 2017 Andrey Cherepanov <cas@altlinux.org> 0.4.6-alt1
- New version

* Sat Mar 11 2017 Andrey Cherepanov <cas@altlinux.org> 0.4.5-alt2
- Rebuild with new %%ruby_sitearchdir location

* Wed Mar 08 2017 Andrey Cherepanov <cas@altlinux.org> 0.4.5-alt1
- New version

* Mon Sep 12 2016 Andrey Cherepanov <cas@altlinux.org> 0.4.4-alt2
- Rebuild with Ruby 2.3.1

* Fri Jun 03 2016 Andrey Cherepanov <cas@altlinux.org> 0.4.4-alt1
- New version

* Fri May 22 2015 Andrey Cherepanov <cas@altlinux.org> 0.3.18-alt1
- Initial build for ALT Linux
