Name:     vml
Version:  0.1.1
Release:  alt1

Summary:  Tool for easily and transparently work with qemu virtual machines
License:  MIT
Group:    Emulators
Url:      https://github.com/Obirvalger/vml

Packager: Mikhail Gordeev <obirvalger@altlinux.org>

Source:   %name-%version.tar

ExclusiveArch: x86_64 aarch64

BuildRequires: rust-cargo libssl-devel
BuildRequires: /proc

Requires: rsync socat openssh-clients /usr/bin/kvm cloud-utils

%description
VML is a tool for easily and transparently work with qemu virtual machines.
Virtaul machines presend as directories with vml.toml files in it. VML is able
to initialize images with cloud-init. Virtual machines with ALT, Centos, Debian
and Ubuntu could be created with just one command.

%prep
%setup

%build
export RUSTFLAGS="-g"
cargo build \
    --release \
    %{?_smp_mflags} \
    --offline \
    --target %_arch-unknown-linux-gnu

%install
install -Dm 755 target/%_arch-unknown-linux-gnu/release/%name %buildroot%_bindir/%name
install -Dm 644 files/config.toml %buildroot%_sysconfdir/%name/config.toml
install -Dm 644 files/images.toml %buildroot%_sysconfdir/%name/images.toml

mkdir -p %buildroot%_datadir/zsh/site-functions
%buildroot%_bindir/%name completion zsh > %buildroot%_datadir/zsh/site-functions/_%name
mkdir -p %buildroot%_datadir/bash-completion/completions
%buildroot%_bindir/%name completion bash > %buildroot%_datadir/bash-completion/completions/%name
mkdir -p %buildroot%_datadir/fish/vendor_completions.d
%buildroot%_bindir/%name completion fish > %buildroot%_datadir/fish/vendor_completions.d/%name.fish

%files
%_bindir/%name
%_sysconfdir/%name
%config(noreplace) %attr(0644,root,root) %_sysconfdir/%name/config.toml
%config(noreplace) %attr(0644,root,root) %_sysconfdir/%name/images.toml
%_datadir/zsh/site-functions/_%name
%_datadir/bash-completion/completions/%name
%_datadir/fish/vendor_completions.d/%name.fish
%doc doc *.md

%changelog
* Mon Apr 12 2021 Mikhail Gordeev <obirvalger@altlinux.org> 0.1.1-alt1
- 0.1.1

* Mon Mar 29 2021 Mikhail Gordeev <obirvalger@altlinux.org> 0.1.0-alt1
- Initial build for Sisyphus
