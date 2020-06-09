%define _unpackaged_files_terminate_build 1
%define module_name YAML-PP
# BEGIN SourceDeps(oneline):
BuildRequires: perl(B.pm) perl(B/Deparse.pm) perl(Carp.pm) perl(Cpanel/JSON/XS.pm) perl(Data/Dump.pm) perl(Data/Dumper.pm) perl(Encode.pm) perl(Encode/CN.pm) perl(Encode/JP.pm) perl(Encode/KR.pm) perl(Encode/TW.pm) perl(Exporter.pm) perl(ExtUtils/MakeMaker.pm) perl(File/Basename.pm) perl(File/Spec.pm) perl(FindBin.pm) perl(HTML/Entities.pm) perl(IO/All.pm) perl(IO/Handle.pm) perl(IPC/Open3.pm) perl(JSON.pm) perl(JSON/PP.pm) perl(JSON/XS.pm) perl(MIME/Base64.pm) perl(Module/Load.pm) perl(Mojo/JSON.pm) perl(Mojolicious.pm) perl(Scalar/Util.pm) perl(Term/ANSIColor.pm) perl(Test/Deep.pm) perl(Test/More.pm) perl(Test/Warn.pm) perl(Text/Table.pm) perl(URI/Escape.pm) perl(YAML.pm) perl(YAML/Syck.pm) perl(YAML/Tiny.pm) perl(YAML/XS.pm) perl(base.pm) perl(blib.pm) perl(boolean.pm) perl(constant.pm) perl(lib.pm) perl(overload.pm)
BuildRequires: perl(strict.pm) perl(warnings.pm)
# END SourceDeps(oneline)
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 0.022
Release: alt1
Summary: YAML Parser and Loader
Group: Development/Perl
License: perl
Url: %CPAN %module_name

Source0: http://www.cpan.org/authors/id/T/TI/TINITA/%{module_name}-%{version}.tar.gz
BuildArch: noarch

%description
This is Yet Another YAML Parser. For why this project was started, see
the section on "WHY".

This project contains a Parser the YAML::PP::Parser manpage and a Loader
the YAML::PP::Loader manpage.

%package scripts
Summary: %module_name scripts
Group: Development/Perl
Requires: %name = %{?epoch:%epoch:}%version-%release

%description scripts
scripts for %module_name
%prep
%setup -q -n %{module_name}-%{version}

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README CONTRIBUTING.md Changes examples
%perl_vendor_privlib/Y*

%files scripts
%_bindir/*

%changelog
* Tue Jun 09 2020 Igor Vlasenko <viy@altlinux.ru> 0.022-alt1
- automated CPAN update

* Tue Mar 03 2020 Igor Vlasenko <viy@altlinux.ru> 0.021-alt1
- automated CPAN update

* Tue Feb 25 2020 Igor Vlasenko <viy@altlinux.ru> 0.020-alt1
- automated CPAN update

* Mon Feb 24 2020 Igor Vlasenko <viy@altlinux.ru> 0.019-alt2
- to Sisyphus as perl-Pegex dep

* Fri Feb 14 2020 Igor Vlasenko <viy@altlinux.ru> 0.019-alt1
- updated by package builder

* Sun Jul 07 2019 Igor Vlasenko <viy@altlinux.ru> 0.018-alt1
- updated by package builder

* Sun Jun 30 2019 Igor Vlasenko <viy@altlinux.ru> 0.017-alt1
- updated by package builder

* Tue May 21 2019 Igor Vlasenko <viy@altlinux.ru> 0.016-alt1
- updated by package builder

* Fri May 17 2019 Igor Vlasenko <viy@altlinux.ru> 0.015-alt1
- updated by package builder

* Fri May 10 2019 Igor Vlasenko <viy@altlinux.ru> 0.014-alt1
- updated by package builder

* Wed May 01 2019 Igor Vlasenko <viy@altlinux.ru> 0.013-alt1
- updated by package builder

* Mon Apr 15 2019 Igor Vlasenko <viy@altlinux.ru> 0.012-alt1
- updated by package builder

* Mon Mar 25 2019 Igor Vlasenko <viy@altlinux.ru> 0.011-alt1
- updated by package builder

* Sun Nov 04 2018 Igor Vlasenko <viy@altlinux.ru> 0.010-alt1
- regenerated from template by package builder

* Tue Oct 02 2018 Igor Vlasenko <viy@altlinux.ru> 0.009-alt1
- regenerated from template by package builder

* Thu Jun 21 2018 Igor Vlasenko <viy@altlinux.ru> 0.007-alt1
- regenerated from template by package builder

* Wed Apr 04 2018 Igor Vlasenko <viy@altlinux.ru> 0.006-alt1
- regenerated from template by package builder

* Sat Nov 25 2017 Igor Vlasenko <viy@altlinux.ru> 0.005-alt1
- regenerated from template by package builder

* Sun Sep 24 2017 Igor Vlasenko <viy@altlinux.ru> 0.004-alt1
- regenerated from template by package builder

* Wed May 03 2017 Igor Vlasenko <viy@altlinux.ru> 0.002-alt1
- initial import by package builder

