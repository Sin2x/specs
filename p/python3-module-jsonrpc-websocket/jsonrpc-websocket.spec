Name: python3-module-jsonrpc-websocket
Version: 3.1.4
Release: alt1

Summary: JSON-RPC websocket client library for asyncio
License: BSD
Group: Development/Python
Url: https://pypi.org/project/jsonrpc-websocket/

Source0: %name-%version-%release.tar

BuildArch: noarch
BuildRequires: rpm-build-python3
BuildRequires: python3(setuptools)
BuildRequires: python3(wheel)

%description
%summary

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%files
%doc LICENSE.* README.*
%python3_sitelibdir/jsonrpc_websocket
%python3_sitelibdir/jsonrpc_websocket-%version.dist-info

%changelog
* Thu Jul 21 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 3.1.4-alt1
- 3.1.4 released

* Wed May 18 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 3.1.2-alt1
- 3.1.2 released

* Mon Oct 04 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 3.1.0-alt1
- 3.1.0 released

* Mon Nov 23 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.2.1-alt1
- 1.2.1 released

* Mon Jan 13 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.0.2-alt1
- initial
