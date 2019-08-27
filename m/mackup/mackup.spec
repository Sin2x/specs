%define _unpackaged_files_terminate_build 1

Name: mackup
Version: 0.8.27
Release: alt2
Summary: Keep your application settings in sync
License: GNU GPL v3.0
Group: Other
Url: https://github.com/lra/mackup
Source: %name-%version.tar

BuildArch: noarch
BuildRequires(pre): rpm-build-python3
Requires: python3-module-%name

%description
What does it do:
- Back ups your application settings in a safe directory (e.g. Dropbox)
- Syncs your application settings among all your workstations
- Restores your configuration on any fresh install in one command line
By only tracking pure configuration files, it keeps the crap out of your
freshly new installed workstation (no cache, temporary and locally specificfiles
are transfered). Mackup makes setting up the environment easy and simple, saving
time for your family, great ideas, and all the cool stuff you like.

%package -n python3-module-%name
Summary: Keep your application settings in sync
Group: Other
BuildArch: noarch

%description -n python3-module-%name
This package contains python module for %name

%prep
%setup

%build
%python3_build

%install
%python3_install
mkdir -p %buildroot/%_sysconfdir/%name
sed -i "/MACKUP_CONFIG_FILE/s/.mackup.cfg/\%_sysconfdir\/%name\/mackup.cfg/" %buildroot/%python3_sitelibdir/%name/constants.py
mv %buildroot/%python3_sitelibdir/%name/applications/mackup.cfg %buildroot/%_sysconfdir/%name

%files
%_bindir/%name
%config(noreplace) %_sysconfdir/%name/mackup.cfg

%files -n python3-module-%name
%python3_sitelibdir/%{name}*

%changelog
* Tue Aug 27 2019 Alexander Makeenkov <amakeenk@altlinux.org> 0.8.27-alt2
- build python3-module-mackup package
- move mackup.cfg in /etc/mackup
- remove unnecessary build requires

* Mon Aug 26 2019 Alexander Makeenkov <amakeenk@altlinux.org> 0.8.27-alt1
- New version

* Wed Jul 31 2019 Alexander Makeenkov <amakeenk@altlinux.org> 0.8.26-alt1
- New version

* Sun Jul 21 2019 Alexander Makeenkov <amakeenk@altlinux.org> 0.8.25-alt3
- Minor spec fix

* Sun Jul 14 2019 Alexander Makeenkov <amakeenk@altlinux.org> 0.8.25-alt2
- Fixed replacing of mackup.cfg file

* Sun Jul 14 2019 Alexander Makeenkov <amakeenk@altlinux.org> 0.8.25-alt1
- New version

* Wed May 22 2019 Alexander Makeenkov <amakeenk@altlinux.org> 0.8.24-alt1
- New version

* Mon Mar 04 2019 Alexander Makeenkov <amakeenk@altlinux.org> 0.8.22-alt1
- Initial build for ALT

