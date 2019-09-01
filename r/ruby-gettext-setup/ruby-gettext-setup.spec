%define        pkgname gettext-setup
 
Name: 	       ruby-%pkgname
Version:       0.30
Release:       alt3
 
Summary:       A gem that configures gettext for internationalization
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/puppetlabs/gettext-setup-gem
%vcs           https://github.com/puppetlabs/gettext-setup-gem.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch
 
Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%gem_replace_version fast_gettext ~> 1.7

%description
This is a simple gem to set up i18n for Ruby projects (including Sinatra
web apps) using gettext and fast gettext.

This project sets the default locale to English. If the user has set a
different locale in their browser preferences, and we support the user's
preferred locale, strings and data formatting will be customized for
that locale.


%package       doc
Summary:       Documentation files for %gemname gem
Group:         Documentation
BuildArch:     noarch
 
%description   doc
Documentation files for %gemname gem.


%prep
%setup
 
%build
%ruby_build --use=%gemname --version-replace=%version
 
%install
%ruby_install

%check
%ruby_test
 
%files
%doc README*
%ruby_gemspec
%ruby_gemlibdir

%files         doc
%ruby_gemdocdir


%changelog
* Fri Jun 21 2019 Pavel Skrylev <majioa@altlinux.org> 0.30-alt3
- Use Ruby Policy 2.0

* Tue Sep 25 2018 Pavel Skrylev <majioa@altlinux.org> 0.30-alt2
- Update fastgettext to 1.7

* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 0.30-alt1.3
- Rebuild with new Ruby autorequirements.

* Fri Mar 30 2018 Andrey Cherepanov <cas@altlinux.org> 0.30-alt1.2
- Rebuild with Ruby 2.5.1

* Tue Mar 13 2018 Andrey Cherepanov <cas@altlinux.org> 0.30-alt1.1
- Rebuild with Ruby 2.5.0

* Tue Feb 13 2018 Andrey Cherepanov <cas@altlinux.org> 0.30-alt1
- New version.

* Sat Dec 02 2017 Andrey Cherepanov <cas@altlinux.org> 0.29-alt1
- New version.

* Tue Sep 26 2017 Andrey Cherepanov <cas@altlinux.org> 0.28-alt2
- Rebuild with Ruby 2.4.2

* Sat Sep 02 2017 Andrey Cherepanov <cas@altlinux.org> 0.28-alt1
- New version

* Wed Jul 12 2017 Andrey Cherepanov <cas@altlinux.org> 0.26-alt1
- New version

* Wed May 31 2017 Andrey Cherepanov <cas@altlinux.org> 0.25-alt1
- New version

* Fri Apr 21 2017 Andrey Cherepanov <cas@altlinux.org> 0.24-alt1
- New version
- Package gemspec
- Require dependencies from gemspec

* Thu Mar 30 2017 Andrey Cherepanov <cas@altlinux.org> 0.20-alt1
- New version

* Mon Mar 20 2017 Andrey Cherepanov <cas@altlinux.org> 0.16-alt1
- New version

* Tue Feb 28 2017 Andrey Cherepanov <cas@altlinux.org> 0.13-alt1
- New version

* Mon Oct 24 2016 Andrey Cherepanov <cas@altlinux.org> 0.7-alt1
- Initial build in Sisyphus
