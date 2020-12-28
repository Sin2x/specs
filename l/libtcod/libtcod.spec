# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/python3 gcc-c++
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%define major   1
%define libname libtcod%{major}
%define devname libtcod-devel

Name:           libtcod
Version:        1.15.1
Release:        alt1_1
Summary:        Color console, input management and other tools for roguelike games
Group:          System/Libraries
License:        BSD
URL:            https://github.com/libtcod/libtcod
Source0:        https://github.com/libtcod/libtcod/archive/%{version}/%{name}-%{version}.tar.gz
Patch0:         libtcod-1.15.1-autotools.patch

BuildRequires:  pkgconfig(sdl2)
#BuildRequires:  pkgconfig(libutf8proc)
BuildRequires:  pkgconfig(zlib)

Provides:       bundled(libutf8proc)
Provides:       bundled(lodepng)
Source44: import.info

%description
libtcod, a.k.a. "The Doryen Library", is a free, fast, portable and
uncomplicated API for roguelike developpers providing an advanced
true color console, input, and lots of other utilities frequently
used in roguelikes.

#----------------------------------------------------------------------

%package -n     %{libname}
Summary:        Color console, input management and other tools for roguelike games
Group:          System/Libraries

%description -n %{libname}
libtcod, a.k.a. "The Doryen Library", is a free, fast, portable and
uncomplicated API for roguelike developpers providing an advanced
true color console, input, and lots of other utilities frequently
used in roguelikes.

%files -n       %{libname}
%{_libdir}/%{name}*.so.%{major}
%{_libdir}/%{name}*.so.%{major}.*

#----------------------------------------------------------------------

%package -n     %{devname}
Summary:        Development headers for %{name}
Group:          Development/C
Requires:       %{libname} = %{version}-%{release}
Provides:       %{name}-devel = %{version}-%{release}

%description -n %{devname}
This package contains development headers and libraries for %{name}.

%files -n       %{devname}
%doc CHANGELOG.md
%doc --no-dereference LIBTCOD-CREDITS.txt LICENSE.txt
%{_includedir}/%{name}/
%{_libdir}/%{name}*.so
%{_libdir}/pkgconfig/%{name}.pc

#----------------------------------------------------------------------

%prep
%setup -q
%patch0 -p1


rm -rf src/vendor/zlib

%build
cd buildsys/autotools
autoreconf -vfi
%configure
%make_build

%install
cd buildsys/autotools
%makeinstall_std

find %{buildroot}%{_libdir} -name "*.la" -delete -o -name "*.a" -delete

# pkg-config entry
install -d %{buildroot}%{_libdir}/pkgconfig
cat << EOF > %{buildroot}%{_libdir}/pkgconfig/%{name}.pc
prefix=%{_prefix}
exec_prefix=\${prefix}
includedir=\${exec_prefix}/include
libdir=\${exec_prefix}/%{_lib}

Name: %{name}
Description: Color console, input management and other tools for roguelike games
Version: %{version}
Libs: -L\${libdir} -ltcod
Libs.private: -lz -lSDL
Cflags: -I\${includedir}/%{name}
EOF


%changelog
* Mon Dec 28 2020 Igor Vlasenko <viy@altlinux.ru> 1.15.1-alt1_1
- new version

* Sat Jul 14 2018 Igor Vlasenko <viy@altlinux.ru> 1.6.6-alt1_2
- update by mgaimport

* Thu Jun 07 2018 Igor Vlasenko <viy@altlinux.ru> 1.6.6-alt1_1
- update by mgaimport

* Sun Mar 18 2018 Igor Vlasenko <viy@altlinux.ru> 1.6.3-alt1_1
- new version

