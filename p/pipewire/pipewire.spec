%def_disable snapshot

%define _libexecdir %_prefix/libexec
%define ver_major 0.3
%define api_ver 0.3
%define spa_api_ver 0.2
%define gst_api_ver 1.0

%def_enable gstreamer
%def_enable systemd
#system service: not recommended and disabled by default
%def_disable systemd_system_service
%def_enable vulkan
%ifarch %e2k
%def_disable examples
%else
%def_enable examples
%endif
%def_enable docs
%def_enable man
%def_enable check

Name: pipewire
Version: %ver_major.21
Release: alt1

Summary: Media Sharing Server
Group: System/Servers
License: MIT
Url: https://pipewire.org/

%if_disabled snapshot
#Source: http://freedesktop.org/software/%name/releases/%name-%version.tar.gz
Source: https://github.com/PipeWire/pipewire/archive/%version/%name-%version.tar.gz
%else
Vcs: https://github.com/PipeWire/pipewire.git
Source: %name-%version.tar
%endif
Patch: %name-0.3.19-alt-rpath.patch

Requires: %name-libs = %version-%release
Requires: rtkit

%define gst_ver 1.10

BuildRequires(pre): meson
BuildRequires: libgio-devel libudev-devel libdbus-devel
BuildRequires: libalsa-devel libjack-devel libpulseaudio-devel
BuildRequires: libv4l-devel libsndfile-devel
BuildRequires: libavformat-devel libavcodec-devel libavfilter-devel
BuildRequires: libbluez-devel
# BT codecs
BuildRequires: libsbc-devel libfdk-aac-devel libldac-devel
#BuildRequires: libopenaptx-devel
# for pw-top
BuildRequires: libncurses-devel
%if_enabled gstreamer
BuildRequires: pkgconfig(gstreamer-%gst_api_ver) >= %gst_ver
BuildRequires: pkgconfig(gstreamer-base-%gst_api_ver)
BuildRequires: pkgconfig(gstreamer-plugins-base-%gst_api_ver)
BuildRequires: pkgconfig(gstreamer-net-%gst_api_ver)
BuildRequires: pkgconfig(gstreamer-allocators-%gst_api_ver)
%endif
%{?_enable_systemd:BuildRequires: libsystemd-devel}
%{?_enable_vulkan:BuildRequires: libvulkan-devel}
%{?_enable_docs:BuildRequires: doxygen graphviz fonts-type1-urw}
%{?_enable_man:BuildRequires: xmltoman}
%{?_enable_check:BuildRequires: /proc gcc-c++}

%description
PipeWire is a multimedia server for Linux and other Unix like operating
systems.

%package libs
Summary: Libraries for PipeWire clients
Group: System/Libraries

%description libs
This package contains the runtime libraries for any application that wishes
to interface with a PipeWire media server.

%package libs-devel
Summary: Headers and libraries for PipeWire client development
Group: Development/C
Requires: %name-libs = %version-%release

%description libs-devel
Headers and libraries for developing applications that can communicate with
a PipeWire media server.

%package libs-devel-doc
Summary: PipeWire media server documentation
Group: Documentation
# https://bugzilla.altlinux.org/34101
BuildArch: noarch
Conflicts: %name-libs-devel < %version

%description libs-devel-doc
This package contains documentation for the PipeWire media server.

%package utils
Summary: PipeWire media server utilities
Group: System/Servers
Requires: %name-libs = %version-%release

%description utils
This package contains command line utilities for the PipeWire media server.

%prep
%setup
#%%patch

%build
export LIB=%_lib
%meson \
	%{?_enable_docs:-Ddocs=true} \
	%{?_enable_man:-Dman=true} \
	%{?_enable_gstreamer:-Dgstreamer=true} \
	%{?_disable_vulkan:-Dvulkan=false} \
	%{?_disable_systemd:-Dsystemd=false} \
	%{?_enable_systemd_system_service:-Dsystemd-system-service=true} \
	%{?_disable_examples:-Dexamples=false}
%nil
%meson_build

%install
%meson_install

%check
%meson_test

%pre
%_sbindir/groupadd -r -f %name 2>/dev/null ||:
%_sbindir/useradd -r -N -g %name -d / \
	-s /dev/null -c "PipeWire System Daemon" %name 2>/dev/null ||:

