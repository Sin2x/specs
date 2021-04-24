# SPDX-License-Identifier: GPL-2.0-only
%define _unpackaged_files_terminate_build 1

Name: ispc
Version: 1.15.0
Release: alt2
Summary: Intel Implicit SPMD Program Compiler
License: BSD-3-Clause
Group: Development/C

%define docdir %_docdir/%name-%version

Source: %name-%version.tar

# Story: https://pharr.org/matt/blog/2018/04/30/ispc-all.html
Vcs: https://github.com/ispc/ispc.git
Url: https://ispc.github.io/

BuildRequires(pre): rpm-macros-cmake
BuildRequires: banner
BuildRequires: cmake
BuildRequires: clang-devel >= 11.0.0
BuildRequires:  llvm-devel >= 11.0.0
BuildRequires:  llvm-devel-static >= 11.0.0
BuildRequires: libstdc++-devel
BuildRequires: libstdc++-devel-static
BuildRequires: flex
BuildRequires: python3-devel
BuildRequires: python3-tools
BuildRequires: libncurses-devel
BuildRequires: zlib-devel
BuildRequires: /proc

# armh: clang-11: error: unsupported option '--with-fpu=hardfp'
ExclusiveArch: %ix86 x86_64 aarch64

%description
ispc is a compiler for a variant of the C programming language, with
extensions for "single program, multiple data" (SPMD) programming. Under the
SPMD model, the programmer writes a program that generally appears to be a
regular serial program, though the execution model is actually that a number
of program instances execute in parallel on the hardware.

ispc compiles a C-based SPMD programming language to run on the SIMD units of
CPUs and the Intel Xeon Phi architecture; it frequently provides a 3x or more
speedup on CPUs with 4-wide vector SSE units and 5x-6x on CPUs with 8-wide AVX
vector units, without any of the difficulty of writing intrinsics code.
Parallelization across multiple cores is also supported by ispc, making it
possible to write programs that achieve performance improvement that scales by
both number of cores and vector unit size.

%package checkinstall
Summary: checkinstall for %name
Group: Development/C
Requires(pre): gcc-c++
Requires(pre): %name = %EVR

%description checkinstall
This package will try to build all %name examples.

%prep
%setup

%build
# -DISPC_INCLUDE_TESTS=OFF = we don't have FileCheck
# -DISPC_NO_DUMPS=ON       =
#	CMake Warning at cmake/LLVMConfig.cmake:105 (message):
#	  LLVM was built without assertions enabled (-DLLVM_ENABLE_ASSERTIONS=OFF).
#	  This disables dumps, which are required for ISPC to be fully functional.
# -DWASM_ENABLED=ON requires emcc.
# -DGENX_ENABLED=ON requires level_zero.

%cmake \
	-DCMAKE_BUILD_TYPE=RelWithDebInfo \
	-DCMAKE_INSTALL_PREFIX=%prefix \
	-DCMAKE_EXE_LINKER_FLAGS="%optflags -fPIE" \
	-DLLVM_DIR=$(llvm-config --cmakedir) \
	-DISPC_NO_DUMPS=ON \
	-DISPC_INCLUDE_TESTS=OFF \
	-DISPC_INCLUDE_EXAMPLES=OFF \

%ifarch %ix86
  # Workaround https://github.com/ispc/ispc/issues/2066
  # /usr/include/gnu/stubs.h:10:11: fatal error: 'gnu/stubs-64.h' file not found
  sed -i s/-m64/-m32/g ./BUILD/CMakeFiles/ispc.dir/build.make
  # There is similar problem on armh with `gnu/stubs-soft.h'.
%endif

%cmake_build VERBOSE=1

%pre checkinstall
set -ex
mkdir /tmp/BUILD
cd /tmp/BUILD
cmake %docdir/examples
# Fix: aarch64-alt-linux-g++: error: unrecognized command-line option '-m64'
[ $(arch) = aarch64 ] && find -name flags.make | xargs sed -i 's/-m64//'
make -j$(nproc)
simple/simple

%install
%cmake_install DESTDIR=%buildroot install

mkdir -p %buildroot%docdir
cp -a LICENSE.txt README.md SECURITY.md contrib/ docs/*.rst examples/ \
   docs/ReleaseNotes.txt %buildroot%docdir

%files
%_bindir/%name
%_bindir/check_isa
%docdir

%files checkinstall

%check
banner check
PATH=BUILD/bin:$PATH
# Increase timeout from 10 to 100 or beekeeper will sometimes fail.
sed -i /run_command/s/10/100/ run_tests.py
# Tests are from .travis.yml
check_isa
ispc --support-matrix
%ifarch x86_64
  ./run_tests.py --jobs=$(nproc) --non-interactive
  ./run_tests.py --jobs=$(nproc) --non-interactive --arch=x86_64
%endif
%ifarch %ix86
  ./run_tests.py --jobs=$(nproc) --non-interactive --arch=x86
%endif
%ifarch aarch64
  ./run_tests.py --jobs=$(nproc) --non-interactive --arch=aarch64 --target=neon-i32x8
%endif
%ifarch armh
  ./run_tests.py --jobs=$(nproc) --non-interactive --arch=arm --target=neon-i32x8
%endif

%changelog
* Fri Apr 23 2021 Vitaly Chikunov <vt@altlinux.org> 1.15.0-alt2
- Use latest Clang/LLVM (11.0).
- Enable x86 and aarch64.

* Mon Dec 21 2020 Vitaly Chikunov <vt@altlinux.org> 1.15.0-alt1
- Update to v1.15.0 (2020-12-18).

* Sun Aug 30 2020 Vitaly Chikunov <vt@altlinux.org> 1.14.1-alt1
- Update to v1.14.1 (2020-08-28).

* Fri Jul 31 2020 Vitaly Chikunov <vt@altlinux.org> 1.14.0-alt1
- Update to v1.14.0 (2020-07-30).

* Wed May 06 2020 Vitaly Chikunov <vt@altlinux.org> 1.13.0-alt4
- spec: Add test to compile all examples in checkinstall.

* Wed May 06 2020 Vitaly Chikunov <vt@altlinux.org> 1.13.0-alt3
- Add examples and documentation to the package.

* Fri May 01 2020 Vitaly Chikunov <vt@altlinux.org> 1.13.0-alt2
- spec: Improve %%check section.

* Sat Apr 25 2020 Vitaly Chikunov <vt@altlinux.org> 1.13.0-alt1
- Update to v1.13.0.
- Use Clang/LLVM 10.
- spec: Add tests into %%check section.

* Sat Mar 28 2020 Vitaly Chikunov <vt@altlinux.org> 1.12.0-alt2
- Clean up spec to fix compiling.

* Sat Mar 07 2020 Vitaly Chikunov <vt@altlinux.org> 1.12.0-alt1
- Initial import of v1.12.0.
