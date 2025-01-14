%define _deffontdir catalogue:%_sysconfdir/X11/fontpath.d
%define _xorgmoduledir %_libdir/X11/modules

Name: tigervnc
Version: 1.11.0
Release: alt1
Summary: A TigerVNC remote display system

Group: Networking/Remote access
License: GPLv2+
URL: http://www.tigervnc.com

BuildRequires(pre): rpm-macros-cmake
Requires: xauth xkeyboard-config fonts-bitmap-misc xorg-dri-swrast
Provides: tightvnc
Obsoletes: tightvnc

Source0: %name-%version.tar.gz
Source1: vncserver.init
Source2: vncserver.service
Source3: vncserver.pl
Source4: vncserver.man

Source100: xorg-server-source.tar
Source101: tightpasswd.tar.gz
Source200: repatch_spec.sh
Source201: tigervnc.unused

## FC patches
Patch1: FC-xserver120.patch
Patch2: FC-let-user-know-about-not-using-view-only-password.patch
Patch3: FC-working-tls-on-fips-systems.patch
Patch4: FC-utilize-system-crypto-policies.patch
Patch5: FC-passwd-crash-with-malloc-checks.patch
Patch6: FC-tolerate-specifying-boolparam.patch
Patch7: FC-systemd-service.patch
Patch8: FC-correctly-start-vncsession-as-daemon.patch
Patch9: FC-selinux-missing-compression-and-correct-location.patch
Patch10: FC-selinux-policy-improvements.patch
Patch11: FC-argb-runtime-ximage-byteorder-selection.patch

## Ubuntu patches
Patch101: Ubuntu-0000-find-fltk-libs.patch
Patch102: Ubuntu-0001-x0vncserver-build-make-missing-libraries-fatal-errors.patch
Patch103: Ubuntu-0002-fix-linking.patch
Patch104: Ubuntu-0010-fix-xtigervnc-build.patch
Patch105: Ubuntu-0020-buildtime-from-debian-changelog.patch
Patch106: Ubuntu-0102-fix-spelling-error-in-manpages-to-shutup-lintian.patch
Patch107: Ubuntu-0151-make-cmake-enable-options-mandatory-if-turned-on.patch
Patch108: Ubuntu-0175-xtigervncviewer-WM_CLASS.patch
Patch109: Ubuntu-0205-defined-CMAKE_INSTALL_FULL_BINDIR.patch
Patch110: Ubuntu-0210-use-tigervncsession-name.patch
Patch111: Ubuntu-0220-remove-systemd-service-obsolete-syslog-target.patch
Patch112: Ubuntu-0300-fix-Xtigervnc-boolparam-parsing.patch
Patch113: Ubuntu-rh_0904-Added-RH-patch-tigervnc11-rh588342.patch-which-fixes.patch
Patch114: Ubuntu-rh_tigervnc-manpages.patch
Patch115: Ubuntu-rh_tigervnc-cursor.patch
Patch116: Ubuntu-rh_tigervnc-working-tls-on-fips-systems.patch
Patch117: Ubuntu-CVE-2014-8240-849479.patch

## ALT patches
Patch501: tigervnc-stdinpasswd.patch
Patch502: ALT-FC-xserver120.patch
Patch601: U_0001-Properly-store-certificate-exceptions.patch
Patch602: U_0002-Properly-store-certificate-exceptions-in-Java-viewer.patch

# Automatically added by buildreq on Thu Dec 19 2019
# optimized out: cmake-modules fontconfig glibc-kernheaders-generic glibc-kernheaders-x86 libGL-devel libICE-devel libX11-devel libXau-devel libXext-devel libXfixes-devel libXi-devel libXrender-devel libcrypt-devel libglvnd-devel libgpg-error libgpg-error-devel libsasl2-3 libstdc++-devel perl pkg-config python2-base sh4 xorg-proto-devel
BuildRequires: ImageMagick-tools cmake doxygen flex gcc-c++ libGL-devel libSM-devel libXdamage-devel libXdmcp-devel libXfont2-devel libXinerama-devel libXrandr-devel libXtst-devel libdrm-devel libfltk-devel libgcrypt-devel libgnutls-devel libjpeg-devel libpam-devel libpciaccess-devel libpixman-devel libssl-devel libxkbfile-devel libxshmfence-devel xorg-xtrans-devel zlib-devel

