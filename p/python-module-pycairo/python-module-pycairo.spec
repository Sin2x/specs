%def_disable snapshot
%def_enable python2
%def_with doc

%define modname cairo
%define oname py%modname
%define ver_major 1.18

Name: python-module-%oname
Version: %ver_major.2
Release: alt1

Summary: Pycairo is a set of Python bindings for the cairo vector graphics library
Group: Development/Python
License: LGPLv2.1/MPLv1.1
Url: https://github.com/pygobject/pycairo

%if_disabled snapshot
Source: %url/releases/download/v%version/%oname-%version.tar.gz
%else
# VCS: https://github.com/pygobject/pycairo.git
Source: %oname-%version.tar
%def_with bootstrap
%endif

%{?_enable_python2:%setup_python_module %modname}

BuildRequires: libcairo-devel >= 1.13.1
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel
%{?_with_bootstrap:BuildRequires: python3-module-Pygments}
%{?_with_doc:
BuildRequires(pre): rpm-macros-sphinx3
BuildRequires: texlive-latex-base python3-module-sphinx-devel python3-module-sphinx_rtd_theme}

%if_enabled python2
BuildRequires(pre): rpm-build-python
BuildRequires: python-devel
%{?_with_bootstrap:BuildRequires: python-module-Pygments}
%endif

%description
The Pycairo bindings are designed to match the cairo C API as closely as
possible, and to deviate only in cases which are clearly better implemented in
a more 'Pythonic' way.

%package -n python3-module-%oname
Summary: Python3 bindings for Cairo
Group: Development/Python3

%description -n python3-module-%oname
This package provides Python3 wrappers for Cairo library

%package -n python3-module-%oname-devel
Summary: Development files for pycairo
Group: Development/Python
Requires: python3-module-%oname = %version-%release
Requires: %name-common-devel = %version-%release

%description -n python3-module-%oname-devel
Development files for pycairo.

%package common-devel
Summary: Common development files for %oname
Group: Development/Python

%description common-devel
Common development files for %oname used for both python2 and python3.

%package devel
Summary: Development files for pycairo
Group: Development/Python
Requires: %name = %version-%release
Requires: %name-common-devel = %version-%release

%description devel
Development files for pycairo.

%package docs
Summary: Documentation for pycairo
Group: Development/Documentation
BuildArch: noarch

%description docs
Documentation for pycairo.

%package -n python3-module-%oname-tests
Summary: Tests for pycairo
Group: Development/Python3
Requires: python3-module-%oname = %version-%release

%description -n python3-module-%oname-tests
Documentation for pycairo.

%package -n python3-module-%oname-examples
Summary: Examples for pycairo
Group: Development/Python3
Requires: python3-module-%oname = %version-%release

%description -n python3-module-%oname-examples
Examples for pycairo.

%package -n python3-module-%oname-pickles
Summary: Pickles for pycairo
Group: Development/Python3

%description -n python3-module-%oname-pickles
Pickles for pycairo.

%prep
%setup -n %oname-%version %{?_enable_python2:-a0
mv %oname-%version py2build}

# fix pc-file install
subst 's|\"lib\"|"%_lib"|' setup.py %{?_enable_python2:py2build/setup.py}

%{?_with_doc:%prepare_sphinx3 docs}

%build
# incomplete support
%define opts --pkgconfigdir=%_pkgconfigdir
%python3_build
%{?_with_doc:%make -C docs}

%if_enabled python2
pushd py2build
%python_build
popd
%endif

%install
%if_enabled python2
pushd py2build
%python_install
popd
%endif

%python3_install

# docs
install -d %buildroot%_docdir/%name-%version
install -p -m644 NEWS README* \
	%buildroot%_docdir/%name-%version

%if_with doc
cp -fR docs/_build/reference %buildroot%_docdir/%name-%version/

