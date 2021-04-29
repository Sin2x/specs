%define mname update-kernel

Name: alterator-update-kernel
Version: 1.4
Release: alt1

Source:%name-%version.tar

Summary: alterator module for update kernel
License: GPL
Group: System/Configuration/Other

Requires: alterator-l10n >= 2.9.82-alt1
BuildPreReq: alterator >= 4.10-alt1 alterator-lookout

%ifarch %e2k
BuildRequires: guile20-devel libguile20-devel
%else
BuildRequires: guile22-devel
%endif

%description
An alterator module with graphical and web interface that implements
the functionality of the update-kernel utility for updating / installing
and removing kernels, installing and removing kernel modules.

%prep
%setup -q

%build
%make_build

%install
export GUILE_LOAD_PATH=/usr/share/alterator/lookout
%makeinstall

%files
%_datadir/alterator/applications/*

%dir %_datadir/alterator/ui/%mname
%_datadir/alterator/ui/%mname/*.scm
%_datadir/alterator/ui/%mname/*.html

%dir %_datadir/alterator/ui/%mname/update
%_datadir/alterator/ui/%mname/update/*.scm
%_datadir/alterator/ui/%mname/update/*.html

%dir %_alterator_libdir/ui/%mname
%_alterator_libdir/ui/%mname/*.go

%dir %_alterator_libdir/ui/%mname/update
%_alterator_libdir/ui/%mname/update/*.go

%_alterator_backend3dir/%mname
%_datadir/dbus-1/interfaces/*.xml

%changelog
* Thu Apr 29 2021 Ivan Savin <svn17@altlinux.org> 1.4-alt1
- Refactoring.
- Update xml file after refactoring.
- Fix set_default_kernel.
- Moving a message from the backend.

* Thu Apr 22 2021 Ivan Savin <svn17@altlinux.org> 1.3-alt3
- Add introspection file for alterator-dbus.

* Fri Apr 02 2021 Ivan Savin <svn17@altlinux.org> 1.3-alt2
- Fix spec.

* Fri Mar 05 2021 Ivan Savin <svn17@altlinux.org> 1.3-alt1
- Fix set_default_kernel for rpi4.

* Wed Feb 24 2021 Ivan Savin <svn17@altlinux.org> 1.2-alt2
- Correcting the text of the error message.

* Fri Feb 19 2021 Ivan Savin <svn17@altlinux.org> 1.2-alt1
- Replace apt_update, update_kernel and install_modules to action write.
- Improves the available kernel version in GUI.
- Improves the automatic selection of modules
  to install when installing a different kernel flavour.
- Minor GUI fix.

* Mon Feb 15 2021 Ivan Savin <svn17@altlinux.org> 1.1-alt1
- Fixes for translation.

* Tue Feb 09 2021 Ivan Savin <svn17@altlinux.org> 1.0-alt2
- Add button locking between transactions.

* Fri Feb 05 2021 Ivan Savin <svn17@altlinux.org> 1.0-alt1
- Add an ability to remove old kernels.
- Add an ability to remove kernel modules.
- Add an ability to install kernels of different types (flavours).
- Improves the graphical interface.

* Wed Sep 09 2020 Ivan Savin <svn17@altlinux.org> 0.3-alt1
- Added an ability to install modules.

* Sat Aug 22 2020 Ivan Savin <svn17@altlinux.org> 0.2-alt1
- Added translation.

* Thu Aug 13 2020 Ivan Savin <svn17@altlinux.org> 0.1-alt1
- Initial commit.


