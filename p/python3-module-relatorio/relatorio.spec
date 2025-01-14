%define _unpackaged_files_terminate_build 1
%define oname relatorio

%def_with check

Name: python3-module-%oname
Version: 0.10.0
Release: alt1

Summary: A templating library able to output odt and pdf files
License: GPL-3
Group: Development/Python3
Url: https://pypi.org/project/relatorio/

Source0: https://files.pythonhosted.org/packages/98/50/a72676bad791bec1f5399667d982f50d64215ca86e16ecce479b28b4b5b1/%oname-%version.tar.gz
BuildArch: noarch

BuildRequires(pre): rpm-build-python3

%if_with check
# install_requires:
BuildRequires: python3(genshi)
BuildRequires: python3(lxml)

# testing
BuildRequires: python3(python-magic)
BuildRequires: python3(tox)
BuildRequires: python3(tox_no_deps)
%endif

%description
A templating library which provides a way to easily output all kind of
different files (odt, ods, png, svg, ...). Adding support for more
filetype is easy: you just have to create a plugin for this.

relatorio also provides a report repository allowing you to link python
objects and report together, find reports by mimetypes/name/python
objects.

%prep
%setup -n %oname-%version

%build
%python3_build_debug

%install
%python3_install

# don't package tests
rm -r %buildroot%python3_sitelibdir/%oname/tests/

%check
# `test` command of setuptools is deprecated
sed -i 's/{envpython} setup.py test/python -m unittest discover/' tox.ini
export PIP_NO_INDEX=YES
export TOXENV=py3
tox.py3 --sitepackages --no-deps -vvr -s false

%files
%doc CHANGELOG README
%_bindir/relatorio-render
%python3_sitelibdir/%oname/
%python3_sitelibdir/%oname-%version-py%_python3_version.egg-info/

%changelog
* Thu Sep 16 2021 Stanislav Levin <slev@altlinux.org> 0.10.0-alt1
- 0.9.0 -> 0.10.0.

* Fri Oct 18 2019 Andrey Bychkov <mrdrew@altlinux.org> 0.9.0-alt1
- Version updated to 0.9.0

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.6.4-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 0.6.4-alt1
- automated PyPI update

* Fri Mar 06 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.1-alt3
- Fixed build

* Tue Oct 21 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.1-alt2
- Moved tests into separate package

* Mon Oct 20 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.1-alt1
- Initial build for Sisyphus

