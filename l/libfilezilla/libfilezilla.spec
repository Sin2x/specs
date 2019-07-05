%define _unpackaged_files_terminate_build 1

%define soname 0

Name: libfilezilla
Version: 0.17.1
Release: alt1
Summary: Small and modern C++ library
License: GPLv2+
Group: System/Libraries
Url: https://lib.filezilla-project.org/

# Repacked http://download.filezilla-project.org/libfilezilla/%name-%version.tar.bz2
Source: %name-%version.tar

BuildRequires: cppunit-devel doxygen gcc-c++ graphviz libnettle-devel
BuildRequires: libgnutls-devel

%description
libfilezilla is a free, open source C++ library, offering some basic
functionality to build high-performing, platform-independent programs.
Some of the highlights include:

* A typesafe, multi-threaded event system that's very simple to use yet
  extremely efficient.
* Timers for periodic events.
* A datetime class that not only tracks timestamp but also their
  accuracy, which simplifies dealing with timestamps originating from
  different sources.
* Simple process handling for spawning child processes with redirected
  I/O.

%package -n libfilezilla%soname
Summary: Small and modern C++ library
Group: System/Libraries

%description -n	libfilezilla%soname
libfilezilla is a free, open source C++ library, offering some basic
functionality to build high-performing, platform-independent programs.
Some of the highlights include:

* A typesafe, multi-threaded event system that's very simple to use yet
  extremely efficient.
* Timers for periodic events.
* A datetime class that not only tracks timestamp but also their
  accuracy, which simplifies dealing with timestamps originating from
  different sources.
* Simple process handling for spawning child processes with redirected
  I/O.

%package devel
Summary: Development package for %name
Group: Development/C++
Requires: libfilezilla%soname = %EVR

%description devel
Header files for development with %name.

%prep
%setup

%build
%configure \
	--disable-static \
	%nil

%make_build

pushd doc
make html
popd

%install
%makeinstall_std

find %buildroot -name '*.la' -delete

%find_lang %name

%check
LC_ALL=en_US.UTF-8 make check

%files -n libfilezilla%soname -f %name.lang
%doc AUTHORS ChangeLog NEWS README
%_libdir/%name.so.%{soname}*

%files devel
%doc AUTHORS ChangeLog NEWS README
%doc doc/doxygen-doc/*
%_includedir/%name/
%_libdir/%name.so
%_pkgconfigdir/%name.pc

%changelog
* Thu Jul 04 2019 Aleksei Nikiforov <darktemplar@altlinux.org> 0.17.1-alt1
- Updated to upstream version 0.17.1.

* Tue Feb 19 2019 Egor Zotov <egorz@altlinux.org> 0.15.1-alt1
- Updated to upstream version 0.15.1.

* Wed Jan 24 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 0.11.2-alt1
- Updated to upstream version 0.11.2.

* Thu Jun 08 2017 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.9.2-alt1
- Updated to 0.9.2.

* Wed Feb 22 2017 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.9.1-alt1
- Updated to 0.9.1.

* Thu Dec 22 2016 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.9.0-alt1
- Updated to 0.9.0.

* Thu Sep 01 2016 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.6.1-alt1
- Updated to 0.6.1.

* Mon Jun 27 2016 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.5.3-alt1
- Updated to 0.5.3.

* Thu Jun 02 2016 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.5.2-alt1
- Updated to 0.5.2.

* Wed May 04 2016 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.5.0-alt1
- Updated to 0.5.0.

* Wed Mar 30 2016 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.4.0.1-alt1
- Initial build.
