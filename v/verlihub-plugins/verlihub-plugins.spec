%define pluginlist "chatroom forbid iplog isp messanger replacer stats"

Name: verlihub-plugins
Version: 0.1
Release: alt3

Summary: Plugins for verlihub

Url: http://www.verlihub-project.org
License: GPL
Group: Development/C

Source: http://prdownloads.sourceforge.net/verlihub/All-0.1.tar.bz2
Packager: Vitaly Lipatov <lav@altlinux.ru>

Patch: verlihub-plugins-gcc8-fix.patch

# Automatically added by buildreq on Fri Apr 25 2008
BuildRequires: gcc-c++ libGeoIP-devel libMySQL-devel liblua5-devel libpcre-devel libverlihub-devel zlib-devel

%description
This package contains various plugins for verlihub:
%pluginlist


%prep
%setup -n %name -c %name-%version
%patch -p1

%build
for i in `echo %pluginlist` ; do
	cd $i
	%configure --disable-static
	%make_build
	cd ..
done

%install
for i in `echo %pluginlist` ; do
	cd $i
	%makeinstall_std
	cd ..
done

%files
#%doc
#%_bindir/%name
%_datadir/verlihub/*
%_libdir/*.so*
#%python_sitelibdir/*

%changelog
* Wed Feb 19 2020 Andrey Bychkov <mrdrew@altlinux.org> 0.1-alt3
- Dependency on python 2 removed.

* Thu Feb 14 2019 Ivan Razzhivin <underwit@altlinux.org> 0.1-alt2.qa2.2
- GCC8 fix

* Wed Apr 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.1-alt2.qa2.1
- (NMU) rebuild with gcc5-c++ (for new C++ ABI).

* Wed Apr 17 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 0.1-alt2.qa2
- NMU: rebuilt for debuginfo.

* Wed Dec 02 2009 Repocop Q. A. Robot <repocop@altlinux.org> 0.1-alt2.qa1
- NMU (by repocop): the following fixes applied:
  * post_ldconfig for verlihub-plugins
  * postun_ldconfig for verlihub-plugins
  * postclean-05-filetriggers for spec file

* Thu Jul 03 2008 Vitaly Lipatov <lav@altlinux.ru> 0.1-alt2
- lua plugin build in standalone package

* Fri Apr 25 2008 Vitaly Lipatov <lav@altlinux.ru> 0.1-alt1
- initial build for ALT Linux Sisyphus
