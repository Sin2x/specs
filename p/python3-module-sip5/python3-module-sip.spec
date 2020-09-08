%define oname sip
%define pkg_version %(echo %version | sed 's/\\./,/g')

Name: python3-module-sip5
Version: 5.4.0
Release: alt1

Summary: Python3 bindings generator for C/C++ libraries

License: GPL v2, GPL v3 licenses, and under a license similar to the BSD license
Group: Development/Python3
URL: http://www.riverbankcomputing.com/software/sip/

# Source-url: %__pypi_url %oname
Source: %name-%version.tar

BuildRequires(pre): rpm-build-intro

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel

BuildRequires: flex gcc-c++

%py3_provides %oname

Provides: python3-module-%oname-devel = %version-%release
Obsoletes: python3-module-%oname-devel < %version-%release
Conflicts: python3-module-sip < %version
Conflicts: python3-module-sip-devel

%description
SIP is a collection of tools that makes it very easy
to create Python bindings for C and C++ libraries.

SIP comprises a set of build tools and a sip module.
The build tools process a set of specification files
and generates C or C++ code which is then compiled
to create the bindings extension module.
Several extension modules may be installed
in the same Python package.
Extension modules can be built so that they are
independent of the version of Python being used.
In other words a wheel created from them
can be installed with any version of Python starting with v3.5.

The specification files contain a description of the interface
of the C or C++ library, i.e. the classes, methods, functions and variables.
The format of a specification file is almost identical to a C or C++ header file,
so much so that the easiest way of creating a specification file
is to edit a copy of the corresponding header file.

The sip module provides support functions to the automatically generated code.
The sip module is installed as part of the same Python package
as the generated extension modules.
Unlike the extension modules the sip module is specific
to a particular version of Python (e.g. v3.5, v3.6, v3.7, v3.8).

SIP makes it easy to exploit existing C or C++ libraries
in a productive interpretive programming environment.
SIP also makes it easy to take a Python application (maybe a prototype)
and selectively implement parts of the application (maybe for performance reasons) in C or C++.

%prep
%setup

# hack to drop .abi3 from binaries (TODO: add support to python3.req/prov)
# see https://www.python.org/dev/peps/pep-3149/
%__subst "s|suffixes = importlib.machinery.EXTENSION_SUFFIXES|suffixes = ['.so']|" sipbuild/buildable.py 

%build
%python3_build_debug

%install
%python3_install

%files
%doc README NEWS LICENSE*
%_bindir/sip5
%_bindir/sip-*
%python3_sitelibdir/sip-*
%python3_sitelibdir/sipbuild/

%changelog
* Sun Sep 06 2020 Vitaly Lipatov <lav@altlinux.ru> 5.4.0-alt1
- full spec rewrite
- new version 5.4.0 (with rpmrb script)
- download sources from PyPi
- drop PyQt4, PyQt5 subpackages
- drop .abi3 from binary extensions

* Sat Feb 08 2020 Anton Midyukov <antohami@altlinux.org> 4.19.19-alt3
- fix PATH to sip3 (it was broken in 4.19.13-alt1)

* Thu Feb 06 2020 Vitaly Lipatov <lav@altlinux.ru> 4.19.19-alt2
- fix build: add python2-base buildreq

* Mon Oct 07 2019 Vitaly Lipatov <lav@altlinux.ru> 4.19.19-alt1
- new version 4.19.19 (with rpmrb script)

* Sun Feb 03 2019 Anton Midyukov <antohami@altlinux.org> 4.19.13-alt1
- new version (4.19.13) with rpmgs script
- build PyQt4 and PyQt5-sip modules

* Wed Aug 22 2018 Sergey V Turchin <zerg@altlinux.org> 4.19.7-alt1.3
- move sipconfig and sipdistutils to devel subpackage

* Wed Aug 22 2018 Sergey V Turchin <zerg@altlinux.org> 4.19.7-alt1.2
- move .pyi to devel subpackage

* Thu Mar 22 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 4.19.7-alt1.1
- (NMU) Rebuilt with python-3.6.4.

* Wed Feb 14 2018 Vitaly Lipatov <lav@altlinux.ru> 4.19.7-alt1
- new version 4.19.7 (with rpmrb script)

* Tue Oct 03 2017 Vitaly Lipatov <lav@altlinux.ru> 4.19.3-alt1
- new version (4.19.3) with rpmgs script

* Sat Apr 02 2016 Ivan Zakharyaschev <imz@altlinux.org> 4.16.9-alt2
- (.spec) use updated correct %%__python3_includedir and %%__libpython3.

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 4.16.9-alt1.1
- NMU: Use buildreq for BR.

