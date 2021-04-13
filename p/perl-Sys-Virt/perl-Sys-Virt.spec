%define _unpackaged_files_terminate_build 1
%define dist Sys-Virt
Name: perl-%dist
Version: 7.2.0
Release: alt1

Summary: Represent and manage a libvirt hypervisor connection
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source0: http://www.cpan.org/authors/id/D/DA/DANBERR/%{dist}-v%{version}.tar.gz

# Automatically added by buildreq on Wed Oct 19 2011
BuildRequires: libvirt-devel perl-Test-Pod perl-Test-Pod-Coverage perl-XML-XPath perl(Module/Build.pm)

%description
The Sys::Virt module provides a Perl XS binding to the libvirt
virtual machine management APIs. This allows machines running
within arbitrary virtualization containers to be managed with
a consistent API.

%prep
%setup -q -n %{dist}-v%{version}

%build
export NPROCS=1
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc AUTHORS Changes README examples
%perl_vendor_archlib/Sys
%perl_vendor_autolib/Sys

%changelog
* Tue Apr 13 2021 Igor Vlasenko <viy@altlinux.org> 7.2.0-alt1
- automated CPAN update

* Mon Mar 15 2021 Igor Vlasenko <viy@altlinux.org> 7.1.0-alt1
- automated CPAN update

* Thu Jan 21 2021 Igor Vlasenko <viy@altlinux.ru> 7.0.0-alt1
- automated CPAN update

* Fri Dec 11 2020 Igor Vlasenko <viy@altlinux.ru> 6.10.0-alt1
- automated CPAN update

* Sat Oct 24 2020 Igor Vlasenko <viy@altlinux.ru> 6.8.0-alt1
- automated CPAN update

* Tue Jun 09 2020 Igor Vlasenko <viy@altlinux.ru> 6.3.0-alt1
- automated CPAN update

* Tue Mar 31 2020 Igor Vlasenko <viy@altlinux.ru> 6.1.0-alt1
- automated CPAN update

* Wed Feb 12 2020 Igor Vlasenko <viy@altlinux.ru> 6.0.0-alt1
- automated CPAN update

* Mon Oct 28 2019 Igor Vlasenko <viy@altlinux.ru> 5.8.0-alt1
- automated CPAN update

* Wed Sep 11 2019 Igor Vlasenko <viy@altlinux.ru> 5.7.0-alt1
- automated CPAN update

* Thu Aug 22 2019 Igor Vlasenko <viy@altlinux.ru> 5.6.0-alt1
- automated CPAN update

* Wed Jul 17 2019 Igor Vlasenko <viy@altlinux.ru> 5.5.0-alt1
- automated CPAN update

* Mon Jun 17 2019 Igor Vlasenko <viy@altlinux.ru> 5.4.0-alt1
- automated CPAN update

* Mon Apr 15 2019 Igor Vlasenko <viy@altlinux.ru> 5.2.0-alt1
- automated CPAN update

* Wed Mar 27 2019 Igor Vlasenko <viy@altlinux.ru> 5.1.0-alt1
- automated CPAN update

* Mon Feb 04 2019 Igor Vlasenko <viy@altlinux.ru> 5.0.0-alt1
- automated CPAN update

* Thu Jan 24 2019 Igor Vlasenko <viy@altlinux.ru> 4.10.0-alt1.1
- rebuild with new perl 5.28.1

* Mon Jan 21 2019 Igor Vlasenko <viy@altlinux.ru> 4.10.0-alt1
- automated CPAN update

* Wed Oct 24 2018 Igor Vlasenko <viy@altlinux.ru> 4.8.0-alt1
- automated CPAN update

* Thu Sep 20 2018 Igor Vlasenko <viy@altlinux.ru> 4.7.0-alt1
- automated CPAN update

* Tue Aug 14 2018 Igor Vlasenko <viy@altlinux.ru> 4.6.0-alt1
- automated CPAN update

* Fri Jul 20 2018 Igor Vlasenko <viy@altlinux.ru> 4.5.0-alt1
- automated CPAN update

* Wed Jun 06 2018 Igor Vlasenko <viy@altlinux.ru> 4.4.0-alt1
- automated CPAN update

* Thu Apr 05 2018 Igor Vlasenko <viy@altlinux.ru> 4.2.0-alt1
- automated CPAN update

* Mon Feb 19 2018 Igor Vlasenko <viy@altlinux.ru> 4.0.0-alt1
- automated CPAN update

* Mon Dec 18 2017 Igor Vlasenko <viy@altlinux.ru> 3.9.1-alt1
- automated CPAN update

* Fri Dec 15 2017 Igor Vlasenko <viy@altlinux.ru> 3.8.0-alt1.1
- rebuild with new perl 5.26.1

* Wed Nov 01 2017 Igor Vlasenko <viy@altlinux.ru> 3.8.0-alt1
- automated CPAN update

* Tue Sep 26 2017 Igor Vlasenko <viy@altlinux.ru> 3.7.0-alt1
- automated CPAN update

