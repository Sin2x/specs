%define _unpackaged_files_terminate_build 1

Name: gerbera
Version: 1.5.0
Release: alt1

Summary: UPnP Media Server
Group: System/Servers
License: GPLv2 and MIT
Url: https://gerbera.io
Source: %name-%version.tar
Patch: %name-%version-%release.patch

Requires: %name-data = %EVR

BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: libupnp-devel >= 1.12.1
BuildRequires: libfmt-devel
BuildRequires: libspdlog-devel >= 1.4
BuildRequires: libuuid-devel
BuildRequires: libexpat-devel
BuildRequires: libsqlite3-devel
BuildRequires: libduktape-devel
BuildRequires: libcurl-devel
BuildRequires: libtag-devel
BuildRequires: libmagic-devel
BuildRequires: libpugixml-devel
BuildRequires: libexif-devel
BuildRequires: libexiv2-devel
BuildRequires: libavformat-devel
BuildRequires: libavutil-devel
BuildRequires: libffmpegthumbnailer-devel
BuildRequires: zlib-devel
BuildRequires: libmatroska-devel
BuildRequires: libsystemd-devel
BuildRequires: libmysqlclient-devel

%description
Gerbera is a UPnP media server which allows you to stream your digital
media through your home network and consume it on a variety of UPnP
compatible devices.

%package data
Summary: Data files for Gerbera
BuildArch: noarch
Group: System/Servers

%description data
Data files for the Gerbera media server.

%prep
%setup
%patch -p1

%build
%cmake \
    -DWITH_JS=1 \
    -DWITH_MYSQL=0 \
    -DWITH_CURL=1 \
    -DWITH_TAGLIB=1 \
    -DWITH_MAGIC=1 \
    -DWITH_AVCODEC=1 \
    -DWITH_EXIF=1 \
    -DWITH_EXIV2=1 \
    -DWITH_FFMPEGTHUMBNAILER=1 \
    -DWITH_INOTIFY=1 \
    -DWITH_SYSTEMD=1 \
    -DWITH_MYSQL=1 \
    -DUPNP_HAS_REUSEADDR=1

%cmake_build

%install
mkdir -p %buildroot{%_sysconfdir,%_localstatedir,%_logdir}/%name
%cmakeinstall_std

%buildroot%_bindir/%name --create-config --home %_localstatedir/%name > %buildroot%_sysconfdir/%name/config.xml

mkdir -p %buildroot%_logrotatedir
cat > %buildroot%_logrotatedir/%name << 'EOF'
/var/log/gerbera/gerbera {
      monthly
      missingok
      create 0644 gerbera gerbera
      notifempty
      compress
}
EOF

touch %buildroot%_localstatedir/%name/{%name.db,%name.html}

%pre
groupadd -r -f %name >/dev/null 2>&1 ||:
useradd -r -n -g %name -d %_localstatedir/%name -s /dev/null \
    -c 'Gerbera UPnP Media Server' %name >/dev/null 2>&1 ||:

%post
%post_service %name

%preun
%preun_service  %name

%files
%doc LICENSE.md AUTHORS CONTRIBUTING.md ChangeLog.md
%doc doc/*.rst
%dir %attr(750,root,%name) %_sysconfdir/%name
%config(noreplace) %attr(750,root,%name) %_sysconfdir/%name/config.xml
%attr(750,%name,adm) %_logdir/%name
%config(noreplace) %_logrotatedir/%name
%_bindir/%name
%_man1dir/*
%_unitdir/%name.service
%attr(3770,root,%name) %dir %_localstatedir/%name
%ghost %attr(775,%name,%name) %_localstatedir/%name/%name.db
%ghost %attr(775,%name,%name) %_localstatedir/%name/%name.html


%files data
%_datadir/%name
%config(noreplace) %_datadir/%name/js/import.js
%config(noreplace) %_datadir/%name/js/playlists.js
%config(noreplace) %_datadir/%name/js/common.js

%changelog
* Sun May 24 2020 Alexey Shabalin <shaba@altlinux.org> 1.5.0-alt1
- Initial build.

