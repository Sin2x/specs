%define native_code_gen %nil
%define dyn_libs %nil
%define no_interpreter %nil

%ifarch %ix86 x86_64
%define native_code_gen --enable-split-objs
%define dyn_libs --enable-shared
%else
%define no_interpreter --ghc-option=-DALT_NO_GHCI --flags=-templateHaskell
%endif

Name: rpm-build-haskell
Version: 1.4.6
Release: alt1

Summary: RPM helpers to rebuild Haskell packages
License: Public domain
Group: Development/Haskell

Source: scripts-%version.tar
Source1: macros
Source2: buildreq-ignore
Source3: haskell.env

# Uses the modular reqprov subsystem
Conflicts: rpm-build < 4.0.4-alt78

%description
RPM macros and reqprov helpers to be used in Haskell packages.

There is currently no support for compilers other than GHC.

%prep
%setup -n scripts-%version

%install
mkdir -p %buildroot%_rpmlibdir
cp haskell.* -t %buildroot%_rpmlibdir/
mkdir -p %buildroot%_rpmmacrosdir
sed \
	-e 's/@ENABLE_SPLIT_OBJS@/%{native_code_gen}/' \
	-e 's/@ENABLE_SHARED@/%{dyn_libs}/' \
	-e 's/@NO_INTERPRETER@/%{no_interpreter}/' \
	%SOURCE1 > %buildroot%_rpmmacrosdir/haskell
install -D %SOURCE2 \
	%buildroot%_sysconfdir/buildreqs/files/ignore.d/rpm-build-haskell
install -D -m0755 %SOURCE3 \
	%buildroot%_rpmmacrosdir/haskell.env
install -D -m0755 hs_gen_filelist.sh %buildroot%_libexecdir/%name/hs_gen_filelist.sh

%files
%_rpmlibdir/haskell.*
%_rpmmacrosdir/haskell*
%_sysconfdir/buildreqs/files/ignore.d/rpm-build-haskell
%_libexecdir/%name

%changelog
* Wed Jun 30 2021 Evgeny Sinelnikov <sin@altlinux.org> 1.4.6-alt1
- Fix the field() function against newest package.conf format with
  additional spaces between option name and value

* Fri Mar 15 2019 Evgeny Sinelnikov <sin@altlinux.org> 1.4.5-alt1
- Add modules dynamic directory libraries option and fixed haskell modules
  subdirectory option for 8.x.x or newest ghc versions only

* Wed Feb 27 2019 Evgeny Sinelnikov <sin@altlinux.org> 1.4.4-alt1
- Add ld preload for dynamic libraries

* Mon Feb 25 2019 Evgeny Sinelnikov <sin@altlinux.org> 1.4.3-alt1
- Replace modules dynamic libraries separate single directory %%_libdir/$compiler/lib

* Fri Feb 22 2019 Evgeny Sinelnikov <sin@altlinux.org> 1.4.2-alt1
- Replace subdirectory for libraries to compiler directory as it prefer in newest ghc

* Wed Feb 20 2019 Evgeny Sinelnikov <sin@altlinux.org> 1.4.1-alt1
- Set modules dynamic directory libraries to %%_libdir/$compiler/lib/$pkgid

* Wed Feb 20 2019 Evgeny Sinelnikov <sin@altlinux.org> 1.4-alt1
- Fixed build requires like "base-4.10.1.0" or "ghc-boot-8.2.2" (Closes: 36137)

* Wed Feb 20 2019 Gleb F-Malinovskiy <glebfm@altlinux.org> 1.3.1-alt1
- Removed BuildArch: noarch to fix regression in %%hs_configure2 macro
  definition on x86_64 and %%ix86 architectures.
- %%hs_configure2: Pass -DALT_NO_GHCI on architectures without GHCi support.

* Fri Feb 08 2019 Gleb F-Malinovskiy <glebfm@altlinux.org> 1.3-alt1
- Fixed build of ghc modules on non-x86 architectures.
- Added mipsel, aarch64, and ppc64le architectures
  to %%ghc_arches macro.

* Wed Nov 21 2018 Grigory Ustinov <grenka@altlinux.org> 1.2-alt1
- add %%ghc_arches macro.

* Thu Dec 14 2017 Ivan Zakharyaschev <imz@altlinux.org> 1.1-alt1
- correct/cleanup macro uses (they were introduced in 1-alt26
  and they generate warnings)
