%define        pkgname nokogiri

Name:          ruby-%pkgname
Version:       1.10.3
Release:       alt2
Summary:       Ruby libraries for Nokogiri (HTML, XML, SAX, and Reader parser)
Group:         Development/Ruby
License:       MIT
URL:           https://nokogiri.org/
%vcs           https://github.com/sparklemotion/nokogiri.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
Source:        %name-%version.tar
Patch:         shutdown-libxml2-warning.patch

BuildRequires(pre): rpm-build-ruby
BuildRequires: libxml2-devel libxslt-devel java-devel ruby-pkg-config zlib-devel
# BuildRequires: db2latex-xsl xhtml1-dtds
BuildRequires: gem(hoe)
BuildRequires: gem(rake-compiler)
BuildRequires: gem(concourse)
BuildRequires: gem(rexical)
BuildRequires: gem(racc)
BuildRequires: gem(mini_portile2)

%description
Nokogiri parses and searches XML/HTML very quickly, and also has correctly
implemented CSS3 selector support as well as XPath support.
This package contanis Ruby libraries for Nokogiri.

%package       -n %pkgname
Summary:       HTML, XML, SAX, and Reader parser
Group:         Development/Other
BuildArch:     noarch

%description   -n %pkgname
Nokogiri parses and searches XML/HTML very quickly, and also has correctly
implemented CSS3 selector support as well as XPath support.
This package contanis Ruby libraries for Nokogiri.


%package       devel
Summary:       Development files for %gemname gem
Group:         Development/Ruby
BuildArch:     noarch

%description   devel
Development files for %gemname gem.


%package       doc
Summary:       Documentation for %gemname gem
Group:         Development/Documentation
BuildArch:     noarch

%description doc
Documentation for %gemname gem.


%prep
%setup
%patch -p1

%build
%ruby_build

%install
%ruby_install

%check
%ruby_test

%files
%ruby_gemspec
%ruby_gemlibdir
%ruby_gemextdir

%files         -n %pkgname
%_bindir/*

%files         doc
%ruby_gemdocdir

%files         devel
%ruby_includedir/*

%changelog
* Tue Jun 18 2019 Pavel Skrylev <majioa@altlinux.org> 1.10.3-alt2
- Fix spec

* Fri Apr 26 2019 Andrey Cherepanov <cas@altlinux.org> 1.10.3-alt1
- New version.

* Mon Feb 04 2019 Pavel Skrylev <majioa@altlinux.org> 1.10.1-alt4
- Use Ruby Policy 2.0.

* Fri Jan 25 2019 Pavel Skrylev <majioa@altlinux.org> 1.10.1-alt3
- Fixed extension installation folder.

* Fri Jan 18 2019 Pavel Skrylev <majioa@altlinux.org> 1.10.1-alt2
- Fixed spec.

* Wed Jan 16 2019 Pavel Skrylev <majioa@altlinux.org> 1.10.1-alt1
- Bump to 1.10.1;
- Place library files into gem folder.

* Fri Oct 05 2018 Andrey Cherepanov <cas@altlinux.org> 1.8.5-alt1
- New version.

* Thu Jul 26 2018 Andrey Cherepanov <cas@altlinux.org> 1.8.4-alt1.1
- Rebuild with new Ruby autorequirements.

* Thu Jul 05 2018 Andrey Cherepanov <cas@altlinux.org> 1.8.4-alt1
- New version.
- Package as gem.
- Simplify requirements and add requirements for rake tasks.

* Mon Jun 18 2018 Andrey Cherepanov <cas@altlinux.org> 1.8.3-alt1
- New version.

* Fri Mar 30 2018 Andrey Cherepanov <cas@altlinux.org> 1.8.2-alt1.2
- Rebuild with Ruby 2.5.1

* Tue Mar 13 2018 Andrey Cherepanov <cas@altlinux.org> 1.8.2-alt1.1
- Rebuild with Ruby 2.5.0

* Mon Jan 29 2018 Andrey Cherepanov <cas@altlinux.org> 1.8.2-alt1
- New version.

* Wed Sep 20 2017 Andrey Cherepanov <cas@altlinux.org> 1.8.1-alt1
- New version

* Tue Sep 05 2017 Andrey Cherepanov <cas@altlinux.org> 1.8.0-alt1.1
- Rebuild with Ruby 2.4.1

* Mon Jun 05 2017 Andrey Cherepanov <cas@altlinux.org> 1.8.0-alt1
- New version

* Wed May 10 2017 Andrey Cherepanov <cas@altlinux.org> 1.7.2-alt1
- New version

* Mon Mar 20 2017 Andrey Cherepanov <cas@altlinux.org> 1.7.1-alt1
- Nrw version

* Sat Mar 11 2017 Andrey Cherepanov <cas@altlinux.org> 1.7.0.1-alt1
- New version
- Rebuild with new %%ruby_sitearchdir location

* Mon Sep 12 2016 Andrey Cherepanov <cas@altlinux.org> 1.6.8-alt1
- New version

* Fri May 22 2015 Andrey Cherepanov <cas@altlinux.org> 1.6.6.2-alt1
- 1.6.6.2
- Rebuild with new version of libxml2

* Wed Mar 19 2014 Led <led@altlinux.ru> 1.6.1-alt2
- Rebuilt with ruby-2.0.0-alt1

* Sat Mar 15 2014 Led <led@altlinux.ru> 1.6.1-alt1
- 1.6.1

* Fri Apr 12 2013 Led <led@altlinux.ru> 1.5.9-alt1
- 1.5.9
- updated URL
- updated BuildRequires
- fixed Group for %%name-doc subpackage
- moved %%_bindir/nokogiri to separate subpackage

* Sat Dec 15 2012 Led <led@altlinux.ru> 1.5.5-alt2
- fixed for renamed %_bindir/rex -> %_bindir/rexical
- %%files: fixed "File listed twice"

* Fri Dec 07 2012 Led <led@altlinux.ru> 1.5.5-alt1.1
- Rebuilt with ruby-1.9.3-alt1

* Wed Mar 24 2012 Andriy Stepanov <stanv@altlinux.ru> 1.5.5-alt1
- New version

* Wed Mar 23 2011 Andriy Stepanov <stanv@altlinux.ru> 1.4.4.2-alt2
- Fix build

* Wed Mar 23 2011 Andriy Stepanov <stanv@altlinux.ru> 1.4.4.2-alt1
- [1.4.4.2]

* Wed Mar 17 2010 Timur Batyrshin <erthad@altlinux.org> 1.4.0-alt1
- [1.4.0]

* Sun Jun 28 2009 Alexey I. Froloff <raorn@altlinux.org> 1.3.2-alt1
- [1.3.2]

* Thu Sep 25 2008 Grigory Batalov <bga@altlinux.ru> 1.1.0-alt1
- Initial build for ALT Linux.
