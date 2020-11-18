Name: pdfpc
Version: 4.4.1
Release: alt1
Summary: A GTK based presentation viewer application for GNU/Linux

Group: Other
License: GPLv2+
Url: https://github.com/pdfpc/pdfpc
Source: %name-%version.tar

BuildRequires(pre): rpm-macros-cmake
BuildRequires: cmake gst-plugins1.0-devel libgee0.8-devel libgtk+3-devel libpoppler-glib-devel vala

Provides: pdf-presenter-console

%description
pdfpc is a GTK based presentation viewer application for GNU/Linux which
uses Keynote like multi-monitor output to provide meta information to
the speaker during the presentation. It is able to show a normal
presentation window on one screen, while showing a more sophisticated
overview on the other one providing information like a picture of the
next slide, as well as the left over time till the end of the
presentation. The input files processed by pdfpc are PDF documents,
which can be created using nearly any of today's presentation software.

%prep
%setup

%build
%cmake \
	-DSYSCONFDIR=/etc \
	#
%cmake_build

%install
%cmakeinstall_std

%files
%doc README.rst CHANGELOG.txt
%_bindir/%name
%config(noreplace) %_sysconfdir/%{name}rc
%_mandir/man1/%{name}*
%_mandir/man5/%{name}*
%_datadir/pixmaps/%name

%changelog
* Wed Nov 18 2020 Grigory Ustinov <grenka@altlinux.org> 4.4.1-alt1
- Automatically updated to 4.4.1.

* Thu Mar 26 2020 Grigory Ustinov <grenka@altlinux.org> 4.4.0-alt1
- Automatically updated to 4.4.0.

* Wed Jul 10 2019 Grigory Ustinov <grenka@altlinux.org> 4.3.4-alt1
- New version 4.3.4.

* Fri May 17 2019 Grigory Ustinov <grenka@altlinux.org> 4.3.2-alt1
- New version 4.3.2 (Closes: #36536).

* Fri Jun 22 2018 Elvira Khabirova <lineprinter@altlinux.org> 4.1.2-alt1
- New version.
- Build directly from git.

* Tue Mar 07 2017 Elvira Khabirova <lineprinter@altlinux.org> 4.0.6-alt1
- New version 4.0.6.

* Thu Jan 19 2017 Elvira Khabirova <lineprinter@altlinux.org> 4.0.5.0.18.g0350b1a-alt1
- New version 4.0.5-18-g0350b1a.

* Tue Oct 04 2016 Gleb F-Malinovskiy <glebfm@altlinux.org> 4.0.3-alt1
- Initial build.
