Name: python3-module-jsonrpc-async
Version: 2.0.0
Release: alt1

Summary: JSON-RPC client implementation for asyncio python code
License: BSD
Group: Development/Python
Url: https://pypi.org/project/jsonrpc-async/

Source0: %name-%version-%release.tar

BuildArch: noarch
BuildRequires: rpm-build-python3 python3-module-setuptools

%description
%summary

%prep
%setup

%build
%python3_build

%install
%python3_install

%files
%doc LICENSE.* README.*
%python3_sitelibdir/jsonrpc_async
%python3_sitelibdir/jsonrpc_async-%version-*-info

%changelog
* Tue Apr 13 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.0.0-alt1
- 2.0.0 released

* Mon Jan 13 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.1.1-alt1
- initial
