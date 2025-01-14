Name: alterator-module-executor
Version: 0.0.2
Release: alt1

Summary: Alterator-manager module for running executable files and scripts
License: GPL-2
Group: System/Configuration/Other

BuildRequires: cmake gcc
BuildRequires: libgio-devel libsystemd-devel alterator-manager-devel >= 0.0.3

Requires: alterator-manager >= 0.0.3-alt0

Source: %name-%version.tar

%description
Alterator-manager module for running executable files and scripts.

%prep
%setup -q

%build
%cmake -DCMAKE_BUILD_TYPE=Release
%cmake_build

%install
%cmakeinstall_std
mkdir -p %buildroot%_datadir/alterator/modules/executor

%files
%dir %_datadir/alterator/modules/executor
/usr/libexec/alterator/*

%changelog
* Sat Oct 22 2022 Evgeny Sinelnikov <sin@altlinux.org> 0.0.2-alt1
- Second work version.

* Wed Oct 12 2022 Ivan Savin <svn17@altlinux.org> 0.0.1-alt1
- First work version.

