Name: python3-module-Pillow
Version: 8.1.1
Release: alt1

Summary: Python Imaging Library
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/Pillow/

Source0: %name-%version-%release.tar

BuildRequires: rpm-build-python3 python3-module-setuptools
BuildRequires: pkgconfig(libjpeg)
BuildRequires: pkgconfig(libopenjp2)
BuildRequires: pkgconfig(libtiff-4)
BuildRequires: pkgconfig(zlib)
BuildRequires: pkgconfig(freetype2)
BuildRequires: pkgconfig(lcms2)
BuildRequires: pkgconfig(imagequant)
BuildRequires: pkgconfig(libwebp)
BuildRequires: pkgconfig(libwebpmux)

%description
Pillow is the friendly PIL fork by Alex Clark and Contributors.
PIL is the Python Imaging Library by Fredrik Lundh and Contributors.

%prep
%setup

%build
%python3_build

%install
%python3_install

%check
PYTHONPATH=%buildroot%python3_sitelibdir python3 selftest.py

%add_python3_req_skip tkinter

%files
%doc *.rst docs/COPYING LICENSE *.md
%python3_sitelibdir/PIL
%python3_sitelibdir/Pillow-%version-*-info

%changelog
* Tue Mar 16 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 8.1.1-alt1
- 8.1.1 released (fixes: CVE-2021-25291)

* Fri Feb 19 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 8.1.0-alt1
- 8.1.0 released

* Tue Sep 22 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 7.2.0-alt2
- avoid tkinter dependency

* Mon Sep 21 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 7.2.0-alt1
- 7.2.0 released

* Mon Oct 07 2019 Vitaly Lipatov <lav@altlinux.ru> 6.2.0-alt1
- new version 6.2.0 (with rpmrb script)

* Sun Jul 01 2018 Vitaly Lipatov <lav@altlinux.ru> 5.2.0-alt1
- new version 5.2.0 (with rpmrb script) with check enabled
- drop PIL.pth, it was an illusion to support import Image
- rewrite install, check and make docs (thanks, Fedora)
- add openjpeg support

* Wed Apr 25 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 5.1.0-alt2
- (NMU) Rebuilt with python-3.6.4.

* Tue Apr 24 2018 Vitaly Lipatov <lav@altlinux.ru> 5.1.0-alt1
- new version 5.1.0 (with rpmrb script)
- build with libeimagequant support

* Wed Oct 04 2017 Vitaly Lipatov <lav@altlinux.ru> 4.3.0-alt1
- switch to build from tarball
- new version (4.3.0) with rpmgs script

* Fri Mar 24 2017 Vladimir D. Seleznev <vseleznv@altlinux.org> 3.0.0-alt2.dev0.git20150806.1.qa1
- NMU: rebuilt against Tcl/Tk 8.6.

* Mon May 23 2016 Ivan Zakharyaschev <imz@altlinux.org> 3.0.0-alt2.dev0.git20150806.1
- BR: sphinx_rtd_theme (the theme is optional since sphinx-1.4.1).

* Sat Apr  2 2016 Ivan Zakharyaschev <imz@altlinux.org> 3.0.0-alt2.dev0.git20150806
- (.spec) use the new correct %%__python3_includedir.

* Wed Jan 27 2016 Mikhail Efremov <sem@altlinux.org> 3.0.0-alt1.dev0.git20150806.1
- NMU: Use buildreq for BR.

* Thu Aug 06 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.0.0-alt1.dev0.git20150806
- Version 3.0.0.dev0

* Fri Mar 06 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.7.0-alt1.git20150302
- New snapshot
- Added devel package

* Sun Mar 01 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.7.0-alt1.git20150225
- Snapshot from git

* Fri Jan 02 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.7.0-alt1
- Version 2.7.0

* Sat Jul 26 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.5.1-alt3
- Added PIL.pth into python3-module-%oname

* Fri Jul 25 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.5.1-alt2
- Provides python-module-imaging

* Mon Jul 21 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.5.1-alt1
- Initial build for Sisyphus

