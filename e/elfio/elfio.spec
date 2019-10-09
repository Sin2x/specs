Group: Other
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%global debug_package %{nil}

Name:           elfio
Version:        3.4
Release:        alt2_11
Summary:        C++ library for reading and generating ELF files

License:        MIT
URL:            http://elfio.sourceforge.net/
Source0:        https://downloads.sf.net/elfio/elfio-%{version}.tar.gz

BuildRequires:  gcc-c++
Source44: import.info

%description
ELFIO is a small, header-only C++ library that provides a simple interface for
reading and generating files in ELF binary format.

It is used as a standalone library - it is not dependent on any other product
or project. Adhering to ISO C++, it compiles on a wide variety of
architectures and compilers.

While the library is easy to use, some basic knowledge of the ELF binary
format is required. Such Information can easily be found on the Web.


%package devel
Group: Other
Summary:        %{summary}
Provides:       %{name}-static = %{version}-%{release}
BuildArch:      noarch

%description devel
ELFIO is a small, header-only C++ library that provides a simple interface for
reading and generating files in ELF binary format.

It is used as a standalone library - it is not dependent on any other product
or project. Adhering to ISO C++, it compiles on a wide variety of
architectures and compilers.

While the library is easy to use, some basic knowledge of the ELF binary
format is required. Such Information can easily be found on the Web.


%prep
%setup -q
%ifarch %e2k
# -std=c++03 by default as of lcc 1.23.20
%add_optflags -std=c++11
%endif

%build
%configure
%make_build


%install
%makeinstall_std
# Binaries are the examples and have too generic names: elfdump tutorial write_obj writer
rm %{buildroot}%{_bindir}/*


%check
# Sanity check
examples/elfdump/elfdump %{_bindir}/make

%files devel
%doc --no-dereference COPYING
%doc AUTHORS doc/elfio.pdf README
%{_includedir}/elfio/


%changelog
* Wed Oct 09 2019 Michael Shigorin <mike@altlinux.org> 3.4-alt2_11
- E2K: explicit -std=c++11

* Mon Sep 30 2019 Igor Vlasenko <viy@altlinux.ru> 3.4-alt1_11
- new version

