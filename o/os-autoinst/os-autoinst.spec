%define _unpackaged_files_terminate_build 1

Name: os-autoinst
Version: 4.6
Release: alt2
Summary: OS-level test automation
License: GPLv2+
Group: Development/Tools
Url: https://github.com/os-autoinst/os-autoinst/
Source: %name-%version.tar
Patch1: fixstartvmuefi.patch

BuildRequires: perlcritic
BuildRequires: autoconf
BuildRequires: automake
BuildRequires: gcc-c++
BuildRequires: libtool
BuildRequires: libopencv-devel
BuildRequires: perl-devel
BuildRequires: perl-Test-Warnings
BuildRequires: perl-Package-Generator
BuildRequires: perl(Test/Most.pm)
BuildRequires: perl(Test/Mock/Time.pm)
BuildRequires: perl(ExtUtils/MakeMaker.pm)
BuildRequires: perl(ExtUtils/Embed.pm)
BuildRequires: perl(Module/CPANfile.pm)
BuildRequires: perl(Perl/Critic.pm)
BuildRequires: perl(Perl/Tidy.pm)
BuildRequires: perl(Pod/Html.pm)
BuildRequires: perl(Term/ReadLine.pm)
BuildRequires: perl(Test/MockObject.pm)
BuildRequires: pkgconfig
BuildRequires: pkgconfig(libpng)
BuildRequires: pkgconfig(fftw3)
BuildRequires: pkgconfig(sndfile)
BuildRequires: pkgconfig(theoraenc)
BuildRequires: systemd
BuildRequires: perl(Devel/Cover.pm)
BuildRequires: perl(Test/Strict.pm)
BuildRequires: perl(Pod/Coverage.pm)
BuildRequires: perl(Test/Compile.pm)
BuildRequires: perl(Socket/MsgHdr.pm)
BuildRequires: perl(Test/Fatal.pm)
BuildRequires: perl(Test/MockModule.pm)
BuildRequires: perl(Test/MockTime.pm)
BuildRequires: perl(Test/More.pm)
BuildRequires: perl(Test/Output.pm)
BuildRequires: perl(Test/Pod.pm)
BuildRequires: perl(Test/Warnings.pm)
BuildRequires: perl(Try/Tiny.pm)
BuildRequires: perl(Mojo/IOLoop/ReadWriteProcess.pm)
BuildRequires: perl(Test/Exception.pm)
BuildRequires: perl-IO-stringy
BuildRequires: perl(File/Touch.pm)
BuildRequires: perl(XML/SemanticDiff.pm)
BuildRequires: perl-Pod-Spell
BuildRequires: ispell ispell-en
#BuildConflicts: pve-qemu-aux pve-qemu-img
BuildRequires: /usr/bin/qemu-system-i386
#BuildRequires: /usr/bin/qemu-img
BuildRequires: qemu-img qemu-aux
BuildRequires: perl(Mojo/File.pm)
BuildRequires: perl(Carp/Always.pm) perl(Data/Dump.pm) perl(Crypt/DES.pm) perl(JSON.pm) perl(JSON/XS.pm) perl(autodie.pm) perl(Class/Accessor/Fast.pm) perl(Exception/Class.pm) perl(File/Which.pm) perl(IPC/Run/Debug.pm) perl(Net/DBus.pm) perl(Net/SNMP.pm) perl(Net/IP.pm) perl(IPC/System/Simple.pm) perl(Net/SSH2.pm) perl(XML/LibXML.pm) perl(YAML/PP.pm) yamllint perl(Inline/Python.pm)
BuildRequires: perl(Mojolicious.pm) python3-module-setuptools
BuildPreReq: cmake rpm-macros-cmake ninja-build rpm-macros-ninja-build ctest
Requires: qemu-kvm
Requires: tesseract
Requires: withlock
Requires: perl(Carp/Always.pm) perl(Data/Dump.pm) perl(Net/SNMP.pm) perl(Net/IP.pm)
Requires: /usr/bin/qemu-img
Requires: optipng
Requires: qemu >= 2.0.0

ExclusiveArch: i586 x86_64 ppc64le aarch64

%add_perl_lib_path %buildroot%_libexecdir/os-autoinst
%add_python3_lib_path %_libexecdir/os-autoinst
%add_python3_req_skip perl

%description
The OS-autoinst project aims at providing a means to run fully
automated tests. Especially to run tests of basic and low-level
operating system components such as bootloader, kernel, installer and
upgrade, which can not easily and safely be tested with other
automated testing frameworks. However, it can just as well be used to
test applications on top of a newly installed OS.

%package openvswitch
Summary: Open vSwitch support for os-autoinst
Group: System/Servers
#BuildArch: noarch

Requires: %name = %EVR
Requires: openvswitch

%description openvswitch
This package contains Open vSwitch support for os-autoinst.

