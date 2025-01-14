Name: dropbear
Summary: A smallish SSH server and client
Version: 2022.82
Release: alt1
License: MIT
Group: System/Servers
Url: https://matt.ucc.asn.au/dropbear/dropbear.html
Vcs: https://github.com/mkj/dropbear

Source: %name-%version.tar.bz2
Source1: localoptions.h
Source2: dropbear.service
Source3: dropbear.sysconfig

BuildRequires: zlib-devel

%description
Dropbear is a relatively small SSH 2 server.

%package scp
Summary: Standalone scp program from OpenSSH
Group: %group

Conflicts: openssh-common

%description scp
The Dropbear distribution includes a standalone version of OpenSSH's scp
program.

# TODO: Use static versons for embedding and leave documentation where it belongs

%prep
%setup
install -p %SOURCE1 localoptions.h

%build
%configure
%make_build all scp SCPPROGRESS=1

%install
%makeinstall
install -D -m 0755 scp %buildroot%_bindir/scp
mkdir -p %buildroot%_sysconfdir/%name
install -Dpm644 %SOURCE2 %buildroot%_unitdir/%name.service
install -Dpm644 %SOURCE3 %buildroot%_sysconfdir/sysconfig/%name

%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%set_verify_elf_method strict

%check
./dropbearkey -t rsa -f dropbear_rsa_host_key
! ./dropbearkey -t dss -f dropbear_dss_host_key
./dropbearkey -t ecdsa -f dropbear_ecdsa_host_key
./dropbearkey -t ed25519 -f dropbear_ed25519_host_key

%post
%post_service %name

%preun
%preun_service %name

