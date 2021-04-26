%global pypi_name pbr

%def_without doc
%def_without python3

%define descr \
PBR is a library that injects some useful and sensible default behaviors \
into your setuptools run. It started off life as the chunks of code that \
were copied between all of the OpenStack projects. Around the time that \
OpenStack hit 18 different projects each with at least 3 active \
branches, it seems like a good time to make that code into a proper \
re-usable library.

Name:       python-module-%pypi_name
Version:    5.5.0
Release:    alt4

Summary:    Python Build Reasonableness

Group:      Development/Python
License:    Apache-2.0
URL:        http://pypi.python.org/pypi/pbr

# git://git.openstack.org/openstack-dev/pbr
Source: %name-%version.tar

BuildRequires: python-module-setuptools python-module-unittest2 python-module-d2to1
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools python3-module-unittest2 python3-module-d2to1
BuildRequires: python3-module-sphinxcontrib-apidoc
%endif

BuildArch:  noarch

%description
%descr

%package -n python3-module-%pypi_name
Summary:    Python Build Reasonableness
Group:      Development/Python3
Requires:   python3-module-pip

%description -n python3-module-%pypi_name
%descr

%prep
%setup
# Remove the requirements file so that pbr hooks don't add it
# to distutils requiers_dist config
rm -rf {test-,}requirements.txt

# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%if_with python3
cp -fR . ../python3
%endif

%build
export PBR_VERSION="%version"

export SKIP_PIP_INSTALL=1
%python_build

%if_with python3
pushd ../python3
%python3_build
popd
%endif

%if_with doc
# generate html docs
sphinx-build doc/source html
# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}
%endif

%install
export PBR_VERSION="%version"

%if_with python3
pushd ../python3
%python3_install
popd
pushd %buildroot%_bindir
for i in $(ls); do
    mv $i $i.py3
done
popd
%endif

%python_install

%files
%doc README.rst LICENSE
%if_with doc
%doc html
%endif
#_bindir/*
%if_with python3
%exclude %_bindir/*.py3
%endif
%python_sitelibdir/%pypi_name-%version-py*.egg-info
%python_sitelibdir/%pypi_name
%exclude %python_sitelibdir/%pypi_name/tests

%if_with python3
%files -n python3-module-%pypi_name
%doc README.rst LICENSE
%_bindir/*.py3
%python3_sitelibdir/%pypi_name-%version-py*.egg-info
%python3_sitelibdir/%pypi_name
%exclude %python3_sitelibdir/%pypi_name/tests
%endif

%changelog
* Mon Apr 26 2021 Vitaly Lipatov <lav@altlinux.ru> 5.5.0-alt4
- don't pack bin tools

* Sun Apr 25 2021 Vitaly Lipatov <lav@altlinux.ru> 5.5.0-alt3
- build python2 module only

* Tue Oct 27 2020 Stanislav Levin <slev@altlinux.org> 5.5.0-alt2
- Stopped packaging of tests.

* Thu Sep 03 2020 Grigory Ustinov <grenka@altlinux.org> 5.5.0-alt1
- Automatically updated to 5.5.0.

* Wed May 20 2020 Grigory Ustinov <grenka@altlinux.org> 5.4.5-alt1
- Build new version 5.4.5.
- Build docs with python3.
- Clean up BR's.

* Wed Dec 11 2019 Grigory Ustinov <grenka@altlinux.org> 5.4.4-alt1
- Build new version 5.4.4.

* Fri Sep 13 2019 Grigory Ustinov <grenka@altlinux.org> 5.4.3-alt1
- Build new version.

* Thu Aug 29 2019 Anton Farygin <rider@altlinux.ru> 5.4.2-alt2
- removed buildrequires on himself

* Tue Aug 06 2019 Grigory Ustinov <grenka@altlinux.org> 5.4.2-alt1
- Build new version.

* Fri Jul 19 2019 Grigory Ustinov <grenka@altlinux.org> 5.4.1-alt1
- Build new version.

* Thu Jul 11 2019 Grigory Ustinov <grenka@altlinux.org> 5.4.0-alt1
- Build new version.

* Fri Jun 21 2019 Grigory Ustinov <grenka@altlinux.org> 5.3.1-alt1
- Build new version.

* Mon Jun 17 2019 Grigory Ustinov <grenka@altlinux.org> 5.3.0-alt1
- Build new version.

* Mon Jun 03 2019 Grigory Ustinov <grenka@altlinux.org> 5.2.1-alt1
- Build new version.

* Mon Apr 29 2019 Grigory Ustinov <grenka@altlinux.org> 5.2.0-alt1
- Build new version.

* Mon Mar 04 2019 Grigory Ustinov <grenka@altlinux.org> 5.1.3-alt1
- Build new version.

* Fri Feb 01 2019 Grigory Ustinov <grenka@altlinux.org> 5.1.2-alt1
- Build new version.

* Thu Nov 08 2018 Grigory Ustinov <grenka@altlinux.org> 5.1.1-alt1
- Build new version.

* Wed Oct 24 2018 Grigory Ustinov <grenka@altlinux.org> 5.1.0-alt1
- Build new version.

* Mon Oct 08 2018 Grigory Ustinov <grenka@altlinux.org> 4.3.0-alt1
- Build new version.

* Thu Aug 09 2018 Grigory Ustinov <grenka@altlinux.org> 4.2.0-alt1
- Build new version.

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 3.1.1-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Wed Oct 25 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 3.1.1-alt1
- Updated to upstream version 3.1.1.

* Tue May 23 2017 Lenar Shakirov <snejok@altlinux.ru> 2.0.0-alt1
- Version 2.0.0

* Sat Jan 14 2017 Michael Shigorin <mike@altlinux.org> 1.8.1-alt1.1.1.1
- BOOTSTRAP: introduce doc knob (avoid sphinx)

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.8.1-alt1.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Wed Jan 27 2016 Mikhail Efremov <sem@altlinux.org> 1.8.1-alt1.1
- NMU: Use buildreq for BR.

* Tue Oct 27 2015 Alexey Shabalin <shaba@altlinux.ru> 1.8.1-alt1
- 1.8.1
- add tests subpackage

* Sat Jul 25 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3.0-alt1
- Version 1.3.0

* Mon Jan 19 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.10.7-alt1
- Version 0.10.7

* Wed Aug 20 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.10.0-alt1
- Version 0.10.0 (ALT #30192)

* Tue Aug 19 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5.23-alt1.1
- Added module for Python 3

* Mon Dec 16 2013 Pavel Shilovsky <piastry@altlinux.org> 0.5.23-alt1
- Initial release for Sisyphus (based on Fedora)
