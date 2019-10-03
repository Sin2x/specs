# Note: mkl is a Intel Compiler thing
%def_disable snapshot

BuildRequires(pre): rpm-build-python
%define python_noarch %python_sitelibdir_noarch
%define modname scipy
%define ver_major 1.2

%define numpy_version 1.15.4

%def_with python3

Name: python-module-%modname
Version: %ver_major.0
Release: alt5

Summary: SciPy is the library of scientific codes

License: BSD
Group: Development/Python
Url: http://www.scipy.org/

%setup_python_module %modname
Requires: %python_noarch
Requires: python-module-numpy >= %numpy_version

#add_python_req_skip swig2_ext symeig vtk
%add_python_req_skip distutils

%if_disabled snapshot
Source: https://github.com/%modname/%modname/releases/download/v%version/%modname-%version.tar.xz
%else
#VCS git://github.com/scipy/scipy.git
Source: %modname-%version.tar
%endif
Source1: site.cfg
Patch1: fix-unicode-use.patch

BuildRequires(pre): rpm-macros-make
BuildRequires(pre): rpm-macros-sphinx
BuildPreReq: gcc-c++ gcc-fortran liblapack-devel libnumpy-devel libnumpy-py3-devel python-module-Cython python-module-Pyrex python-module-alabaster python-module-html5lib python-module-ipyparallel python-module-matplotlib-sphinxext python-module-numpy-testing python-module-objects.inv python-module-sphinx-pickles python3-module-Cython python3-module-html5lib python3-module-jinja2-tests  python3-module-numpy-testing rpm-build-python3 time vixie-cron

#BuildRequires: gcc-c++ gcc-fortran liblapack-devel python-module-Pyrex
#BuildRequires: python-module-ctypes libnumpy-devel python-modules-curses
#BuildRequires: libsuitesparse-devel python-module-Cython
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildRequires: python3-devel python3-module-distribute
#BuildPreReq: python3-module-Pygments libnumpy-py3-devel
#BuildPreReq: python-tools-2to3 python3-module-Cython
#BuildPreReq: boost-python3-devel
%endif

%description
SciPy is the library of scientific codes built on top of NumPy.

%if_with python3
%package -n python3-module-%modname
Summary: SciPy is the library of scientific codes (Python 3)
Group: Development/Python3
Requires: %python3_sitelibdir_noarch
Requires: python3-module-numpy >= %numpy_version
%add_python3_req_skip _min_spanning_tree _shortest_path _tools
%add_python3_req_skip _traversal sympy
%add_python3_req_skip distutils

%description -n python3-module-%modname
SciPy is the library of scientific codes built on top of NumPy.

%package -n python3-module-%modname-devel
Summary: Development files of SciPy (Python 3)
Group: Development/Python3
Requires: python3-module-%modname = %version-%release
Requires: python3-devel libnumpy-py3-devel

%description -n python3-module-%modname-devel
SciPy is the library of scientific codes built on top of NumPy.

This package contains development files of SciPy.

%endif

%package devel
Summary: Development files of SciPy
Group: Development/Python
Requires: %name = %version-%release
Requires: python-devel libnumpy-devel

%description devel
SciPy is the library of scientific codes built on top of NumPy.

This package contains development files of SciPy.

%prep
%setup -n %modname-%version
%patch1 -p1
install -p -m644 %SOURCE1 .
sed -i 's|@LIBDIR@|%_libdir|g' site.cfg doc/Makefile
sed -i 's|@PYVER@|%_python_version|g' doc/Makefile

# Find and comment out Pytest imports, since main package should
# not require test deps
grep -zPqsr '[ ]*from scipy._lib._testutils import PytestTester\n[ ]*test = PytestTester\(__name__\)\n[ ]*del PytestTester\n' || exit 1
grep -zPrl '[ ]*from scipy._lib._testutils import PytestTester\n[ ]*test = PytestTester\(__name__\)\n[ ]*del PytestTester\n' | xargs \
sed -i '/from scipy._lib._testutils import PytestTester/,/del PytestTester/ {s/^/# /}'

