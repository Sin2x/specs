Name:		ltxml
Version:	1.2.7
Release:	alt4
License:	GPL
Group:		Text tools
Summary:	LT XML toolkit

Requires:	zlib

URL:		http://www.ltg.ed.ac.uk/software/xml/
Source:		ftp://ftp.cogsci.ed.ac.uk/pub/LTXML/%{name}-%{version}.tar.gz
Patch:		%{name}-1.2.7-configure.in.patch
Patch1:     ltxml-without-sys_errlist.patch

BuildRequires:	autoconf zlib-devel

%description
The LT XML tool-kit includes stand-alone tools for a
wide range of processing of well-formed XML documents,
including searching and extracting, down-translation
(e.g. report generation, formatting), tokenising and sorting.

Sequences of tool applications can be pipelined together
to achieve complex results.

%package devel
Summary:	LT XML API libraries and header files
Group:		Development/C
Requires:	zlib-devel

%description devel
LT XML API libraries and header files.

%prep
%setup -q -n %{name}-%{version}/XML
%patch -p2
%patch1 -p3

%build
%__autoconf
%add_optflags %optflags_shared -fcommon
%configure --enable-multi-byte
%__make all

%install
%__make install \
	prefix=%{buildroot}/%{_prefix} \
	includedir=%{buildroot}/%{_includedir} \
	libdir=%{buildroot}/%{_libdir} \
	bindir=%{buildroot}/%{_bindir} \
	MANDIR=%{buildroot}/%{_mandir}

%if "%_libexecdir" != "%_libdir"
mv %buildroot%_libexecdir/ltxml* %buildroot%_libdir/
%endif

rm -fv %buildroot%_libdir/*.a

%files
%doc doc ../{00README,00COPYRIGHT,00CHANGES,COPYING}
%{_bindir}/*
%{_libdir}/%{name}*
%{_mandir}/*/*

%files devel
%{_includedir}/*

%changelog
* Tue Oct 12 2021 Grigory Ustinov <grenka@altlinux.org> 1.2.7-alt4
- Fixed FTBFS.

* Thu Apr 08 2021 Grigory Ustinov <grenka@altlinux.org> 1.2.7-alt3
- Fixed FTBFS.

* Mon Jun 06 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.2.7-alt2.1
- (AUTO) subst_x86_64.

* Mon Jan 27 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.7-alt2
- Restored in Sisyphus

* Sat Feb 05 2005 Dimitry V. Ketov <dketov@altlinux.ru> 1.2.7-alt1
- initial build for Sisyphus;
- build static libraries with the -fPIC to reuse their objects in
  the shared ones.

