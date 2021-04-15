Group: Graphics
BuildRequires: libgomp-devel /proc
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%global libname libimagequant

Name:           pngquant
Version:        2.14.1
Release:        alt1_1
Summary:        PNG quantization tool for reducing image file size

License:        GPLv3+

URL:            http://%{name}.org
Source0:        https://github.com/pornel/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
# Comment out failing test on EL < 8 due to old libpng
Patch1:         pngquant-old_libpng.patch

BuildRequires:  gcc
BuildRequires:  libpng-devel >= 1.2.46
BuildRequires:  zlib-devel >= 1.2.3
BuildRequires:  liblcms2-devel
BuildRequires:  %{libname}-devel >= %{version}

Requires:       libpng16 >= 1.2.46
Requires:       zlib >= 1.2.3
Requires:       %{libname} >= %{version}
Source44: import.info


%description
%{name} converts 24/32-bit RGBA PNG images to 8-bit palette with alpha channel
preserved.  Such images are compatible with all modern web browsers and a
compatibility setting is available to help transparency degrade well in
Internet Explorer 6.  Quantized files are often 40-70 percent smaller than
their 24/32-bit version. %{name} uses the median cut algorithm.


%prep
%setup -q
%if 0%{?rhel} &&  0%{?rhel} < 8
%patch1 -p1 -b .oldlibpng
%endif


%build
# add some speed-relevant compiler-flags
export CFLAGS="%{optflags} -fno-math-errno -funroll-loops -fomit-frame-pointer -fPIC"
%configure --with-openmp --with-libimagequant
%make_build


%install
%makeinstall_std


%check
%make_build test


%files
%doc README.md CHANGELOG
%doc --no-dereference COPYRIGHT
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*


%changelog
* Thu Apr 15 2021 Igor Vlasenko <viy@altlinux.org> 2.14.1-alt1_1
- update to new release by fcimport

* Sun Nov 22 2020 Igor Vlasenko <viy@altlinux.ru> 2.12.6-alt1_3
- build on armh

* Mon Mar 30 2020 Igor Vlasenko <viy@altlinux.ru> 2.12.6-alt1_2
- update

* Tue Feb 19 2019 Igor Vlasenko <viy@altlinux.ru> 2.12.2-alt1_2
- to Sisyphus as dependency

* Wed Nov 15 2017 Igor Vlasenko <viy@altlinux.ru> 2.11.2-alt1_2
- new version
- moved to autoimports (check fails)

* Tue Jul 26 2016 Igor Vlasenko <viy@altlinux.ru> 2.7.1-alt1_1
- update to new release by fcimport

* Sun Jun 12 2016 Igor Vlasenko <viy@altlinux.ru> 2.7.0-alt1_1
- converted for ALT Linux by srpmconvert tools

