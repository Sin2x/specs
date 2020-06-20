%define  modulename fastavro

Name:    python3-module-%modulename
Version: 0.23.4
Release: alt1

Summary: Fast Avro for Python
License: MIT
Group:   Development/Python3
URL:     https://github.com/fastavro/fastavro

Packager: Grigory Ustinov <grenka@altlinux.org>

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-Cython
BuildRequires: python3-module-numpy
BuildRequires: python3-module-sphinx
BuildRequires: python3-module-sphinx_rtd_theme

Source:  %modulename-%version.tar

%description
Apache Avro is a data serialization system. The current Python avro package is
packed with features but dog slow. fastavro is less feature complete than avro,
however it is much faster.

%prep
%setup -n %modulename-%version

# Remove the already generated C files so we generate them ourselves
find fastavro/ -name "*.c" -print -delete

%build
export FASTAVRO_USE_CYTHON=1
%python3_build

%install
export FASTAVRO_USE_CYTHON=1
%python3_install

%files
%_bindir/fastavro
%python3_sitelibdir/%modulename/
%python3_sitelibdir/*.egg-info
%doc *.md

%changelog
* Sat Jun 20 2020 Grigory Ustinov <grenka@altlinux.org> 0.23.4-alt1
- Initial build for Sisyphus
