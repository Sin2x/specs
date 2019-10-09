%def_with docs

Name: rapidjson
Version: 1.1.0
Release: alt1.1

Summary: Fast JSON parser and generator for C++
License: MIT
Group: Development/C++

Url: http://miloyip.github.io/%name
# URL: https://github.com/miloyip/%name
Source: %name-%version.tar
# Downstream-patch for gtest.
Patch: rapidjson-1.1.0-do_not_include_gtest_src_dir.patch
Packager: Anton Midyukov <antohami@altlinux.org>

BuildArch: noarch

BuildRequires(pre): rpm-macros-cmake
BuildRequires(pre): rpm-macros-valgrind
BuildRequires: cmake gcc-c++
BuildRequires: libgtest-devel
%{?_enable_valgrind:BuildRequires: valgrind}
%{?_with_docs:BuildRequires: doxygen python-module-pydot}

Provides: %name-devel == %version-%release

%description
RapidJSON is a fast JSON parser and generator for C++.  It was
inspired by RapidXml.

RapidJSON is small but complete.  It supports both SAX and DOM style
API. The SAX parser is only a half thousand lines of code.

RapidJSON is fast.  Its performance can be comparable to strlen().
It also optionally supports SSE2/SSE4.1 for acceleration.

RapidJSON is self-contained.  It does not depend on external
libraries such as BOOST.  It even does not depend on STL.

RapidJSON is memory friendly.  Each JSON value occupies exactly
16/20 bytes for most 32/64-bit machines (excluding text string). By
default it uses a fast memory allocator, and the parser allocates
memory compactly during parsing.

RapidJSON is Unicode friendly.  It supports UTF-8, UTF-16, UTF-32
(LE & BE), and their detection, validation and transcoding
internally. For example, you can read a UTF-8 file and let RapidJSON
transcode the JSON strings into UTF-16 in the DOM. It also supports
surrogates and "\u0000" (null character).

JSON(JavaScript Object Notation) is a light-weight data exchange
format. RapidJSON should be in fully compliance with RFC4627/ECMA-404.

%package doc
Summary: Documentation-files for %name
Group: Documentation
BuildArch: noarch

%description doc
This package contains the documentation-files for %name.

%prep
%setup
%patch -p1 -b .gtest

# Fix 'W: wrong-file-end-of-line-encoding'.
find example -type f -name '*.c*' -print0 |
	xargs -r0 subst -p 's!\r$!!g' license.txt

# Create an uncluttered backup of examples for inclusion in %%doc.
cp -a example examples

# Disable -Werror.
find . -type f -name 'CMakeLists.txt' -print0 |
	xargs -r0 sed -i -e's![ \t]*-march=native!!g' -e's![ \t]*-Werror!!g'

%build
%cmake \
    -DDOC_INSTALL_DIR=%_docdir/%name-%version \
    -DGTESTSRC_FOUND=TRUE \
    -DGTEST_SOURCE_DIR=.
%cmake_build

%install
%cmakeinstall_std

# Move pkgconfig and CMake-stuff to generic datadir.
mv -f %buildroot%_libdir/* %buildroot%_datadir

# Copy the documentation-files to final location.
cp -at %buildroot%_docdir/%name-%version -- \
	license.txt CHANGELOG.md readme*.md examples

# Find and purge build-sys files.
find %buildroot -type f -name 'CMake*.txt' -print0 |
	xargs -r0 rm -fv --

%files
%doc %dir %_docdir/%name-%version
%doc %_docdir/%name-%version/license.txt
%doc %_docdir/%name-%version/CHANGELOG.md
%doc %_docdir/%name-%version/readme*.md
%_datadir/cmake
%_datadir/pkgconfig/*
%_includedir/%name

%files doc
%doc %dir %_docdir/%name-%version
%doc %_docdir/%name-%version/examples
%if_with docs
%doc %_docdir/%name-%version/html
%endif # docs

%changelog
* Wed Oct 09 2019 Michael Shigorin <mike@altlinux.org> 1.1.0-alt1.1
- Move to rpm-macros-valgrind.
- Spec cleanup.

* Wed Nov 15 2017 Anton Midyukov <antohami@altlinux.org> 1.1.0-alt1
- Initial build for ALT Sisyphus.