%prep
%setup
%patch1 -p1
sed  -i 's/ my $thisversion = qx{git -C $dirname rev-parse HEAD};/ my $thisversion = "%version";/' isotovideo
sed  -i 's/ chomp(my $git_hash = qx{git rev-parse HEAD});/ chomp(my $git_hash = "%version");/' OpenQA/Isotovideo/Utils.pm
sed -e 's,/bin/env python,/bin/python3,' -i crop.py
# don't require qemu within OBS
# and exclude known flaky tests in OBS check
# https://progress.opensuse.org/issues/52652
# 07-commands: https://progress.opensuse.org/issues/60755
for i in 07-commands 10-terminal 13-osutils 14-isotovideo 18-qemu-options 18-backend-qemu 28-signalblocker 99-full-stack; do
    rm -f t/$i.t
done

%build
#mkdir -p m4
%cmake -DSYSTEMD_SERVICE_DIR:STRING="%_unitdir" -GNinja
%ninja_build -C BUILD

%install
%ninja_install -C BUILD install-openvswitch
rm %buildroot%_libexecdir/os-autoinst/crop.py*

%check
export CI=1
%ninja_build -C BUILD check-pkg-build

%files
%_docdir/*
%perl_vendorarch/tinycv.pm
%perl_vendorarch/auto/tinycv
%_libexecdir/os-autoinst
%exclude %_libexecdir/os-autoinst/os-autoinst-openvswitch
%_bindir/*

%files openvswitch
%_libexecdir/os-autoinst/os-autoinst-openvswitch
%_unitdir/os-autoinst-openvswitch.service
%config(noreplace) %_sysconfdir/dbus-1/system.d/org.opensuse.os_autoinst.switch.conf

%changelog
* Mon Apr 12 2021 Alexandr Antonov <aas@altlinux.org> 4.6-alt2
- update to current version

* Mon Mar 15 2021 Alexandr Antonov <aas@altlinux.org> 4.6-alt1
- update to current version

* Fri Jan 22 2021 Alexandr Antonov <aas@altlinux.org> 4.5.1527308405.8b586d5-alt18
- update to current version

* Wed Dec 02 2020 Alexandr Antonov <aas@altlinux.org> 4.5.1527308405.8b586d5-alt17
- update to current version

* Thu Oct 08 2020 Alexandr Antonov <aas@altlinux.org> 4.5.1527308405.8b586d5-alt16
- update to current version

* Thu Aug 06 2020 Alexandr Antonov <aas@altlinux.org> 4.5.1527308405.8b586d5-alt15
- update to current version

* Wed Jul 15 2020 Alexandr Antonov <aas@altlinux.org> 4.5.1527308405.8b586d5-alt14
- update to current version

* Wed Jun 10 2020 Alexandr Antonov <aas@altlinux.org> 4.5.1527308405.8b586d5-alt13
- update to current version

* Fri Apr 24 2020 Alexandr Antonov <aas@altlinux.org> 4.5.1527308405.8b586d5-alt12
- update to current version

* Tue Apr 07 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 4.5.1527308405.8b586d5-alt11
- Fixed build with opencv-4.3.0.

* Wed Feb 26 2020 Alexandr Antonov <aas@altlinux.org> 4.5.1527308405.8b586d5-alt10
- update to current version

* Tue Feb 04 2020 Alexandr Antonov <aas@altlinux.org> 4.5.1527308405.8b586d5-alt9
- update to current version

* Mon Dec 30 2019 Alexandr Antonov <aas@altlinux.org> 4.5.1527308405.8b586d5-alt8
- update to current version

* Tue Oct 29 2019 Alexandr Antonov <aas@altlinux.org> 4.5.1527308405.8b586d5-alt7
- update to current version

* Mon Sep 30 2019 Alexandr Antonov <aas@altlinux.org> 4.5.1527308405.8b586d5-alt6
- update to current version

* Wed Jul 31 2019 Alexandr Antonov <aas@altlinux.org> 4.5.1527308405.8b586d5-alt5
- update to current version

* Fri Jul 5 2019 Alexandr Antonov <aas@altlinux.org> 4.5.1527308405.8b586d5-alt4
- update to current version

* Mon Apr 8 2019 Alexandr Antonov <aas@altlinux.org> 4.5.1527308405.8b586d5-alt3
- update to current version

* Tue Feb 5 2019 Alexandr Antonov <aas@altlinux.org> 4.5.1527308405.8b586d5-alt2
- update to current version

* Thu Jan 24 2019 Igor Vlasenko <viy@altlinux.ru> 4.5.1527308405.8b586d5-alt1.2
- rebuild with new perl 5.28.1

* Fri Dec 28 2018 Igor Vlasenko <viy@altlinux.ru> 4.5.1527308405.8b586d5-alt1.1
- NMU: fixed build (Build Conflict with pve-qemu-aux pve-qemu-img)

* Tue Jun 19 2018 Alexandr Antonov <aas@altlinux.org> 4.5.1527308405.8b586d5-alt1
- initial build for ALT
