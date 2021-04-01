%define oname mistune

Name: python3-module-%oname
Version: 0.8.3
Release: alt2
Summary: The fastest markdown parser in pure Python
License: BSD
Group: Development/Python3
Url: https://pypi.python.org/pypi/mistune/

# https://github.com/lepture/mistune.git
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-module-wheel
BuildPreReq: python3-module-nose
BuildPreReq: python3-module-Cython

%py3_provides %oname


%description
The fastest markdown parser in pure Python, inspired by marked.

Features:

* Pure Python. Tested in Python 2.6+, Python 3.3+ and PyPy.
* Very Fast. It is the fastest in all pure Python markdown parsers.
* More Features. Table, footnotes, autolink, fenced code etc.

%prep
%setup

%build
%add_optflags -fno-strict-aliasing
%python3_build

%install
%python3_install
rm -fR %buildroot%python3_sitelibdir/*.py \
	%buildroot%python3_sitelibdir/__pycache__

%check
export PYTHONPATH=%buildroot%python3_sitelibdir
nosetests3 -v

%files
%doc *.rst docs/*.rst
%python3_sitelibdir/*

%changelog
* Thu Apr 01 2021 Grigory Ustinov <grenka@altlinux.org> 0.8.3-alt2
- Drop python2 support.

* Sat Aug 25 2018 Anton Midyukov <antohami@altlinux.org> 0.8.3-alt1
- Version 0.8.3

* Thu Mar 22 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 0.7-alt3.git20150811.1.1.1
- (NMU) Rebuilt with python-3.6.4.

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.7-alt3.git20150811.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Mon Mar 28 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.7-alt3.git20150811.1
- (NMU) rebuild with python3-3.5 & rpm-build-python3-0.1.10
  (for ABI dependence and new python3(*) reqs)

* Mon Mar 28 2016 Denis Medvedev <nbr@altlinux.org> 0.7-alt3.git20150811
- Cython brought back

* Tue Mar 22 2016 Denis Medvedev <nbr@altlinux.org> 0.7-alt2.git20150811
- Removed cython dependency for python3.5 adaptation.

* Sat Aug 22 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.7-alt1.git20150811
- New snapshot

* Mon Aug 03 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.7-alt1.git20150730
- Version 0.7

* Wed Apr 22 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5.1-alt1.git20150416
- Initial build for Sisyphus

