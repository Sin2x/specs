%global import_path github.com/fleetdm/fleet
Name:     fleet
Version:  3.4.0
Release:  alt1

Summary:  The premier osquery fleet manager.
License:  MIT
Group:    Other
Url:      https://github.com/fleetdm/fleet

Packager: Mikhail Gordeev <obirvalger@altlinux.org>

Source:   %name-%version.tar

BuildRequires(pre): rpm-build-golang
BuildRequires: golang

%description
%summary

%prep
%setup

%build
export BUILDDIR="$PWD/.build"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"

%golang_prepare

cd .build/src/%import_path
export LDFLAGS="$LDFLAGS -X github.com/kolide/kit/version.version=%version"
%golang_build cmd/fleet cmd/fleetctl

%install
export BUILDDIR="$PWD/.build"
export IGNORE_SOURCES=1

%golang_install

%files
%_bindir/*
%doc *.md

%changelog
* Tue Nov 24 2020 Mikhail Gordeev <obirvalger@altlinux.org> 3.4.0-alt1
- Initial build for Sisyphus
