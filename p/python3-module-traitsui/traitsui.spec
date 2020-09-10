%define _unpackaged_files_terminate_build 1

%define oname traitsui

%def_disable bootstrap

Name: python3-module-%oname
Version: 7.0.1
Release: alt1
Summary: A set of user interface tools designed to complement Traits
Group: Development/Python3
License: BSD, EPL and LGPL
URL: https://docs.enthought.com/traitsui
BuildArch: noarch

# https://github.com/enthought/traitsui.git
Source: %oname-%version.tar

Patch1: %oname-alt-docs.patch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setupdocs

%if_disabled bootstrap
BuildRequires(pre): python3-module-sphinx-devel
BuildRequires: python3-module-setupdocs
BuildRequires: python3-module-traits
BuildRequires: python3-module-sphinx-sphinx-build-symlink
%endif

# skip wx requirements
%add_python3_req_skip pyface.ui.wx.grid.api
%add_python3_req_skip pyface.ui.wx.grid.trait_grid_cell_adapter
%add_python3_req_skip pyface.ui.wx.image_list
%add_python3_req_skip pyface.ui.wx.progress_dialog
%add_python3_req_skip pyface.wx.dialog
%add_python3_req_skip pyface.wx.drag_and_drop
%add_python3_req_skip wx.animate wx.calendar wx.combo wx.gizmos
%add_python3_req_skip wx.grid wx.html wx.lib.masked wx.lib.mixins.listctrl
%add_python3_req_skip wx.lib.scrolledpanel wx.stc wx.wizard

# skip pickle requirements
%add_python3_req_skip matplotlib.backends.backend_wx matplotlib.backends.backend_wxagg

%description
TraitsUI is a set of user interface tools designed to complement Traits.
In the simplest case, it can automatically generate a user interface for
editing a Traits-based object, with no additional coding on the part of
the programmer-user. In more sophisticated uses, it can implement a
Model-View-Controller (MVC) design pattern for Traits-based objects.

%package tests
Summary: Tests for TraitsUI (Python 3)
Group: Development/Python3
Requires: %name = %EVR

%description tests
TraitsUI is a set of user interface tools designed to complement Traits.
In the simplest case, it can automatically generate a user interface for
editing a Traits-based object, with no additional coding on the part of
the programmer-user. In more sophisticated uses, it can implement a
Model-View-Controller (MVC) design pattern for Traits-based objects.

This package contains tests for TraitsUI.

%package docs
Summary: Documentation for TraitsUI
Group: Development/Documentation

%description docs
TraitsUI is a set of user interface tools designed to complement Traits.
In the simplest case, it can automatically generate a user interface for
editing a Traits-based object, with no additional coding on the part of
the programmer-user. In more sophisticated uses, it can implement a
Model-View-Controller (MVC) design pattern for Traits-based objects.

This package contains documentation for TraitsUI.

%package pickles
Summary: Pickles for TraitsUI
Group: Development/Python3
AutoReq: nopython

%description pickles
TraitsUI is a set of user interface tools designed to complement Traits.
In the simplest case, it can automatically generate a user interface for
editing a Traits-based object, with no additional coding on the part of
the programmer-user. In more sophisticated uses, it can implement a
Model-View-Controller (MVC) design pattern for Traits-based objects.

This package contains pickles for TraitsUI.

%prep
%setup
%patch1 -p1

%if_disabled bootstrap
%prepare_sphinx3 docs
ln -s ../objects.inv docs/source/
%endif

%build
%python3_build_debug

%if_disabled bootstrap
%make -C docs html
%make -C docs pickle
%endif

%install
%python3_install

%if_disabled bootstrap
# pickles
cp -fR docs/build/pickle %buildroot%python3_sitelibdir/%oname/
%endif

%files
%doc image_LICENSE*.txt LICENSE.txt
%doc *.rst
%doc CHANGES.txt TODO.txt
%python3_sitelibdir/%oname
%python3_sitelibdir/%oname-%version-py*.egg-info
%exclude %python3_sitelibdir/%oname/tests
%exclude %python3_sitelibdir/%oname/*/tests
%if_disabled bootstrap
%exclude %python3_sitelibdir/%oname/pickle
%endif

%files tests
%python3_sitelibdir/%oname/tests
%python3_sitelibdir/%oname/*/tests

%if_disabled bootstrap
%files docs
%doc docs/build/html docs/*.txt docs/*.ppt docs/*.pdf

%files pickles
%python3_sitelibdir/%oname/pickle
%endif

%changelog
* Wed Sep 09 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 7.0.1-alt1
- Updated to upstream version 7.0.1.

* Sun Feb 02 2020 Vitaly Lipatov <lav@altlinux.ru> 6.1.1-alt2
- NMU: build without python2

* Fri Jul 19 2019 Aleksei Nikiforov <darktemplar@altlinux.org> 6.1.1-alt1
- Updated to upstream version 6.1.1.
- Built modules for python-3.

* Mon Sep 24 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 6.0.0-alt1
- Updated to upstream version 6.0.0.

* Sun May 03 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.5.0-alt1.git20150224
- New snapshot

* Mon Nov 03 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.5.0-alt1.git20140911
- New snapshot

* Wed May 07 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.5.0-alt1.git20140110
- Version 4.5.0

* Mon Oct 28 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.3.0-alt2.git20131022
- Moved all tests into tests subpackage

* Sun Oct 27 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.3.0-alt1.git20131022
- New snapshot

* Mon May 06 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.3.0-alt1.git20130413
- Version 4.3.0

* Wed Jan 30 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.2.1-alt1.git20130108
- New snapshot

* Mon Oct 15 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.2.1-alt1.git20121009
- Version 4.2.1

* Sat May 12 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.1.1-alt1.git20120408
- New snapshot
- Added module for Python 3

* Thu Jan 26 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.1.1-alt1.git20120122
- Version 4.1.1

* Thu Nov 24 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.2-alt2.git20111103
- Moved tests into separate package

* Mon Nov 21 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.2-alt1.git20111103
- Initial build for Sisyphus

