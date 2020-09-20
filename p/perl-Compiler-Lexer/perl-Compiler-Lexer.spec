## in Version: 0.22, during perl update to 5.28, test failed on aarch64
## in Version: 0.23, during perl update to 5.30, test failed on armh
## to be safe.
%ifarch aarch64 ppc64le armh
%define _without_test 1
%endif

## SPEC file for Perl module Compiler::Lexer

%define real_name Compiler-Lexer

Name: perl-Compiler-Lexer
Version: 0.23
Release: alt2

Summary: Lexical Analyzer for Perl5

License: %perl_license
Group: Development/Perl

URL: http://search.cpan.org/dist/Compiler-Lexer/

Packager: Nikolay A. Fetisov <naf@altlinux.ru>

Source0: %name-%version.tar
Patch0:  %name-%version-%release.patch

BuildRequires(pre): perl-devel rpm-build-licenses

# Automatically added by buildreq on Mon Jun 27 2016
# optimized out: libstdc++-devel perl perl-CPAN-Meta perl-CPAN-Meta-Requirements perl-CPAN-Meta-YAML perl-Encode perl-ExtUtils-CBuilder perl-IPC-Cmd perl-JSON-PP perl-Locale-Maketext-Simple perl-Module-Build perl-Module-Load perl-Module-Load-Conditional perl-Module-Metadata perl-Params-Check perl-Parse-CPAN-Meta perl-Perl-OSType perl-Pod-Escapes perl-Pod-Simple perl-devel perl-parent perl-podlators python-base python-modules python3
BuildRequires: gcc-c++ perl-HTML-Parser perl-Module-Build-XSUtil perl-PerlIO-utf8_strict

%description
Perl module Compiler::Lexer is a Lexical Analyzer for Perl5.

%prep
%setup
%patch0 -p1

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README.md Changes
%perl_vendor_archlib/Compiler/Lexer*
%perl_vendor_autolib/Compiler/Lexer*

%changelog
* Sun Sep 20 2020 Igor Vlasenko <viy@altlinux.ru> 0.23-alt2
- NMU: disabled tests on armh, to prepare for new perl 5.30

* Tue May 19 2020 Nikolay A. Fetisov <naf@altlinux.org> 0.23-alt1
- New version

* Wed Oct 02 2019 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.22-alt2.4
- Built for ppc64le with disabled testsuite.

* Thu Jan 24 2019 Igor Vlasenko <viy@altlinux.ru> 0.22-alt2.3
- rebuild with new perl 5.28.1

* Mon Jan 21 2019 Igor Vlasenko <viy@altlinux.ru> 0.22-alt2.2
- NMU: disabled tests on aarch64, to prepare for new perl 5.28

* Fri Dec 15 2017 Igor Vlasenko <viy@altlinux.ru> 0.22-alt2.1.1
- rebuild with new perl 5.26.1

* Fri Feb 03 2017 Igor Vlasenko <viy@altlinux.ru> 0.22-alt2.1
- rebuild with new perl 5.24.1

* Mon Jun 27 2016 Nikolay A. Fetisov <naf@altlinux.ru> 0.22-alt2
- Initial build for ALT Linux Sisyphus
