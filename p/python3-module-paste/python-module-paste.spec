%define oname Paste
%def_with bootstrap

Name: python3-module-paste
Version: 3.5.0
Release: alt1.1

Summary: Tools for using a Web Server Gateway Interface stack

License: MIT
Group: Development/Python
Url: https://github.com/cdent/paste/

# Source-url: %__pypi_url %oname
Source: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-intro >= 2.2.5
BuildRequires(pre): rpm-build-python3

BuildRequires: python3-module-setuptools

%py3_provides Paste
%add_python3_req_skip scgi hotshot rfc822
%add_python3_req_skip flup.middleware.session hotshot.stats
# FIXME:mask python2 modules
%add_python3_req_skip cStringIO thread urlparse

%add_python3_self_prov_path %buildroot%python3_sitelibdir/paste/wsgilib.py

%description
These provide several pieces of "middleware" (or filters) that can be
nested to build web applications. Each piece of middleware uses the
WSGI (PEP 333) interface, and should be compatible with other
middleware based on those interfaces.

%prep
%setup

%build
%python3_build

%install
%python3_install
# hack for autocreate "provides python2.5(paste)"
touch %buildroot%python3_sitelibdir/paste/__init__.py


%files
%python3_sitelibdir/paste/
%python3_sitelibdir/*.egg-info


%changelog
* Sun Nov 13 2022 Daniel Zagaynov <kotopesutility@altlinux.org> 3.5.0-alt1.1
- NMU: used %%add_python3_self_prov_path macro to skip self-provides from dependencies.

* Sat Jul 10 2021 Vitaly Lipatov <lav@altlinux.ru> 3.5.0-alt1
- build python3 module separately, cleanup build

* Wed Oct 09 2019 Oleg Solovyov <mcpain@altlinux.org> 2.0.3-alt2
- disable unneeded "next" fix from 2to3

* Fri May 25 2018 Andrey Bychkov <mrdrew@altlinux.org> 2.0.3-alt1.1
- fix requires

* Tue May 22 2018 Andrey Bychkov <mrdrew@altlinux.org> 2.0.3-alt1
- updated version to 2.0.3 from tarball

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.7.5.1-alt3.hg20140319.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 1.7.5.1-alt3.hg20140319.1
- NMU: Use buildreq for BR.

* Sat Feb 07 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.7.5.1-alt3.hg20140319
- Deteled bad suffix from version

* Mon Jul 14 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.7.5.1-alt2.hg20140319
- New snapshot

* Wed Sep 18 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.7.5.1-alt2.hg20130410
- New snapshot

* Mon Apr 15 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.7.5.1-alt2.hg20130207
- Use 'find... -exec...' instead of 'for ... $(find...'

* Tue Apr 02 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.7.5.1-alt1.hg20130207
- New snapshot

* Fri Mar 22 2013 Aleksey Avdeev <solo@altlinux.ru> 1.7.5.1-alt1.hg20120305.1
- Rebuild with Python-3.3

* Fri Apr 13 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.7.5.1-alt1.hg20120305
- New snapshot
- Added module for Python 3

* Fri Jan 27 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.7.5.1-alt1.hg20110817
- Version 1.7.5.1

* Mon Oct 24 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.7.3.1-alt2.1
- Rebuild with Python-2.7

* Sun Jun 26 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.7.3.1-alt2
- Added %%py_provides Paste

* Wed May 05 2010 Andrey Rahmatullin <wrar@altlinux.ru> 1.7.3.1-alt1
- 1.7.3.1
- remove some optional dependencies (closes: #23442)

* Wed Nov 18 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.7.2-alt1.1
- Rebuilt with python 2.6

* Mon Mar 30 2009 Vladimir V. Kamarzin <vvk@altlinux.org> 1.7.2-alt1
- Initial build for Sisyphus