# pickles
install -d %buildroot%python3_sitelibdir/%oname/pickle
cp -fR docs/_build/.doctrees/* %buildroot%python3_sitelibdir/%oname/pickle/

# tests and examples
cp -fR examples tests %buildroot%python3_sitelibdir/%modulename/
for i in $(find %buildroot%python3_sitelibdir/%modulename/examples -type d)
do
	touch $i/__init__.py
done

%pre -n python3-module-%oname-pickles
rm -fR %python3_sitelibdir/%oname/pickle
%endif # doc

%files
%if_enabled python2
%python_sitelibdir/%modulename
%endif

%files -n python3-module-%oname
%python3_sitelibdir/%modname/
%if_with doc
%exclude %python3_sitelibdir/%modulename/tests
%exclude %python3_sitelibdir/%modulename/examples
%endif
%doc %dir %_docdir/%name-%version
%doc %_docdir/%name-%version/NEWS
%doc %_docdir/%name-%version/README*

%files common-devel
%_includedir/%oname/

%files devel
%_pkgconfigdir/%oname.pc

%files -n python3-module-%oname-devel
%_pkgconfigdir/py3cairo.pc

%if_with doc
%files docs
%doc %dir %_docdir/%name-%version
%doc %_docdir/%name-%version
%exclude %_docdir/%name-%version/NEWS
%exclude %_docdir/%name-%version/README*

%files -n python3-module-%oname-tests
%python3_sitelibdir/%modulename/tests

%files -n python3-module-%oname-examples
%python3_sitelibdir/%modulename/examples

%files -n python3-module-%oname-pickles
%dir %python3_sitelibdir/%oname
%python3_sitelibdir/%oname/pickle/
%endif

%changelog
* Sat Oct 26 2019 Yuri N. Sedunov <aris@altlinux.org> 1.18.2-alt1
- 1.18.2
- made python2 build optional

* Sat Apr 20 2019 Yuri N. Sedunov <aris@altlinux.org> 1.18.1-alt1
- 1.18.1

* Sat Nov 24 2018 Yuri N. Sedunov <aris@altlinux.org> 1.18.0-alt1
- 1.18.0

* Thu Oct 25 2018 Yuri N. Sedunov <aris@altlinux.org> 1.17.1-alt1
- 1.17.1

* Thu Mar 22 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 1.16.3-alt1.1
- (NMU) Rebuilt with python-3.6.4.

* Fri Mar 02 2018 Yuri N. Sedunov <aris@altlinux.org> 1.16.3-alt1
- 1.16.3

* Mon Sep 04 2017 Yuri N. Sedunov <aris@altlinux.org> 1.15.2-alt1
- 1.15.2

* Fri Jun 09 2017 Yuri N. Sedunov <aris@altlinux.org> 1.13.3-alt1
- 1.13.3

* Thu Jun 01 2017 Yuri N. Sedunov <aris@altlinux.org> 1.13.2-alt1
- 1.13.2

* Wed May 10 2017 Yuri N. Sedunov <aris@altlinux.org> 1.13.1-alt1
- 1.13.1

* Sat Apr 22 2017 Yuri N. Sedunov <aris@altlinux.org> 1.12.0-alt1
- 1.12.0

* Sat Apr 22 2017 Yuri N. Sedunov <aris@altlinux.org> 1.11.0-alt1
- 1.11.0 (new upstream), built 2 & 3 modules from one source

* Thu Jan 12 2017 Michael Shigorin <mike@altlinux.org> 1.10.1-alt2.git20120522.1
- BOOTSTRAP: added doc knob (on by default)

* Thu Oct 11 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.10.1-alt2.git20120522
- New snapshot

* Mon Nov 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.10.1-alt2.git20110619
- Enabled docs (except pdf) and pickles

* Mon Oct 24 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.10.1-alt1.git20110619.1
- Rebuild with Python-2.7
- bootstrap without docs and pickles

* Sat Aug 20 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.10.1-alt1.git20110619
- New snapshot
- Fixed updating (ALT #26118)

* Mon May 09 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.10.1-alt1.git20110502
- Version 1.10.1

* Tue Apr 05 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.8.11-alt1.git20110328.1
- Rebuilt with python-module-sphinx-devel

* Tue Mar 29 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.8.11-alt1.git20110328
- Some fixes from upstream

* Sun Mar 13 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.8.11-alt1.git20110123
- Version 1.8.11
- Rebuilt for debuginfo

* Thu Oct 28 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.8.10-alt1.git20100922.1
- Rebuilt for soname set-versions

* Mon Oct 18 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.8.10-alt1.git20100922
- Version 1.8.10 (ALT #24355)

* Fri Feb 26 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.8.9-alt1.git20100114
- Version 1.8.9
- Added docs, tests, examples and pickles packages

* Tue Nov 10 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.8.6-alt1.1
- Rebuilt with python 2.6

* Wed Jul 01 2009 Alexey Shabalin <shaba@altlinux.ru> 1.8.6-alt1
- new version 1.8.6 (with rpmrb script)
- update buildreq
- add patch for build with python-2.5 (upstream requires 2.6)

* Tue Sep 30 2008 Alexey Shabalin <shaba@altlinux.ru> 1.4.12-alt1
- new version 1.4.12 (with rpmrb script)

* Thu Jan 24 2008 Grigory Batalov <bga@altlinux.ru> 1.4.0-alt1.1
- Rebuilt with python-2.5.

* Sun Jun 24 2007 Vitaly Lipatov <lav@altlinux.ru> 1.4.0-alt1
- new version 1.4.0 (with rpmrb script)

* Sat Apr 07 2007 Vitaly Lipatov <lav@altlinux.ru> 1.2.6-alt1
- new version 1.2.6 (with rpmrb script)

* Sat Sep 02 2006 Vitaly Lipatov <lav@altlinux.ru> 1.2.2-alt0.1
- new version 1.2.2 (with rpmrb script)

* Sun Apr 30 2006 Vitaly Lipatov <lav@altlinux.ru> 1.0.2-alt3
- rebuild with new cairo

* Thu Feb 09 2006 Vitaly Lipatov <lav@altlinux.ru> 1.0.2-alt2
- update build requires

* Tue Nov 22 2005 Vitaly Lipatov <lav@altlinux.ru> 1.0.2-alt1
- fix build/install sections (#7930)
- split devel package

* Tue Oct 04 2005 Vitaly Lipatov <lav@altlinux.ru> 1.0.2-alt0.1
- new version
- add pycairo.pc to install

* Mon Sep 12 2005 Vitaly Lipatov <lav@altlinux.ru> 1.0.0-alt2
- enable build cairo.gtk

* Fri Sep 02 2005 Vitaly Lipatov <lav@altlinux.ru> 1.0.0-alt1
- new version

* Sun Aug 28 2005 Vitaly Lipatov <lav@altlinux.ru> 0.9.0-alt0.1
- first build for ALT Linux Sisyphus
