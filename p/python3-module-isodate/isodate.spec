%define _unpackaged_files_terminate_build 1
%define oname isodate

Name: python3-module-%oname
Version: 0.5.4
Release: alt2
Summary: An ISO 8601 date/time/duration parser and formater
License: BSD
Group: Development/Python3
Url: http://pypi.python.org/pypi/isodate

Source0: https://pypi.python.org/packages/f4/5b/fe03d46ced80639b7be9285492dc8ce069b841c0cebe5baacdd9b090b164/%{oname}-%{version}.tar.gz
BuildArch: noarch

BuildRequires(pre): rpm-build-python3

%description
This module implements ISO 8601 date, time and duration parsing. The
implementation follows ISO8601:2004 standard, and implements only
date/time representations mentioned in the standard. If something is not
mentioned there, then it is treated as non existent, and not as an
allowed option.

For instance, ISO8601:2004 never mentions 2 digit years. So, it is not
intended by this module to support 2 digit years. (while it may still be
valid as ISO date, because it is not explicitly forbidden.) Another
example is, when no time zone information is given for a time, then it
should be interpreted as local time, and not UTC.

As this module maps ISO 8601 dates/times to standard Python data types,
like date, time, datetime and timedelta, it is not possible to convert
all possible ISO 8601 dates/times. For instance, dates before 0001-01-01
are not allowed by the Python date and datetime classes. Additionally
fractional seconds are limited to microseconds. That means if the parser
finds for instance nanoseconds it will round it to microseconds.

%package tests
Summary: Tests for isodate
Group: Development/Python3
Requires: %name = %version-%release

%description tests
This module implements ISO 8601 date, time and duration parsing. The
implementation follows ISO8601:2004 standard, and implements only
date/time representations mentioned in the standard. If something is not
mentioned there, then it is treated as non existent, and not as an
allowed option.

This package contains tests for isodate.

%prep
%setup -n %{oname}-%{version}

%build
%python3_build

%install
%python3_install

%files
%doc *.txt *.rst
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests

%files tests
%python3_sitelibdir/*/tests

%changelog
* Wed Jul 28 2021 Grigory Ustinov <grenka@altlinux.org> 0.5.4-alt2
- Drop python2 support.

* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 0.5.4-alt1
- automated PyPI update

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.5.0-alt1.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.5.0-alt1.1
- NMU: Use buildreq for BR.

* Fri Jul 11 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5.0-alt1
- Version 0.5.0

* Mon Apr 01 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.9-alt1
- Version 0.4.9

* Fri Mar 22 2013 Aleksey Avdeev <solo@altlinux.ru> 0.4.8-alt1.1
- Rebuild with Python-3.3

* Tue May 08 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.8-alt1
- Initial build for Sisyphus
