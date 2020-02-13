%define _unpackaged_files_terminate_build 1

%define oname greenlet

Name: python3-module-%oname
Version: 0.4.15
Release: alt2

Summary: Lightweight in-process concurrent programming
License: MIT
Group: Development/Python3
Url: http://pypi.python.org/pypi/greenlet

# https://github.com/python-greenlet/greenlet.git
Source0: https://pypi.python.org/packages/03/a6/8842d7215e1c54537eb5d0b8fd3e8562cc869b6d193317b11027ff7d8009/%{oname}-%{version}.tar.gz

BuildRequires(pre): rpm-build-python3
BuildRequires: gcc-c++


%description
The greenlet package is a spin-off of Stackless, a version of CPython
that supports micro-threads called "tasklets". Tasklets run
pseudo-concurrently (typically in a single or a few OS-level threads)
and are synchronized with data exchanges on "channels".

A "greenlet", on the other hand, is a still more primitive notion of
micro- thread with no implicit scheduling; coroutines, in other words.
This is useful when you want to control exactly when your code runs. You
can build custom scheduled micro-threads on top of greenlet; however, it
seems that greenlets are useful on their own as a way to make advanced
control flow structures. For example, we can recreate generators; the
difference with Python's own generators is that our generators can call
nested functions and the nested functions can yield values too.
Additionally, you don't need a "yield" keyword. See the example in
tests/test_generator.py.

Greenlets are provided as a C extension module for the regular
unmodified interpreter.

%package tests
Summary: Tests for greenlet
Group: Development/Python3
BuildArch: noarch
Requires: %name = %version-%release

%description tests
The greenlet package is a spin-off of Stackless, a version of CPython
that supports micro-threads called "tasklets". Tasklets run
pseudo-concurrently (typically in a single or a few OS-level threads)
and are synchronized with data exchanges on "channels".

This package contains tests for greenlet.

%prep
%setup -q -n %{oname}-%{version}

%build
%python3_build_debug

%install
%python3_install

%check
%__python3 setup.py test -v
export PYTHONPATH=$PWD
%__python3 run-tests.py -n

%files
%doc AUTHORS LICENSE NEWS README* doc/*.txt
%python3_sitelibdir/*
%_includedir/python%_python3_version%_python3_abiflags/greenlet

%files tests
%doc tests


%changelog
* Thu Feb 13 2020 Andrey Bychkov <mrdrew@altlinux.org> 0.4.15-alt2
- Build for python2 disabled.

* Wed Feb 13 2019 Nikita Ermakov <arei@altlinux.org> 0.4.15-alt1
- Update to 0.4.15

* Thu Mar 22 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 0.4.11-alt1.1.1
- (NMU) Rebuilt with python-3.6.4.

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.4.11-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 0.4.11-alt1
- automated PyPI update

* Thu Mar 17 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.4.9-alt1.git20150830.1.1
- (NMU) rebuild with python3-3.5 & rpm-build-python3-0.1.10
  (for ABI dependence and new python3(*) reqs)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.4.9-alt1.git20150830.1
- NMU: Use buildreq for BR.

* Mon Aug 31 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.9-alt1.git20150830
- Version 0.4.9
- Enabled check

* Tue Oct 28 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.5-alt1.git20141020
- Version 0.4.5

* Fri Jul 11 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.2-alt1.git20140626
- Version 0.4.2

* Tue Sep 17 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.1-alt1.git20130902
- Version 0.4.1

* Sun Mar 24 2013 Aleksey Avdeev <solo@altlinux.ru> 0.4.0-alt1.git20121205.1
- Rebuild with Python-3.3

* Thu Feb 14 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.0-alt1.git20121205
- Version 0.4.0

* Mon Jun 04 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.2-alt1.hg20111215
- Version 0.3.2
- Added module for Python 3

* Thu Apr 12 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 0.3.1-alt1.hg20110903.1
- Rebuild to remove redundant libpython2.7 dependency

* Fri Dec 09 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.1-alt1.hg20110903
- New snapshot

* Mon Oct 24 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.3.1-alt1.hg20110326.1
- Rebuild with Python-2.7

* Tue May 10 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.1-alt1.hg20110326
- New snapshot

* Fri Mar 25 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.1-alt1.hg20100606.1
- Rebuilt for debuginfo

* Tue Jun 22 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.1-alt1.hg20100606
- Initial build for Sisyphus (ALT #23646)