%files
%_bindir/%name
%_bindir/pw-jack
%_bindir/%name-pulse

%{?_enable_examples:%_bindir/%name-media-session}
%{?_enable_gstreamer:%_libdir/gstreamer-%gst_api_ver/libgst%name.so}
%dir %_sysconfdir/%name/
%_sysconfdir/%name/%name.conf
%dir %_sysconfdir/%name/media-session.d
%_sysconfdir/%name/media-session.d/alsa-monitor.conf
%_sysconfdir/%name/media-session.d/bluez-monitor.conf
%_sysconfdir/%name/media-session.d/media-session.conf
%_sysconfdir/%name/media-session.d/v4l2-monitor.conf
%_sysconfdir/%name/media-session.d/with-jack
%_sysconfdir/%name/media-session.d/with-pulseaudio
%_udevrulesdir/90-%name-alsa.rules
%_datadir/alsa-card-profile/
%if_enabled systemd
%_prefix/lib/systemd/user/%name.service
%_prefix/lib/systemd/user/%name.socket
%_prefix/lib/systemd/user/%name-pulse.service
%_prefix/lib/systemd/user/%name-pulse.socket

%{?_enable_systemd_system_service:
%_unitdir/%name.service
%_unitdir/%name.socket}
%endif
%_datadir/alsa/alsa.conf.d/50-pipewire.conf
%_datadir/alsa/alsa.conf.d/99-pipewire-default.conf
%if_enabled man
%_man1dir/%name.1*
%_man1dir/pw-jack.1*
#%_man1dir/pw-pulse.1*
%_man5dir/%name.conf.5*
%endif
%doc README* NEWS

%files libs
%_libdir/lib%name-%api_ver.so.*
%_libdir/%name-%api_ver/
%_libdir/spa-%spa_api_ver/
%_libdir/alsa-lib/

%files libs-devel
%_libdir/lib%name-%api_ver.so
%_includedir/%name-%api_ver/
%_includedir/spa-%spa_api_ver/
%_pkgconfigdir/lib%name-%api_ver.pc
%_pkgconfigdir/libspa-%spa_api_ver.pc

%if_enabled docs
%files libs-devel-doc
%_datadir/doc/%name/html
%endif

%files utils
%_bindir/pw-cat
%_bindir/pw-cli
%_bindir/pw-dot
%_bindir/pw-dump
%_bindir/pw-metadata
%_bindir/pw-mididump
%_bindir/pw-midiplay
%_bindir/pw-midirecord
%_bindir/pw-mon
%_bindir/pw-play
%_bindir/pw-profiler
%_bindir/pw-record
%_bindir/pw-top
%{?_enable_examples:%_bindir/pw-reserve}
%_bindir/spa-inspect
%_bindir/spa-monitor
%_bindir/spa-resample
%_bindir/spa-acp-tool
%if_enabled man
%_man1dir/pw-cat.1.*
%_man1dir/pw-cli.1*
%_man1dir/pw-dot.1.*
#%_man1dir/pw-dump.1.*
%_man1dir/pw-metadata.1.*
%_man1dir/pw-mididump.1.*
%_man1dir/pw-mon.1*
%_man1dir/pw-profiler.1.*
%endif


%changelog
* Thu Feb 04 2021 Yuri N. Sedunov <aris@altlinux.org> 0.3.21-alt1
- 0.3.21

* Thu Jan 21 2021 Yuri N. Sedunov <aris@altlinux.org> 0.3.20-alt1
- 0.3.20

* Tue Jan 05 2021 Yuri N. Sedunov <aris@altlinux.org> 0.3.19-alt1
- updated to 0.3.19-4-g18b5199d

* Tue Dec 15 2020 Yuri N. Sedunov <aris@altlinux.org> 0.3.18-alt1
- updated to 0.3.18-1-g13cb51ef

* Fri Nov 27 2020 Yuri N. Sedunov <aris@altlinux.org> 0.3.17-alt1
- 0.3.17

* Fri Nov 20 2020 Yuri N. Sedunov <aris@altlinux.org> 0.3.16-alt1
- updated to 0.3.16-1-g4d085816

* Wed Nov 04 2020 Yuri N. Sedunov <aris@altlinux.org> 0.3.15-alt1
- updated to 0.3.15-2-g7a437696

