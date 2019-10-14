%define _unpackaged_files_terminate_build 1

Name: papirus-folders
Version: 1.4.0
Release: alt1
Summary: Allows to change the color of folders
License: MIT
Group: Other
Url: https://github.com/PapirusDevelopmentTeam/papirus-folders
Source: %name-%version.tar
Packager: Alexander Makeenkov <amakeenk@altlinux.org>

BuildArch: noarch
Requires: bash >= 4.0

%description
Papirus-folders is a bash script that allows changing the color
of folders in Papirus icon theme and its forks (which based on
version 20171007 and newer).

%prep
%setup

%install
%makeinstall_std

%files
%_bindir/%name
%_datadir/bash-completion/completions/%name
%_datadir/zsh/vendor-completions/_%name
%doc LICENSE README.md

%changelog
* Sun Oct 13 2019 Alexander Makeenkov <amakeenk@altlinux.org> 1.4.0-alt1
- Initial build for ALT
