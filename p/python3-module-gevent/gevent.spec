%define oname gevent

%def_disable embed

Name: python3-module-%oname
Version: 21.1.2
Release: alt1

Summary: Coroutine-based network library

License: MIT
Group: Development/Python3
Url: http://pypi.python.org/pypi/gevent

#add_findreq_skiplist %python_sitelibdir/gevent/_socket3.py
#add_python_req_skip test

# Source-url: %__pypi_url %oname
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires(pre): rpm-build-intro >= 2.2.4

BuildRequires: libev-devel libuv-devel libcares-devel

BuildRequires: python3-module-repoze.sphinx.autointerface
BuildRequires: python3-module-greenlet
BuildRequires: python3-module-OpenSSL
BuildRequires: python3-module-Cython python3-module-cryptography python3-module-html5lib

%py3_requires greenlet
%add_python3_req_skip gevent.libev._corecffi

%description
gevent is a coroutine-based Python networking library
that uses greenlet to provide a high-level synchronous API on top of the libev or libuv event loop.

Features include:
* Fast event loop based on libev or libuv.
* Lightweight execution units based on greenlets.
* API that re-uses concepts from the Python standard library (for examples there are events and queues).
* Cooperative sockets with SSL support
* Cooperative DNS queries performed through a threadpool, dnspython, or c-ares.
* Monkey patching utility to get 3rd party modules to become cooperative
* TCP/UDP/HTTP servers
* Subprocess support (through gevent.subprocess)
* Thread pools

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: %name = %EVR

%description -n python3-module-%oname-tests
This package contains tests for %oname.

%package -n python3-module-greentest
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR
Requires: python3-module-%oname-tests = %EVR

%description -n python3-module-greentest
gevent is a coroutine-based Python networking library that uses greenlet
to provide a high-level synchronous API on top of libevent event loop.

This package contains tests for %oname.

%package doc
Summary: Documentation for gevent
Group: Development/Documentation
BuildArch: noarch

%description doc
gevent is a coroutine-based Python networking library that uses greenlet
to provide a high-level synchronous API on top of libevent event loop.

This package contains documentation and examples for gevent.

%prep
%setup

%if_disabled embed
rm -rf deps
%endif

#prepare_sphinx doc

%build
%add_optflags -fno-strict-aliasing
%if_disabled embed
export GEVENT_NO_CFFI_BUILD=1
export LIBEV_EMBED=0
export CARES_EMBED=0
%endif

export CYTHON=cython3
rm -fR src/gevent/_util_py2.py*
# remove all versions of greentest, leave only versions for current python3 version
pushd src/greentest
for i in * ; do
	if [ -z "$(echo $i | grep ^%__python3_version$)" ] ; then
		rm -fR $i
	fi
done
popd
%python3_build_debug

%install
%if_disabled embed
export GEVENT_NO_CFFI_BUILD=1
export LIBEV_EMBED=0
export CARES_EMBED=0
%endif

%python3_install
cp -fR src/greentest %buildroot%python3_sitelibdir/

#doc

#export PYTHONPATH=%buildroot%python_sitelibdir
#pushd doc
#make pickle
#make html

%files
%doc AUTHORS LICENSE* TODO *.rst
%python3_sitelibdir/*
%exclude %python3_sitelibdir/greentest
%exclude %python3_sitelibdir/%oname/tests
%exclude %python3_sitelibdir/%oname/testing

%files -n python3-module-%oname-tests
%python3_sitelibdir/%oname/tests/
%python3_sitelibdir/%oname/testing/

%files -n python3-module-greentest
%python3_sitelibdir/greentest

#files doc
#doc doc/_build/html
#doc examples

%changelog
* Wed Apr 21 2021 Vitaly Lipatov <lav@altlinux.ru> 21.1.2-alt1
- new version (21.1.2) with rpmgs script
- build python3 module separately

* Wed May 08 2019 Stanislav Levin <slev@altlinux.org> 1.4.0-alt2
- Moved the tests out to subpackage.

* Wed Feb 13 2019 Nikita Ermakov <arei@altlinux.org> 1.4.0-alt1
- Updated to upstream version 1.4.0.

* Thu Mar 22 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 1.2.2-alt1.1
- (NMU) Rebuilt with python-3.6.4.

* Mon Dec 18 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 1.2.2-alt1
- Updated to upstream version 1.2.2.

* Fri Aug 18 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 1.1.2-alt2
- Updated runtime dependencies.

* Wed Aug 16 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 1.1.2-alt1
- Updated to upstream version 1.1.2.

* Tue Apr 26 2016 Denis Medvedev <nbr@altlinux.org> 1.1.0-alt2.b4.dev0.git20150825.3
- (NMU) with sphinx changed.

* Thu Mar 24 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.1.0-alt2.b4.dev0.git20150825.2.1
- (NMU) rebuild with python3-3.5 & rpm-build-python3-0.1.10
  (for ABI dependence and new python3(*) reqs)

* Thu Mar 24 2016 Denis Medvedev <nbr@altlinux.org> 1.1.0-alt2.b4.dev0.git20150825.2
- NMU dependencies organization.

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 1.1.0-alt2.b4.dev0.git20150825.1
- NMU: Use buildreq for BR.

* Mon Aug 31 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.0-alt2.b4.dev0.git20150825
- Version 1.1b4.dev0

* Mon Mar 02 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.0-alt1.git20141213
- New snapshot
- Extracted greentest into separate package

* Sun Aug 31 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.0-alt1.git20140820
- New snapshot

* Fri Jul 11 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.0-alt1.git20140623
- Version 1.1.0

* Mon Apr 15 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0-alt4.git20130221
- Use 'find... -exec...' instead of 'for ... $(find...'

* Sat Mar 23 2013 Aleksey Avdeev <solo@altlinux.ru> 1.0-alt3.git20130221.1
- Rebuild with Python-3.3

* Thu Mar 07 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0-alt3.git20130221
- New snapshot

* Tue Jun 05 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0-alt2.hg20120529
- Fixed using email.message

* Mon Jun 04 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0-alt1.hg20120529
- New snapshot
- Added module for Python 3

* Thu Apr 12 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 1.0-alt1.hg20110818.1.1
- Rebuild to remove redundant libpython2.7 dependency

* Mon Oct 24 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.0-alt1.hg20110818.1
- Rebuild with Python-2.7

* Wed Aug 24 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0-alt1.hg20110818
- Version 1.0

* Tue May 10 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.14.0-alt1.hg20110502
- New snapshot

* Tue Apr 05 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.14.0-alt1.hg20110325.1
- Rebuilt with python-module-sphinx-devel

* Fri Mar 25 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.14.0-alt1.hg20110325
- Version 0.14.0

* Mon Aug 02 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.13.0-alt1.hg20100802
- New snapshot

* Tue Jun 22 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.13.0-alt1.hg20100621
- Version 0.13.0
- Added doc and pickles

* Wed Feb 03 2010 Vitaly Lipatov <lav@altlinux.ru> 0.11.2-alt1
- initial build for ALT Linux Sisyphus
