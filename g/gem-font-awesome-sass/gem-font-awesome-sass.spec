%define        gemname font-awesome-sass

Name:          gem-font-awesome-sass
Version:       5.15.1
Release:       alt1
Summary:       Font-Awesome SASS gem for use in Ruby projects
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/FortAwesome/font-awesome-sass
Vcs:           https://github.com/fortawesome/font-awesome-sass.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(sassc) >= 1.11
BuildRequires: gem(bundler) >= 1.3 gem(bundler) < 3
BuildRequires: gem(compass) >= 0
BuildRequires: gem(rake) >= 0

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency bundler >= 2.1.4,bundler < 3
Requires:      gem(sassc) >= 1.11
Provides:      gem(font-awesome-sass) = 5.15.1


%description
'font-awesome-sass' is a Sass-powered version of FontAwesome for your Ruby
projects and plays nicely with Ruby on Rails, Compass, Sprockets,
etc.

Refactored to support more Ruby environments with code and documentation humbly
used from the excellent bootstrap-sass project by the Bootstrap team.


%package       -n gem-font-awesome-sass-doc
Version:       5.15.1
Release:       alt1
Summary:       Font-Awesome SASS gem for use in Ruby projects documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета font-awesome-sass
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(font-awesome-sass) = 5.15.1

%description   -n gem-font-awesome-sass-doc
Font-Awesome SASS gem for use in Ruby projects documentation
files.

'font-awesome-sass' is a Sass-powered version of FontAwesome for your Ruby
projects and plays nicely with Ruby on Rails, Compass, Sprockets,
etc.

Refactored to support more Ruby environments with code and documentation humbly
used from the excellent bootstrap-sass project by the Bootstrap team.

%description   -n gem-font-awesome-sass-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета font-awesome-sass.


%package       -n gem-font-awesome-sass-devel
Version:       5.15.1
Release:       alt1
Summary:       Font-Awesome SASS gem for use in Ruby projects development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета font-awesome-sass
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(font-awesome-sass) = 5.15.1
Requires:      gem(bundler) >= 1.3 gem(bundler) < 3
Requires:      gem(compass) >= 0
Requires:      gem(rake) >= 0

%description   -n gem-font-awesome-sass-devel
Font-Awesome SASS gem for use in Ruby projects development
package.

'font-awesome-sass' is a Sass-powered version of FontAwesome for your Ruby
projects and plays nicely with Ruby on Rails, Compass, Sprockets,
etc.

Refactored to support more Ruby environments with code and documentation humbly
used from the excellent bootstrap-sass project by the Bootstrap team.

%description   -n gem-font-awesome-sass-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета font-awesome-sass.


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

%files         -n gem-font-awesome-sass-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-font-awesome-sass-devel
%doc README.md


%changelog
* Thu Sep 02 2021 Pavel Skrylev <majioa@altlinux.org> 5.15.1-alt1
- ^ 5.11.2 -> 5.15.1

* Thu Sep 26 2019 Pavel Skrylev <majioa@altlinux.org> 5.11.2-alt1
- update (^) 5.8.1 -> 5.11.2
- fix (!) spec

* Thu Jun 06 2019 Pavel Skrylev <majioa@altlinux.org> 5.8.1-alt1
- Initial build for Sisyphus, packaged as a gem with usage Ruby Policy 2.0.
