%define _unpackaged_files_terminate_build 1
%define oname demjson

%def_disable check

Name: python3-module-%oname
Version: 2.2.4
Release: alt2
Summary: encoder, decoder, and lint/validator for JSON compliant with RFC 7159
License: LGPLv3.0
Group: Development/Python3
Url: https://pypi.python.org/pypi/demjson/

# https://github.com/dmeranda/demjson.git
Source0: https://pypi.python.org/packages/96/67/6db789e2533158963d4af689f961b644ddd9200615b8ce92d6cad695c65a/%{oname}-%{version}.tar.gz
BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python-tools-2to3 python3-module-pytest
%py3_provides %oname

Conflicts: python-module-%oname
Obsoletes: python-module-%oname

%description
The "demjson" module, and the included "jsonlint" script, provide
methods for encoding and decoding JSON formatted data, as well as
checking JSON data for errors and/or portability issues. The jsonlint
command/script can be used from the command line without needing any
programming.

Although the standard Python library now includes basic JSON support
(which it did not when demjson was first written), this module provides
a much more comprehensive implementation with many features not found
elsewhere. It is especially useful for error checking or for parsing
JavaScript data which may not strictly be valid JSON data.

%prep
%setup -n %{oname}-%{version}

find . -type f -name '*.py' -exec 2to3 -w -n '{}' +

%build
%python3_build

%install
%python3_install

%check
export PYTHONPATH=$PWD
py.test-%_python3_version

%files
%doc *.txt *.md docs/*
%_bindir/*
%python3_sitelibdir/*

%changelog
* Fri Jul 23 2021 Grigory Ustinov <grenka@altlinux.org> 2.2.4-alt2
- Drop python2 support.

* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 2.2.4-alt1
- automated PyPI update

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 2.2.2-alt1.git20140625.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 2.2.2-alt1.git20140625.1
- NMU: Use buildreq for BR.

* Fri Oct 24 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.2.2-alt1.git20140625
- Initial build for Sisyphus
