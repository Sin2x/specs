# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-python3 rpm-macros-mageia-compat
BuildRequires: gcc-c++ python-devel rpm-build-python
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%define shortname comps
%define major 0
%define libname lib%{shortname}%{major}
%define libname_devel lib%{shortname}-devel

Name:           libcomps
Version:        0.1.14
Release:        alt1_2
Summary:        Comps XML file manipulation library

Group:          System/Libraries
License:        GPLv2+
URL:            https://github.com/rpm-software-management/libcomps
Source0:        https://github.com/rpm-software-management/libcomps/archive/%{name}-%{version}.tar.gz
BuildRequires:  pkgconfig(zlib)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(check)
BuildRequires:  pkgconfig(expat)
BuildRequires:  ccmake cmake ctest
Patch0:         gcc10.patch
Patch1:         remove-unused-global-variable-missing-extern.patch


# prevent provides from nonstandard paths:
%define __provides_exclude_from ^(%{python3_sitelibdir}/.*\\.so)$
Source44: import.info

%description
Libcomps is library for structure-like manipulation with content of
comps XML files. Supports read/write XML file, structure(s) modification.

%package -n %{libname}
Summary:        Libraries for %{name}
Group:          System/Libraries

%description -n %{libname}
Libraries for %{name}.

%package -n %{libname_devel}
Summary:        Development files for libcomps library
Group:          Development/C
Provides:       %{name}-devel = %{version}-%{release}
Requires:       %{libname}%{?_isa} = %{version}-%{release}

%description -n %{libname_devel}
Development files for %{name}.

%package doc
Summary:        Documentation files for libcomps library
Group:          Development/C
BuildArch:      noarch
BuildRequires:  doxygen

%description doc
Documentation files for libcomps library.

%package -n python-module-libcomps-doc
Summary:        Documentation files for python bindings libcomps library
Group:          Development/Python
Requires:       python3-module-libcomps = %{version}-%{release}
BuildArch:      noarch
BuildRequires:  python3-module-sphinx python3-module-sphinx-sphinx-build-symlink
BuildRequires:  python3-module-sphinx_rtd_theme

%description -n python-module-libcomps-doc
Documentation files for python bindings libcomps library.

%package -n python3-module-libcomps
Summary:        Python 3 bindings for libcomps library
%{?python_provide:%python_provide python3-libcomps}
Group:          Development/Python
BuildRequires:  python3-devel
Requires:       %{libname}%{?_isa} = %{version}-%{release}
# We're no longer providing the Python 2 subpackage
Obsoletes:      python2-libcomps < 0.1.11

%description -n python3-module-libcomps
Python3 bindings for libcomps library.


%prep
%setup -q -n %{name}-%{name}-%{version}
%patch0 -p1
%patch1 -p1


# Fix build with sphinx 1.8.3
sed -i -e 's,sphinx.ext.pngmath,sphinx.ext.imgmath,' libcomps/src/python/docs/doc-sources/conf.py.in

%build
%{mageia_cmake} -DPYTHON_DESIRED:STRING=3 -DSPHINX_EXECUTABLE="%{_bindir}/sphinx-build-3" ./libcomps/
%mageia_cmake_build
%mageia_cmake_build docs
%mageia_cmake_build pydocs

%check
make test -C %{_vpath_builddir}

%install
%mageia_cmake_install

%files -n %{libname}
%doc README.md
%doc --no-dereference COPYING
%{_libdir}/libcomps.so.%{major}

%files -n %{libname_devel}
%{_includedir}/*
%{_libdir}/libcomps.so
%{_libdir}/pkgconfig/%{name}.pc

%files doc
%doc build/docs/libcomps-doc/html

%files -n python-module-libcomps-doc
%doc build/src/python/docs/html

%files -n python3-module-libcomps
%{python3_sitelibdir}/libcomps
%{python3_sitelibdir}/%{name}-%{version}-py%{__python3_version}.egg-info



%changelog
* Tue Feb 25 2020 Igor Vlasenko <viy@altlinux.ru> 0.1.14-alt1_2
- new version

* Thu Apr 25 2019 Igor Vlasenko <viy@altlinux.ru> 0.1.11-alt1_1
- update by mgaimport

* Tue Jan 22 2019 Igor Vlasenko <viy@altlinux.ru> 0.1.9-alt1_1
- update by mgaimport

* Thu Mar 22 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 0.1.8-alt1_3.1
- (NMU) Rebuilt with python-3.6.4.

* Sun Mar 18 2018 Igor Vlasenko <viy@altlinux.ru> 0.1.8-alt1_3
- new version

