%define  oname numba

Name:    python3-module-%oname
Version: 0.52.0
Release: alt2

Summary: A Just-In-Time Compiler for Numerical Functions in Python

License: BSD
Group:   Development/Python3
URL:     https://pypi.org/project/numba

Packager: Grigory Ustinov <grenka@altlinux.org>

BuildRequires(pre): rpm-build-python3 python3-module-six
BuildRequires: python3-module-setuptools
BuildRequires: gcc-c++ libgomp-devel libnumpy-py3-devel

Source:  %oname-%version.tar

Patch: f96db3dc74bcc619464d2842d87112b63e02117d.patch

%description
Numba is an open source, NumPy-aware optimizing compiler for Python sponsored by
Anaconda, Inc. It uses the LLVM compiler project to generate machine code from
Python syntax.

Numba can compile a large subset of numerically-focused Python, including many
NumPy functions. Additionally, Numba has support for automatic parallelization
of loops, generation of GPU-accelerated code, and creation of ufuncs and
C callbacks.

%prep
%setup -n %oname-%version
%patch -p1
# Use system six instead of bundled
find -type f -name '*.py*' -exec sed -i 's|numba.six.moves|six.moves|'  -- '{}' +

%build
%python3_build

%install
%python3_install

mv %buildroot%_bindir/numba %buildroot%_bindir/numba3
mv %buildroot%_bindir/pycc %buildroot%_bindir/pycc3

%files
%_bindir/numba3
%_bindir/pycc3
%python3_sitelibdir/%oname/
%python3_sitelibdir/*.egg-info
%doc CHANGE_LOG *.rst

%changelog
* Sun Feb 14 2021 Grigory Ustinov <grenka@altlinux.org> 0.52.0-alt2
- Fixed build with python3.9.

* Wed Dec 02 2020 Grigory Ustinov <grenka@altlinux.org> 0.52.0-alt1
- Build new version.

* Sun Oct 04 2020 Grigory Ustinov <grenka@altlinux.org> 0.51.2-alt1
- Build new version.

* Sat Jun 27 2020 Grigory Ustinov <grenka@altlinux.org> 0.50.1-alt1
- Build new version.

* Wed Dec 18 2019 Grigory Ustinov <grenka@altlinux.org> 0.46.0-alt1
- Build new version.

* Thu Sep 05 2019 Grigory Ustinov <grenka@altlinux.org> 0.45.1-alt1
- Initial build for Sisyphus (Closes: #35680).
