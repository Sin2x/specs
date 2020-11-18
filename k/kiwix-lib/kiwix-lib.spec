Name:     kiwix-lib
Version:  9.4.1
Release:  alt1

Summary:  Common code base for all Kiwix ports
License:  GPL-3.0
Group:    Other
Url:      https://github.com/kiwix/kiwix-lib

Packager: Andrey Cherepanov <cas@altlinux.org>

Source:   %name-%version.tar

BuildRequires(pre): meson
BuildRequires: gcc-c++
BuildRequires: cmake
BuildRequires: libcurl-devel
BuildRequires: libicu-devel
BuildRequires: libmicrohttpd-devel
BuildRequires: libpugixml-devel
BuildRequires: libzim-devel
BuildRequires: mustache-cpp-devel
BuildRequires: zlib-devel

%description
%summary

%package -n libkiwix
Summary: Common code base for all Kiwix ports
Group: System/Libraries

%description -n libkiwix
%summary

%package -n libkiwix-devel
Summary: Development files for common code base for all Kiwix ports
Group: Development/C++

%description -n libkiwix-devel
%summary

%prep
%setup

%build
%meson
%meson_build

%install
%meson_install

%files -n libkiwix
%doc AUTHORS README.md
%_libdir/*.so.*

%files -n libkiwix-devel
%_bindir/kiwix-compile-resources
%_includedir/*
%_libdir/*.so
%_libdir/pkgconfig/kiwix.pc
%_man1dir/*.1*

%changelog
* Wed Nov 18 2020 Andrey Cherepanov <cas@altlinux.org> 9.4.1-alt1
- New version.

* Sun Aug 30 2020 Andrey Cherepanov <cas@altlinux.org> 9.4.0-alt1
- New version.

* Sat Jul 18 2020 Andrey Cherepanov <cas@altlinux.org> 9.3.1-alt1
- New version.

* Thu Jul 02 2020 Andrey Cherepanov <cas@altlinux.org> 9.3.0-alt1
- New version.

* Wed Jul 01 2020 Andrey Cherepanov <cas@altlinux.org> 9.2.3-alt1
- New version.

* Wed Jun 03 2020 Andrey Cherepanov <cas@altlinux.org> 9.2.2-alt1
- New version.

* Tue Jun 02 2020 Andrey Cherepanov <cas@altlinux.org> 9.2.1-alt1
- New version.

* Mon May 18 2020 Andrey Cherepanov <cas@altlinux.org> 9.2-alt1
- New version.

* Thu May 14 2020 Andrey Cherepanov <cas@altlinux.org> 9.1.2-alt1
- New version.

* Tue Apr 28 2020 Andrey Cherepanov <cas@altlinux.org> 9.1.1-alt1
- Initial build for Sisyphus