- discard %%hs_package_register (not used anywhere)

* Thu Oct 22 2015 Ivan Zakharyaschev <imz@altlinux.org> 1-alt26
- allow to build SRPMs which don't build-require ghc or
  ghc%%{ghc_version}-common (legacy ones).

* Thu Oct 22 2015 Ivan Zakharyaschev <imz@altlinux.org> 1-alt25
- .spec: do own our directory.

* Thu Oct 22 2015 Ivan Zakharyaschev <imz@altlinux.org> 1-alt24
- .spec: do not require rpm-build (express the compatibility with
  Conflicts).
- .spec: use standard new /usr/lib/locations for the scripts
  according to https://www.altlinux.org/RPM_Macros_Packaging_Policy.

* Sat Dec 22 2012 Denis Smirnov <mithraen@altlinux.ru> 1-alt23
- fix building haskell packages with binaries and without libraries

* Fri Dec 21 2012 Denis Smirnov <mithraen@altlinux.ru> 1-alt22
- auto add conf-file when packaging libraries

* Sun Jul 01 2012 Denis Smirnov <mithraen@altlinux.ru> 1-alt21
- fix filelist for packaging

* Sun Jul 01 2012 Denis Smirnov <mithraen@altlinux.ru> 1-alt20
- not try to package /usr/bin

* Sun Jul 01 2012 Denis Smirnov <mithraen@altlinux.ru> 1-alt19
- create filelist for all files that can be build from cabal package

* Sat Mar 17 2012 Denis Smirnov <mithraen@altlinux.ru> 1-alt18
- remove unneeded requires

* Sat Mar 17 2012 Denis Smirnov <mithraen@altlinux.ru> 1-alt17
- remove ghc(package) provides, use only provides with ghc version

* Thu Aug 04 2011 Denis Smirnov <mithraen@altlinux.ru> 1-alt16
- fix install for non-library packages

* Sun Sep 19 2010 Denis Smirnov <mithraen@altlinux.ru> 1-alt15
- enable build shared libraries

* Mon Sep 13 2010 Denis Smirnov <mithraen@altlinux.ru> 1-alt14
- fix filelist creation for profiling libs build

* Mon Sep 13 2010 Denis Smirnov <mithraen@altlinux.ru> 1-alt13
- more strict requires

* Mon Sep 13 2010 Denis Smirnov <mithraen@altlinux.ru> 1-alt12
- build all libs with profiling versions

* Sat Sep 11 2010 Denis Smirnov <mithraen@altlinux.ru> 1-alt11
- add some useful macros

* Fri Sep 10 2010 Denis Smirnov <mithraen@altlinux.ru> 1-alt10
- ignore builtin_ffi/builtin_rts requires

* Thu Sep 09 2010 Denis Smirnov <mithraen@altlinux.ru> 1-alt9
- add requires to haskell-filetrigger

* Thu Sep 09 2010 Denis Smirnov <mithraen@altlinux.ru> 1-alt8
- ghc 6.12 support

* Thu Mar 18 2010 Alexander Myltsev <avm@altlinux.ru> 1-alt7
- Fix the hs_package_register macro for ghc 6.10.4.

* Mon Nov 17 2008 Alexander Myltsev <avm@altlinux.ru> 1-alt6
- Stop using the 'configure --user' hack.

* Thu Jun 19 2008 Alexander Myltsev <avm@altlinux.ru> 1-alt5
- Use versionless build-deps.
- Add a buildreq ignore rule (fixes #17878).

* Fri Jan 18 2008 Alex V. Myltsev <avm@altlinux.ru> 1-alt4
- Accept *.package.conf files (that's what gtk2hs uses, maybe it's right).
- Fix errors when "depends:" lines contain commas or versionless items.

* Mon Jan 14 2008 Alex V. Myltsev <avm@altlinux.ru> 1-alt3
- More useful macros: %%hs_package_register, %%hs_setup etc.

* Sat Jan 12 2008 Alex V. Myltsev <avm@altlinux.ru> 1-alt2
- Fix bug with multiline values in *.pkg files.

* Tue Jan 08 2008 Alex V. Myltsev <avm@altlinux.ru> 1-alt1
- Initial build for Sisyphus.
