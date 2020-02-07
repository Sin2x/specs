%define _unpackaged_files_terminate_build 1
%define oname cpuinfo

Name: python3-module-%oname
Version: 3.3.0
Release: alt3

Summary: Get CPU info with pure Python 2 & 3
License: MIT
Group: Development/Python3
BuildArch: noarch
Url: https://pypi.python.org/pypi/py-cpuinfo

Source: py-%oname-%version.tar

BuildRequires(pre): rpm-build-python3
# /proc is needed for tests
BuildRequires: /proc

Conflicts: python-module-%oname <= 3.3.0-alt2


%description
Py-cpuinfo gets CPU info with pure Python.
Py-cpuinfo should work without any extra programs or libraries, beyond what your OS provides.
It does not require any compilation(C/C++, assembly, et cetera) to use.

%prep
%setup -n py-%oname-%version

%build
%python3_build_debug

%install
%python3_install

%check
%__python3 setup.py test

%files
%doc README.rst
%_bindir/*
%python3_sitelibdir/*


%changelog
* Fri Feb 07 2020 Andrey Bychkov <mrdrew@altlinux.org> 3.3.0-alt3
- Version in conflict on py2 module added.

* Thu Feb 06 2020 Andrey Bychkov <mrdrew@altlinux.org> 3.3.0-alt2
- Build for python3 disabled.

* Thu Nov 09 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 3.3.0-alt1
- Initial build for ALT.
