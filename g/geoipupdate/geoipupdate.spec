%define _unpackaged_files_terminate_build 1

Name: geoipupdate
Version: 4.7.1
Release: alt1

Summary: GeoIP update client code
Group: Networking/Other
License: Apache-2.0
URL: https://github.com/maxmind/geoipupdate

Source0: %name-%version.tar
Source1: %name-%version-vendor.tar

BuildRequires(pre): rpm-build-golang rpm-macros-golang
BuildRequires: pandoc

%description
The GeoIP Update program performs automatic updates of GeoIP2 and
GeoIP Legacy binary databases. CSV databases are not supported.

%prep
%setup
%setup -a 1

%build

export BUILDDIR="$PWD/.build"
export IMPORT_PATH="github.com/gofrs"
export GOPATH="%go_path"
export GOFLAGS="-mod=vendor"

%golang_prepare

%golang_build cmd/%name
rm -rf $BUILDDIR/src

%install
export BUILDDIR="$PWD/.build"
export GOPATH="%go_path"

%golang_install

%files
%_bindir/%name

%changelog
* Thu Apr 29 2021 Egor Ignatov <egori@altlinux.org> 4.7.1-alt1
- Update to version 4.7.1

* Fri Feb 12 2021 Egor Ignatov <egori@altlinux.org> 4.6.0-alt1
- Update to version 4.6.0

* Fri Nov 03 2017 Yuri N. Sedunov <aris@altlinux.org> 2.5.0-alt1
- 2.5.0

* Mon May 29 2017 Yuri N. Sedunov <aris@altlinux.org> 2.4.0-alt1
- 2.4.0

* Sat Jan 07 2017 Yuri N. Sedunov <aris@altlinux.org> 2.3.1-alt1
- 2.3.1

* Tue Jan 26 2016 Yuri N. Sedunov <aris@altlinux.org> 2.2.2-alt1
- 2.2.2

* Wed Apr 08 2015 Yuri N. Sedunov <aris@altlinux.org> 2.2.1-alt1
- first build for Sisyphus

