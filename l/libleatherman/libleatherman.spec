Name:    libleatherman
Version: 1.12.2
Release: alt1
Summary: A collection of C++ and CMake utility libraries
 
Group:   System/Libraries
License: Apache-2.0
Url:     https://github.com/puppetlabs/leatherman
Packager: Andrey Cherepanov <cas@altlinux.org>
 
Source: leatherman-%version.tar
Patch1: fedora-shared_nowide.patch
 
BuildRequires(pre): cmake
BuildRequires(pre): rpm-build-ninja
BuildRequires: gcc-c++
BuildRequires: boost-devel
BuildRequires: boost-filesystem-devel
BuildRequires: boost-locale-devel
BuildRequires: boost-log-devel
BuildRequires: libcurl-devel

%description
A collection of C++ and CMake utility libraries.

%package devel
Summary: cpp-hocon development headers
Group: Development/Other
Provides: leatherman-devel = %version-%release
Obsoletes: leatherman-devel < %version-%release
Requires: boost-locale-devel

%description devel
Development headers for leatherman.

%prep
%setup -n leatherman-%version
%patch1 -p1
# Ruby 2.3 fix: replace rb_data_object_alloc symbol with rb_data_object_wrap
sed -i 's/rb_data_object_alloc/rb_data_object_wrap/g' \
	$( grep -rl rb_data_object_alloc ruby )
%ifarch %e2k
# actually any EDG-based compiler (up to and including 5.0 it seems);
# see also http://bugs.webkit.org/show_bug.cgi?id=29034 and mcst#5101
sed -r -i.orig 's,reinterpret_cast<char\*\*\*>,(char***),g' ruby/src/api.cc
%endif

%build
%cmake -GNinja \
       -DLEATHERMAN_SHARED=TRUE \
       -DENABLE_CXX_WERROR=OFF
%ninja_build -C BUILD

%install
%ninja_install -C BUILD

%files
%doc *.md
%_libdir/leatherman_*.so.*
%_datadir/locale/*/LC_MESSAGES/leatherman_*.mo

%files devel
%_libdir/leatherman_*.so
%_includedir/leatherman
%_libdir/cmake/leatherman

%changelog
* Tue Oct 20 2020 Andrey Cherepanov <cas@altlinux.org> 1.12.2-alt1
- New version.
- Build using ninja.

* Tue Jul 14 2020 Andrey Cherepanov <cas@altlinux.org> 1.12.1-alt1
- New version.

* Mon Jun 22 2020 Michael Shigorin <mike@altlinux.org> 1.12.0-alt3
- E2K: workaround cast problem.

* Wed Jun 10 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 1.12.0-alt2
- Unbundled boost-nowide library.

* Wed Apr 29 2020 Andrey Cherepanov <cas@altlinux.org> 1.12.0-alt1
- New version.

* Fri Mar 27 2020 Andrey Cherepanov <cas@altlinux.org> 1.11.0-alt1
- New version.

* Mon Jan 20 2020 Andrey Cherepanov <cas@altlinux.org> 1.10.0-alt1
- New version.

* Mon Dec 02 2019 Andrey Cherepanov <cas@altlinux.org> 1.9.1-alt1
- New version.

* Thu Oct 31 2019 Andrey Cherepanov <cas@altlinux.org> 1.9.0-alt1
- New version.

* Tue Oct 29 2019 Andrey Cherepanov <cas@altlinux.org> 1.8.0-alt1
- New version.

* Mon Oct 07 2019 Andrey Cherepanov <cas@altlinux.org> 1.7.3-alt1
- New version.

* Tue Sep 17 2019 Andrey Cherepanov <cas@altlinux.org> 1.7.2-alt1
- New version.

* Fri Aug 16 2019 Andrey Cherepanov <cas@altlinux.org> 1.7.1-alt1
- New version.

* Wed Jun 19 2019 Andrey Cherepanov <cas@altlinux.org> 1.7.0-alt1
- New version.

* Thu Mar 28 2019 Andrey Cherepanov <cas@altlinux.org> 1.6.0-alt1
- New version.

* Tue Mar 12 2019 Ivan A. Melnikov <iv@altlinux.org> 1.5.4-alt1
- New version.
- Disable -Werror to build with recent gcc.

* Thu Nov 01 2018 Andrey Cherepanov <cas@altlinux.org> 1.5.3-alt1
- New version.

* Fri Oct 12 2018 Andrey Cherepanov <cas@altlinux.org> 1.5.2-alt1
- New version.

* Thu Oct 04 2018 Andrey Cherepanov <cas@altlinux.org> 1.5.1-alt1
- New version.

* Wed Sep 19 2018 Andrey Cherepanov <cas@altlinux.org> 1.5.0-alt1
- New version.

* Sun Jun 24 2018 Andrey Cherepanov <cas@altlinux.org> 1.4.2-alt1
- New version.

* Thu May 31 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 1.4.1-alt1.1
- NMU: rebuilt with boost-1.67.0

* Thu Apr 19 2018 Andrey Cherepanov <cas@altlinux.org> 1.4.1-alt1
- New version.

* Tue Feb 13 2018 Andrey Cherepanov <cas@altlinux.org> 1.4.0-alt1
- New version.

* Mon Nov 06 2017 Andrey Cherepanov <cas@altlinux.org> 1.3.0-alt1
- New version

* Sun Feb 19 2017 Andrey Cherepanov <cas@altlinux.org> 0.11.0-alt1
- new version 0.11.0

* Sat Jan 28 2017 Andrey Cherepanov <cas@altlinux.org> 0.10.2-alt1
- new version 0.10.2

* Tue Jan 17 2017 Andrey Cherepanov <cas@altlinux.org> 0.10.1-alt1
- Initial build in Sisyphus

