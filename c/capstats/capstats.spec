Name: capstats
Version: 0.26
Release: alt1

Summary: A command-line tool collecting packet statistics

License: %bsd
Url: https://github.com/zeek/capstats
Group: Networking/Other

Packager: Andriy Stepanov <stanv@altlinux.ru>

# Source-url: https://github.com/zeek/capstats/archive/v%version.tar.gz
Source: %name-%version.tar

BuildRequires: cmake gcc-c++
BuildRequires: libpcap-devel
BuildRequires(pre): rpm-build-licenses
BuildRequires: zeek-cmake

%description
capstats is a small tool to collect statistics on the current load of a
network interface, using either libpcap or the native interface for Endace.
It reports statistics per time interval and/or for the tool total run-time.

%prep
%setup
rm -rf cmake/
ln -s %_datadir/zeek-cmake/ cmake

%build
%cmake
%cmake_build

%install
%cmakeinstall_std

%files
%doc CHANGES COPYING README
%_bindir/%name

%changelog
* Sun Jun 09 2019 Vitaly Lipatov <lav@altlinux.ru> 0.26-alt1
- rewrite spec, use cmake directly
- use external cmake scripts used in Zeek

* Fri Dec 26 2014 Andriy Stepanov <stanv@altlinux.ru> 0.21-alt1
- Build for ALTLinux

