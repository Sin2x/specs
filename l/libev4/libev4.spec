%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%set_verify_elf_method strict

%{?optflags_lto:%global optflags_lto %optflags_lto -ffat-lto-objects}

%set_automake_version 1.11

Name:		libev4
Version:	4.33
Release:	alt2
Summary:	libev - an event notification library
License:	BSD or GPL v2+
URL:		http://software.schmorp.de/pkg/libev
Group:		System/Libraries

# Source-url: http://dist.schmorp.de/libev/libev-%version.tar.gz
Source:		%name-%version.tar
Source1:	libev.pc.in
Source2:	%name.watch

%description
The libev API provides a mechanism to execute a callback function when
a specific event occurs on a file descriptor or after a timeout has
been reached. It is meant to replace the asynchronous event loop found
in event-driven network servers.

%package -n libev-devel
Summary:	Header files for libev library
Group:		Development/C
Requires:	%name = %EVR

%description -n libev-devel
Header files for libev library.

%package -n libev-devel-static
Summary:	Static libev library
Group:		Development/C
Requires:	libev-devel = %EVR

%description -n libev-devel-static
Static libev library.

%prep
%setup
# Add pkgconfig support
cp -p %{SOURCE1} .
sed -i.pkgconfig -e 's|Makefile|Makefile libev.pc|' configure.ac configure
sed -i.pkgconfig -e 's|lib_LTLIBRARIES|pkgconfigdir = $(libdir)/pkgconfig\n\npkgconfig_DATA = libev.pc\n\nlib_LTLIBRARIES|' Makefile.am Makefile.in

%build
%add_optflags -D_FILE_OFFSET_BITS=64

aclocal
automake
%autoreconf
%configure --with-pic
#--disable-static
%make_build

%install
%makeinstall

# move to libev and create compat symlinks
pushd %buildroot%_includedir/
mkdir libev
mv *.h libev/
ln -s libev/ev.h libev/ev++.h .
popd

%files
%doc Changes LICENSE README
%_libdir/libev.so.*

%files -n libev-devel
%_libdir/libev.so
%_includedir/ev.h
%_includedir/ev++.h
%_includedir/libev
%_libdir/pkgconfig/libev.pc
%_man3dir/*

%files -n libev-devel-static
%_libdir/libev.a

%changelog
* Mon Oct 11 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 4.33-alt2
- Fixed build with LTO

* Sun Jan 24 2021 Pavel Vainerman <pv@altlinux.ru> 4.33-alt1
- new version (4.33) with rpmgs script

* Sun Jan 26 2020 Pavel Vainerman <pv@altlinux.ru> 4.24-alt2
- added patch for c++11 ot higher

* Mon Mar 27 2017 Denis Smirnov <mithraen@altlinux.ru> 4.24-alt1
- new version 4.24

* Wed Dec 23 2015 Denis Smirnov <mithraen@altlinux.ru> 4.22-alt1
- new version 4.22

* Wed Jun 24 2015 Denis Smirnov <mithraen@altlinux.ru> 4.20-alt1
- new version 4.20

* Sun Sep 28 2014 Denis Smirnov <mithraen@altlinux.ru> 4.19-alt1
- new version 4.19

* Mon Sep 15 2014 Denis Smirnov <mithraen@altlinux.ru> 4.18-alt1
- new version 4.18

* Mon Sep 15 2014 Denis Smirnov <mithraen@altlinux.ru> 4.15-alt2
- add watch-file

* Thu Nov 28 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.15-alt1.1
- Fixed build

* Tue Sep 10 2013 Denis Smirnov <mithraen@altlinux.ru> 4.15-alt1
- 4.15

* Sat Oct 13 2012 Denis Smirnov <mithraen@altlinux.ru> 4.11-alt1
- 4.11

* Sat Dec 17 2011 Igor Vlasenko <viy@altlinux.ru> 4.04-alt1
- 4.04

* Mon Dec 06 2010 Denis Smirnov <mithraen@altlinux.ru> 4.0.1-alt1
- 4.0.1

* Mon Nov 01 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.43-alt3
- Rebuilt for soname set-versions

* Tue Mar 09 2010 Timur Batyrshin <erthad@altlinux.org> 3.43-alt2
- removed obsolete %post/%postun sections

* Tue Aug 26 2008 Kirill A. Shutemov <kas@altlinux.ru> 3.43-alt1
- First build for ALT Linux
