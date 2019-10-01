%define _unpackaged_files_terminate_build 1
%define oname texext

%def_with python3

Name: python-module-%oname
Version: 0.6.1
Release: alt2
Summary: Sphinx extensions for working with LaTeX math
License: BSD
Group: Development/Python
BuildArch: noarch
Url: https://github.com/matthew-brett/texext

# https://github.com/matthew-brett/texext.git
Source: %name-%version.tar
Patch0: texext-0.6.1-Adapt-tests-to-Sphinx-2-output.patch

BuildRequires: python-devel python-module-setuptools python-module-sphinxtesters
BuildRequires: python2.7(docutils) python2.7(sphinx.errors) python2.7(sphinxtesters) python2.7(sympy) python2.7(nose.tools) python2.7(matplotlib.sphinxext.plot_directive)
BuildRequires: python2.7(pytest)
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3(pytest)
BuildRequires: python3-devel python3-module-setuptools python3-module-sphinxtesters
BuildRequires: python3(docutils) python3(sphinx.errors) python3(sphinxtesters) python3(sympy) python3(nose.tools) python3(matplotlib.sphinxext.plot_directive)
%endif

%description
Texext - sphinx extensions for working with LaTeX math.

%if_with python3
%package -n python3-module-%oname
Summary: Sphinx extensions for working with LaTeX math
Group: Development/Python3

%description -n python3-module-%oname
Texext - sphinx extensions for working with LaTeX math.
%endif

%prep
%setup
%patch0 -p1

# fix version info
sed -i \
	-e "s/git_refnames\s*=\s*\"[^\"]*\"/git_refnames = \" \(tag: %version\)\"/" \
	%oname/_version.py

%if_with python3
cp -fR . ../python3
%endif

%build
%python_build_debug

%if_with python3
pushd ../python3
%python3_build_debug
popd
%endif

%install
%python_install

%if_with python3
pushd ../python3
%python3_install
popd
%endif

%check
py.test -vv

%if_with python3
pushd ../python3
py.test3 -vv
popd
%endif

%files
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%python3_sitelibdir/*
%endif

%changelog
* Tue Oct 01 2019 Stanislav Levin <slev@altlinux.org> 0.6.1-alt2
- Fixed testing against Sphinx 2.x.

* Mon Dec 24 2018 Grigory Ustinov <grenka@altlinux.org> 0.6.1-alt1
- Build new version.

* Tue Nov 28 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.5-alt1
- Initial build for ALT.
