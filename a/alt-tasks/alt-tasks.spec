Name: alt-tasks
Version: 0.2.0
Release: alt1

Summary: Utility for observing ALT Linux tasks
License: GPLv3
Group: Other

Packager: Alexey Appolonov <alexey@altlinux.org>

# http://git.altlinux.org/people/alexey/packages/?p=alt-tasks.git
Source: %{name}-%{version}.tar

BuildRequires: golang

%description
%{name} recursively searches for and parses all "d-t-s-evr.list" files in
specified directories, then selects and prints out those tasks that satisfy
a given criteria.

%prep
%setup

%build
%make_build

%install
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_defaultdocdir}/%{name}
cp %{name}  %{buildroot}%{_bindir}
cp COPYING readme.txt %{buildroot}%{_defaultdocdir}/%{name}

%files
%{_bindir}/%{name}
%{_defaultdocdir}/%{name}

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

%changelog
* Fri Jun 19 2020 Alexey Appolonov <alexey@altlinux.org> 0.2.0-alt1
- Improved performance by the use of binary dumps.

* Tue May 12 2020 Alexey Appolonov <alexey@altlinux.org> 0.1.0-alt1
- Initial release.
