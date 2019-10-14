%define _unpackaged_files_terminate_build 1

Name: sdcc
Epoch: 1
Version: 3.9.0
Release: alt1
Group: Development/C
URL: http://sdcc.sourceforge.net
License: GPL
Summary: Small Device C Compiler

Source: %name-%version.tar

Patch1: %name-%version-alt.patch

BuildRequires: flex gcc-c++ boost-devel gputils /usr/bin/makeinfo
BuildRequires: zlib-devel
BuildRequires: /usr/bin/python3

Requires: %name-common = %EVR

%description
SDCC is a free open source, retargettable, optimizing ANSI C compiler
suite that targets a growing list of processors including the Intel
MCS51 based microprocessors (8031, 8032, 8051, 8052, etc.), Maxim
(formerly Dallas) DS80C390 variants, Freescale (formerly Motorola)
HC08 based (hc08, s08) and Zilog Z80 based MCUs (z80, z180, gbz80,
Rabbit 2000/3000, Rabbit 3000A). Work is in progress on supporting
the Microchip PIC16 and PIC18 targets. It can be retargeted for other
microprocessors.

%package common
License: GPL, LGPL
Group:   Development/C
Summary: Libraries and Header Files for the SDCC C compiler

%description common
SDCC is a free open source, retargettable, optimizing ANSI C compiler
suite that targets a growing list of processors including the Intel
MCS51 based microprocessors (8031, 8032, 8051, 8052, etc.), Maxim
(formerly Dallas) DS80C390 variants, Freescale (formerly Motorola)
HC08 based (hc08, s08) and Zilog Z80 based MCUs (z80, z180, gbz80,
Rabbit 2000/3000, Rabbit 3000A). Work is in progress on supporting
the Microchip PIC16 and PIC18 targets. It can be retargeted for other
microprocessors.

%package doc
License:   GPL
Group:     Development/C
Summary:   Documentation for the SDCC C compiler
BuildArch: noarch

%description doc
SDCC is a free open source, retargettable, optimizing ANSI C compiler
suite that targets a growing list of processors including the Intel
MCS51 based microprocessors (8031, 8032, 8051, 8052, etc.), Maxim
(formerly Dallas) DS80C390 variants, Freescale (formerly Motorola)
HC08 based (hc08, s08) and Zilog Z80 based MCUs (z80, z180, gbz80,
Rabbit 2000/3000, Rabbit 3000A). Work is in progress on supporting
the Microchip PIC16 and PIC18 targets. It can be retargeted for other
microprocessors.

%prep
%setup
%patch1 -p1

%build
PYTHON=python3 \
%configure \
	--docdir=%_docdir/%name-%version \
	--enable-werror=no \
	%nil

%make_build

%install
%makeinstall_std

%files 
%_bindir/*

%files common
%_datadir/%name

%files doc
%_docdir/%name-%version

%changelog
* Mon Oct 14 2019 Aleksei Nikiforov <darktemplar@altlinux.org> 1:3.9.0-alt1
- Updated to upstream version 3.9.0 (Closes: #37328).

* Tue Sep 26 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 1:3.6.0-alt1
- Updated to upstream version 3.6.0.

* Thu Mar 12 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 8378-alt1.1
- Removed -Werror flag

* Sat Jan 12 2013 Yury A. Romanov <damned@altlinux.ru> 8378-alt1
- Switched to 8378

* Tue Nov 27 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5119-alt1.qa3
- Fixed build with make 3.82

* Wed Jun 20 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5119-alt1.qa2
- Fixed build with glibc 2.11.3

* Tue Nov 10 2009 Repocop Q. A. Robot <repocop@altlinux.org> 5119-alt1.qa1
- NMU (by repocop): the following fixes applied:
  * docdir-is-not-owned for sdcc
  * postclean-05-filetriggers for spec file

* Fri Mar 28 2008 Yury A. Romanov <damned@altlinux.ru> 5119-alt1
- 5119

* Thu Jan 03 2008 Yury A. Romanov <damned@altlinux.ru> 4988-alt1
- Initial build

