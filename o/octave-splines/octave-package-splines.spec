# BEGIN SourceDeps(oneline):
BuildRequires: makeinfo
# END SourceDeps(oneline)
%define octpkg splines
Epoch: 1
Name: octave-%octpkg
Version: 1.3.4
Release: alt1
Summary: Additional spline functions for Octave

Group: Sciences/Mathematics
License: GPLv3+, public domain
URL: http://octave.sf.net

Source0: https://downloads.sourceforge.net/project/octave/Octave%%20Forge%%20Packages/Individual%%20Package%%20Releases/%{octpkg}-%{version}.tar.gz

BuildRequires(pre): rpm-build-octave
BuildRequires: octave-devel
%if_with _octave_arch
BuildRequires: gcc-c++ gcc-g77 libfftw3-devel libhdf5-devel liblapack-devel libncurses-devel libreadline-devel
%else
BuildArch: noarch
%endif
Provides: octave(splines) = %version
# Depends: octave (>= 3.6.0)
Requires: octave >= 3.6.0


%description
Additional spline functions.

%prep
%setup -q -n %{octpkg}-%{version}

%build
%octave_build

%install
%octave_install

%files
%doc NEWS COPYING DESCRIPTION
%_datadir/octave/packages/%octpkg-%version
%if_with _octave_arch
%_libdir/octave/packages/%octpkg-%version
%endif

%changelog
* Wed Dec 01 2021 Igor Vlasenko <viy@altlinux.org> 1:1.3.4-alt1
- regenerated from template by package builder

* Wed Feb 19 2020 Andrey Cherepanov <cas@altlinux.org> 1:1.3.3-alt1
- New version.

* Sat May 26 2018 Igor Vlasenko <viy@altlinux.ru> 1:1.3.2-alt1
- build for octave 4.4

* Thu Apr 14 2016 Igor Vlasenko <viy@altlinux.ru> 1:1.2.9-alt1
- regenerated from template by package builder

* Tue Jul 07 2015 Paul Wolneykien <manowar@altlinux.org> 1:1.2.7-alt2
- Rebuild with the next version of Octave: 4.0.0

* Wed Jul 02 2014 Paul Wolneykien <manowar@altlinux.ru> 1:1.2.7-alt1
- updated by octave-package-builder

* Tue Jan 14 2014 Paul Wolneykien <manowar@altlinux.ru> 1:1.2.6-alt1
- updated by octave-package-builder

* Tue Jan 14 2014 Paul Wolneykien <manowar@altlinux.ru> 1:1.2.4-alt2
- Rebuild with the next version of Octave: 3.8.0

* Thu Oct 10 2013 Paul Wolneykien <manowar@altlinux.ru> 1:1.2.4-alt1
- updated by octave-package-builder

* Tue Jan 08 2013 Paul Wolneykien <manowar@altlinux.ru> 1:1.1.2-alt1
- updated by octave-package-builder

* Fri Nov 18 2011 Igor Vlasenko <viy@altlinux.ru> 1.0.7-alt1
- initial import by octave-package-builder

