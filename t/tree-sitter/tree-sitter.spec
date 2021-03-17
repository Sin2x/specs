Name: tree-sitter
Version: 0.19.3
Release: alt2

Summary: Parser generator tool and an incremental parsing library

Group: Development/Tools
License: MIT
Url: https://github.com/tree-sitter/tree-sitter

Source: %name-%version.tar

BuildRequires: gcc make
BuildRequires: rust-cargo
BuildRequires: /proc

%description
Tree-sitter is a parser generator tool and an incremental parsing library.
It can build a concrete syntax tree for a source file and efficiently update
the syntax tree as the source file is edited.

%package -n lib%name
Summary: Tree-sitter library
Group: Development/Other

%description -n lib%name
Tree-sitter library

%package -n lib%name-devel
Summary: Devel package for tree-sitter library
Group: Development/Other
Requires: lib%name = %version-%release

%description -n lib%name-devel
Development files for tree-sitter library

%package -n %name-cli
Summary: Tree-sitter CLI tool
Group: Development/Other

%description -n %name-cli
Tree-sitter CLI tool

%prep
%setup

mkdir -p .cargo
cat >> .cargo/config <<EOF
[source.crates-io]
replace-with = "vendored-sources"

[source.vendored-sources]
directory = "cli/vendor"
EOF

%build
%make_build

cargo build --offline --release

%install
export PREFIX=%_prefix
export DESTDIR=%buildroot
export INCLUDEDIR=%_includedir
export LIBDIR=%_libdir
export PCLIBDIR=%_pkgconfigdir
make install

mkdir -p %buildroot%_bindir
install -m 0755 target/release/%name %buildroot%_bindir

%files -n lib%name
%_libdir/*.so.*
%exclude %_libdir/*.a

%files -n lib%name-devel
%_libdir/*.so
%_includedir/*
%_pkgconfigdir/%name.pc

%files -n %name-cli
%_bindir/%name

%changelog
* Wed Mar 17 2021 Vladimir Didenko <cow@altlinux.ru> 0.19.3-alt2
- build CLI tool

* Tue Mar 16 2021 Vladimir Didenko <cow@altlinux.ru> 0.19.3-alt1
- new version

* Tue Nov 24 2020 Vladimir Didenko <cow@altlinux.ru> 0.17.3-alt1
- initial build for Sisyphus

