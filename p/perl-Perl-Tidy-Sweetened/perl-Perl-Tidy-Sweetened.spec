%define _unpackaged_files_terminate_build 1

Name:  perl-Perl-Tidy-Sweetened
Version: 1.18
Release: alt1
Summary: Tweaks to Perl::Tidy to support some syntactic sugar
License: GPL-1.0+ or Artistic-1.0-Perl
Group: Development/Perl
Url: https://metacpan.org/release/Perl-Tidy-Sweetened
Source: %name-%version.tar
BuildArch: noarch

BuildRequires: perl(Module/Build/Tiny.pm) perl(Perl/Tidy.pm) perl(Test/Most.pm)

%description
There are a number of modules on CPAN that allow users to write their
classes with a more "modern" syntax. These tools eliminate the need to
shift off $self, can support type checking and offer other improvements.
Unfortunately, they can break the support tools that the Perl community has
come to rely on. This module attempts to work around those issues.

%prep
%setup

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes
%perl_vendorlib/*
%_bindir/*
%_man1dir/perlt*

%changelog
* Mon May 16 2022 Alexandr Antonov <aas@altlinux.org> 1.18-alt1
- initial build for ALT