BuildRequires: libfltk-devel >= 1.3.3

BuildRequires: xorg-sdk xorg-font-utils

BuildRequires: libXrender-devel

%ifarch %ix86 x86_64
BuildRequires: nasm
%endif

%description
Virtual Network Computing (VNC) is a remote display system which
allows you to view a computing 'desktop' environment not only on the
machine where it is running, but from anywhere on the Internet and
from a wide variety of machine architectures.  This package contains a
client which will allow you to connect to other desktops running a VNC
server.

%package server
Summary: A TigerVNC server
Group: Networking/Remote access
Provides: tightvnc-server
Obsoletes: tightvnc-server
Requires: %name-common = %version-%release, %name-pam = %version-%release

%description server
The VNC system allows you to access the same desktop from a wide
variety of platforms.  This package is a TigerVNC server, allowing
others to access the desktop on your machine.

%package common
Summary: A TigerVNC and TightVNC compatible passwd utilities
Group: Networking/Remote access
Conflicts: turbovnc-server

%description common
A TigerVNC and TightVNC compatible passwd utilities

%package -n xorg-extension-vnc
Summary: VNC extension for Xorg
Group: Networking/Remote access
Requires: %name-common = %version-%release, %name-pam = %version-%release

%description -n xorg-extension-vnc
TigerVNC extension for Xorg server

%package pam
Summary: PAM module for TigerVNC servers
Group: Networking/Remote access

%description pam
PAM module for TigerVNC servers

%prep
%setup -a101 -a100
cp %SOURCE3 %SOURCE4 .

## FC apply patches
#patch1 -p1 -b .xserver120-rebased
%patch2 -p1 -b .let-user-know-about-not-using-view-only-password
%patch3 -p1 -b .working-tls-on-fips-systems
%patch4 -p1 -b .utilize-system-crypto-policies
%patch5 -p1 -b .passwd-crash-with-malloc-checks
%patch6 -p1 -b .tolerate-specifying-boolparam
%patch7 -p1 -b .systemd-service
%patch8 -p1 -b .correctly-start-vncsession-as-daemon
%patch9 -p1 -b .selinux-missing-compression-and-correct-location
%patch10 -p1 -b .selinux-policy-improvements
%patch11 -p1 -b .argb-runtime-ximage-byteorder-selection

## Ubuntu apply patches
%patch101 -p1
%patch102 -p1
%patch103 -p1
%patch104 -p1
#patch105 -p1
%patch106 -p1
%patch107 -p1
%patch108 -p1
%patch109 -p1
#patch110 -p1
%patch111 -p1
#patch112 -p1
%patch113 -p1
#patch114 -p1
%patch115 -p1
#patch116 -p1
%patch117 -p1

## ALT apply patches
%patch501 -p1
%patch502 -p1
#patch601 -p1
#patch602 -p1

# Unpach Ubuntu's xtigervncviewer
sed -i 's/xtigervncviewer/vncviewer/g' vncviewer/vncviewer.desktop.in.in

%build

%add_optflags -fPIC
%cmake_insource -DCMAKE_INSTALL_UNITDIR:PATH=%_unitdir
%make_build

pushd unix/xserver
%autoreconf
%configure \
	--disable-composite \
	--disable-config-dbus \
	--disable-config-hal \
	--disable-config-udev \
	--disable-devel-docs \
	--disable-dmx \
	--disable-dri \
	--disable-kdrive \
	--disable-selective-werror \
	--disable-static \
	--disable-unit-tests \
	--disable-wayland \
	--disable-xephyr \
	--disable-xnest \
	--disable-xorg \
	--disable-xvfb \
	--disable-xwayland \
	--disable-xwin \
	--enable-dri2 \
	--enable-dri3 \
	--enable-glx \
	--enable-install-libxf86config \
	--enable-ipv6 \
	--with-default-font-path=%_deffontdir \
	--with-dri-driver-path=%_libdir/dri \
	--with-module-dir="%_xorgmoduledir" \
	--with-pic \
	--with-xkb-output=%_localstatedir/xkb

