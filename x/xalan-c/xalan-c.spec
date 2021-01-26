Group: System/Libraries
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-cmake rpm-macros-fedora-compat
# END SourceDeps(oneline)
# fedora bcond_with macro
%define bcond_with() %{expand:%%{?_with_%{1}:%%global with_%{1} 1}}
%define bcond_without() %{expand:%%{!?_without_%{1}:%%global with_%{1} 1}}
# redefine altlinux specific with and without
%define with()         %{expand:%%{?with_%{1}:1}%%{!?with_%{1}:0}}
%define without()      %{expand:%%{?with_%{1}:0}%%{!?with_%{1}:1}}
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%bcond_without icu

Name:           xalan-c
Version:        1.12.0
Release:        alt1_4
Summary:        Xalan XSLT processor for C/C++

License:        ASL 2.0
URL:            http://xalan.apache.org/%{name}/
%global tag Xalan-C_%(echo '%{version}' | tr . _)
%global tar_name xalan_c-%(echo %{version} | cut -d . -f -2)
%global release_url https://github.com/apache/%{name}/releases/download/%{tag}
Source0:        %{release_url}/%{tar_name}.tar.gz
Source1:        %{release_url}/%{tar_name}.tar.gz.asc
Source2:        %{release_url}/KEYS

BuildRequires:  gnupg gnupg2
BuildRequires:  ctest cmake
# Either make or ninja is supported.
BuildRequires:  ninja-build python3-module-ninja_syntax
BuildRequires:  gcc-c++
BuildRequires:  libxerces-c-devel
%if %{with icu}
BuildRequires:  icu-utils libicu-devel
%endif

%global so_version %(echo %{version} | cut -d . -f -2 | tr -d .)
# Required for EPEL8:
%undefine __cmake_in_source_build
Source44: import.info

%description
The Apache Xalan-C++ Project provides a library and a command line program to
transform XML documents using a stylesheet that conforms to XSLT 1.0 standards.

Xalan is a project of the Apache Software Foundation.


%package        devel
Group: Development/Other
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}

%description devel
The %{name}-devel package contains libraries and header files for developing
applications that use %{name}.


%package doc
Group: Documentation
Summary:        Documentation for %{name}
BuildRequires:  doxygen
# Explicit BR required for EPEL8:
BuildRequires:  graphviz libgraphviz
BuildArch: noarch

%description doc
Documentation for %{name}.


%prep

%setup -q -n %{tar_name}


# https://github.com/apache/xalan-c/pull/35
chmod a-x NOTICE

# Remove the Autotools build system cruft from the samples; otherwise, it would
# be installed as documentation. We leave the CmakeLists.txt even though it
# cannot be used standalone; it is used in the build (even though the built
# samples are only tested and not installed), and is annoying to exclude.
rm -vf samples/configure samples/configure.in


%build
cp -at . -- /usr/share/gnu-config/config.{guess,sub}
%{fedora_v2_cmake} \
%if %{with icu}
    -Dtranscoder=icu \
%endif
    -GNinja
%fedora_v2_cmake_build


%install
%fedora_v2_cmake_install
# Remove CMake-installed docs in favor of using the doc macro. We refer to
# _prefix/share instead of _datadir to mirror how the install path is defined
# in the relevant CMakeLists.txt.
rm -rf %{buildroot}%{_prefix}/share/doc/xalan-c/api


# alt fixes for xalan-c.pc
sed -i 's,^Version:,Version: %version,;/^Cflags/d' %buildroot%_pkgconfigdir/xalan-c.pc

%check
%fedora_v2_ctest


# Required for EPEL8:



%files
%doc --no-dereference LICENSE
%doc CREDITS
%doc KEYS
%doc NOTICE
%doc README.md
%{_bindir}/Xalan
%{_libdir}/libxalanMsg.so.%{so_version}
%{_libdir}/libxalanMsg.so.%{so_version}.*
%{_libdir}/libxalan-c.so.%{so_version}
%{_libdir}/libxalan-c.so.%{so_version}.*


%files devel
%{_libdir}/libxalanMsg.so
%{_libdir}/libxalan-c.so
%{_includedir}/xalanc/
%dir %{_libdir}/cmake/XalanC
%{_libdir}/cmake/XalanC/*.cmake
%{_libdir}/pkgconfig/%{name}.pc

%if 0
# non-indentical noarch packages :(
%files doc
%doc --no-dereference LICENSE
%doc CREDITS
%doc KEYS
%doc NOTICE
%doc README.md
%doc docs/*.md docs/images
%doc %{_vpath_builddir}/docs/doxygen/api
%doc samples
%endif

%changelog
* Mon Jan 25 2021 Igor Vlasenko <viy@altlinux.ru> 1.12.0-alt1_4
- update to new release by fcimport

* Sun Dec 08 2019 Igor Vlasenko <viy@altlinux.ru> 1.11.0-alt1_16
- merged e2k patch

* Fri Oct 20 2017 Igor Vlasenko <viy@altlinux.ru> 1.11.0-alt1_12
- update to new release by fcimport

* Tue Jul 26 2016 Igor Vlasenko <viy@altlinux.ru> 1.11.0-alt1_9
- update to new release by fcimport

* Sun Dec 27 2015 Igor Vlasenko <viy@altlinux.ru> 1.11.0-alt1_8
- update to new release by fcimport

* Mon Nov 09 2015 Igor Vlasenko <viy@altlinux.ru> 1.11.0-alt1_7
- new version

* Thu Jul 10 2014 Igor Vlasenko <viy@altlinux.ru> 1.11.0-alt1_4
- dependency

