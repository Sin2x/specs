%define _libexecdir /usr/libexec
%define oname phaul
%def_without check

Name:    phaul-ovz
Version: 0.1.79
Release: alt1

Summary: Process HAULer -- a tool to live-migrate containers and processes
License: LGPL-2.1
Group: System/Configuration/Other
#Vcs: https://src.openvz.org/scm/ovz/p.haul.git
URL: https://src.openvz.org/

Packager: Andrew A. Vasilyev <andy@altlinux.org>

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools
Requires: crtools-ovz
Conflicts: %oname

ExclusiveArch: x86_64

Source: %name-%version.tar
Patch: %name-%version-%release.patch

%description
Process HAULer -- a tool to live-migrate containers and processes.

%prep
%setup -n %name-%version
%patch -p1
find . -name '*.py' -o -name p.haul-wrap | xargs sed -i \
        -e '1s|^#!/usr/bin/env python$|#!/usr/bin/python3|' \
        -e '1s|^#!/usr/bin/python$|#!/usr/bin/python3|' \
        %nil

%build
%python3_build

%install
%__python3 setup.py install --skip-build --root %buildroot --install-scripts %_libexecdir/%oname
# Remove egg-info, module is necessary for phaul only:
rm -rf %buildroot%python3_sitelibdir_noarch/*.egg-info
install -d %buildroot%_sbindir
install -pD -m755 p.haul-ssh p.haul-wrap %buildroot%_sbindir
chmod a+rx %buildroot%python3_sitelibdir_noarch/%oname/shell/{phaul_client,phaul_service}.py

%if_with check
%check
export PYTHONPATH=%buildroot%python3_sitelibdir_noarch
pushd test
popd
%endif

%files
%doc COPYING README.md
%_libexecdir/%oname
%_sbindir/*
%python3_sitelibdir_noarch/*

%changelog
* Mon Mar 08 2021 Andrew A. Vasilyev <andy@altlinux.org> 0.1.79-alt1
- 0.1.79

* Mon Jan 11 2021 Andrew A. Vasilyev <andy@altlinux.org> 0.1.78-alt1
- 0.1.78
- fix libvzctl scripts path

* Tue Dec 08 2020 Andrew A. Vasilyev <andy@altlinux.org> 0.1.77-alt1
- 0.1.77

* Mon Nov 09 2020 Andrew A. Vasilyev <andy@altlinux.org> 0.1.75-alt1
- initial build for ALT

