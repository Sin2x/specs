## SPEC file for Perl module Dist::Zilla::Plugin::DynamicPrereqs

%define real_name Dist-Zilla-Plugin-DynamicPrereqs

%define _unpackaged_files_terminate_build 1

Name: perl-Dist-Zilla-Plugin-DynamicPrereqs
Version: 0.039
Release: alt2

Summary: Dist::Zilla plugin to specify dynamic prerequisites for distribution

License: %perl_license
Group: Development/Perl

URL: https://metacpan.org/release/Dist-Zilla-Plugin-DynamicPrereqs

Packager: Nikolay A. Fetisov <naf@altlinux.org>

Source: %real_name-%version.tar
Patch1: perl-%real_name-0.039-alt-fix_tests.patch

BuildArch: noarch

BuildRequires(pre): perl-devel rpm-build-licenses

# Automatically added by buildreq on Sun Mar 14 2021
# optimized out: perl perl-B-Hooks-EndOfScope perl-CPAN perl-CPAN-Meta perl-CPAN-Meta-Requirements perl-Capture-Tiny perl-Carp-Clan perl-Class-Data-Inheritable perl-Class-Inspector perl-Class-Load perl-Config-INI perl-Config-MVP perl-Config-MVP-Reader-INI perl-Cpanel-JSON-XS perl-Data-OptList perl-Data-Section perl-Devel-Caller perl-Devel-GlobalDestruction perl-Devel-OverloadInfo perl-Devel-StackTrace perl-Dist-CheckConflicts perl-Dist-Zilla perl-Encode perl-Eval-Closure perl-Exception-Class perl-Exporter-Lite perl-Exporter-Tiny perl-File-Copy-Recursive perl-File-Find-Rule perl-File-ShareDir perl-File-pushd perl-JSON-MaybeXS perl-JSON-PP perl-List-MoreUtils perl-List-MoreUtils-XS perl-Log-Dispatch perl-Log-Dispatch-Array perl-Log-Dispatchouli perl-MRO-Compat perl-Mixin-Linewise perl-Module-CoreList perl-Module-Implementation perl-Module-Metadata perl-Module-Pluggable perl-Module-Runtime perl-Moo perl-Moose perl-MooseX-LazyRequire perl-MooseX-OneArgNew perl-MooseX-Role-Parameterized perl-MooseX-SetOnce perl-MooseX-Types perl-MooseX-Types-Perl perl-MooseX-Types-Stringlike perl-Number-Compare perl-Package-DeprecationManager perl-Package-Stash perl-Package-Stash-XS perl-PadWalker perl-Params-Util perl-Params-Validate perl-Params-ValidationCompiler perl-Parse-CPAN-Meta perl-Path-Tiny perl-PerlIO-utf8_strict perl-Pod-Elemental perl-Pod-Eventual perl-Role-HasMessage perl-Role-Identifiable perl-Role-Tiny perl-Scope-Guard perl-Software-License perl-Specio perl-String-Flogger perl-String-RewritePrefix perl-String-Truncate perl-Sub-Exporter perl-Sub-Exporter-ForMethods perl-Sub-Exporter-Progressive perl-Sub-Identify perl-Sub-Install perl-Sub-Name perl-Sub-Quote perl-Syntax-Keyword-Junction perl-Term-ANSIColor perl-Test-Deep perl-Test-Fatal perl-Text-Glob perl-Text-Template perl-Throwable perl-Tie-IxHash perl-Tie-RefHash perl-Try-Tiny perl-Variable-Magic perl-YAML-Tiny perl-aliased perl-autobox perl-autodie perl-devel perl-namespace-autoclean perl-namespace-clean perl-parent python-modules python2-base python3 python3-base python3-module-paste ruby ruby-stdlibs sh4 tzdata
BuildRequires: perl-Class-XSAccessor perl-Dist-Zilla-Plugin-Git perl-Dist-Zilla-Plugin-MakeMaker-Awesome perl-Dist-Zilla-Role-ModuleMetadata perl-File-ShareDir-Install perl-Moose-Autobox perl-MooseX-Aliases perl-MooseX-Params-Validate perl-MooseX-SemiAffordanceAccessor perl-MooseX-StrictConstructor perl-Pod-Coverage perl-Pod-Weaver perl-Ref-Util perl-Ref-Util-XS perl-Test-Deep-JSON perl-Test-File-ShareDir perl-Test-Moose-More perl-Test-Needs perl-YAML

%description
Perl module Dist::Zilla::Plugin::DynamicPrereqs inserts code into
Makefile.PL to indicate dynamic (installer-side) prerequisites.


%prep
%setup -q -n %real_name-%version
%patch1

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README Changes
%perl_vendor_privlib/Dist/Zilla/Plugin/DynamicPrereqs*
%perl_vendor_privlib/auto/*

%changelog
* Sun Mar 14 2021 Nikolay A. Fetisov <naf@altlinux.org> 0.039-alt2
- Bump release to override autoimports package

* Sun Mar 14 2021 Nikolay A. Fetisov <naf@altlinux.org> 0.039-alt1
- Initial build for ALT Linux Sisyphus
