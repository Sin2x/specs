%define oname glumpy

Name: python3-module-%oname
Version: 1.1.0
Release: alt2

Summary: Fast, scalable & beautiful scientific visualisation
License: BSD
Group: Development/Python3
Url: https://pypi.python.org/pypi/glumpy/

# https://github.com/glumpy/glumpy.git
Source: %name-%version.tar
Patch0: port-on-python3.patch

BuildRequires(pre): rpm-build-python3
BuildRequires: python-tools-2to3
BuildRequires: python3-module-numpy python3-module-Cython
BuildRequires: libnumpy-py3-devel
BuildRequires: python3-module-sphinx python3-module-sphinx_rtd_theme
BuildRequires: python3-module-OpenGL

%add_python3_req_skip glumpy.ext.six.moves.urllib

%py3_provides %oname


%description
Glumpy is a python library for scientific visualization that is both
fast, scalable and beautiful. Glumpy offers an intuitive interface
between numpy and modern OpenGL.

%package tests
Summary: Tests for %oname
Group: Development/Python3
Requires: %name = %EVR

%description tests
Glumpy is a python library for scientific visualization that is both
fast, scalable and beautiful. Glumpy offers an intuitive interface
between numpy and modern OpenGL.

This package contains tests for %oname.

%package pickles
Summary: Pickles for %oname
Group: Development/Python3

%description pickles
Glumpy is a python library for scientific visualization that is both
fast, scalable and beautiful. Glumpy offers an intuitive interface
between numpy and modern OpenGL.

This package contains pickles for %oname.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
Glumpy is a python library for scientific visualization that is both
fast, scalable and beautiful. Glumpy offers an intuitive interface
between numpy and modern OpenGL.

This package contains documentation for %oname.

%prep
%setup
%patch0 -p1

sed -i 's|sphinx-build|sphinx-build-3|' doc/Makefile

find ./ -type f -name '*.py' -exec 2to3 -w -n '{}' +

%build
%python3_build_debug

%install
%python3_install

%make -C doc pickle
%make -C doc html

cp -fR doc/_build/pickle %buildroot%python3_sitelibdir/%oname/

%check
%if 0
%__python3 setup.py test
%endif

%files
%doc README.rst LICENSE.txt
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/pickle
%exclude %python3_sitelibdir/*/*/*/test*

%files tests
%python3_sitelibdir/*/*/*/test*

%files pickles
%python3_sitelibdir/*/pickle

%files docs
%doc doc/_build/html examples


%changelog
* Mon Mar 16 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 1.1.0-alt2
- Fixed build with numpy.

* Mon Jan 27 2020 Andrey Bychkov <mrdrew@altlinux.org> 1.1.0-alt1
- Version updated to 1.1.0
- porting on python3.

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.0.3-alt1.git20150322.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Tue Mar 24 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.3-alt1.git20150322
- Initial build for Sisyphus

