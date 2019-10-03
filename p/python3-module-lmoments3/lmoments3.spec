%define _unpackaged_files_terminate_build 1
%define oname lmoments3

%def_with check
Name: python3-module-%oname
Version: 1.0.4
Release: alt1
Summary: Estimate linear moments for statistical distribution functions
License: GPLv3
Group: Development/Python3
Url: https://pypi.org/project/lmoments3/

# https://github.com/OpenHydrology/lmoments3.git
Source: %name-%version.tar
BuildArch: noarch

BuildRequires(pre): rpm-build-python3

%if_with check
BuildPreReq: python3(nose)
BuildPreReq: python3(numpy)
BuildPreReq: python3(numpy.testing)
BuildPreReq: python3(scipy)
%endif

%description
This library was designed to use L-moments to calculate optimal
parameters for a number of distributions. This library extends a number
of scipy distributions and provides some additional distributions
frequently used in Extreme Value Analyses.

%prep
%setup
# workaround for versioneer
grep -qsF ' export-subst' .gitattributes || exit 1
vers_f="$(sed -n 's/ export-subst//p' .gitattributes)"
grep -qs '^[ ]*git_refnames[ ]*=[ ]*""[ ]*$' "$vers_f" || exit 1
sed -i 's/^\([ ]*\)git_refnames[ ]*=[ ]*""[ ]*$/\1git_refnames = " (tag: v%version, upstream\/master)"/' "$vers_f"

%build
%python3_build_debug

%install
%python3_install

%check
nosetests3 -v

%files
%doc CHANGELOG.txt *.rst docs/source/*.rst
%python3_sitelibdir/%oname/
%python3_sitelibdir/%oname-%version-py%_python3_version.egg-info/

%changelog
* Thu Oct 03 2019 Stanislav Levin <slev@altlinux.org> 1.0.4-alt1
- 1.0.2 -> 1.0.4.
- Fixed testing.

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.0.2-alt1.git20150211.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Mon Mar 14 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.0.2-alt1.git20150211.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Tue Apr 21 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.2-alt1.git20150211
- Initial build for Sisyphus