%files
%define _customdocdir %_docdir/%name
%doc [A-Z][A-Z]*
%_bindir/dbclient
%_bindir/dropbearconvert
%_bindir/dropbearkey
%_sbindir/dropbear
%dir %_sysconfdir/%name
%config(noreplace) %_sysconfdir/sysconfig/%name
%_unitdir/%name.service
%_mandir/*/*

%files scp
%_bindir/scp

%changelog
* Sun Jun 19 2022 Vitaly Chikunov <vt@altlinux.org> 2022.82-alt1
- Update to DROPBEAR_2022.82 (2022-04-01). (Fixes: CVE-2018-15599,
  CVE-2018-5399, CVE-2018-20685, CVE-2019-12953, CVE-2020-15833,
  CVE-2020-36254).
- Disable DSS keys.
- Allow password auth.
- Undo authkey_fp patch (as it does not apply to the new codebase).
- Use bundled libtom{crypt,math} maintained by the authors of Dropbear.
- Doc and client packages are merged into main package.
- Add systemd services.
- Correct sftp-server path (to openssh-server binary).

* Fri Jan 12 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 2017.75-alt2
- Rebuilt with new libtommath and libtomcrypt.

* Fri May 19 2017 Fr. Br. George <george@altlinux.ru> 2017.75-alt1
- Autobuild version bump to 2017.75

* Tue Jul 26 2016 Fr. Br. George <george@altlinux.ru> 2016.74-alt1
- Autobuild version bump to 2016.74

* Thu Jul 14 2016 Fr. Br. George <george@altlinux.ru> 2016.73-alt1
- Autobuild version bump to 2016.73

* Mon Dec 28 2015 Fr. Br. George <george@altlinux.ru> 2015.71-alt1
- Autobuild version bump to 2015.71

* Wed Nov 18 2015 Fr. Br. George <george@altlinux.ru> 2015.68-alt1
- Autobuild version bump to 2015.68

* Wed Jan 28 2015 Fr. Br. George <george@altlinux.ru> 2015.67-alt1
- Autobuild version bump to 2015.67

* Tue Aug 19 2014 Fr. Br. George <george@altlinux.ru> 2014.65-alt1
- Autobuild version bump to 2014.65

* Wed Apr 09 2014 Fr. Br. George <george@altlinux.ru> 2014.63-alt1
- Autobuild version bump to 2014.63

* Wed Jan 15 2014 Fr. Br. George <george@altlinux.ru> 2013.62-alt1
- Autobuild version bump to 2013.62
- Update "fingerprint expose" patch

* Sun Oct 27 2013 Fr. Br. George <george@altlinux.ru> 2013.60-alt1
- Autobuild version bump to 2013.60

* Tue Oct 15 2013 Fr. Br. George <george@altlinux.ru> 2013.59-alt1
- Autobuild version bump to 2013.59
- Fix build (patch, new manmage)

* Mon May 20 2013 Fr. Br. George <george@altlinux.ru> 2013.58-alt1
- Autobuild version bump to 2013.58

* Mon Apr 01 2013 Fr. Br. George <george@altlinux.ru> 2013.56-alt1
- Autobuild version bump to 2013.56

* Wed Mar 21 2012 Fr. Br. George <george@altlinux.ru> 2012.55-alt1
- Autobuild version bump to 2012.55

* Tue Jan 10 2012 Fr. Br. George <george@altlinux.ru> 2011.54-alt1
- Autobuild version bump to 2011.54

* Wed Sep 07 2011 Fr. Br. George <george@altlinux.ru> 0.53.1-alt1
- Autobuild version bump to 0.53.1
- Bring back client
- Introduce documentation

* Sun Oct 24 2010 Denis Smirnov <mithraen@altlinux.ru> 0.50-alt4
- rebuild

* Thu Dec 11 2008 Denis Smirnov <mithraen@altlinux.ru> 0.50-alt3
- Add conflicts dropbear-scp -> openssh

* Mon Dec 01 2008 Denis Smirnov <mithraen@altlinux.ru> 0.50-alt2
- cleanup spec

* Wed Aug 15 2007 Denis Smirnov <mithraen@altlinux.ru> 0.50-alt1
- Add DROPBEAR_PASSWORD environment variable to specify a dbclient password
- Use /dev/urandom by default, since that's what everyone does anyway
- Correct vfork() use for uClinux in scp (thanks to Alex Landau)
- Exit with an exit code of 1 if dropbear can't bind to any ports (thanks to
  Nicolai Ehemann)
- Improve network performance and add a -W <receive_window> argument for
  adjusting the tradeoff between network performance and memory consumption.
- Fix a problem where reply packets could be sent during key exchange, in
  violation of the SSH spec. This could manifest itself with connections being
  terminated after 8 hours with new TCP-forward connections being established.
- Add -K <keepalive_time> argument, ensuring that data is transmitted over the
  connection at least every N seconds.
- dropbearkey will no longer generate DSS keys of sizes other than 1024 bits,
  as required by the DSS specification. (Other sizes are still accepted for use
  to provide backwards compatibility).

* Thu Mar 01 2007 Denis Smirnov <mithraen@altlinux.ru> 0.49-alt1
- CVE-2007-1099 fix (dbclient previously would prompt to confirm a mismatching
  hostkey but wouldn't warn loudly. It will now exit upon a mismatch)
- Added -P pidfile argument to the server (from Swen Schillig)
- Add -N dbclient option for "no command"
- Add -f dbclient option for "background after auth"
- Add ability to limit binding to particular addresses, use  -p [address:]port,
  patch from Max-Gerd Retzlaff.
- Fix finding relative-path server hostkeys when running daemonized
- Use $HOME in preference to that from %_sysconfdir/passwd, so that dbclient can still
  work on broken systems.
- Fix various issues found by Klocwork defect analysis, mostly memory leaks and
  error-handling. Thanks to Klocwork for their service.
- Add compile-time LOG_COMMANDS option to log user commands
- Add '-y' flag to dbclient to unconditionally accept host keys,patch from
  Luciano Miguel Ferreira Rocha
- Return immediately for "sleep 10 & echo foo", rather thanwaiting for the
  sleep to return (pointed out by Rob Landley).
- Avoid hanging after exit in certain cases (such as scp)
- Various minor fixes, in particular various leaks reported by Erik Hovland
- Disable core dumps on startup
- Don't erase over every single buffer, since it was a bottleneck.  On systems
  where it really matters, encrypted swap should be utilised.
- Read /dev/[u]random only once at startup to conserve kernel entropy

* Sun Nov 26 2006 Denis Smirnov <mithraen@altlinux.ru> 0.48.1-alt1
- upstream version update update (0.48.1)
- fix license

* Sun Feb 05 2006 Denis Smirnov <mithraen@altlinux.ru> 0.45-alt3
- add scp subpackage

* Thu Feb 02 2006 Denis Smirnov <mithraen@altlinux.ru> 0.45-alt2
- patches from debian (typo in doc and man)

* Wed Feb 01 2006 Denis Smirnov <mithraen@altlinux.ru> 0.45-alt1
- first build for Sisyphus