# not used import
grep -qs '^from numpy.testing import assert_allclose$' \
scipy/sparse/linalg/eigen/lobpcg/lobpcg.py || exit 1
sed -i '/^from numpy\.testing import assert_allclose$/d' \
scipy/sparse/linalg/eigen/lobpcg/lobpcg.py

# _assert_warns is utilized only in tests
grep -qsF '_assert_warns = np.testing.assert_warns' \
scipy/_lib/_numpy_compat.py || exit 1
sed -i 's/\([ ]*\)\(_assert_warns = np\.testing\.assert_warns\)/\1try:\n\1\1\import numpy.testing\n\1\1\2\n\1\except ImportError:\n\1\1pass/' \
scipy/_lib/_numpy_compat.py

%if_with python3
rm -rf ../python3
cp -a . ../python3
sed -i 's|@PYSUFF@|3|' ../python3/site.cfg
%endif

sed -i 's|@PYSUFF@||' site.cfg

mkdir -p ~/.matplotlib
cp %python_sitelibdir/matplotlib/mpl-data/matplotlibrc \
	~/.matplotlib/
sed -i 's|^\(backend\).*|\1 : Agg|' ~/.matplotlib/matplotlibrc

%build
%add_optflags -I%_includedir/suitesparse -fno-strict-aliasing %optflags_shared
%python_build_debug build_ext build_py build_clib \
	config_fc --fcompiler=gnu95

%if_with python3
pushd ../python3
%python3_build_debug build_ext build_py build_clib \
	config_fc --fcompiler=gnu95
popd
%endif

%install
%python_install install_lib install_headers \
	install_data config_fc


# headers
pushd %modname
for i in $(find ./ -name '*.h'); do
    dir=$(echo $i|sed 's|\(.*\)/.*|\1|')
    install -d %buildroot%_includedir/%modname/$dir
    install -p -m644 $i \
	%buildroot%_includedir/%modname/$dir
done
popd

install -p -m644 $(find ./ -name fortranobject.h | head -n 1) \
	%buildroot%_includedir/%modname

%if_with python3
pushd ../python3
%python3_install install_lib install_headers \
	install_data config_fc
find %buildroot%python3_sitelibdir -type f -exec \
	sed -i 's|#! %_bindir/env python|#!%_bindir/python3|' -- '{}' + ||:
find %buildroot%python3_sitelibdir -type f -exec \
	sed -i 's|#!%_bindir/env python|#!%_bindir/python3|' -- '{}' + ||:

# headers
pushd %modname
for i in $(find ./ -name '*.h'); do
    dir=$(echo $i|sed 's|\(.*\)/.*|\1|')
    install -d %buildroot%_includedir/%modname-py3/$dir
    install -p -m644 $i \
	%buildroot%_includedir/%modname-py3/$dir
done
popd


install -p -m644 $(find ./ -name fortranobject.h | head -n 1) \
	%buildroot%_includedir/%modname-py3
popd
pushd %buildroot%python3_sitelibdir/%modname/sparse/csgraph
for i in $(ls *.so); do
	ln -s %python3_sitelibdir/%modname/sparse/csgraph/$i \
		%buildroot%python3_sitelibdir/
done
popd
%endif

# don't package tests and tests' data
for i in $(find %buildroot%python_sitelibdir \
               -name tests -type d \
               -o -name 'conftest.*' -type f \
               -o -name '_testutils.*' -type f \
               -o -name 'gammainc_data.*' -type f \
               -o -name '_mptestutils.*' -type f) \
	 $(find %buildroot%python3_sitelibdir \
               -name tests -type d \
               -o -name 'conftest.*' -type f \
               -o -name '_testutils.*' -type f \
               -o -name 'gammainc_data.*' -type f \
               -o -name '_mptestutils.*' -type f)
do
	rm -r "$i"
done

rm -f %buildroot%python_sitelibdir/scipy/pickle/generated/scipy-stats-rv_discrete-1.py

%find_lang %name

