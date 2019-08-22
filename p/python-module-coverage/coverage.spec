%define _unpackaged_files_terminate_build 1

%define oname coverage

%def_with check
%def_with doc

Name: python-module-%oname
Version: 4.5.4
Release: alt2
Summary: A tool for measuring code coverage of Python programs
License: Apache-2.0
Group: Development/Python
Url: https://pypi.org/project/coverage/

# https://github.com/nedbat/coveragepy.git
Source: %name-%version.tar
Patch: %name-%version-alt.patch

%if_with doc
BuildRequires: libenchant python-module-alabaster python-module-html5lib python-module-sphinxcontrib-spelling
BuildRequires: python-module-sphinx_rtd_theme
%endif

BuildRequires(pre): rpm-build-python3

%if_with check
BuildRequires: python3(eventlet)
BuildRequires: python3(flaky)
BuildRequires: python3(gevent)
BuildRequires: python3(mock)
BuildRequires: python3(PyContracts)
BuildRequires: python3(pytest-xdist)
BuildRequires: python3(tox)
BuildRequires: python3(unittest_mixins)
%endif

%add_findreq_skiplist /usr/lib*/python2.7/site-packages/%oname/lab/genpy.py
%add_python_req_skip lnotab

%description
Coverage.py is a tool for measuring code coverage of Python programs. It
monitors your program, noting which parts of the code have been
executed, then analyzes the source to identify code that could have been
executed but was not.

Coverage measurement is typically used to gauge the effectiveness of
tests. It can show which parts of your product code are being exercised
by tests, and which are not.

%if_with doc
%package doc
Summary: Documentation for Coverage python module
Group: Development/Documentation
BuildArch: noarch

%description doc
Coverage.py is a tool for measuring code coverage of Python programs. It
monitors your program, noting which parts of the code have been
executed, then analyzes the source to identify code that could have been
executed but was not.

This package contains documentation for Coverage.py.

%package pickles
Summary: Pickles for Coverage python module
Group: Development/Python

%description pickles
Coverage.py is a tool for measuring code coverage of Python programs. It
monitors your program, noting which parts of the code have been
executed, then analyzes the source to identify code that could have been
executed but was not.

This package contains pickles for Coverage.py.
%endif

%package -n python3-module-%oname
Summary: A tool for measuring code coverage of Python3 programs
Group: Development/Python3

%description -n python3-module-%oname
Coverage.py is a tool for measuring code coverage of Python programs. It
monitors your program, noting which parts of the code have been
executed, then analyzes the source to identify code that could have been
executed but was not.

Coverage measurement is typically used to gauge the effectiveness of
tests. It can show which parts of your product code are being exercised
by tests, and which are not.

%prep
%setup
%patch -p1

cp -a . ../python3

%build
%add_optflags -fno-strict-aliasing
%python_build_debug

export PYTHONPATH=$PWD
%if_with doc
%make_build dochtml
%make_build pickle
%endif

pushd ../python3
%python3_build_debug
popd

%install
pushd ../python3
%python3_install
popd
mv %buildroot%_bindir/coverage %buildroot%_bindir/coverage3
ln -s coverage3 %buildroot%_bindir/python3-coverage

%python_install

