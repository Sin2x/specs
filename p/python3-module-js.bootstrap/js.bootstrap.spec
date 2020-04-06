%define oname js.bootstrap

Name: python3-module-%oname
Version: 3.4
Release: alt2.dev0.git20150113.1

Summary: fanstatic twitter bootstrap
License: BSD
Group: Development/Python3
Url: https://pypi.python.org/pypi/js.bootstrap/

# https://github.com/RedTurtle/js.bootstrap.git
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools

%py3_requires js js.query

%description
This library packages twitter bootstrap for fanstatic. It is aware of
different modes (normal, minified).

%prep
%setup

%build
%python3_build_debug

%install
%python3_install

%if "%_libexecdir" != "%_libdir"
mv %buildroot%_libexecdir %buildroot%_libdir
%endif

%files
%doc *.txt *.rst
%python3_sitelibdir/*

%changelog
* Mon Apr 06 2020 Andrey Bychkov <mrdrew@altlinux.org> 3.4-alt2.dev0.git20150113.1
- Build for python2 disabled.

* Tue Apr 30 2019 Grigory Ustinov <grenka@altlinux.org> 3.4-alt1.dev0.git20150113.2
- Rebuild with python3.7.

* Tue May 24 2016 Ivan Zakharyaschev <imz@altlinux.org> 3.4-alt1.dev0.git20150113.1.1
- (AUTO) subst_x86_64.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 3.4-alt1.dev0.git20150113.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Tue Jan 13 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.4-alt1.dev0.git20150113
- Version 3.4.dev0

* Thu Oct 09 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.2.1-alt1.dev0.git20140903
- Initial build for Sisyphus

