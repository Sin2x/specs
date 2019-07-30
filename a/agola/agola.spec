%global import_path github.com/agola-io/agola
%global commit ea3e0d1d7c41a72e8eb5820d3a6048edf0b6ae7a

%global __find_debuginfo_files %nil
%global _unpackaged_files_terminate_build 1

%define _runtimedir /run

%set_verify_elf_method unresolved=no
%add_debuginfo_skiplist %go_root %_bindir
%brp_strip_none %_bindir/*


Name:		agola
Version:	0.1.1
Release:	alt1
Summary:	CI/CD redefined

Group:		Development/Other
License:	ASL 2.0
URL:		https://agola.io

Source: %name-%version.tar
Patch: %name-%version.patch


ExclusiveArch:  %go_arches
BuildRequires(pre): rpm-build-golang
BuildRequires: go-bindata

%description
Grafana is an open source, feature rich metrics dashboard and graph editor
for Graphite, Elasticsearch, OpenTSDB, Prometheus and InfluxDB.

%prep
%setup -q
%patch -p1

%build

export BUILDDIR="$PWD/.gopath"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"

%golang_prepare

cd .gopath/src/%import_path

export VERSION=%version
export COMMIT=%commit
export BRANCH=altlinux
export GOFLAGS="-mod=vendor"

%make WEBBUNDLE=1 WEBDISTPATH=dist

%install
export BUILDDIR="$PWD/.gopath"
#export GOPATH="%go_path"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path:$PWD"

mkdir -p %buildroot%_bindir
pushd .gopath/src/%import_path

install -p -m 755 bin/agola %buildroot%_bindir/agola
install -p -m 755 bin/agola-toolbox %buildroot%_bindir/agola-toolbox

%files
%doc LICENSE README.md
%_bindir/*

%changelog
* Sun Jul 21 2019 Alexey Shabalin <shaba@altlinux.org> 0.1.1-alt1
- First build for ALTLinux.
