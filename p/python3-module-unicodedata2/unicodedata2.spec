%define oname unicodedata2

Name: python3-module-%oname
Version: 13.0.0.post2
Release: alt1

Summary: Unicodedata backport for python 2 updated to the latest unicode version
License: Apache-2.0
Group: Development/Python3
Url: https://pypi.python.org/pypi/unicodedata2

# https://github.com/mikekap/unicodedata2.git
Source: %name-%version.tar

Patch: unicodedata2-python3.10.patch

BuildRequires(pre): rpm-build-python3


%description
The versions of this package match unicode versions, so
unicodedata2==7.0.0 is data from unicode 7.0.0. Additionally this
backports support for named aliases and named sequences to python2.

%prep
%setup
%patch -p1

%build
%add_optflags -fno-strict-aliasing
%python3_build_debug

%install
%python3_install

%check
%__python3 setup.py test -v

%files
%doc LICENSE *.md
%python3_sitelibdir/*


%changelog
* Wed Dec 15 2021 Grigory Ustinov <grenka@altlinux.org> 13.0.0.post2-alt1
- Build new version.

* Tue Jan 14 2020 Andrey Bychkov <mrdrew@altlinux.org> 12.1.0-alt1
- Version updated to 12.1.0
- porting on python3

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 7.0.0.2-alt1.git20150807.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Sat Aug 08 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 7.0.0.2-alt1.git20150807
- Initial build for Sisyphus