* Wed Aug 02 2017 Igor Vlasenko <viy@altlinux.ru> 3.5.0-alt1
- automated CPAN update

* Wed Mar 15 2017 Igor Vlasenko <viy@altlinux.ru> 3.1.0-alt1
- automated CPAN update

* Tue Feb 14 2017 Igor Vlasenko <viy@altlinux.ru> 3.0.0-alt1
- automated CPAN update

* Fri Feb 03 2017 Igor Vlasenko <viy@altlinux.ru> 2.5.0-alt1.1
- rebuild with new perl 5.24.1

* Sun Dec 18 2016 Igor Vlasenko <viy@altlinux.ru> 2.5.0-alt1
- automated CPAN update

* Thu Nov 17 2016 Igor Vlasenko <viy@altlinux.ru> 2.4.0-alt1
- automated CPAN update

* Wed Oct 19 2016 Igor Vlasenko <viy@altlinux.ru> 2.3.0-alt1
- automated CPAN update

* Mon Jul 25 2016 Igor Vlasenko <viy@altlinux.ru> 2.0.0-alt1
- automated CPAN update

* Mon Jun 13 2016 Igor Vlasenko <viy@altlinux.ru> 1.3.5-alt1
- automated CPAN update

* Sun Jun 05 2016 Igor Vlasenko <viy@altlinux.ru> 1.3.4-alt1
- automated CPAN update

* Sat Mar 19 2016 Igor Vlasenko <viy@altlinux.ru> 1.3.2-alt1
- automated CPAN update

* Mon Dec 28 2015 Igor Vlasenko <viy@altlinux.ru> 1.3.0-alt1
- automated CPAN update

* Wed Nov 25 2015 Igor Vlasenko <viy@altlinux.ru> 1.2.21-alt1.1
- rebuild with new perl 5.22.0

* Thu Nov 12 2015 Igor Vlasenko <viy@altlinux.ru> 1.2.21-alt1
- automated CPAN update

* Mon Oct 26 2015 Igor Vlasenko <viy@altlinux.ru> 1.2.19-alt1
- automated CPAN update

* Fri May 22 2015 Igor Vlasenko <viy@altlinux.ru> 1.2.15-alt1
- automated CPAN update

* Wed Apr 01 2015 Igor Vlasenko <viy@altlinux.ru> 1.2.13-alt1
- automated CPAN update

* Mon Dec 22 2014 Igor Vlasenko <viy@altlinux.ru> 1.2.11-alt1
- automated CPAN update

* Tue Dec 09 2014 Igor Vlasenko <viy@altlinux.ru> 1.2.9-alt1.1
- rebuild with new perl 5.20.1

* Tue Oct 07 2014 Igor Vlasenko <viy@altlinux.ru> 1.2.9-alt1
- automated CPAN update

* Mon Sep 15 2014 Igor Vlasenko <viy@altlinux.ru> 1.2.8-alt1
- automated CPAN update

* Tue Jul 08 2014 Igor Vlasenko <viy@altlinux.ru> 1.2.6-alt1
- automated CPAN update

* Tue Jun 10 2014 Igor Vlasenko <viy@altlinux.ru> 1.2.5-alt1
- automated CPAN update

* Tue May 13 2014 Igor Vlasenko <viy@altlinux.ru> 1.2.4-alt1
- automated CPAN update

* Wed Apr 09 2014 Igor Vlasenko <viy@altlinux.ru> 1.2.3-alt1
- automated CPAN update

* Thu Mar 06 2014 Igor Vlasenko <viy@altlinux.ru> 1.2.2-alt1
- automated CPAN update

* Thu Dec 05 2013 Igor Vlasenko <viy@altlinux.ru> 1.2.0-alt1
- automated CPAN update

* Wed Nov 06 2013 Igor Vlasenko <viy@altlinux.ru> 1.1.4-alt1
- automated CPAN update

* Tue Oct 22 2013 Igor Vlasenko <viy@altlinux.ru> 1.1.3-alt1
- automated CPAN update

* Thu Aug 29 2013 Vladimir Lettiev <crux@altlinux.ru> 1.1.1-alt1
- 1.0.5 -> 1.1.1

* Wed Jul 24 2013 Igor Vlasenko <viy@altlinux.ru> 1.0.5-alt1
- automated CPAN update

* Sun Sep 02 2012 Vladimir Lettiev <crux@altlinux.ru> 0.9.13-alt1
- 0.9.5 -> 0.9.13
- built for perl-5.16

* Wed Oct 19 2011 Alexey Tourbin <at@altlinux.ru> 0.9.5-alt1
- 0.2.6 -> 0.9.5
- built for perl-5.14

* Tue Apr 19 2011 Alexey Shabalin <shaba@altlinux.ru> 0.2.6-alt1
- 0.2.6

* Thu Nov 04 2010 Vladimir Lettiev <crux@altlinux.ru> 0.2.2-alt1.1
- rebuilt with perl 5.12

* Thu Oct 29 2009 Andriy Stepanov <stanv@altlinux.ru> 0.2.2-alt1
- Package for ALT Linux.