* Sat Oct 31 2020 Yuri N. Sedunov <aris@altlinux.org> 0.3.14-alt1
- 0.3.14

* Mon Sep 28 2020 Yuri N. Sedunov <aris@altlinux.org> 0.3.13-alt1
- updated to 0.3.13-1-g81ca70af

* Sat Sep 19 2020 Yuri N. Sedunov <aris@altlinux.org> 0.3.12-alt1
- updated to 0.3.12-4-g99b3f4a6

* Fri Sep 11 2020 Yuri N. Sedunov <aris@altlinux.org> 0.3.11-alt1
- updated to 0.3.11-1-gc979f181

* Tue Aug 04 2020 Yuri N. Sedunov <aris@altlinux.org> 0.3.9-alt1
- updated to 0.3.9-7-g92901379

* Wed Jul 29 2020 Yuri N. Sedunov <aris@altlinux.org> 0.3.8-alt1
- updated to 0.3.8-1-gc04d57d5

* Tue Jul 21 2020 Yuri N. Sedunov <aris@altlinux.org> 0.3.7-alt1
- updated to 0.3.7-5-gcc0727e6

* Wed Jun 10 2020 Yuri N. Sedunov <aris@altlinux.org> 0.3.6-alt1
- updated to 0.3.6-5-gda9d17e7

* Tue May 12 2020 Yuri N. Sedunov <aris@altlinux.org> 0.3.5-alt1
- updated 0.3.5-2-gfdb3985f

* Fri May 01 2020 Yuri N. Sedunov <aris@altlinux.org> 0.3.4-alt1
- updated to 0.3.4-5-gf11cd322

* Fri Mar 27 2020 Yuri N. Sedunov <aris@altlinux.org> 0.3.2-alt1
- 0.3.2

* Tue Mar 24 2020 Yuri N. Sedunov <aris@altlinux.org> 0.3.1-alt3
- made examples build optional and disabled on %%e2k (
  Checking for function "memfd_create" : NO)

* Mon Mar 23 2020 Yuri N. Sedunov <aris@altlinux.org> 0.3.1-alt2
- made vulkan support optional
- fixed License tag

* Sun Mar 08 2020 Yuri N. Sedunov <aris@altlinux.org> 0.3.1-alt1
- 0.3.1

* Fri Sep 27 2019 Yuri N. Sedunov <aris@altlinux.org> 0.2.7-alt1
- 0.2.7

* Mon May 27 2019 Yuri N. Sedunov <aris@altlinux.org> 0.2.6-alt1
- updated to 0.2.6-1-g37613b67

* Mon May 06 2019 Yuri N. Sedunov <aris@altlinux.org> 0.2.5-alt1.2
- fixed build without docs

* Mon May 06 2019 Yuri N. Sedunov <aris@altlinux.org> 0.2.5-alt1.1
- fixed build without mans

* Mon Dec 24 2018 Yuri N. Sedunov <aris@altlinux.org> 0.2.5-alt1
- updated to 0.2.5-2-gf8b156ac

* Fri Nov 23 2018 Yuri N. Sedunov <aris@altlinux.org> 0.2.4-alt1
- 0.2.4

* Fri Sep 21 2018 Yuri N. Sedunov <aris@altlinux.org> 0.2.3-alt1
- updated to 0.2.3-7-g58efa8c2

* Sat Aug 04 2018 Yuri N. Sedunov <aris@altlinux.org> 0.2.2-alt1
- 0.2.2

* Mon Jun 04 2018 Yuri N. Sedunov <aris@altlinux.org> 0.1.9-alt2
- rebuilt with ffmpeg-4.0

* Fri Mar 02 2018 Yuri N. Sedunov <aris@altlinux.org> 0.1.9-alt1
- 0.1.9

* Thu Jan 25 2018 Yuri N. Sedunov <aris@altlinux.org> 0.1.8-alt1
- 0.1.8

* Sun Nov 26 2017 Yuri N. Sedunov <aris@altlinux.org> 0.1.7-alt1
- 0.1.7

* Mon Nov 06 2017 Yuri N. Sedunov <aris@altlinux.org> 0.1.6-alt1
- 0.1.6

* Tue Sep 19 2017 Yuri N. Sedunov <aris@altlinux.org> 0.1.5-alt1
- first build for Sisyphus

