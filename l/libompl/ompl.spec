# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-fedora-compat
BuildRequires: /usr/bin/R boost-devel boost-filesystem-devel boost-program_options-devel
# END SourceDeps(oneline)
Group: System/Libraries
%add_optflags %optflags_shared
%define oldname ompl
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%global soversion 16
%global apiversion 1.5

Name:           libompl
Version:        1.5.0
Release:        alt1_1
Summary:        The Open Motion Planning Library

License:        BSD
URL:            http://ompl.kavrakilab.org/
Source0:        https://github.com/%{oldname}/%{oldname}/archive/%{version}/%{oldname}-%{version}.tar.gz
BuildRequires:  gcc-c++
BuildRequires:  boost-complete >= 1.42.0
BuildRequires:  ctest cmake
BuildRequires:  doxygen
BuildRequires:  eigen3
BuildRequires:  libflann-devel
BuildRequires:  graphviz libgraphviz
BuildRequires:  libode-devel

# Move the installed CMake configuration from datadir to libdir.
# Refelects best practice with respect to arch-ful CMake configuration.
# Disable build/installation of plannerarena.
# Not submitted upstream.
Patch0: ompl-1.5.0-cmakeinstall.patch
Source44: import.info
Provides: ompl = %{version}-%{release}

%description
The Open Motion Planning Library (OMPL) consists of many state-of-the-art 
sampling-based motion planning algorithms. OMPL itself does not contain 
any code related to, e.g., collision checking or visualization. This is 
a deliberate design choice, so that OMPL is not tied to a particular 
collision checker or visualization front end.

%package        devel
Group: Development/Other
Summary:        Development files for %{oldname}
Requires:       %{name} = %{version}-%{release}
Requires:       boost-complete
Provides: ompl-devel = %{version}-%{release}

%description    devel
The %{oldname}-devel package contains libraries and header files for
developing applications that use %{oldname}.


%prep
%setup -n %{oldname}-%{version} -q
# Get rid of bundled libs
rm -rf src/external/
rm -rf scripts/plannerarena
%patch0 -p0 -b .cmakeinstall

%build
# Python bindings are disabled because dependencies pygccxml and pyplusplus are not packaged for Fedora
mkdir build
cd build
%{fedora_cmake} .. \
  -DCMAKE_BUILD_TYPE=RelWithDebInfo \
  -DCMAKE_SKIP_RPATH=ON \
  -DOMPL_BUILD_PYBINDINGS=OFF \
  -DOMPL_LIB_INSTALL_DIR=%{_lib} \
  -DBOOST_LIBRARYDIR=%{_libdir} \
  -DODE_LIB_PATH=%{_libdir} \
  -DBUILD_OMPL_TESTS=ON  \
  -DOMPL_ODESOLVER=ON \
  -DOMPL_REGISTRATION=OFF

%make_build
make ompl_doc
rm -f ompl_doc/installdox

%install
make -C build install DESTDIR=%{buildroot}

rm -f %{buildroot}%{_datadir}/%{oldname}/demos/*.py
rm -rf %{buildroot}%{_includedir}/%{oldname}/CMakeFiles
rm -rf %{buildroot}%{_bindir}
rm -f %{buildroot}%{_mandir}/man1/plannerareana*

%check
export LD_LIBRARY_PATH=%{buildroot}%{_libdir}
# Test failures can be triggered by builder CPU speed.
# Accept test failures for slow builders.
VERBOSE=1 make -C build test  || exit 0




%files
%doc LICENSE README.md
%{_libdir}/libompl.so.%{version}
%{_libdir}/libompl.so.%{soversion}
%{_mandir}/man1/*.1*

%files devel
%doc build/ompl_doc
%{_libdir}/libompl.so
%{_includedir}/%{oldname}-%{apiversion}
%{_datadir}/%{oldname}
%{_libdir}/pkgconfig/*.pc
%{_libdir}/%{oldname}

%changelog
* Thu Jun 25 2020 Igor Vlasenko <viy@altlinux.ru> 1.5.0-alt1_1
- update to new release by fcimport

* Tue Dec 03 2019 Aleksei Nikiforov <darktemplar@altlinux.org> 1.3.2-alt2_6
- Rebuilt with boost-1.71.0.

* Sat Feb 09 2019 Igor Vlasenko <viy@altlinux.ru> 1.3.2-alt1_6
- update to new release by fcimport

* Sun Jan 27 2019 Igor Vlasenko <viy@altlinux.ru> 1.3.2-alt1_5
- update to new release by fcimport

* Thu May 31 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 1.3.2-alt1_2.1
- NMU: rebuilt with boost-1.67.0

* Mon May 07 2018 Igor Vlasenko <viy@altlinux.ru> 1.3.2-alt1_2
- update to new release by fcimport

* Wed Sep 27 2017 Igor Vlasenko <viy@altlinux.ru> 1.0.0-alt1_17
- update to new release by fcimport

* Thu Aug 03 2017 Igor Vlasenko <viy@altlinux.ru> 1.0.0-alt1_15
- update to new release by fcimport

* Thu Mar 16 2017 Igor Vlasenko <viy@altlinux.ru> 1.0.0-alt1_13
- update to new release by fcimport

* Wed Sep 21 2016 Igor Vlasenko <viy@altlinux.ru> 1.0.0-alt1_11
- update to new release by fcimport

* Sun May 08 2016 Igor Vlasenko <viy@altlinux.ru> 1.0.0-alt1_10
- update to new release by fcimport

* Tue Apr 07 2015 Igor Vlasenko <viy@altlinux.ru> 1.0.0-alt1_2
- update to new release by fcimport

* Sat Jan 03 2015 Ivan A. Melnikov <iv@altlinux.org> 1.0.0-alt1_1.1
- rebuild with boost 1.57.0

* Wed Dec 17 2014 Igor Vlasenko <viy@altlinux.ru> 1.0.0-alt1_1
- update to new release by fcimport

* Wed Aug 27 2014 Igor Vlasenko <viy@altlinux.ru> 0.14.2-alt1_3
- update to new release by fcimport

* Mon Jul 07 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.14.2-alt1_2.1
- Rebuilt with new ode

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 0.14.2-alt1_2
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 0.12.2-alt1_3
- update to new release by fcimport

* Mon Aug 05 2013 Igor Vlasenko <viy@altlinux.ru> 0.12.2-alt1_2
- update to new release by fcimport

* Tue May 07 2013 Igor Vlasenko <viy@altlinux.ru> 0.12.2-alt1_1
- update to new release by fcimport

* Sun Apr 28 2013 Igor Vlasenko <viy@altlinux.ru> 0.11.1-alt1_4
- initial fc import

