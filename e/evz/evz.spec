Name: evz
Version: 0.3.0
Release: alt1

Summary: OpenVZ control tool

License: AGPLv3
Group: System/Configuration/Packaging
Url: https://github.com/Etersoft/evz

Packager: Vitaly Lipatov <lav@altlinux.ru>

# Source-git: https://github.com/Etersoft/evz.git
Source: ftp://updates.etersoft.ru/pub/Korinf/sources/tarball/%name-%version.tar

ExclusiveArch: x86_64

%description
EVZ is implemented as wrapper around vzctl with accent to group operations on containers.

See detailed description in russian here: http://wiki.etersoft.ru/EVZ

%prep
%setup

%install
# install to datadir and so on
%makeinstall version=%version-%release

install -D -m 0644 bash_completion/evz %buildroot%_sysconfdir/bash_completion.d/evz

# shebang.req.files
#chmod a+x %buildroot%_datadir/%name/{erc-}*

%files
#doc README LICENSE TODO
%_bindir/evz
%_datadir/%name/
%_man8dir/*
%_sysconfdir/bash_completion.d/evz

%changelog
* Tue Feb 25 2020 Vitaly Lipatov <lav@altlinux.ru> 0.3.0-alt1
- move the script to /usr/bin
- add qm (qemu) support
- allow all/ALL for stop
- fix destroy listing
- add pct support

* Mon Feb 24 2020 Vitaly Lipatov <lav@altlinux.ru> 0.2.0-alt1
- refactoring with initial docker support
- evz-openvz: don't use vz commands directly
- add ports command

* Sun Mar 24 2019 Vitaly Lipatov <lav@altlinux.ru> 0.1.3-alt1
- evz: add enter support

* Mon Nov 05 2018 Alexey Shabalin <shaba@altlinux.org> 0.1.2-alt2
- build for x86_64 only

* Wed Feb 14 2018 Vitaly Lipatov <lav@altlinux.ru> 0.1.2-alt1
- evz: add restart support
- evz: add set support
- evz: add ubc call

* Sun Nov 19 2017 Vitaly Lipatov <lav@altlinux.ru> 0.1.1-alt1
- fix evz-sh-functions packing

* Fri Nov 17 2017 Vitaly Lipatov <lav@altlinux.ru> 0.1-alt1
- add compact, status
- add help
- improve vz list using (all, ALL for any cases)
- add missed isatty2 func

* Wed Nov 15 2017 Vitaly Lipatov <lav@altlinux.ru> 0.0.3-alt1
- list: add support for all and ALL
- evz: add initial info

* Wed Nov 08 2017 Vitaly Lipatov <lav@altlinux.ru> 0.0.2-alt1
- evz: add list, exec

* Sat Oct 28 2017 Vitaly Lipatov <lav@altlinux.ru> 0.0.1-alt1
- initial build for ALT Linux Sisyphus
