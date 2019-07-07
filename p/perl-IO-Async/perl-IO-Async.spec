%define _unpackaged_files_terminate_build 1
%global oname IO-Async

Name: perl-%oname
Version: 0.74
Release: alt1

Summary: Asynchronous event-driven programming
Group: Development/Perl
License: perl

Url: %CPAN %oname
# https://cpan.metacpan.org/authors/id/P/PE/PEVANS/%oname-%version.tar.gz
Source: %oname-%version.tar
Patch1: %oname-0.71-alt-build.patch

BuildArch: noarch
BuildRequires: /proc perl(IO/Socket/IP.pm) perl(Module/Build.pm) perl(Test/Refcount.pm) perl(Future.pm) perl(Test/Fatal.pm) perl(Future/Utils.pm) perl-devel perl(Test/Identity.pm) perl(Struct/Dumb.pm) perl(Future/IO.pm)

%add_findreq_skiplist */IO/Async/MergePoint.pm

%description
%summary

%package -n perl-Future-IO-Impl-IOAsync
Summary: Future::IO Implementation using IO::Async
Group: Development/Perl
Requires: %name = %EVR

%description -n perl-Future-IO-Impl-IOAsync
Future::IO Implementation using IO::Async

%prep
%setup -q -n %oname-%version
%patch1 -p2
# on ppc64le, but ifarch did not expand here :(
#ifarch ppc64le
[ %version = 0.74 ] && rm -f t/70future-io.t
#endif

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README examples
%perl_vendor_privlib/IO/Async*

%files -n perl-Future-IO-Impl-IOAsync
%perl_vendor_privlib/Future/IO/Impl/IOAsync.pm

%changelog
* Sun Jul 07 2019 Igor Vlasenko <viy@altlinux.ru> 0.74-alt1
- new version

* Mon Jun 17 2019 Igor Vlasenko <viy@altlinux.ru> 0.73-alt2
- added perl-Future-IO-Impl-IOAsync subpackage

* Mon Jun 17 2019 Igor Vlasenko <viy@altlinux.ru> 0.73-alt1
- new version

* Thu Apr 05 2018 Igor Vlasenko <viy@altlinux.ru> 0.72-alt1
- automated CPAN update

* Fri Aug 18 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.71-alt1
- Updated to upstream version 0.71.

* Wed Nov 11 2015 Igor Vlasenko <viy@altlinux.ru> 0.69-alt1
- automated CPAN update

* Thu Oct 15 2015 Igor Vlasenko <viy@altlinux.ru> 0.68-alt1
- automated CPAN update

* Wed Dec 17 2014 Igor Vlasenko <viy@altlinux.ru> 0.64-alt1
- automated CPAN update

* Fri Jul 25 2014 Igor Vlasenko <viy@altlinux.ru> 0.63-alt1
- automated CPAN update

* Tue Jun 24 2014 Igor Vlasenko <viy@altlinux.ru> 0.62-alt1
- automated CPAN update

* Sat Dec 14 2013 Vladimir Lettiev <crux@altlinux.ru> 0.61-alt1
- initial build for ALTLinux