#check
#pushd %buildroot%python_sitelibdir
#python -c "import scipy ; scipy.test()"
#popd
#rm -f %buildroot%python_sitelibdir/*.so \
#	%buildroot%python_sitelibdir/*.cpp

%files -f %name.lang
%python_sitelibdir/*
%files devel
%_includedir/*
%if_with python3
%exclude %_includedir/%modname-py3
%endif

%if_with python3
%files -n python3-module-%modname -f %name.lang
%python3_sitelibdir/*

%files -n python3-module-%modname-devel
%_includedir/%modname-py3
%endif

%changelog
* Wed Oct 02 2019 Stanislav Levin <slev@altlinux.org> 1.2.0-alt5
- Dropped dependency on tests packages.

* Wed Jul 17 2019 Dmitry Terekhin <jqt4@altlinux.org> 1.2.0-alt4
- Removed dependency from python-module-numdifftools

* Mon Dec 31 2018 Mikhail Gordeev <obirvalger@altlinux.org> 1.2.0-alt3
- Add more unicode fixes
- Add Requires to numpy with version

* Fri Dec 28 2018 Mikhail Gordeev <obirvalger@altlinux.org> 1.2.0-alt2
- Fix unicode is docstrings

* Wed Dec 26 2018 Mikhail Gordeev <obirvalger@altlinux.org> 1.2.0-alt1
- update to 1.2.0

* Thu Mar 22 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 1.0.0-alt2.1
- (NMU) Rebuilt with python-3.6.4.

* Mon Mar 12 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 1.0.0-alt2
- Fixed build.

* Thu Oct 26 2017 Yuri N. Sedunov <aris@altlinux.org> 1.0.0-alt1
- 1.0.0

* Sat Jul 08 2017 Yuri N. Sedunov <aris@altlinux.org> 0.19.1-alt1
- 0.19.1

* Mon Jun 19 2017 Yuri N. Sedunov <aris@altlinux.org> 0.19.0-alt1
- 0.19.0

* Fri Mar 25 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.17.0-alt1.git20150829.2.1
- (NMU) rebuild with python3-3.5 & rpm-build-python3-0.1.10
  (for ABI dependence and new python3(*) reqs)

* Thu Mar 24 2016 Denis Medvedev <nbr@altlinux.org> 0.17.0-alt1.git20150829.2
- NMU: arranged dependencies.

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.17.0-alt1.git20150829.1
- NMU: Use buildreq for BR.

* Sun Aug 30 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.17.0-alt1.git20150829
- Version 0.17.0

* Sun Apr 26 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.15.1-alt1.git20150425
- Version 0.15.1

* Fri Mar 06 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.15.0-alt2.git20141102
- Fixed build

* Mon Nov 03 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.15.0-alt1.git20141102
- New snapshot

* Wed May 07 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.15.0-alt1.git20140506
- Version 0.15.0

* Thu Jan 16 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.14.0-alt7.git20131020
- Rebuilt with new python-module-sphinx

* Tue Jan 14 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.14.0-alt6.git20131020
- Disabled docs

* Wed Nov 20 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.14.0-alt5.git20131020
- Don't require sympy for module for Python 3

* Wed Nov 06 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.14.0-alt4.git20131020
- Fixed build

* Fri Oct 25 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.14.0-alt3.git20131020
- Fixed linking of qhull.so

* Thu Oct 24 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.14.0-alt2.git20131020
- Fixed linking

* Wed Oct 23 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.14.0-alt1.git20131020
- Version 0.14.0

* Wed Jun 19 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.13.0-alt2.git20130614
- Fixed build

* Sat Jun 15 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.13.0-alt1.git20130614
- Version 0.13.0

* Sat Mar 30 2013 Aleksey Avdeev <solo@altlinux.ru> 0.12.0-alt2.git20121009.1
- Rebuild with Python-3.3
- Fix non-identical noarch packages (python{,3}-module-weave)

* Wed Dec 19 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.12.0-alt2.git20121009
- Set doc-html as noarch

* Fri Oct 12 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.12.0-alt1.git20121009
- Version 0.12.0

* Sun Aug 12 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.11.0-alt5.git20120508
- Built with OpenBLAS instead of GotoBLAS2

* Sun Jun 10 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.11.0-alt4.git20120508
- Fixed build

* Fri May 25 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.11.0-alt3.git20120508
- Fixed scipy.sparse.csgraph importing in module for Python 3

* Sun May 13 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.11.0-alt2.git20120508
- New snapshot
- Added module for Python 3

* Thu Apr 12 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 0.11.0-alt2.git20111011.1
- Rebuild to remove redundant libpython2.7 dependency

* Sun Nov 27 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.11.0-alt2.git20111011
- Enabled docs (except pdf)

* Wed Oct 26 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.11.0-alt1.git20111011.1
- Rebuild with Python-2.7

* Mon Oct 24 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.11.0-alt1.git20111011
- Version 0.11.0

* Mon Jul 18 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.10.0-alt1.git20110716
- New snapshot

* Sun Apr 10 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.10.0-alt1.git20110402.3
- Built with docs

* Fri Apr 08 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.10.0-alt1.git20110402.2
- Rebuilt with GotoBLAS2 1.13-alt3
- Bootstrap (without docs)

* Thu Apr 07 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.10.0-alt1.git20110402.1
- Fixed underlinking of modules

* Thu Apr 07 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.10.0-alt1.git20110402
- Version 0.10.0
- Rebuilt with lapack-goto instead of lapack

* Tue Apr 05 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.0-alt1.svn20100607.6
- Rebuilt with ATLAS 3.9.35

* Mon Mar 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.0-alt1.svn20100607.5
- Rebuilt with lapack 3.3.0-alt4

* Tue Mar 08 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.0-alt1.svn20100607.4
- Added -g into compiler flags
- Moved all development files into devel package

* Fri Feb 25 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.0-alt1.svn20100607.3
- Rebuilt for debuginfo

* Tue Oct 26 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.0-alt1.svn20100607.2
- Rebuilt for soname set-versions

* Wed Oct 13 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.0-alt1.svn20100607.1
- Fixed underlinking

* Wed Jun 09 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.0-alt1.svn20100607
- Version 0.9.0

* Fri Apr 02 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8.0-alt2.svn20100202.2
- Rebuilt with new NumPy

* Tue Mar 02 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8.0-alt2.svn20100202.1
- Rebuilt with updated macro %%prepare_sphinx

* Thu Feb 04 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8.0-alt2.svn20100202
- Rebuilt with reformed NumPy
- Added
  + documentation (HTML & PDF)
  + pickles, devel and tests packages, plus weave in root of
    %%python_sitelibdir
  + %%check section

* Fri Jan 22 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8.0-alt2.svn20100121
- New snapshot
- Rebuild with new NumPy
- Extracted examples and tests into separate package
- Added docs packages

* Mon Jan 11 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8.0-alt2.svn20100109
- New snapshot
- Fixed error of find numpy library (ALT #22707)

* Thu Dec 31 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8.0-alt2.svn20091231
- New snapshot
- Rebuilt without python-module-Numeric

* Mon Nov 16 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8.0-alt2.svn20090913.1
- Rebuilt with python 2.6

* Sun Sep 13 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8.0-alt2.svn20090913
- New snapshot

* Fri Sep 04 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8.0-alt2.svn20090902.1
- Disabled strict aliasing rules

* Wed Sep 02 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8.0-alt2.svn20090902
- Rebuilt with shared libraries of SuiteSparse

* Thu Aug 27 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8.0-alt2.svn20090827
- New snapshot

* Sun Aug 02 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8.0-alt2.svn20090730.2
- Fixed svn version for special_version.py

* Fri Jul 31 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8.0-alt2.svn20090730.1
- Version 0.8.0

* Thu Dec 04 2008 Vitaly Lipatov <lav@altlinux.ru> 0.7.0-alt1
- new version 0.7.0b1
- update buildreqs, cleanup spec

* Sun Jul 06 2008 Vitaly Lipatov <lav@altlinux.ru> 0.6.0-alt1
- initial build for ALT Linux Sisyphus
