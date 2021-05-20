%define _unpackaged_files_terminate_build 1

%define  oname mypy
%def_with check

# mypyc doesn't work on 32bit arches
# https://github.com/mypyc/mypyc/issues/760
%ifarch %ix86 armh
%def_without mypyc
%else
%def_with mypyc
%endif

Name:    python3-module-%oname
Version: 0.812
Release: alt2

Summary: Optional static typing for Python 3 and 2 (PEP 484)
License: MIT
Group:   Development/Python3
URL:     https://github.com/python/mypy

Packager: Grigory Ustinov <grenka@altlinux.org>

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-dev python3-module-setuptools

# Needed to generate the man pages
BuildRequires:  help2man
BuildRequires: python3-module-typeshed

%if_with check
# TODO: unbundle googletest
BuildRequires: /proc
BuildRequires: gcc-c++
BuildRequires: python3(lxml)
BuildRequires: python3(mypy_extensions)
BuildRequires: python3(psutil)
BuildRequires: python3(pytest)
BuildRequires: python3(pytest_xdist)
BuildRequires: python3(tox)
BuildRequires: python3(typing)
BuildRequires: python3(typing_extensions)
%endif

Source:  %name-%version.tar
Patch0: %name-%version-alt.patch

%description
Mypy is an optional static type checker for Python.  You can add type
hints to your Python programs using the upcoming standard for type
annotations introduced in Python 3.5 beta 1 (PEP 484), and use mypy to
type check them statically. Find bugs in your programs without even
running them!

%if_with mypyc
%package -n python3-module-mypyc
Summary: Mypy to Python C Extension Compiler
Group: Development/Python3
Requires: python3-module-%oname = %EVR
Requires: python3-dev

%description -n python3-module-mypyc
Mypyc is a compiler that compiles mypy-annotated, statically typed Python
modules into CPython C extensions. Currently our primary focus is on making
mypy faster through compilation -- the default mypy wheels are compiled with
mypyc. Compiled mypy is about 4x faster than without compilation.
%endif

%prep
%setup
%autopatch -p1

# Python2 parser
rm mypy/fastparse2.py

# upstream may merge typeshed, remove only if empty
rmdir ./mypy/typeshed/
ln -s %python3_sitelibdir_noarch/typeshed ./mypy/

%build
%python3_build

%install
%python3_install

%if "%python3_sitelibdir" != "%python3_sitelibdir_noarch"
    mkdir -p %buildroot%python3_sitelibdir
    mv %buildroot%python3_sitelibdir_noarch/* %buildroot%python3_sitelibdir/
%endif

# don't bundle typeshed
rm -r %buildroot%python3_sitelibdir/%oname/typeshed
ln -s %python3_sitelibdir_noarch/typeshed %buildroot%python3_sitelibdir/%oname/

# Generate man pages
mkdir -p %buildroot%_man1dir

PYTHONPATH=%buildroot%python3_sitelibdir \
    help2man --no-info --version-string 'mypy %version-dev' \
        --no-discard-stderr -o %buildroot%_man1dir/mypy.1 \
        %buildroot%_bindir/mypy

PYTHONPATH=%buildroot%python3_sitelibdir \
    help2man --no-info --version-string 'mypy stubgen %version-dev' \
        --no-discard-stderr -o %buildroot%_man1dir/stubgen.1 \
        %buildroot%_bindir/stubgen

# don't package tests
rm -r %buildroot%python3_sitelibdir/%oname/test/
rm -r %buildroot%python3_sitelibdir/mypyc/external/googletest/
rm -r %buildroot%python3_sitelibdir/mypyc/test/
rm -r %buildroot%python3_sitelibdir/mypyc/test-data/

%if_without mypyc
rm %buildroot%_bindir/mypyc
rm -r %buildroot%python3_sitelibdir/mypyc/
%endif

%check
# https://github.com/mypyc/mypyc/issues/760
TESTS="mypy/test"
%ifnarch %ix86 armh
TESTS="$TESTS mypyc/test"
%endif

export PIP_NO_BUILD_ISOLATION=no
export PIP_NO_INDEX=YES
export TOXENV=py3
tox.py3 --sitepackages -vvr -- -vv $TESTS

%files
%doc README.md
%python3_sitelibdir/%oname
%python3_sitelibdir/%oname-%version-py%_python3_version.egg-info/
%_bindir/%oname
%_bindir/dmypy
%_bindir/stubgen
%_bindir/stubtest
%_man1dir/mypy.1*
%_man1dir/stubgen.1*

%if_with mypyc
%files -n python3-module-mypyc
%python3_sitelibdir/mypyc/
%_bindir/mypyc
%endif

%changelog
* Thu May 20 2021 Fr. Br. George <george@altlinux.ru> 0.812-alt2
- Fix tempfile.TemporaryDirectory() naming in tests

* Tue Mar 23 2021 Stanislav Levin <slev@altlinux.org> 0.812-alt1
- 0.790 -> 0.812.

* Wed Oct 28 2020 Stanislav Levin <slev@altlinux.org> 0.790-alt2
- Fixed FTBFS(virtualenv 20.1.0).

* Wed Oct 14 2020 Stanislav Levin <slev@altlinux.org> 0.790-alt1
- 0.782 -> 0.790.

* Tue Sep 15 2020 Stanislav Levin <slev@altlinux.org> 0.782-alt1
- 0.701 -> 0.782.

* Wed Apr 24 2019 Grigory Ustinov <grenka@altlinux.org> 0.701-alt1
- Initial build for Sisyphus
