%define _unpackaged_files_terminate_build 1
Name: perl-JavaScript-Minifier
Version: 1.16
Release: alt1

Summary: JavaScript::Minifier - Perl extension for minifying JavaScript code
Group: Development/Perl
License: Perl

Url: %CPAN JavaScript-Minifier
Source: %name-%version.tar

BuildArch: noarch
BuildRequires: perl-devel

%description
%summary

%prep
%setup -q

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README.md README examples
%perl_vendor_privlib/JavaScript/Minifier*
%doc Changes README

%changelog
* Fri Mar 05 2021 Igor Vlasenko <viy@altlinux.org> 1.16-alt1
- new version

* Wed Feb 10 2021 Igor Vlasenko <viy@altlinux.ru> 1.15-alt1
- new version

* Thu Oct 15 2015 Igor Vlasenko <viy@altlinux.ru> 1.14-alt1
- automated CPAN update

* Wed Dec 17 2014 Igor Vlasenko <viy@altlinux.ru> 1.12-alt1
- automated CPAN update

* Tue Jun 24 2014 Igor Vlasenko <viy@altlinux.ru> 1.11-alt1
- automated CPAN update

* Tue Jan 15 2013 Vladimir Lettiev <crux@altlinux.ru> 1.05-alt1
- initial build for ALTLinux