%make_build LIBS="-ljpeg -lpam -lz -lgnutls -lm" CPPFLAGS="-I/usr/include/libdrm"
popd

# Build icons
##pushd media
##%cmake_insource -DDATA_DIR:PATH=%_datadir
##%make
##popd

# Build tightvnc compatible vncpasswd
pushd tightpasswd
cc %optflags *.c -o tightpasswd
popd

%install
%makeinstall_std

%makeinstall_std -C unix/xserver/hw/vnc

# Install Xvnc as service
install -pD -m755 %SOURCE1 %buildroot%_initddir/vncserver

mkdir -p %buildroot%_sysconfdir/sysconfig
cat << __EOF__ > %buildroot%_sysconfdir/sysconfig/vncservers
# The VNCSERVERS variable is a list of display:user pairs.
# The VNCSERVERARGS[N] variable is a list of display's (N) parameters.
#
# Uncomment the line below to start a VNC server on display :1
# as my 'myusername' (adjust this to your own).  You will also
# need to set a VNC password; run 'man vncpasswd' to see how
# to do that.
#
# DO NOT RUN THIS SERVICE if your local area network is
# untrusted!  For a secure way of using VNC, see
# <URL:http://www.uk.research.att.com/vnc/sshvnc.html>.

# VNCSERVERS="1:myusername"
# VNCSERVERARGS[1]="-geometry 800x600 -localhost"
__EOF__

install -D contrib/packages/rpm/el7/SOURCES/10-libvnc.conf %buildroot%_sysconfdir/X11/xorg.conf.d/vnc.conf

# Build tightvnc compatible vncpasswd
install tightpasswd/tightpasswd %buildroot%_bindir/tightpasswd
install tightpasswd/vncpasswd.man %buildroot%_man1dir/tightpasswd.1

install vncserver.pl %buildroot/%_bindir/vncserver
install vncserver.man %buildroot/%_man1dir/vncserver.1

%find_lang %name

