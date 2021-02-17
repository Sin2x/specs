# Updated using gear-remotes-uscan

%global import_path github.com/restic/restic
Name:     restic
Version:  0.12.0
Release:  alt1

Summary:  Fast, secure, efficient backup program
License:  BSD-2-Clause
Group:    Archiving/Backup
Vcs:      https://github.com/restic/restic
Url:      https://restic.net/

Source:   %name-%version.tar

BuildRequires(pre): rpm-build-golang
BuildRequires: golang

%description
restic is a backup program that is fast, efficient and secure.

%prep
%setup

%build
export BUILDDIR="$PWD/.build"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"

%golang_prepare

cd .build/src/%import_path
%golang_build cmd/restic

%install
export BUILDDIR="$PWD/.build"
export IGNORE_SOURCES=1

%golang_install

for f in doc/man/*.?; do
    install -Dp "$f" "%buildroot/%_man1dir/$(basename "$f")"
done

%check
PATH=%buildroot%_bindir:$PATH
restic version
export RESTIC_PASSWORD=testic
restic --repo ../test init
restic --repo ../test backup .
restic --repo ../test restore latest -t ../x
cd ../x
restic --repo ../test backup .
S=($(restic --repo ../test snapshots | grep localhost | cut -d' ' -f1))
restic --repo ../test diff ${S[*]}
restic --repo ../test check --read-data
cd ..
diff -qr %name-%version x

%files
%_bindir/*
%_man1dir/*.1*
%doc *.md

%changelog
* Wed Feb 17 2021 Mikhail Gordeev <obirvalger@altlinux.org> 0.12.0-alt1
- Update to v0.12.0.

* Sun Nov 08 2020 Mikhail Gordeev <obirvalger@altlinux.org> 0.11.0-alt1
- Update to v0.11.0.

* Sun Mar 15 2020 Vitaly Chikunov <vt@altlinux.org> 0.9.6-alt1
- Update to v0.9.6.
- Add some tests into %%check.

* Fri Mar 15 2019 Vitaly Chikunov <vt@altlinux.org> 0.9.4-alt1
- Initial build for Sisyphus
