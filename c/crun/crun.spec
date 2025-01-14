%global _unpackaged_files_terminate_build 1
%define git_commit d4a45e999c9c81bdeb7d0f67513a40a55419bf30
%define __nprocs 8

Summary: OCI runtime written in C
Name: crun
Version: 1.7
Release: alt1
Group: Development/Other
License: GPLv2+
Url: https://github.com/containers/crun

Source0: %name-%version.tar
# git submodules
Source11: libocispec.tar
Source12: image-spec.tar
Source13: runtime-spec.tar
Source14: yajl.tar

BuildRequires: libcap-devel
BuildRequires: libsystemd-devel
BuildRequires: libseccomp-devel
%ifarch aarch64 ppc64le x86_64
BuildRequires: libcriu-devel >= 3.13
%endif
BuildRequires: gperf
BuildRequires: go-md2man
BuildRequires: python3
BuildRequires: cmake
Provides: oci-runtime = 2

%description
crun is a runtime for running OCI containers

%prep
%setup
tar -xf %SOURCE11 -C libocispec
tar -xf %SOURCE12 -C libocispec/image-spec
tar -xf %SOURCE13 -C libocispec/runtime-spec
tar -xf %SOURCE14 -C libocispec/yajl
echo "%version" > .tarball-version
printf "/* autogenerated.  */\n#ifndef GIT_VERSION\n# define GIT_VERSION \"%s\"\n#endif\n" %git_commit > git-version.h

%build
%autoreconf
%configure \
	--disable-silent-rules \
	--enable-embedded-yajl=yes
%make_build

%install
%makeinstall_std
rm -f %buildroot%_libdir/*.a

%files
%doc COPYING
%_bindir/%name
%_man1dir/*

%changelog
* Tue Nov 08 2022 Andrew A. Vasilyev <andy@altlinux.org> 1.7-alt1
- 1.7

* Wed Sep 07 2022 Andrew A. Vasilyev <andy@altlinux.org> 1.6-alt1
- 1.6

* Wed Jul 20 2022 Andrew A. Vasilyev <andy@altlinux.org> 1.5-alt1
- 1.5

* Wed Apr 27 2022 Andrew A. Vasilyev <andy@altlinux.org> 1.4.5-alt1
- 1.4.5

* Thu Mar 24 2022 Andrew A. Vasilyev <andy@altlinux.org> 1.4.4-alt1
- 1.4.4

* Thu Mar 03 2022 Andrew A. Vasilyev <andy@altlinux.org> 1.4.3-alt1
- 1.4.3

* Wed Jan 26 2022 Andrew A. Vasilyev <andy@altlinux.org> 1.4.2-alt1
- 1.4.2

* Fri Jan 14 2022 Andrew A. Vasilyev <andy@altlinux.org> 1.4.1-alt1
- 1.4.1

* Fri Nov 05 2021 Andrew A. Vasilyev <andy@altlinux.org> 1.3-alt1
- 1.3

* Fri Oct 08 2021 Andrew A. Vasilyev <andy@altlinux.org> 1.2-alt1
- 1.2

* Mon Sep 27 2021 Andrew A. Vasilyev <andy@altlinux.org> 1.1-alt1
- 1.1

* Thu Aug 26 2021 Andrew A. Vasilyev <andy@altlinux.org> 1.0-alt1
- 1.0

* Mon Jul 26 2021 Andrew A. Vasilyev <andy@altlinux.org> 0.21-alt1
- 0.21

* Tue Jun 15 2021 Alexey Shabalin <shaba@altlinux.org> 0.20.1-alt1
- 0.20.1

* Sat Apr 24 2021 Alexey Shabalin <shaba@altlinux.org> 0.19.1-alt1
- 0.19.1

* Sat Feb 27 2021 Alexey Shabalin <shaba@altlinux.org> 0.18-alt1
- 0.18

* Fri Jan 22 2021 Alexey Shabalin <shaba@altlinux.org> 0.17-alt1
- 0.17

* Tue Nov 24 2020 Andrew A. Vasilyev <andy@altlinux.org> 0.16-alt1
- 0.16

* Tue Nov 03 2020 Andrew A. Vasilyev <andy@altlinux.org> 0.15.1-alt1
- 0.15.1

* Wed Sep 23 2020 Andrew A. Vasilyev <andy@altlinux.org> 0.15-alt1
- 0.15

* Tue Sep 08 2020 Andrew A. Vasilyev <andy@altlinux.org> 0.14.1-alt1
- 0.14.1

* Sat Jul 04 2020 Alexey Shabalin <shaba@altlinux.org> 0.14-alt1
- 0.14

* Fri Mar 13 2020 Alexey Shabalin <shaba@altlinux.org> 0.13-alt1
- 0.13

* Wed Dec 11 2019 Alexey Shabalin <shaba@altlinux.org> 0.10.6-alt1
- 0.10.6 (fixes: CVE-2019-18837)

* Wed Nov 06 2019 Alexey Shabalin <shaba@altlinux.org> 0.10.4-alt1
- 0.10.4

* Thu Oct 10 2019 Alexey Shabalin <shaba@altlinux.org> 0.10.2-alt1
- 0.10.2

* Mon Sep 23 2019 Alexey Shabalin <shaba@altlinux.org> 0.9.1-alt1
- 0.9.1

* Fri Sep 13 2019 Alexey Shabalin <shaba@altlinux.org> 0.9-alt1
- Initial build