* Mon Jul 20 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.16.9-alt1
- Version 4.16.9

* Mon Jun 15 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.16.8-alt1
- Version 4.16.8

* Thu Mar 26 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.16.7-alt1
- Version 4.16.7

* Wed Mar 18 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.16.6-alt1
- Version 4.16.6

* Sun Jan 18 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.16.5-alt1
- Version 4.16.5

* Tue Nov 11 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.16.4-alt1
- Version 4.16.4

* Mon Jul 07 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.16.2-alt1
- Version 4.16.2

* Fri Jun 20 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.16.1-alt1
- Version 4.16.1

* Fri Jun 06 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.16-alt1
- Version 4.16

* Tue May 27 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.15.5-alt1
- Version 4.15.5

* Wed Dec 04 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.15.3-alt1
- Version 4.15.3

* Sat Nov 16 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.15.0-alt1
- Version 4.15.0 (ALT #29568)

* Mon Apr 15 2013 Andrey Cherepanov <cas@altlinux.org> 4.14.3-alt2.1
- Simplify module version set up

* Fri Apr 05 2013 Aleksey Avdeev <solo@altlinux.ru> 4.14.3-alt2
- Fix versions sets in sipconfig.py

* Fri Mar 01 2013 Aleksey Avdeev <solo@altlinux.ru> 4.14.3-alt1
- Version 4.14.3

* Thu Dec 20 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.14.2-alt2
- Release up

* Thu Dec 20 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.14.2-alt1
- Version 4.14.2

* Mon Sep 10 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.13.3-alt1
- Version 4.13.3

* Mon May 21 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.13.2-alt3
- Fixed config for python3-module-sip

* Sun May 20 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.13.2-alt2
- Added module for Python 3

* Thu Apr 12 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 4.13.2-alt1.1
- Rebuild to remove redundant libpython2.7 dependency

* Fri Feb 24 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.13.2-alt1
- Version 4.13.2

* Tue Jan 24 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.13.1-alt1
- Version 4.13.1

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 4.12.3-alt1.1
- Rebuild with Python-2.7

* Sun Jul 24 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.12.3-alt1
- Version 4.12.3

* Sun Mar 06 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.12.1-alt2
- Rebuilt for debuginfo

* Mon Jan 31 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.12.1-alt1
- Version 4.12.1 (ALT #24999)

* Sun Nov 28 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.11.2-alt1
- Version 4.11.2

* Tue Aug 03 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.10.5-alt2
- Set devel package as noarch

* Tue Aug 03 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.10.5-alt1
- Version 4.10.5

* Tue Jan 19 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.10-alt1
- Version 4.10

* Tue Nov 10 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.8.2-alt1.1
- Rebuilt with python 2.6

* Wed Aug 26 2009 Evgeny Sinelnikov <sin@altlinux.ru> 4.8.2-alt1
- Update to new release

* Mon Jul 13 2009 Evgeny Sinelnikov <sin@altlinux.ru> 4.8.1-alt1
- Update to new release

* Tue Nov 25 2008 Evgeny Sinelnikov <sin@altlinux.ru> 4.7.9-alt1
- New version

* Sun Aug 17 2008 Evgeny Sinelnikov <sin@altlinux.ru> 4.7.6-alt3
- Fixed rpath problem and libpython linking (#14655)

* Tue Aug 05 2008 Evgeny Sinelnikov <sin@altlinux.ru> 4.7.6-alt2
- Push rlz@ build to Sisyphus

* Sat Jun 07 2008 Dmitry M. Maslennikov <rlz at altlinux.org> 4.7.6-alt1
- New version

* Tue Jan 01 2008 Ivan Fedorov <ns@altlinux.org> 4.7.3-alt1
- 4.7.3

* Mon Aug 20 2007 Ivan Fedorov <ns@altlinux.org> 4.7-alt1
- 4.7

* Fri Jul 13 2007 Ivan Fedorov <ns@altlinux.org> 4.6-alt1
- 4.6
- Added support for wchar_t.
- The -g command line option releases the GIL whenever a call is made to
  the wrapped library.
- Added the /HoldGIL/ annotation to explicitly retain the GIL when
  calling a particular function in the wrapped library.
- Added sipFindClass() and sipFindNamedEnum() to the public API.
- /TransferThis/ may be specified more than once.
- Added support for __truediv__ and __itruediv__.
- The SIP code generator and module may be built as universal binaries
  under MacOS/X using the -n command line option to configure.py.

* Thu Dec 28 2006 Ivan Fedorov <ns@altlinux.ru> 4.5.2-alt1
- 4.5.2
- spec clean up (rewrite buildreqs)

* Thu Nov 09 2006 Ivan Fedorov <ns@altlinux.ru> 4.5-alt1
- 4.5

* Mon Jun 12 2006 Ivan Fedorov <ns@altlinux.ru> 4.4.5-alt1
- 4.4.5

* Sun May 28 2006 Ivan Fedorov <ns@altlinux.ru> 4.4.3-alt1
- 4.4.3
- fix #9616

* Sun Apr 09 2006 Ivan Fedorov <ns@altlinux.ru> 4.4.1-alt1
- 4.4.1

* Sun Apr 09 2006 Ivan Fedorov <ns@altlinux.ru> 4.4-alt1
- 4.4

* Mon Mar 06 2006 Alexey Morozov <almorozov@altlinux.org> 4.3.2-alt1.0.1
- NMU: fixed provides list for -devel subpackage
- changed XFree86-devel to xorg-x11-devel

* Wed Dec 07 2005 Ivan Fedorov <ns@altlinux.ru> 4.3.2-alt1
- 4.3.2

* Sat Nov 05 2005 Ivan Fedorov <ns@altlinux.ru> 4.3.1-alt1
- 4.3.1

* Sat Mar 12 2005 Ivan Fedorov <ns@altlinux.ru> 4.2.1-alt1
- 4.2.1
- rebuild with python 2.4

* Mon Feb 21 2005 Ivan Fedorov <ns@altlinux.ru> 4.2-alt1
- 4.2

* Thu Jan 27 2005 Ivan Fedorov <ns@altlinux.ru> 4.1.1-alt2
- updating obsoleting of sip

* Tue Jan 04 2005 Ivan Fedorov <ns@altlinux.ru> 4.1.1-alt0.M24.1
- Backport to Master 2.4

* Wed Dec 22 2004 Ivan Fedorov <ns@altlinux.ru> 4.1.1-alt1
- 4.1.1

* Sun Dec 12 2004 Ivan Fedorov <ns@altlinux.ru> 4.1-alt3
- fix spec to be compatible with python policy

* Tue Sep 28 2004 Eugene V. Horohorin <genix@altlinux.ru> 4.1-alt2
- license mistake fix
- spec clean up (using %%python_site_packages_dir instead of old method of %%python_site)

* Tue Sep 21 2004 Eugene V. Horohorin <genix@altlinux.org> 4.1-alt1
- new release

* Thu Sep 02 2004 Eugene V. Horohorin <genix@altlinux.ru> 4.0.1-alt1
- new release

* Wed May 19 2004 Serge V. Sergeev <ssv@altlinux.ru> 4.0-alt0.3
- new release

* Mon Feb 16 2004 Serge V. Sergeev <ssv@altlinux.ru> 3.10-alt1
- new release

* Wed Dec 24 2003 Serge V. Sergeev <ssv@altlinux.ru> 3.9-alt2
- add definitionn of QTDIR variable ( need for new build system )

* Thu Dec 11 2003 Serge V. Sergeev <ssv@altlinux.ru> 3.9-alt1
- new release

* Fri Aug 01 2003 Serge Sergeev <ssv@altlinux.ru> 3.7-alt2
- added _findprov_lib_path macro to temporary solve problem with dependencies

* Tue Jul 08 2003 Serge Sergeev <ssv@altlinux.ru> 3.7-alt1
- new release

* Mon Apr 28 2003 Serge Sergeev <ssv@altlinux.ru> 3.6-alt1
- new release

* Thu Apr 10 2003 Serge Sergeev <ssv@altlinux.ru> 3.6-alt0.1
- New build from snapshot

* Fri Dec 20 2002 Serge Sergeev <ssv@altlinux.ru> 3.5-alt2
- Increase release for upgrade

* Mon Dec 16 2002 Serge Sergeev <ssv@altlinux.ru> 3.5-alt1
- new release

* Mon Dec 16 2002 Serge Sergeev <ssv@altlinux.ru> 3.5-alt0.1.20021205
- new release
- correct version

* Fri Dec 06 2002 Serge Sergeev <ssv@altlinux.ru> 20021205-alt1
- build from snapshot
- some documentation added in separate package

* Tue Nov 05 2002 Serge Sergeev <ssv@altlinux.ru> 3.4-alt1
- new release

* Wed Sep 04 2002 Serge Sergeev <ssv@altlinux.ru> 3.3.2-alt1
- new release

* Fri Aug 02 2002 Serge Sergeev <sergeyssv@mail.ru> 3.3-alt1
- Clean up spec file

* Thu Jul 25  2002 <sergeyssv@mail.ru>
- some fixes

* Thu Jun 06  2002 <sergeyssv@mail.ru>
- Initial release
