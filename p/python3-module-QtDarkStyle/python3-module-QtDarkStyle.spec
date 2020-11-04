Name: python3-module-QtDarkStyle
Version: 2.8.1
Release: alt1

License: MIT
Group: Development/Python
Url: https://github.com/ColinDuquesnoy/QDarkStyleSheet

Summary: The most complete dark stylesheet for Python and Qt applications

# Source-url: https://github.com/ColinDuquesnoy/QDarkStyleSheet/archive/v%version.tar.gz
Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-python3 rpm-build-intro

%description
The most complete dark stylesheet for Qt application (Qt4, Qt5, PySide, PySide2, PyQt4, PyQt5, QtPy, PyQtGraph, Qt.Py).

%prep
%setup

%build
%python3_build

%install
%python3_install

%files
%_bindir/qdarkstyle
%python3_sitelibdir/*

%changelog
* Wed Nov 04 2020 Vitaly Lipatov <lav@altlinux.ru> 2.8.1-alt1
- new version 2.8.1 (with rpmrb script)

* Sun Feb 02 2020 Vitaly Lipatov <lav@altlinux.ru> 2.8-alt1
- initial build for ALT Sisyphus
