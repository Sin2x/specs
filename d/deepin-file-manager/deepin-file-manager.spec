%define repo dde-file-manager

%def_disable clang

Name: deepin-file-manager
Version: 5.2.0.69
Release: alt1
Summary: Deepin File Manager
License: GPL-3.0+
Group: Graphical desktop/Other
Url: https://github.com/linuxdeepin/dde-file-manager
Packager: Leontiy Volodin <lvol@altlinux.org>

Source: %url/archive/%version/%repo-%version.tar.gz
Patch: deepin-file-manager_5.2.0.69_alt_fix-build.patch

ExcludeArch: armh

%if_enabled clang
BuildRequires(pre): clang11.0-devel
%else
%set_gcc_version 7
BuildRequires(pre): gcc7-c++
%endif

BuildRequires(pre): rpm-build-kf5
BuildRequires: git-core desktop-file-utils deepin-gettext-tools deepin-dock-devel libmagic-devel libjemalloc-devel kf5-kcodecs-devel libatk-devel dtk5-widget-devel dtk5-gui-devel deepin-qt-dbus-factory-devel libgtk+2-devel gsettings-qt-devel libsecret-devel libpoppler-cpp-devel libpolkit-devel libpolkitqt5-qt5-devel qt5-base-devel qt5-svg-devel qt5-multimedia-devel qt5-x11extras-devel libtag-devel libuchardet-devel libxcbutil-devel libxcbutil-icccm-devel qt5-linguist udisks2-qt5-devel disomaster-devel qt5-tools libgio-qt-devel libssl-devel libqtxdg-devel libmediainfo-devel libpcre-devel libffmpegthumbnailer-devel libdmr-devel deepin-anything-devel liblucene++-devel libxml2-devel libhtmlcxx-devel libgsf-devel libmimetic-devel

# run command by QProcess
# Requires: deepin-shortcut-viewer deepin-terminal deepin-desktop file-roller gvfs samba xdg-user-dirs gst-plugins-good1.0-qt5
#Recommends:     deepin-manual
# dde-file-manager-lib/configure/global-setting-template-{fedora,pro,js}.js:2:13: error: Expected token `,'

%description
File manager front end of Deepin OS.

%package devel
Summary: Development package for %name
Group: Graphical desktop/Other

%description devel
Header files and libraries for %name.

%package -n deepin-desktop
Summary: Deepin desktop environment - desktop module
Group: Graphical desktop/Other
# Requires: deepin-dock deepin-launcher deepin-session-shell

%description -n deepin-desktop
Deepin desktop environment - desktop module.

%prep
%setup -n %repo-%version
# %%patch -p2

sed -i 's|lrelease|lrelease-qt5|' dde-desktop/translate_generation.sh
sed -i 's|lrelease|lrelease-qt5|' dde-file-manager-lib/generate_translations.sh
sed -i 's|lrelease|lrelease-qt5|' dde-file-manager/generate_translations.sh
sed -i 's|lrelease|lrelease-qt5|' dde-file-manager-plugins/generate_translations.sh
sed -i 's|lupdate|lupdate-qt5|' dde-file-manager-lib/update_translations.sh
sed -i 's|lupdate|lupdate-qt5|' dde-file-manager-plugins/update_translations.sh

# sed -i 's|"groups":|"groups"\ :|' dde-file-manager-lib/configure/global-setting-template*.js

# fix file permissions
find -type f -perm 775 -exec chmod 644 {} \;
sed -i '/deepin-daemon/s|lib|libexec|' dde-zone/mainwindow.h
sed -i 's|lib/gvfs|libexec/gvfs|' %repo-lib/gvfs/networkmanager.cpp
sed -i 's|/lib/dde-dock/plugins|/lib64/dde-dock/plugins|' dde-dock-plugins/disk-mount/disk-mount.pro

#sed -i 's|systembusconf.path = /etc/dbus-1/system.d|systembusconf.path = /usr/share/dbus-1/system.d|' dde-file-manager-daemon/dde-file-manager-daemon.pro
sed -i 's|/usr/lib/systemd/system|%_unitdir|' dde-file-manager-daemon/dde-file-manager-daemon.pro

sed -i 's|-lKF5Codecs|%_K5link/libKF5Codecs.so|' dde-file-manager/dde-file-manager.pro dde-file-manager-lib/dde-file-manager-lib.pro dde-file-manager-daemon/dde-file-manager-daemon.pro

%build
# %%add_optflags -L%%_K5link -lKF5Codecs

