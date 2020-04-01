%define ver_major 3.6

%def_disable snapshot
%def_enable check
# use corresponding 3.6.x version
%define testspec_version %ver_major.3

Name: sassc
Version: %ver_major.1
Release: alt1

Summary: Wrapper around libsass to compile CSS stylesheet
Group: Text tools
License: MIT
Url: http://github.com/sass/sassc

%if_disabled snapshot
Source: %url/archive/%version/%name-%version.tar.gz
Source1: https://github.com/sass/sass-spec/archive/libsass-%testspec_version/sass-spec-libsass-%testspec_version.tar.gz
%else
#VCS: https://github.com/sass/sassc.git
Source: %name-%version.tar
#VCS: https://github.com/sass/sass-spec.git
Source1: sass-spec-%testspec_version.tar
%endif

BuildRequires: gcc-c++ libsass-devel >= %version
%{?_enable_check:BuildRequires: ruby-minitest gem-hrx}

%description
SassC is a wrapper around libsass used to generate a useful command-line
application that can be installed and packaged for several operating systems.

%prep
%setup -a 1
mv sass-spec-%{?_disable_snapshot:libsass-}%testspec_version sass-spec
echo %version > VERSION

%build
%add_optflags %(getconf LFS_CFLAGS)
%autoreconf
%configure
%make_build

%install
%makeinstall_std

%check
ruby sass-spec/sass-spec.rb --impl libsass -c ./%name

%files
%_bindir/%name
%doc LICENSE Readme.md

%changelog
* Fri Aug 09 2019 Yuri N. Sedunov <aris@altlinux.org> 3.6.1-alt1
- 3.6.1

* Wed Jul 18 2018 Yuri N. Sedunov <aris@altlinux.org> 3.5.0-alt1
- 3.5.0

* Thu Feb 22 2018 Yuri N. Sedunov <aris@altlinux.org> 3.4.8-alt1
- first build for Sisyphus

