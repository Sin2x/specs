%define rev r1888502

Name: spamassassin-rules
Version: 3.4.6
Release: alt1

Summary: Rules for SpamAssassin
License: Apache-2.0
Group: Networking/Mail

URL: http://spamassassin.org/
Source: http://www.apache.org/dist/spamassassin/source/Mail-SpamAssassin-rules-%version.%rev.tgz

BuildArch: noarch

# We should require package that contains /usr/share/spamassassin (as we put files in this directory)
# Note this reason here to correctly change requirement in case of package rearrangements.
Requires: perl-Mail-SpamAssassin >= %version
Conflicts: perl-Mail-SpamAssassin < %version

%description
This package contains the default packaged rules for SpamAssassin.

%prep
%setup -c -T -n %name-%version -a0

%build

%install
install -d %buildroot%_datadir/spamassassin
install -pm644 *.cf %buildroot%_datadir/spamassassin

%files
%_datadir/spamassassin

%changelog
* Wed Nov 02 2022 L.A. Kostis <lakostis@altlinux.ru> 3.4.6-alt1
- 3.4.6 (r1888502).

* Thu Mar 25 2021 L.A. Kostis <lakostis@altlinux.ru> 3.4.5-alt1
- 3.4.5 (r1887800)

* Wed Oct 21 2020 Sergey Y. Afonin <asy@altlinux.org> 3.4.4-alt1
- 3.4.4 (r1873061)

* Fri Jan 03 2020 Sergey Y. Afonin <asy@altlinux.org> 3.4.3-alt1
- 3.4.3 (r1871124)
- updated %%License to SPDX syntax

* Mon Dec 31 2018 Igor Vlasenko <viy@altlinux.ru> 3.4.2-alt1
- 3.4.2 (r1840640)

* Sun Nov 15 2015 Sergey Y. Afonin <asy@altlinux.ru> 3.4.1-alt1
- 3.4.1 (r1675274)

* Thu Jun 19 2014 Sergey Y. Afonin <asy@altlinux.ru> 3.4.0-alt1
- 3.4.0 (r1565117)

* Sat Jul 23 2011 Victor Forsiuk <force@altlinux.org> 3.3.2-alt1
- 3.3.2

* Fri Oct 08 2010 Victor Forsiuk <force@altlinux.org> 3.3.1-alt1
- 3.3.1

* Wed Mar 03 2010 Victor Forsiuk <force@altlinux.org> 3.3.0-alt1
- Initial build.
