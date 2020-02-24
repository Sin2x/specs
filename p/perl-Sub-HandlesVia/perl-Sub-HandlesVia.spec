# BEGIN SourceDeps(oneline):
BuildRequires: perl(Class/Method/Modifiers.pm) perl(Class/Tiny.pm) perl(Eval/TypeTiny.pm) perl(Exporter/Shiny.pm) perl(ExtUtils/MakeMaker.pm) perl(List/Util.pm) perl(Moo.pm) perl(Moo/Role.pm) perl(MooX/TypeTiny.pm) perl(Moose.pm) perl(Moose/Role.pm) perl(Moose/Util.pm) perl(Moose/Util/TypeConstraints.pm) perl(MooseX/ArrayRef.pm) perl(MooseX/InsideOut.pm) perl(Mouse.pm) perl(Mouse/Role.pm) perl(Mouse/Util.pm) perl(Mouse/Util/TypeConstraints.pm) perl(Role/Tiny.pm) perl(Test/Fatal.pm) perl(Test/Moose.pm) perl(Test/More.pm) perl(Test/Requires.pm) perl(Type/Params.pm) perl(Types/Standard.pm)
# END SourceDeps(oneline)
%define module_name Sub-HandlesVia
%define _unpackaged_files_terminate_build 1
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 0.013
Release: alt1
Summary: alternative handles_via implementation
Group: Development/Perl
License: perl
URL: https://metacpan.org/release/Sub-HandlesVia

Source0: http://mirror.yandex.ru/mirrors/cpan/authors/id/T/TO/TOBYINK/%{module_name}-%{version}.tar.gz
BuildArch: noarch

%description
If you've used the Moose manpage's native attribute traits, or the MooX::HandlesVia manpage
before, you should have a fairly good idea what this does.

Why re-invent the wheel? Well, this is an implementation that should work
okay with Moo, Moose, Mouse, and any other OO toolkit you throw at it.
One ring to rule them all, so to speak.

Also, unlike the MooX::HandlesVia manpage, it honours type constraints, plus it
doesn't have the limitation that it can't mutate non-reference values.

%prep
%setup -q -n %{module_name}-%{version}
if [ %version = 0.013 ]; then
  sed -i '/List::Util/s/1\.54/1.5/' Makefile.PL
fi

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc CREDITS Changes COPYRIGHT LICENSE README
%perl_vendor_privlib/S*

%changelog
* Mon Feb 24 2020 Igor Vlasenko <viy@altlinux.ru> 0.013-alt1
- new version

