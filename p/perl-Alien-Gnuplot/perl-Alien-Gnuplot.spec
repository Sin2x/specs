%define module_name Alien-Gnuplot
# BEGIN SourceDeps(oneline):
BuildRequires: perl(Test/Exception.pm)
# END SourceDeps(oneline)
BuildRequires: gnuplot
%define _unpackaged_files_terminate_build 1
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 1.034
Release: alt2
Summary: Find and verify functionality of the gnuplot executable.
Group: Development/Perl
License: perl
URL: http://github.com/drzowie/Alien-Gnuplot

Source0: http://mirror.yandex.ru/mirrors/cpan/authors/id/E/ET/ETJ/%{module_name}-%{version}.tar.gz
BuildArch: noarch

# upstream overrides version
# ALT prohibits multiple provides
# so edit provides inplace
%define gnuplotver %(rpmquery --qf '%%{VERSION}' gnuplot 2>/dev/null || echo 5.5)
%filter_from_provides /^perl.Alien.Gnuplot.pm./s,%version,%gnuplotver,

%description
%summary

%prep
%setup -q -n %{module_name}-%{version}

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README*
%perl_vendor_privlib/A*

%changelog
* Thu Nov 18 2021 Igor Vlasenko <viy@altlinux.org> 1.034-alt2
- Sisyphus build

* Wed Jul 28 2021 Igor Vlasenko <viy@altlinux.ru> 1.034-alt1
- updated by package builder

* Sun Feb 26 2017 Igor Vlasenko <viy@altlinux.ru> 1.033-alt1
- regenerated from template by package builder

* Fri Mar 07 2014 Igor Vlasenko <viy@altlinux.ru> 1.030-alt1
- initial import by package builder

