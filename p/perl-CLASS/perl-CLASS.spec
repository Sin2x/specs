%define _unpackaged_files_terminate_build 1
#
#   - CLASS -
#   This spec file was automatically generated by cpan2rpm [ver: 2.028]
#   (ALT Linux revision)
#   The following arguments were used:
#       '--packager=Igor Vlasenko <viy@altlinux.ru>' --url http://search.cpan.org/CPAN/authors/id/M/MS/MSCHWERN/CLASS-1.00.tar.gz http://search.cpan.org/CPAN/authors/id/M/MS/MSCHWERN/CLASS-1.00.tar.gz
#   For more information on cpan2rpm please visit: http://perl.arix.com/
#

%define module CLASS
%define m_distro CLASS
%define m_name CLASS
%define m_author_id unknown
%define _enable_test 1

Name: perl-CLASS
Version: 1.1.7
Release: alt1

Summary: Alias for __PACKAGE__

License: Artistic
Group: Development/Perl
Url: http://search.cpan.org/CPAN/authors/id/M/MS/MSCHWERN/CLASS-1.00.tar.gz

Packager: Igor Vlasenko <viy@altlinux.ru>

BuildArch: noarch
Source0: http://www.cpan.org/authors/id/J/JD/JDEGUEST/%{module}-v%{version}.tar.gz

# Automatically added by buildreq on Thu Sep 29 2011
BuildRequires: perl-devel

%description
CLASS and $CLASS are both synonyms for __PACKAGE__.  Easier to type.

$CLASS has the additional benefit of working in strings.

%prep
%setup -q -n %{module}-v%{version}
%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README Changes
%perl_vendor_privlib/CLASS*

%changelog
* Fri Mar 25 2022 Igor Vlasenko <viy@altlinux.org> 1.1.7-alt1
- automated CPAN update

* Thu Sep 29 2011 Igor Vlasenko <viy@altlinux.ru> 1.00-alt1
- initial build for ALT Linux Sisyphus