%files -f %name.lang
%doc LICENCE.TXT *.rst
%_bindir/vncviewer
%_desktopdir/*.desktop
%_iconsdir/hicolor/*/apps/*.png
%_iconsdir/hicolor/*/apps/*.svg
%_man1dir/vncviewer.1*

%files server
%_initddir/vncserver
%_unitdir/vncserver@.service
%config(noreplace) %_sysconfdir/sysconfig/vncservers
%config(noreplace) %_sysconfdir/tigervnc
%_bindir/vncconfig
%_bindir/x0vncserver
%_bindir/Xvnc
%_bindir/vncserver
%_sbindir/*
%_prefix/libexec/*
%_man1dir/Xvnc.1*
%_man1dir/vncconfig.1*
%_man8dir/*.8*
%_man1dir/x0vncserver.1*

%files common
%_bindir/vncpasswd
%_bindir/tightpasswd
%_man1dir/vncpasswd.1*
%_man1dir/tightpasswd.1*

%files pam
%_sysconfdir/pam.d/*

%files -n xorg-extension-vnc
%config(noreplace) %_sysconfdir/X11/xorg.conf.d/vnc.conf
%_xorgmoduledir/extensions/*.so

%changelog
* Fri Aug 06 2021 Fr. Br. George <george@altlinux.ru> 1.11.0-alt1
- Udate to 1.11.0
- Update patches

* Mon Jan 25 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 1.10.1-alt5
- Fixed desktop file (Closes: 39595).

* Tue Nov 17 2020 Fr. Br. George <george@altlinux.ru> 1.10.1-alt4
- Fix CVE-2020-26117

* Thu Sep 17 2020 Fr. Br. George <george@altlinux.ru> 1.10.1-alt3
- Update patches, fix vncviwewer "invalid resolution" bug

* Sat Jun 06 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.10.1-alt2
- add explicit libGL-devel buildreq

* Thu Jun 04 2020 Evgeniy Korneechev <ekorneechev@altlinux.org> 1.10.1-alt1
- New version
- Update FC-passwd-crash-with-malloc-checks.patch

* Thu Dec 19 2019 Fr. Br. George <george@altlinux.ru> 1.10.0-alt1
- Version up
- Update to XServer 1.20.6
- Update patches

* Wed Jul 24 2019 Fr. Br. George <george@altlinux.ru> 1.9.0-alt4
- Update to XServer 1.20 (ALT: #37059)

* Thu May 30 2019 Pavel Moseev <mars@altlinux.org> 1.9.0-alt3
- fix tooltip translation

* Tue May 07 2019 Evgeniy Korneechev <ekorneechev@altlinux.org> 1.9.0-alt2
- Spec cleanup
- Fix repocop's test 'rpm-filesystem-conflict-file'

* Mon Mar 25 2019 Evgeniy Korneechev <ekorneechev@altlinux.org> 1.9.0-alt1
- New version (ALT #36339)
- Update FC-getmaster.patch and tigervnc-stdinpasswd.patch

* Wed Aug 02 2017 Evgeniy Korneechev <ekorneechev@altlinux.org> 1.8.0-alt2
- Rebuild with new xorg-server (1.19.3) - fix discrepancy of ABI vnc-module and server
- Update FC-xserver116-rebased.patch

* Wed Aug 02 2017 Evgeniy Korneechev <ekorneechev@altlinux.org> 1.8.0-alt1
- New version
- Removed FC patch (.libvnc-os)
- Updated buildrequires

* Fri Jan 27 2017 Evgeniy Korneechev <ekorneechev@altlinux.org> 1.7.0-alt2
- vncserver.init: added ability to specify the display settings
- default "xstartup": added exporting environment variable LANG

* Tue Jan 10 2017 Evgeniy Korneechev <ekorneechev@altlinux.org> 1.7.0-alt1
- New version (ALT #32741, #32898)

* Mon Apr 25 2016 Fr. Br. George <george@altlinux.ru> 1.6.0-alt1
- Update FC patches, fix one
- (cas@) New version (ALT #30662)
- (cas@) Rebuild with xorg-server 1.18.2
- (cas@) Package vncserver@.service file
- (cas@) Return missing xorg-extension-vnc configuration file

* Thu Jun 25 2015 Fr. Br. George <george@altlinux.ru> 1.3.1-alt1
- Version update
- FC patches import
- Old vncpasswd binary renamed to tightpasswd

* Wed Apr 22 2015 Fr. Br. George <george@altlinux.ru> 1.3.0-alt1
- Massive submajor version update

* Wed Oct 22 2014 Valery Inozemtsev <shrek@altlinux.ru> 1.1.0-alt2
- disabled vnc extension

* Wed May 02 2012 Valery Inozemtsev <shrek@altlinux.ru> 1.1.0-alt1
- 1.1.0

* Sun Jul 24 2011 Valery Inozemtsev <shrek@altlinux.ru> 1.0.90-alt6
- enabled VeNCrypt

* Tue Jun 21 2011 Valery Inozemtsev <shrek@altlinux.ru> 1.0.90-alt5
- updated xorg-server-source to 1.10.2
- enabled ipv6
- fixed CVE-2011-1775

* Tue Apr 19 2011 Valery Inozemtsev <shrek@altlinux.ru> 1.0.90-alt4
- updated build dependencies
- updated xorg-server-source to 1.9.5

* Sun Nov 07 2010 Valery Inozemtsev <shrek@altlinux.ru> 1.0.90-alt3
- SVN snapshot 2010-08-13 (4123)

* Mon Oct 04 2010 Valery Inozemtsev <shrek@altlinux.ru> 1.0.90-alt2
- rebuild with libcrypto.so.10

* Wed Apr 14 2010 Valery Inozemtsev <shrek@altlinux.ru> 1.0.90-alt1
- vncpasswd compatibility to tightvnc

* Tue Mar 30 2010 Valery Inozemtsev <shrek@altlinux.ru> 1.0.90-alt0.20100219svn3993
- initial release
