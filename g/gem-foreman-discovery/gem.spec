%define        gemname foreman_discovery

Name:          gem-foreman-discovery
Version:       18.0.4
Release:       alt1
Summary:       MaaS Discovery Plugin for Foreman
License:       GPL-3.0
Group:         Development/Ruby
Url:           https://github.com/theforeman/foreman_discovery
Vcs:           https://github.com/theforeman/foreman_discovery.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_alias_names foreman_discovery,foreman-discovery
Provides:      gem(foreman_discovery) = 18.0.4


%description
A plugin to enable Metal-as-a-Service discovery functionality in foreman.


%package       -n gem-foreman-discovery-doc
Version:       18.0.4
Release:       alt1
Summary:       MaaS Discovery Plugin for Foreman documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета foreman_discovery
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(foreman_discovery) = 18.0.4

%description   -n gem-foreman-discovery-doc
MaaS Discovery Plugin for Foreman documentation files.

A plugin to enable Metal-as-a-Service discovery functionality in foreman.

%description   -n gem-foreman-discovery-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета foreman_discovery.


%package       -n gem-foreman-discovery-devel
Version:       18.0.4
Release:       alt1
Summary:       MaaS Discovery Plugin for Foreman development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета foreman_discovery
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(foreman_discovery) = 18.0.4

%description   -n gem-foreman-discovery-devel
MaaS Discovery Plugin for Foreman development package.

A plugin to enable Metal-as-a-Service discovery functionality in foreman.

%description   -n gem-foreman-discovery-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета foreman_discovery.


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

%files         -n gem-foreman-discovery-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-foreman-discovery-devel
%doc README.md


%changelog
* Wed Oct 27 2021 Pavel Skrylev <majioa@altlinux.org> 18.0.4-alt1
- ^ 17.1.0 -> 18.0.4

* Wed Sep 01 2021 Pavel Skrylev <majioa@altlinux.org> 17.1.0-alt1
- + packaged gem with Ruby Policy 2.0
