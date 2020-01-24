%define oname numpy-stl

Name: python3-module-%oname
Version: 2.10.1
Release: alt1

Summary: Library to make reading, writing and modifying both binary and ascii STL files easy
License: BSD
Group: Development/Python3
Url: https://pypi.python.org/pypi/numpy-stl/
BuildArch: noarch

# https://github.com/WoLpH/numpy-stl.git
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-matplotlib
BuildRequires: python3-module-python_utils
BuildRequires: python3-module-pytest python3-module-pytest-runner
BuildRequires: python3-module-docutils python3-module-sphinx

%py3_provides stl


%description
Simple library to make working with STL files (and 3D objects in
general) fast and easy.

Due to all operations heavily relying on numpy this is one of the
fastest STL editing libraries for Python available.

%prep
%setup

sed -i 's|sphinx-build|sphinx-build-3|' docs/Makefile

%build
%python3_build_debug

%install
%python3_install

%make -C docs html

%check
rm -fR build conf.py*
%__python3 setup.py test

%files
%doc *.rst docs/_build/html
%_bindir/*
%python3_sitelibdir/stl
%python3_sitelibdir/*.egg-info

%changelog
* Fri Jan 24 2020 Andrey Bychkov <mrdrew@altlinux.org> 2.10.1-alt1
- Porting on Python3.

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.3.6-alt2.git20141210.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Tue Jan 26 2016 Sergey Alembekov <rt@altlinux.ru> 1.3.6-alt2.git20141210
- Rebuild with "def_disable check"
- Cleanup buildreq

* Thu Dec 11 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3.6-alt1.git20141210
- Version 1.3.6

* Fri Nov 28 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3.5-alt1.git20141127
- Version 1.3.5

* Thu Nov 06 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3.4-alt1.git20141104
- Version 1.3.4

* Mon Oct 27 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3.3-alt1.git20141024
- Initial build for Sisyphus

