%define oldname neovim
%define oname pynvim

Name: python3-module-%oldname
Version: 0.4.2
Release: alt1

Summary: Python 3 client to Neovim

License: %asl
Group: Development/Python
Url: https://github.com/neovim/pynvim

Source: %name-%version.tar
BuildArch: noarch

AutoReqProv: nopython
%define __python %nil

BuildRequires(pre): rpm-build-python3 rpm-build-licenses
BuildRequires: python3-module-pytest-runner

%description
Pynvim implements support for python plugins in Nvim. It also works as a library
for connecting to and scripting Nvim processes through its msgpack-rpc API.

%prep
%setup -n %name-%version

%build
%python3_build

%install
%python3_install

%files
%python3_sitelibdir/%oname/
%python3_sitelibdir/%oldname/
%python3_sitelibdir/*.egg-*

%changelog
* Wed Sep 30 2020 Vladimir Didenko <cow@altlinux.org> 0.4.2-alt1
- new release

* Tue Jan 28 2020 Vladimir Didenko <cow@altlinux.org> 0.4.1-alt1
- new release

* Thu Nov 28 2019 Vladimir Didenko <cow@altlinux.org> 0.4.0-alt1
- new release

* Tue Jan 29 2019 Vladimir Didenko <cow@altlinux.org> 0.3.2-alt1
- new release

* Wed Jan 9 2019 Vladimir Didenko <cow@altlinux.org> 0.3.1-alt1
- new release

* Wed Jul 25 2018 Vladimir Didenko <cow@altlinux.org> 0.2.6-alt1
- initial build for Sisyphus
