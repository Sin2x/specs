Name: pamtester
Version: 0.1.2
Release: alt2
Epoch: 1
License: GPL
Group: Accessibility
Summary: Utility for testing pluggable authentication modules (PAM) facility
Url: http://pamtester.sourceforge.net/

BuildRequires: pam-devel

Source: %name-%version.tar

Patch: %name-%version-nulluser.patch

%description
pamtester is a tiny utility program to test the pluggable authentication
modules (PAM) facility, which is a de facto standard of unified authentication
management mechanism in many unices and similar OSes including Solaris, HP-UX,
*BSD, MacOSX and Linux.

%prep
%setup
%patch -p1

%build
%autoreconf
%configure
%make

%install
%make_install DESTDIR=%buildroot install

%files
%_bindir/pamtester
%_man1dir/pamtester.*

%changelog
* Wed Mar 18 2020 Paul Wolneykien <manowar@altlinux.org> 1:0.1.2-alt2
- Allow to pass "NULL" or "" as a username to skip PAM_USER setting (patch).

* Wed Feb 05 2020 Mikhail Novosyolov <mikhailnov@altlinux.org> 1:0.1.2-alt1
- NMU: fixed typo in version (0.1.12 -> 0.1.2), bumped epoch (Closes: 38036)

* Thu Mar 22 2018 Igor Vlasenko <viy@altlinux.ru> 0.1.12-alt1.qa2
- NMU: added URL

* Mon Apr 15 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 0.1.12-alt1.qa1
- NMU: rebuilt for debuginfo.

* Wed Jan 26 2011 Afanasov Dmitry <ender@altlinux.org> 0.1.12-alt1
- initial build
