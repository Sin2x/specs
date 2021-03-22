Name: python3-module-ajsonrpc
Version: 1.1.0
Release: alt1

Summary: Async JSON-RPC 2.0 protocol
License: MIT
Group: Development/Python
Url: https://pypi.org/project/wsproto/

Source0: %name-%version-%release.tar

BuildArch: noarch
BuildRequires: rpm-build-python3 python3-module-setuptools

%description
%summary

%prep
%setup
sed -i '/^__version__/ s,0\.0\.0,%version,' ajsonrpc/__init__.py

%build
%python3_build

%install
%python3_install

%add_python3_req_skip sanic.response
%add_python3_req_skip tornado.web

%files
%python3_sitelibdir/ajsonrpc
%python3_sitelibdir/ajsonrpc-%version-*-info

%changelog
* Mon Mar 22 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.1.0-alt1
- initial
