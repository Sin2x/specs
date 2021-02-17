Name: gsimplecal
Version: 2.2
Release: alt1

Summary: Simple and lightweight GTK calendar
License: BSD-3-Clause
Group: Office
Url: https://github.com/dmedvinsky/gsimplecal/

# https://github.com/dmedvinsky/gsimplecal.git
Source: %name-%version.tar

BuildRequires: gcc-c++ libgtk+3-devel

%description
%name is a lightweight calendar application written in C++ using GTK2.

It was intentionally made for use with tint2 panel in the openbox
environment to be launched upon clock click, but of course it will work
without it.

%prep
%setup

%build
%autoreconf
%configure
%make_build

%install
%makeinstall_std

%files
%_bindir/%name
%_man1dir/*

%changelog
* Wed Feb 17 2021 Leontiy Volodin <lvol@altlinux.org> 2.2-alt1
- Version 2.2

* Mon Sep 08 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0-alt1.git20140809
- Version 2.0

* Fri Apr 19 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 0.8-alt1.qa1
- NMU: rebuilt for updated dependencies.

* Mon May 9 2011 Egor Glukhov <kaman@altlinux.org> 0.8-alt1
- Initial build
