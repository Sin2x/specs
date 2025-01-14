%define _unpackaged_files_terminate_build 1
#
#   - Tie::Cycle -
#   This spec file was automatically generated by cpan2rpm [ver: 2.028]
#   (ALT Linux revision)
#   The following arguments were used:
#       Tie::Cycle
#   For more information on cpan2rpm please visit: http://perl.arix.com/
#

%define module Tie-Cycle
%define m_distro Tie-Cycle
%define m_name Tie::Cycle
%define m_author_id unknown
%define _enable_test 1

Name: perl-Tie-Cycle
Version: 1.227
Release: alt1

Summary: Cycle through a list of values via a scalar

License: Artistic
Group: Development/Perl
Url: http://www.cpan.org

Packager: Kirill Maslinsky <kirill@altlinux.org>

BuildArch: noarch
Source0: http://www.cpan.org/authors/id/B/BD/BDFOY/%{module}-%{version}.tar.gz

BuildRequires: perl-devel

%description
You use `Tie::Cycle' to go through a list over and over again.
Once you get to the end of the list, you go back to the beginning.
You don't have to worry about any of this since the magic of
tie does that for you.

The tie takes an array reference as its third argument. The tie
should succeed unless the argument is not an array reference.
Previous versions required you to use an array that had more
than one element (what's the pointing of looping otherwise?),
but I've removed that restriction since the number of elements
you want to use may change depending on the situation.

During the tie, this module makes a shallow copy of the array
reference. If the array reference contains references, and those
references are changed after the tie, the elements of the cycle
will change as well. See the included test.pl script for an
example of this effect.

%prep
%setup -q -n %{module}-%{version}
%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc CONTRIBUTING.md README.pod Changes examples
%perl_vendor_privlib/Tie/*

%changelog
* Wed Jan 19 2022 Igor Vlasenko <viy@altlinux.org> 1.227-alt1
- automated CPAN update

* Fri Jan 15 2021 Igor Vlasenko <viy@altlinux.ru> 1.226-alt1
- automated CPAN update

* Wed Aug 02 2017 Igor Vlasenko <viy@altlinux.ru> 1.225-alt1
- automated CPAN update

* Tue May 09 2017 Igor Vlasenko <viy@altlinux.ru> 1.224-alt1
- automated CPAN update

* Tue Feb 14 2017 Igor Vlasenko <viy@altlinux.ru> 1.222-alt1
- automated CPAN update

* Wed Feb 10 2016 Igor Vlasenko <viy@altlinux.ru> 1.221-alt1
- automated CPAN update

* Tue Oct 07 2014 Igor Vlasenko <viy@altlinux.ru> 1.21-alt1
- automated CPAN update

* Tue Aug 19 2014 Igor Vlasenko <viy@altlinux.ru> 1.20-alt1
- automated CPAN update

* Wed Oct 09 2013 Igor Vlasenko <viy@altlinux.ru> 1.19-alt1
- automated CPAN update

* Thu Jan 24 2013 Kirill Maslinsky <kirill@altlinux.org> 1.17-alt1
- initial build for ALT Linux Sisyphus

