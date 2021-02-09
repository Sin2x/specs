
%define _unpackaged_files_terminate_build 1
%def_enable check

Name:    yq
Version: 2.12.0
Release: alt2

Summary: Command-line YAML, XML and TOML processor
License: Apache-2.0
Group:   Other
URL:     https://github.com/kislyuk/yq

Packager: Ivan A. Melnikov <iv@altlinux.org>

BuildRequires: rpm-build-python3
%if_enabled check
BuildRequires: jq
BuildRequires: python3-module-xmltodict >= 0.11.0
BuildRequires: python3-module-toml >= 0.9.4
BuildRequires: python3(argcomplete)
BuildRequires: python3(yaml)
BuildRequires: /proc
%endif

BuildArch: noarch

Source:  %name-%version.tar

Requires: jq
Requires: python3-module-xmltodict >= 0.11.0
Requires: python3-module-toml >= 0.10.0

%description
yq is a command-line YAML, XML and TOML processor.
It is a jq wrapper for YAML, XML and TOML documents.

%prep
%setup -n %name-%version

%build
%python3_build

%install
%python3_install

%check
sed -i '/expect_exit_codes=.* sys.stdin.isatt/d' ./test/test.py
%__python3 ./test/test.py -v

%files
%_bindir/*
%python3_sitelibdir/%name/
%python3_sitelibdir/*.egg-info

%changelog
* Tue Feb 09 2021 Ivan A. Melnikov <iv@altlinux.org> 2.12.0-alt2
- add %%check section

* Tue Feb 09 2021 Ivan A. Melnikov <iv@altlinux.org> 2.12.0-alt1
- 2.12.0

* Mon Sep 07 2020 Ivan A. Melnikov <iv@altlinux.org> 2.11.0-alt1
- 2.11.0

* Tue May 12 2020 Ivan A. Melnikov <iv@altlinux.org> 2.10.1-alt1
- 2.10.1

* Mon Dec 23 2019 Ivan A. Melnikov <iv@altlinux.org> 2.10.0-alt1
- 2.10.0
- switch to python3

* Tue Nov 05 2019 Ivan A. Melnikov <iv@altlinux.org> 2.9.2-alt1
- 2.9.2

* Wed Jan 30 2019 Ivan A. Melnikov <iv@altlinux.org> 2.7.2-alt1
- 2.7.2
- require python-module-toml (closes: #36001)

* Fri Oct 12 2018 Ivan A. Melnikov <iv@altlinux.org> 2.7.0-alt1
- 2.7.0

* Fri Jun 08 2018 Ivan A. Melnikov <iv@altlinux.org> 2.6.0-alt1
- Initial build for Sisyphus
