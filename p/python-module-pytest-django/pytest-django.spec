%define _unpackaged_files_terminate_build 1
%define oname pytest-django

%def_with check

Name: python-module-%oname
Version: 3.5.1
Release: alt1

Summary: A Django plugin for py.test
License: BSD
Group: Development/Python
Url: https://pypi.org/project/pytest-django/
# https://github.com/pytest-dev/pytest-django.git
BuildArch: noarch

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python2.7(setuptools_scm)
BuildRequires: python3(setuptools_scm)

%if_with check
BuildRequires: python3-module-django2.2
BuildRequires: python3-module-django2.2-tests
BuildRequires: python3-module-django2.2-dbbackend-sqlite3
BuildRequires: python3(pytest-xdist)
BuildRequires: python3(tox)
%endif

%py_requires pathlib2
%py_provides %oname

# we have several versions of Django
# so, we cannot rely on auto-requires
%filter_from_requires /^python2\.7(django\(\..*\)\?)/d
%filter_from_requires /^python3(django\(\..*\)\?)/d

%description
pytest-django allows you to test your Django project/applications with
the pytest testing tool.

%package -n python3-module-%oname
Summary: A Django plugin for py.test
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
pytest-django allows you to test your Django project/applications with
the pytest testing tool.

%prep
%setup
# haven't packaged yet
grep -qsF 'django-configurations' setup.py || exit 1
sed -i '/django-configurations/d' setup.py

cp -fR . ../python3

%build
# SETUPTOOLS_SCM_PRETEND_VERSION: when defined and not empty,
# its used as the primary source for the version number in which
# case it will be a unparsed string
export SETUPTOOLS_SCM_PRETEND_VERSION=%version
%python_build_debug

pushd ../python3
%python3_build_debug
popd

%install
export SETUPTOOLS_SCM_PRETEND_VERSION=%version
%python_install

pushd ../python3
%python3_install
popd

%check
sed -i -e '/^\[testenv\]$/a whitelist_externals =\
    \/bin\/cp\
    \/bin\/sed\
commands_pre =\
    \/bin\/cp {env:_PYTEST_BIN:} \{envbindir\}\/pytest\
    \/bin\/sed -i \x271c #!\{envpython\}\x27 \{envbindir\}\/pytest' \
-e '/^setenv[ ]*=/a\
    py%{python_version_nodots python}: _PYTEST_BIN=%_bindir\/py.test\
    py%{python_version_nodots python3}: _PYTEST_BIN=%_bindir\/py.test3' \
tox.ini

export SETUPTOOLS_SCM_PRETEND_VERSION=%version
export PIP_NO_INDEX=YES
export TOXENV=py%{python_version_nodots python3}
tox.py3 --sitepackages -v

%files
%doc AUTHORS *.rst
%python_sitelibdir/*

%files -n python3-module-%oname
%doc AUTHORS *.rst
%python3_sitelibdir/*


%changelog
* Fri Aug 16 2019 Stanislav Levin <slev@altlinux.org> 3.5.1-alt1
- 2.8.0 -> 3.5.1.
- Enabled testing for Python3.

* Fri May 25 2018 Andrey Bychkov <mrdrew@altlinux.org> 2.8.0-alt3.1
- rebuild with all requires

* Thu May 17 2018 Andrey Bychkov <mrdrew@altlinux.org> 2.8.0-alt3
- rebuild with python3.6

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 2.8.0-alt2.git20150303.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Tue Feb 02 2016 Sergey Alembekov <rt@altlinux.ru> 2.8.0-alt2.git20150303
- cleanup buildreq
- disable tests

* Fri Mar 06 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.8.0-alt1.git20150303
- Version 2.8.0

* Fri Oct 17 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.7.0-alt1.git20141012
- Initial build for Sisyphus

