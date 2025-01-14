%define _unpackaged_files_terminate_build 1

Name: i3lock
Version: 2.13
Release: alt1

Summary: improved screen locker (for X-session)
License: BSD
Group: Graphical desktop/Other

URL: http://i3wm.org/i3lock/
Source: %name-%version.tar
Patch0: i3lock-pam-fixes.patch

BuildRequires: libev-devel, libxcbutil-image-devel, libxcbutil-devel, libxcbutil-xrm-devel, libxkbcommon-x11-devel, libcairo-devel, libpam0-devel

%description
i3lock is a simple screen locker like slock.
After starting it, you will see a white screen
(you can configure the color/an image).
You can return to your screen by entering your password.
i3lock forks so you can combine it with an alias to suspend to RAM.
You can specify whether i3lock should bell upon a wrong password.
i3lock uses PAM and therefore is compatible with LDAP etc.

%description -l ru_RU.UTF-8
i3lock - это простой блокировщик экрана, например, как slock.
После запуска Вы увидите белый экран (но Вы можете настроить цвет/изображение).
Чтобы вернуться к своему рабочему пространству, введите пароль.

%prep
%setup
%patch0 -p1
%autoreconf

%build
%configure  --sysconfdir=%_sysconfdir --disable-sanitizers

%make_build -C *-alt-linux-gnu*

%install
%make install -C *-alt-linux-gnu* DESTDIR=%buildroot


%files
%_man1dir/i3lock.*
%doc README.md
%attr(2711, root, shadow) %_bindir/i3lock
%_sysconfdir/pam.d/*

%changelog
* Thu Jun 02 2022 Daniel Zagaynov <kotopesutility@altlinux.org> 2.13-alt1
- Initial release for Sisyphus.
