BuildRequires: libgomp-devel /proc
Group: Development/C
%add_optflags %optflags_shared
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           libimagequant
Version:        2.13.1
Release:        alt1_1
Summary:        Palette quantization library

License:        GPLv3+ and MIT
URL:            https://github.com/ImageOptim/libimagequant
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz

# Fix shared library permissions
Patch0:         libimagequant_solibperm.patch

BuildRequires:  gcc
Source44: import.info

%description
Small, portable C library for high-quality conversion of RGBA images to 8-bit
indexed-color (palette) images.


%package        devel
Group: Development/C
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%setup -q
%patch0 -p1



%build
%configure --with-openmp
%make_build


%install
%makeinstall_std

# Don't ship static library
rm -f %{buildroot}%{_libdir}/%{name}.a





%files
%doc --no-dereference COPYRIGHT
%doc README.md CHANGELOG
%{_libdir}/%{name}.so.0

%files devel
%{_includedir}/%{name}.h
%{_libdir}/%{name}.so
%{_libdir}/pkgconfig/imagequant.pc


%changelog
* Tue Jan 26 2021 Igor Vlasenko <viy@altlinux.ru> 2.13.1-alt1_1
- update to new release by fcimport

* Mon Mar 30 2020 Igor Vlasenko <viy@altlinux.ru> 2.12.6-alt1_2
- update

* Tue Feb 19 2019 Igor Vlasenko <viy@altlinux.ru> 2.12.2-alt1_2
- new version

* Wed Nov 15 2017 Igor Vlasenko <viy@altlinux.ru> 2.11.3-alt1_1
- new version

