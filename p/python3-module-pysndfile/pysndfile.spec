%define _unpackaged_files_terminate_build 1

%define oname pysndfile

Name: python3-module-%oname
Version: 1.1.0
Release: alt3

Summary: Cython wrapper class for reading/writing soundfiles using libsndfile
License: LGPLv3
Group: Development/Python3
Url: https://pypi.python.org/pypi/pysndfile/

Source: %oname-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: gcc-c++ libsndfile-devel
BuildRequires: python3-dev python3-module-setuptools
BuildRequires: python3-module-Cython libnumpy-py3-devel
BuildRequires: python3-module-numpy-testing
BuildRequires: python3-module-html5lib python3-module-notebook

%description
pysndfile is a python package providing PySndfile, a Cython wrapper
class around libsndfile. PySndfile provides methods for reading and
writing a large variety of soundfile formats on a variety of plattforms.
PySndfile provides a rather complete access to the different sound file
manipulation options that are available in libsndfile.

Due to the use of libsndfile nearly all sound file formats, (besides mp3
and derived formats) can be read and written with PySndfile.

%prep
%setup -n %oname-%version

rm -f *.cpp

%build
%python3_build_debug

%install
%python3_install

%check
export CFLAGS="%optflags"
export CXXFLAGS="%optflags"
export FFLAGS="%optflags"

%__python3 setup.py test
PYTHONPATH=%buildroot%python3_sitelibdir python3 tests/pysndfile_test.py

%files
%doc ChangeLog README.*
%python3_sitelibdir/*


%changelog
* Thu Mar 19 2020 Andrey Bychkov <mrdrew@altlinux.org> 1.1.0-alt3
- Build for python2 disabled.

* Sun Oct 14 2018 Igor Vlasenko <viy@altlinux.ru> 1.1.0-alt2.qa1
- NMU: applied repocop patch

* Wed May 30 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 1.1.0-alt2
- Rebuilt without clang.

* Thu Mar 22 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 1.1.0-alt1.1
- (NMU) Rebuilt with python-3.6.4.

* Tue Mar 06 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 1.1.0-alt1
- Updated to upstream version 1.1.0.

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.0.0-alt2.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Tue Jan 09 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 1.0.0-alt2
- Fixed build.

* Tue Dec 26 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 1.0.0-alt1
- Updated to upstream version 1.0.0.

* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 0.2.11-alt1
- automated PyPI update

* Thu Mar 17 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.2.10-alt1.1.1
- (NMU) rebuild with python3-3.5 & rpm-build-python3-0.1.10
  (for ABI dependence and new python3(*) reqs)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.2.10-alt1.1
- NMU: Use buildreq for BR.

* Thu Nov 20 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.10-alt1
- Initial build for Sisyphus

