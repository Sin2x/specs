Name: bitlbee-facebook
Version: 1.2.2
Release: alt1
Group: Networking/IRC
License: GPLv2
Url: https://wiki.bitlbee.org/HowtoFacebookMQTT
Summary: MQTT (Facebook) plugin for bitlbee
Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires: bitlbee-devel libjson-glib-devel zlib-devel

%description
As an alternative to the now (mostly-)defunct XMPP service provided by
facebook, jgeboski (who also wrote bitlbee-steam) made a new plugin based on
the facebook messenger mobile client (which uses a protocol called MQTT).  It
also happens to work much better than the XMPP service ever did, and supports
groupchats.

%prep
%setup
%patch -p1

%build
%autoreconf
%configure \
    --with-plugindir=%_libdir/bitlbee
# smp incompatible build
make

%install
%makeinstall DESTDIR=%buildroot libdir=%_libdir/bitlbee

%files
%doc README NEWS ChangeLog COPYING AUTHORS
%_libdir/bitlbee/facebook.so

%changelog
* Tue Feb 23 2021 L.A. Kostis <lakostis@altlinux.ru> 1.2.2-alt1
- 1.2.2.

* Sat Jan 12 2019 L.A. Kostis <lakostis@altlinux.ru> 1.1.2-alt3.7682a35
- Fix smp build.

* Sat Jan 12 2019 L.A. Kostis <lakostis@altlinux.ru> 1.1.2-alt2.7682a35
- Updated to 1.1.2 7682a35 GIT.

* Fri Mar 23 2018 L.A. Kostis <lakostis@altlinux.ru> 1.1.2-alt1.g553593d
- Updated to 1.1.2 553593d GIT.

* Tue Sep 15 2015 L.A. Kostis <lakostis@altlinux.ru> 0.1.0-alt1
- Initial build for ALTLinux.