install -d %buildroot%python_sitelibdir/%oname/lab
install -p -m644 lab/* %buildroot%python_sitelibdir/%oname/lab

%if_with doc
install -d %buildroot%_docdir/%name
cp -fR doc/_build/html/* %buildroot%_docdir/%name/
cp -fR doc/_build/pickle %buildroot%python_sitelibdir/%oname/
%endif

%check
# don't freeze versions
sed -i 's/==/>=/g' tox.ini requirements/pytest.pip
export PIP_NO_INDEX=YES
# don't measure coverage of ourselves
export COVERAGE_COVERAGE=no
# run tests for Python3, Python2 needs more work
export TOXENV=py%{python_version_nodots python3}
# don't run in parallel
tox.py3 --sitepackages -v

%files
%doc CHANGES.rst README.rst TODO.txt
%python_sitelibdir/%oname
%python_sitelibdir/%oname-%version-py*.egg-info
%if_with doc
%exclude %python_sitelibdir/%oname/pickle
%endif
%_bindir/coverage
%_bindir/coverage2
%_bindir/coverage-%_python_version

%if_with doc
%files doc
%_docdir/%name

%files pickles
%python_sitelibdir/%oname/pickle
%endif

%files -n python3-module-%oname
%_bindir/coverage3
%_bindir/coverage-%_python3_version
%_bindir/python3-coverage
%python3_sitelibdir/%oname
%python3_sitelibdir/%oname-%version-py*.egg-info

%changelog
* Wed Aug 21 2019 Stanislav Levin <slev@altlinux.org> 4.5.4-alt2
- Fixed testing against Pytest 5.1.

* Wed Aug 14 2019 Stanislav Levin <slev@altlinux.org> 4.5.4-alt1
- 4.5.3 -> 4.5.4.

* Mon Apr 22 2019 Stanislav Levin <slev@altlinux.org> 4.5.3-alt1
- 4.5.1 -> 4.5.3.
- Enabled testing for Python3 package.

* Wed Mar 13 2019 Igor Vlasenko <viy@altlinux.ru> 4.5.1-alt3
- NMU: added _bindir/python3-coverage compat symlink

* Wed Feb 20 2019 Stanislav Levin <slev@altlinux.org> 4.5.1-alt2
- Dropped dependency on sphinxcontrib-napoleon.

* Fri May 25 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 4.5.1-alt1
- Updated to upstream version 4.5.1.

* Thu Mar 22 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 4.4.1-alt1.1
- (NMU) Rebuilt with python-3.6.4.

* Mon Oct 23 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 4.4.1-alt1
- Updated to upstream version 4.4.1.

* Mon Jan 02 2017 Michael Shigorin <mike@altlinux.org> 4.0-alt1.a7.git20150730.1.3
- BOOTSTRAP:
  + made python3 knob *really* work
  + added doc knob (on by default) to avoid hairy sphinx BRs

* Sun Jan 01 2017 Michael Shigorin <mike@altlinux.org> 4.0-alt1.a7.git20150730.1.2
- BOOTSTRAP: made python3 knob actually work

* Thu Mar 17 2016 Ivan Zakharyaschev <imz@altlinux.org> 4.0-alt1.a7.git20150730.1.1
- (NMU) rebuild with python3-3.5 & rpm-build-python3-0.1.10
  (for ABI dependence and new python3(*) reqs)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 4.0-alt1.a7.git20150730.1
- NMU: Use buildreq for BR.

* Fri Jul 31 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0-alt1.a7.git20150730
- Version 4.0a7

* Tue Feb 17 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0-alt1.a6.git20150216
- Version 4.0a6

* Sat Jul 19 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0-alt1.a0.hg20140719
- New snapshot

* Fri Jul 11 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0-alt1.a0.hg20140708
- Version 4.0a0

* Thu Nov 28 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.7.1-alt1.hg20131027
- Version 3.7.1

* Mon Sep 16 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.6.1-alt2.a1.hg20130915
- Version 3.6.1a1

* Sun Feb 17 2013 Aleksey Avdeev <solo@altlinux.ru> 3.6.1-alt2.a0.hg20130202
- Fix build with Python3-3.3.x

* Wed Feb 13 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.6.1-alt1.a0.hg20130202
- Version 3.6.1a0

* Tue Apr 10 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.5.2-alt2.b1.hg20120329
- New snapshot
- Avoid requirement for %name on Python 3

* Wed Feb 08 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 3.5.2-alt2.b1.hg20111031
- Build with Python3

* Fri Dec 09 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.5.2-alt1.b1.hg20111031
- Version 3.5.2b1
- Added pickles subpackage

* Mon Oct 24 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 3.5-alt1.a1.hg20110502.1
- Rebuild with Python-2.7

* Tue May 10 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.5-alt1.a1.hg20110502
- New snapshot

* Fri Mar 25 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.5-alt1.a1.hg20101120.1
- Rebuilt for debuginfo

* Mon Nov 22 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.5-alt1.a1.hg20101120
- Version 3.5a1

* Mon Jul 26 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.4-alt1.a1.hg20100725
- Version 3.4a1

* Wed Nov 18 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.1.0b1-alt1.hg20090922.1
- Rebuilt with python 2.6

* Wed Sep 23 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.1.0b1-alt1.hg20090922
- Initial build for Sisyphus

