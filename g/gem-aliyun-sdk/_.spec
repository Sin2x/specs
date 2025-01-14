%define        gemname aliyun-sdk

Name:          gem-aliyun-sdk
Version:       0.8.0
Release:       alt1
Summary:       Aliyun OSS SDK for Ruby
License:       MIT
Group:         Development/Ruby
Url:           https://www.rubydoc.info/gems/aliyun-sdk/
Vcs:           https://github.com/aliyun/aliyun-oss-ruby-sdk.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(nokogiri) >= 1.6 gem(nokogiri) < 2
BuildRequires: gem(rest-client) >= 2.0 gem(rest-client) < 3
BuildRequires: gem(bundler) >= 1.10 gem(bundler) < 3
BuildRequires: gem(rake) >= 10.4 gem(rake) < 14
BuildRequires: gem(rake-compiler) >= 0.9.0 gem(rake-compiler) < 2
BuildRequires: gem(rspec) >= 3.3 gem(rspec) < 4
BuildRequires: gem(webmock) >= 3.0 gem(webmock) < 4
BuildRequires: gem(simplecov) >= 0.10.0 gem(simplecov) < 1
BuildRequires: gem(minitest) >= 5.8 gem(minitest) < 6

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency bundler >= 2.1.4,bundler < 3
%ruby_use_gem_dependency rake >= 13.0.1,rake < 14
%ruby_use_gem_dependency simplecov >= 0.17,simplecov < 1
%ruby_use_gem_dependency rake-compiler >= 1.1.2,rake-compiler < 2
%ruby_use_gem_dependency addressable >= 2.8.0,addressable < 3
%ruby_use_gem_dependency term-ansicolor >= 1.7.1,term-ansicolor < 2
Requires:      gem(nokogiri) >= 1.6 gem(nokogiri) < 2
Requires:      gem(rest-client) >= 2.0 gem(rest-client) < 3
Provides:      gem(aliyun-sdk) = 0.8.0


%description
Alibaba Cloud OSS SDK for Ruby is a Ruby client program for convenient access to
Alibaba Cloud OSS (Object Storage Service) RESTful APIs. For more information
about OSS, visit the OSS official website.


%package       -n gem-aliyun-sdk-doc
Version:       0.8.0
Release:       alt1
Summary:       Aliyun OSS SDK for Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aliyun-sdk
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aliyun-sdk) = 0.8.0

%description   -n gem-aliyun-sdk-doc
Aliyun OSS SDK for Ruby documentation files.

Alibaba Cloud OSS SDK for Ruby is a Ruby client program for convenient access to
Alibaba Cloud OSS (Object Storage Service) RESTful APIs. For more information
about OSS, visit the OSS official website.

%description   -n gem-aliyun-sdk-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aliyun-sdk.


%package       -n gem-aliyun-sdk-devel
Version:       0.8.0
Release:       alt1
Summary:       Aliyun OSS SDK for Ruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aliyun-sdk
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aliyun-sdk) = 0.8.0
Requires:      gem(bundler) >= 1.10 gem(bundler) < 3
Requires:      gem(rake) >= 10.4 gem(rake) < 14
Requires:      gem(rake-compiler) >= 0.9.0 gem(rake-compiler) < 2
Requires:      gem(rspec) >= 3.3 gem(rspec) < 4
Requires:      gem(webmock) >= 3.0 gem(webmock) < 4
Requires:      gem(simplecov) >= 0.10.0 gem(simplecov) < 1
Requires:      gem(minitest) >= 5.8 gem(minitest) < 6

%description   -n gem-aliyun-sdk-devel
Aliyun OSS SDK for Ruby development package.

Alibaba Cloud OSS SDK for Ruby is a Ruby client program for convenient access to
Alibaba Cloud OSS (Object Storage Service) RESTful APIs. For more information
about OSS, visit the OSS official website.

%description   -n gem-aliyun-sdk-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aliyun-sdk.


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

%files         -n gem-aliyun-sdk-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-aliyun-sdk-devel
%doc README.md
%ruby_includedir/*


%changelog
* Sat Apr 16 2022 Pavel Skrylev <majioa@altlinux.org> 0.8.0-alt1
- ^ 0.7.2 -> 0.8.0

* Mon Jun 15 2020 Pavel Skrylev <majioa@altlinux.org> 0.7.2-alt1
- + packaged gem with usage Ruby Policy 2.0
