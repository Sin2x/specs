%global import_path github.com/rootless-containers/rootlesskit
Name:     rootlesskit
Version:  0.14.6
Release:  alt1

Summary:  Linux-native "fake root" for implementing rootless containers
License:  Apache-2.0
Group:    System/Configuration/Other
Url:      https://github.com/rootless-containers/rootlesskit

Packager: Mikhail Gordeev <obirvalger@altlinux.org>

Source:   %name-%version.tar

BuildRequires(pre): rpm-build-golang
BuildRequires: golang

Requires: shadow-submap

%description
RootlessKit is a Linux-native implementation of "fake root" using
user_namespaces(7).

The purpose of RootlessKit is to run Docker and Kubernetes as an unprivileged
user (known as "Rootless mode"), so as to protect the real root on the host
from potential container-breakout attacks.

%prep
%setup

%build
export BUILDDIR="$PWD/.build"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"

%golang_prepare

cd .build/src/%import_path
%golang_build cmd/rootlesskit cmd/rootlessctl cmd/rootlesskit-docker-proxy

%install
export BUILDDIR="$PWD/.build"
export IGNORE_SOURCES=1

%golang_install

mkdir -p %buildroot%_sysctldir
cat > %buildroot%_sysctldir/80-rootlesskit.conf << EOF
kernel.userns_restrict = 0
EOF

%post
control newgidmap public 2>/dev/null ||:
control newuidmap public 2>/dev/null ||:

%files
%_bindir/*
%_sysctldir/80-rootlesskit.conf
%doc *.md

%changelog
* Tue Feb 01 2022 Mikhail Gordeev <obirvalger@altlinux.org> 0.14.6-alt1
- Initial build for Sisyphus
