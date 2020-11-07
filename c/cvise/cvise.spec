Name: cvise
Version: 1.8.0
Release: alt2

Summary: Super-parallel Python port of the C-Reduce

License: BSD-3-Clause
Group: Development/C++
Url: https://github.com/marxin/cvise

Packager: Vitaly Lipatov <lav@altlinux.ru>

# Source-url: https://github.com/marxin/cvise/archive/v%version.tar.gz
Source: %name-%version.tar

BuildRequires: astyle
BuildRequires: clang-devel >= 10
# FIXME
BuildRequires: clang-devel-static >= 10
BuildRequires: cmake
BuildRequires: flex
BuildRequires: gcc-c++
BuildRequires: indent
BuildRequires: llvm-devel >= 10
# FIXME
BuildRequires: llvm-devel-static >= 10
BuildRequires: libncurses-devel
#BuildRequires: ninja

BuildRequires: python3-module-pebble
BuildRequires: python3-module-psutil
BuildRequires: python3-module-pytest
BuildRequires: unifdef
BuildRequires: pytest3

BuildRequires(pre): rpm-build-python3
BuildRequires(pre): rpm-build-intro >= 2.1.5

# use no more than system_memory/3000 build procs (see https://bugzilla.altlinux.org/show_bug.cgi?id=35112)
%_tune_parallel_build_by_procsize 3000


%add_python3_lib_path %_datadir/cvise

Requires: astyle
Requires: clang
Requires: indent
Requires: llvm
Requires: unifdef

AutoProv: no

%description
C-Vise is a super-parallel Python port of the C-Reduce. The port is fully
compatible to the C-Reduce and uses the same efficient
LLVM-based C/C++ reduction tool named clang_delta.

C-Vise is a tool that takes a large C, C++ or OpenCL program that
has a property of interest (such as triggering a compiler bug) and
automatically produces a much smaller C/C++ or OpenCL program that
has the same property. It is intended for use by people who discover
and report bugs in compilers and other tools that process C/C++ or OpenCL code.

%prep
%setup
# TODO: https://bugzilla.altlinux.org/show_bug.cgi?id=38660
%__subst '14ilist(APPEND CMAKE_PREFIX_PATH "/usr/share/cmake/Modules")' CMakeLists.txt

%build
%cmake -DCMAKE_INSTALL_LIBEXECDIR=%_libexecdir
%cmake_build

%check
cd BUILD
pytest3 -v .

%install
%cmakeinstall_std
rm -rfv %buildroot%_datadir/cvise/tests/


%files
%doc COPYING
%_bindir/cvise
%_bindir/cvise-delta
%_datadir/cvise/
%dir %_libexecdir/cvise/
%_libexecdir/cvise/clex
%_libexecdir/cvise/clang_delta
%_libexecdir/cvise/clex
%_libexecdir/cvise/strlex
%_libexecdir/cvise/topformflat

%changelog
* Sat Nov 07 2020 Vitaly Lipatov <lav@altlinux.ru> 1.8.0-alt2
- disable python modules provide, drop tests files from the package

* Wed Oct 21 2020 Vitaly Lipatov <lav@altlinux.ru> 1.8.0-alt1
- new version 1.8.0 (with rpmrb script)

* Tue Jul 07 2020 Vitaly Lipatov <lav@altlinux.ru> 1.5.0-alt1
- new version 1.5.0 (with rpmrb script)

* Tue Jun 30 2020 Vitaly Lipatov <lav@altlinux.ru> 1.4.0-alt1
- initial build for ALT Sisyphus
