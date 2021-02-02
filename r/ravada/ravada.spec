%def_without check

Name: ravada
Summary: Remote Virtual Desktops Manager
Version: 0.11.0
Release: alt1
License: AGPL-3.0
Group: Development/Perl
Url: https://ravada.upc.edu/
Vcs: https://github.com/UPC/ravada.git
Packager: Andrew A. Vasilyev <andy@altlinux.ru>

Source: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-perl

BuildRequires: ImageMagick-tools
BuildRequires: bridge-utils iproute2 net-tools qemu-img wget

BuildRequires: perl-Authen-Passphrase
BuildRequires: perl-DateTime-Format-DateParse
BuildRequires: perl-DateTime
BuildRequires: perl-DBD-SQLite
BuildRequires: perl-DBIx-Connector
BuildRequires: perl-devel
BuildRequires: perl-File-Rsync
BuildRequires: perl-IO-Interface
BuildRequires: perl-IO-stringy
BuildRequires: perl-IPC-Run3
BuildRequires: perl-IPTables-ChainMgr
BuildRequires: perl-JSON-XS
BuildRequires: perl-ldap
BuildRequires: perl-Locale-Maketext
BuildRequires: perl-Locale-Maketext-Lexicon
BuildRequires: perl-Magick
BuildRequires: perl-Mojolicious >= 7.01
BuildRequires: perl-Mojolicious-Plugin-I18N
BuildRequires: perl-Moose
BuildRequires: perl-MooseX-Types
BuildRequires: perl-MooseX-Types-NetAddr-IP
BuildRequires: perl-Net-DNS
BuildRequires: perl-Net-OpenSSH
BuildRequires: perl-Net-Ping
BuildRequires: perl-PBKDF2-Tiny
BuildRequires: perl-Proc-PID-File
BuildRequires: perl-Sys-Virt
BuildRequires: perl-Test-Pod-Coverage
BuildRequires: perl-XML-LibXML
BuildRequires: perl-YAML
# NO Sys::Statistics::Linux

%if_with check
BuildRequires: /proc
BuildRequires: perl-Test-Moose-More
BuildRequires: perl-Test-Perl-Critic
%endif

%define __spec_autodep_custom_pre export PERL5OPT='-I%buildroot%perl_vendor_privlib -MRavada'; export TZ=UTC
%set_perl_req_method relaxed
%global __find_requires export TZ=UTC; /usr/lib/rpm/find-requires

%description
Ravada is a software that allows the user to connect to a remote virtual desktop

%prep
%setup -q -n %name-%version

%build
# set environment variable to make sure DateTime::TimeZone::Local
# could determine timezone during tests
export TZ=UTC
perl Makefile.PL INSTALLDIRS=vendor
%make_build

%install
export TZ=UTC
%perl_vendor_install
install -D -m755 script/rvd_back %buildroot%_sbindir/rvd_back
install -D -m755 script/rvd_front %buildroot%_sbindir/rvd_front
mkdir -p %buildroot%_datadir/%name
cp -rp templates %buildroot%_datadir/%name
mkdir -p %buildroot%_sysconfdir
install -p -m644 etc/%name.conf %buildroot%_sysconfdir/%name.conf
install -p -m644 etc/rvd_front.conf.example %buildroot%_sysconfdir/rvd_front.conf
mkdir -p %buildroot%_unitdir
install -p -m644 etc/systemd/*.service %buildroot%_unitdir

%check
export TZ=UTC
export PATH=$PATH:/sbin
make test

%preun
%preun_service rvd_back
%preun_service rvd_front

%post
%post_service rvd_back
# First installation, not upgrade.
if [ $1 -eq 1 ]; then
    systemctl enable rvd_back.service || :
fi

%post_service rvd_front
# First installation, not upgrade.
if [ $1 -eq 1 ]; then
    systemctl enable rvd_front.service || :
fi

%files
%doc LICENSE MANIFEST README.md
%perl_vendor_privlib/*
%_sbindir/*
%_datadir/%name
%_unitdir/*.service
%config(noreplace)%_sysconfdir/%name.conf
%config(noreplace)%_sysconfdir/rvd_front.conf

%changelog
* Tue Feb 02 2021 Andrew A. Vasilyev <andy@altlinux.org> 0.11.0-alt1
- 0.11.0

* Mon Dec 21 2020 Andrew A. Vasilyev <andy@altlinux.org> 0.10.5-alt1
- 0.10.5

* Mon Dec 14 2020 Andrew A. Vasilyev <andy@altlinux.org> 0.10.4-alt1
- 0.10.4

* Wed Dec 09 2020 Andrew A. Vasilyev <andy@altlinux.org> 0.10.3-alt1
- 0.10.3

* Wed Dec 02 2020 Andrew A. Vasilyev <andy@altlinux.org> 0.10.2-alt1
- 0.10.2

* Wed Nov 25 2020 Andrew A. Vasilyev <andy@altlinux.org> 0.10.1-alt1
- 0.10.1

* Wed Nov 11 2020 Andrew A. Vasilyev <andy@altlinux.org> 0.10.0-alt1
- 0.10.0

* Thu Oct 08 2020 Andrew A. Vasilyev <andy@altlinux.org> 0.9.0-alt1
- 0.9.0

* Wed Aug 05 2020 Andrew A. Vasilyev <andy@altlinux.org> 0.8.3-alt1
- initial build for ALT Linux Sisyphus

