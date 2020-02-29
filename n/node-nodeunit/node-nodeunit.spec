%define pname nodeunit

Name: node-nodeunit
Version: 0.11.3
Release: alt1

Summary: Easy unit testing in node.js and the browser, based on the assert module

License: MIT License
Group: Development/Other
Url: https://github.com/caolan/nodeunit

Packager: Vitaly Lipatov <lav@altlinux.ru>

# Source-url: https://github.com/caolan/nodeunit/archive/%version.tar.gz
Source: %name-%version.tar

Source1: %name-development-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-intro >= 1.9.18

BuildRequires: rpm-build-nodejs node
BuildRequires(pre): rpm-macros-nodejs

BuildRequires: node-typescript

#AutoReq: no
#AutoProv: no

%description
The project is very stale. We've kept it working on new versions of node,
and sometimes merged small PRs that help teams relying on nodeunit.

Nodeunit was the arguably first testing framework developed for node.
It was very useful at the time, but there's an overwhelming number
of other worthwhile testing solutions out there that are actively maintained.
tap, ava, tape, mocha, jasmine, jest, ... the list goes on and on.

You are strongly encouraged to check out other more modern testing options.

%prep
%setup -a 1

%build
%npm_build
npm test
npm prune --production

%check
#npm test
echo "Checking %pname loading ..."
node -e 'require("./")'

%install
%npm_install
mkdir -p %buildroot%_bindir
ln -sr %buildroot%nodejs_sitelib/%pname/bin/nodeunit %buildroot%_bindir/nodeunit
cp -a node_modules %buildroot/%nodejs_sitelib/%pname/
# TODO: remove all test subdir
rm -rf %buildroot/%nodejs_sitelib/%pname/test/
# extra reqs
rm -rf %buildroot/%nodejs_sitelib/%pname/node_modules/resolve/test/

%files
%doc LICENSE README.md
%_bindir/nodeunit
%nodejs_sitelib/%pname/

%changelog
* Fri Feb 28 2020 Vitaly Lipatov <lav@altlinux.ru> 0.11.3-alt1
- initial build for ALT Sisyphus
