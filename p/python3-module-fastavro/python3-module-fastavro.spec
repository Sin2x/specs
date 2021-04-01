%define  modulename fastavro

Name:    python3-module-%modulename
Version: 1.3.5
Release: alt1

Summary: Fast Avro for Python

License: MIT
Group:   Development/Python3
URL:     https://github.com/fastavro/fastavro

Packager: Grigory Ustinov <grenka@altlinux.org>

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-Cython

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
* Thu Apr 01 2021 Grigory Ustinov <grenka@altlinux.org> 1.3.5-alt1
- Automatically updated to 1.3.5.

* Mon Mar 22 2021 Grigory Ustinov <grenka@altlinux.org> 1.3.4-alt1
- Automatically updated to 1.3.4.

* Wed Mar 17 2021 Grigory Ustinov <grenka@altlinux.org> 1.3.3-alt1
- Automatically updated to 1.3.3.

* Mon Feb 22 2021 Grigory Ustinov <grenka@altlinux.org> 1.3.2-alt1
- Automatically updated to 1.3.2.

* Mon Jan 25 2021 Grigory Ustinov <grenka@altlinux.org> 1.3.0-alt1
- Automatically updated to 1.3.0.

* Thu Jan 21 2021 Grigory Ustinov <grenka@altlinux.org> 1.2.4-alt1
- Automatically updated to 1.2.4.

* Thu Jan 14 2021 Grigory Ustinov <grenka@altlinux.org> 1.2.3-alt1
- Automatically updated to 1.2.3.

* Thu Dec 24 2020 Grigory Ustinov <grenka@altlinux.org> 1.2.2-alt1
- Automatically updated to 1.2.2.

* Thu Dec 03 2020 Grigory Ustinov <grenka@altlinux.org> 1.2.1-alt1
- Automatically updated to 1.2.1.

* Tue Nov 24 2020 Grigory Ustinov <grenka@altlinux.org> 1.2.0-alt1
- Automatically updated to 1.2.0.

* Wed Nov 18 2020 Grigory Ustinov <grenka@altlinux.org> 1.1.1-alt1
- Automatically updated to 1.1.1.

* Tue Nov 10 2020 Grigory Ustinov <grenka@altlinux.org> 1.1.0-alt1
- Automatically updated to 1.1.0.

* Wed Sep 16 2020 Grigory Ustinov <grenka@altlinux.org> 1.0.0-alt1
- Automatically updated to 1.0.0.

* Sat Jun 20 2020 Grigory Ustinov <grenka@altlinux.org> 0.23.4-alt1
- Initial build for Sisyphus.
