# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/octave-config /usr/bin/rpcgen libtirpc-devel linux-gpib-devel makeinfo texinfo
# END SourceDeps(oneline)
%def_with _octave_arch
%define octpkg instrument-control
Name: octave-%octpkg
Version: 0.7.1
Release: alt1
Summary: Instrument Control

Group: Sciences/Mathematics
License: GPLv3+
Url: http://octave.sourceforge.net/

Source0: https://downloads.sourceforge.net/project/octave/Octave%%20Forge%%20Packages/Individual%%20Package%%20Releases/%{octpkg}-%{version}.tar.gz

BuildRequires(pre): rpm-build-octave
BuildRequires: octave-devel
%if_with _octave_arch
BuildRequires: gcc-c++ gcc-g77 libfftw3-devel libhdf5-devel liblapack-devel libncurses-devel libreadline-devel
%else
BuildArch: noarch
%endif
Provides: octave(instrument-control) = %version
# Depends: octave (>= 3.8.0)
Requires: octave >= 3.8.0


%description
Low level I/O functions for serial, i2c, spi, parallel, tcp, gpib, vxi11, udp and usbtmc interfaces.

%prep
%setup -q -n %{octpkg}-%{version}

%build
%octave_build

%install
%octave_install

%files
%doc COPYING README.md NEWS DESCRIPTION doc
%_datadir/octave/packages/%octpkg-%version
%if_with _octave_arch
%_libdir/octave/packages/%octpkg-%version
%endif

%changelog
* Fri Apr 08 2022 Andrey Cherepanov <cas@altlinux.org> 0.7.1-alt1
- new version

* Wed Dec 01 2021 Igor Vlasenko <viy@altlinux.org> 0.7.0-alt1
- regenerated from template by package builder

* Tue Dec 01 2020 Igor Vlasenko <viy@altlinux.ru> 0.6.0-alt1
- regenerated from template by package builder

* Sun Jun 23 2019 Igor Vlasenko <viy@altlinux.ru> 0.4.0-alt2
- rebuild with octave 5

* Sat Apr 27 2019 Igor Vlasenko <viy@altlinux.ru> 0.4.0-alt1
- regenerated from template by package builder

* Thu May 24 2018 Igor Vlasenko <viy@altlinux.ru> 0.3.1-alt1
- initial import by package builder

