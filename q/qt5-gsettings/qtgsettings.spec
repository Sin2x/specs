Name: qt5-gsettings
Version: 1.3.0
Release: alt1

Summary: Qt-style API to wrap GSettings
License: LGPL
Group: System/Libraries
Url: https://github.com/lirios/qtgsettings

Source: %name-%version-%release.tar

BuildRequires: gcc-c++
BuildRequires: cmake-modules-liri
BuildRequires: pkgconfig(Qt5Core)
BuildRequires: pkgconfig(Qt5Qml)
BuildRequires: pkgconfig(gio-2.0)

%package -n libqt5-gsettings
Summary: Qt-style API to wrap GSettings
Group: System/Libraries

%package devel
Summary: Qt-style API for AccountsService DBus service
Group: Development/C++

%description
%summary

%description -n libqt5-gsettings
%summary

%description devel
%summary
this package contains development part of %name

%prep
%setup

%build
%cmake
%cmake_build

%install
%cmakeinstall_std

%files -n libqt5-gsettings
%_libdir/libQt5GSettings.so.*
%_libdir/qt5/qml/QtGSettings

%files devel
%_includedir/Qt5GSettings
%_libdir/libQt5GSettings.so
%_libdir/cmake/Qt5GSettings
%_pkgconfigdir/Qt5GSettings.pc

%changelog
* Mon Oct 07 2019 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.3.0-alt1
- initial