%qmake_qt5 \
           CONFIG+=nostrip \
           unix:LIBS+="-L%_K5link -lKF5Codecs" \
           QT.KCodecs.libs=%_K5link \
           PREFIX=%prefix \
           DTK_VERSION=%version \
           LIB_INSTALL_DIR=%_libdir \
%if_enabled clang
           QMAKE_STRIP= -spec linux-clang \
%endif
           filemanager.pro

%make_build

%install
%makeinstall INSTALL_ROOT=%buildroot

# %%check
# desktop-file-validate %%buildroot%%_desktopdir/%%repo.desktop
# desktop-file-validate %%buildroot%%_desktopdir/dde-computer.desktop ||:
# desktop-file-validate %%buildroot%%_desktopdir/dde-trash.desktop ||:

%files
%doc README.md LICENSE
%_bindir/%repo
%_bindir/%repo-daemon
%_bindir/%repo-pkexec
%_bindir/dde-property-dialog
%_libdir/lib%repo.so.*
%dir %_libdir/%repo/
%dir %_libdir/%repo/tools/
%dir %_libdir/%repo/tools/thumbnail/
%_libdir/%repo/tools/thumbnail/video*
%_datadir/%repo/
%_iconsdir/hicolor/scalable/apps/*.svg
%_desktopdir/%repo.desktop
%_datadir/dbus-1/interfaces/com.deepin.filemanager.filedialog.xml
%_datadir/dbus-1/interfaces/com.deepin.filemanager.filedialogmanager.xml
%_datadir/glib-2.0/schemas/com.deepin.dde.dock.module.disk-mount.gschema.xml
%_datadir/glib-2.0/schemas/com.deepin.dde.filemanager.gschema.xml
%_datadir/dbus-1/services/com.deepin.filemanager.filedialog.service
%_datadir/dbus-1/services/org.freedesktop.FileManager.service
%_datadir/dbus-1/system-services/com.deepin.filemanager.daemon.service
%config(noreplace) %_sysconfdir/dbus-1/system.d/com.deepin.filemanager.daemon.conf
%_unitdir/dde-filemanager-daemon.service
%dir %_datadir/deepin/
%_datadir/deepin/%repo/
%_datadir/polkit-1/actions/com.deepin.filemanager.daemon.policy
%_datadir/polkit-1/actions/com.deepin.pkexec.dde-file-manager.policy
%ifnarch aarch64 ppc64le
%dir %_libdir/deepin-anything-server-lib/
%dir %_libdir/deepin-anything-server-lib/plugins/
%dir %_libdir/deepin-anything-server-lib/plugins/handlers/
%_libdir/deepin-anything-server-lib/plugins/handlers/libdde-anythingmonitor.so
%endif
%ifnarch i586
%dir %_libdir/dde-dock/
%dir %_libdir/dde-dock/plugins/
%dir %_libdir/dde-dock/plugins/system-trays/
%_libdir/dde-dock/plugins/system-trays/libdde-disk-mount-plugin.so
%endif
%dir %_libdir/%repo/plugins/
%dir %_libdir/%repo/plugins/previews/
%_libdir/%repo/plugins/previews/*.so
# Bad elfs detected.
%exclude %_libdir/%repo/plugins/previews/libdde-music-preview-plugin.so

%files devel
%_includedir/%repo/
%_pkgconfigdir/%repo.pc
%_libdir/lib%repo.so

%files -n deepin-desktop
%_bindir/dde-desktop
%_desktopdir/dde-computer.desktop
%_desktopdir/dde-trash.desktop
%_desktopdir/dde-home.desktop
%_desktopdir/dde-open.desktop
%dir %_datadir/dde-desktop
%_datadir/dde-desktop/translations/
%dir %_datadir/dde-disk-mount-plugin
%_datadir/dde-disk-mount-plugin/translations/
%_datadir/dbus-1/services/com.deepin.dde.desktop.service

%changelog
* Mon Nov 02 2020 Leontiy Volodin <lvol@altlinux.org> 5.2.0.69-alt1
- New version (5.2.0.69) with rpmgs script.

* Mon Oct 12 2020 Leontiy Volodin <lvol@altlinux.org> 5.2.0.61-alt1
- New version (5.2.0.61) with rpmgs script.
- Removed requires.

* Mon Oct 05 2020 Leontiy Volodin <lvol@altlinux.org> 5.2.0.59-alt1
- New version (5.2.0.59) with rpmgs script.

* Mon Sep 14 2020 Leontiy Volodin <lvol@altlinux.org> 5.2.0.45-alt1
- Initial build for ALT Sisyphus (thanks fedora for this spec).
