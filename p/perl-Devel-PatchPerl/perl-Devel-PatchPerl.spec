%define _unpackaged_files_terminate_build 1
Name: perl-Devel-PatchPerl
Version: 2.02
Release: alt1

Summary: Patch perl source a la Devel::PPPort's buildperl.pl
Group: Development/Perl
License: perl

Url: %CPAN Devel-PatchPerl
Source: %name-%version.tar

BuildArch: noarch
BuildRequires: perl-Module-Pluggable perl-File-pushd perl-devel perl-IPC-Cmd

%description
%summary

%prep
%setup -q

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%_bindir/patchperl
%_man1dir/patchperl*
%perl_vendor_privlib/Devel/PatchPerl*
%doc Changes README

%changelog
* Wed Nov 18 2020 Igor Vlasenko <viy@altlinux.ru> 2.02-alt1
- new version

* Sat Jun 06 2020 Igor Vlasenko <viy@altlinux.ru> 2.00-alt1
- new version

* Mon Apr 27 2020 Igor Vlasenko <viy@altlinux.ru> 1.92-alt1
- new version

* Sat Mar 14 2020 Igor Vlasenko <viy@altlinux.ru> 1.90-alt1
- new version

* Mon Feb 17 2020 Igor Vlasenko <viy@altlinux.ru> 1.86-alt1
- new version

* Wed Nov 27 2019 Igor Vlasenko <viy@altlinux.ru> 1.80-alt1
- new version

* Tue Nov 19 2019 Igor Vlasenko <viy@altlinux.ru> 1.78-alt1
- new version

* Thu Nov 07 2019 Igor Vlasenko <viy@altlinux.ru> 1.66-alt1
- new version

* Mon Jun 17 2019 Igor Vlasenko <viy@altlinux.ru> 1.64-alt1
- new version

* Wed Jun 05 2019 Igor Vlasenko <viy@altlinux.ru> 1.62-alt1
- new version

* Tue May 21 2019 Igor Vlasenko <viy@altlinux.ru> 1.60-alt1
- new version

* Mon Apr 29 2019 Igor Vlasenko <viy@altlinux.ru> 1.58-alt1
- new version

* Tue Feb 26 2019 Igor Vlasenko <viy@altlinux.ru> 1.56-alt1
- new version

* Tue Feb 19 2019 Igor Vlasenko <viy@altlinux.ru> 1.54-alt1
- new version

* Tue Jun 26 2018 Igor Vlasenko <viy@altlinux.ru> 1.52-alt1
- automated CPAN update

* Fri Feb 17 2017 Igor Vlasenko <viy@altlinux.ru> 1.48-alt1
- automated CPAN update

* Tue Dec 20 2016 Igor Vlasenko <viy@altlinux.ru> 1.46-alt1
- automated CPAN update

* Sun Sep 25 2016 Igor Vlasenko <viy@altlinux.ru> 1.44-alt1
- automated CPAN update

* Thu May 26 2016 Igor Vlasenko <viy@altlinux.ru> 1.42-alt1
- automated CPAN update

* Thu Mar 03 2016 Igor Vlasenko <viy@altlinux.ru> 1.40-alt1
- automated CPAN update

* Thu Oct 15 2015 Igor Vlasenko <viy@altlinux.ru> 1.38-alt1
- automated CPAN update

* Thu Dec 25 2014 Igor Vlasenko <viy@altlinux.ru> 1.30-alt1
- automated CPAN update

* Wed Dec 17 2014 Igor Vlasenko <viy@altlinux.ru> 1.28-alt1
- automated CPAN update

* Tue Jun 24 2014 Igor Vlasenko <viy@altlinux.ru> 1.24-alt1
- automated CPAN update

* Tue Sep 10 2013 Vladimir Lettiev <crux@altlinux.ru> 1.10-alt1
- 0.94 -> 1.10

* Tue Sep 10 2013 Vladimir Lettiev <crux@altlinux.ru> 0.94-alt1
- 0.76 -> 0.94

* Wed Oct 10 2012 Vladimir Lettiev <crux@altlinux.ru> 0.76-alt2
- packaged patchperl

* Wed Oct 10 2012 Vladimir Lettiev <crux@altlinux.ru> 0.76-alt1
- initial build for ALTLinux

