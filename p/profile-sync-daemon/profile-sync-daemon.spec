Name: profile-sync-daemon
Version: 6.40
Release: alt1
Summary: Offload browser profiles to RAM for speed a wear reduction
Summary(ru_RU.UTF-8): Выгружает профиль браузера в ОЗУ для ускорения его работы
License: MIT
Group: Networking/WWW
Url: https://github.com/graysky2/profile-sync-daemon
Packager: Anton Midyukov <antohami@altlinux.org>

Source: %name-%version.tar

BuildArch: noarch
%add_findreq_skiplist %_bindir/%name

%description
Profile-sync-daemon (psd) is a tiny pseudo-daemon designed to manage your
browser's profile in tmpfs and to periodically sync it back to your physical
disc (HDD/SSD). This is accomplished via a symlinking step and an innovative
use of rsync to maintain back-up and synchronization between the two. One of
the major design goals of psd is a completely transparent user experience.

To automatically start psd, use the command:
systemctl --user enable psd psd-resync.timer && systemctl --user start psd psd-resync.timer

%description -l ru_RU.UTF-8
Profile-sync-daemon (psd) представляет собой псевдо-демон, управляющий вашим
профилем браузера в tmpfs и периодически синхронизирующий его для восстановления
на вашем физическом диске (HDD/SSD). Это достигается с помощью создания
символических ссылок и инновационного использованию Rsync для резервного
копирования и синхронизации. Поддерживается большинство современных браузеров.

Для автоматического запуска psd, используйте команду:
systemctl --user enable psd psd-resync.timer && systemctl --user start psd psd-resync.timer

%prep
%setup

sed -i '/Wants=psd-resync.service/d' init/psd.service
sed -i '/\[Timer\]/a OnStartupSec=10s' init/psd-resync.timer

cat>>init/psd-resync.timer<<END

[Install]
WantedBy=timers.target
END

%build
%make_build

%install
%makeinstall_std

%post
echo 'To automatically start psd, use the command:'
echo 'systemctl --user enable psd psd-resync.timer && systemctl --user start psd psd-resync.timer'

%files
%doc README*
%doc MIT
%_datadir/psd
%_bindir/*
%dir %_datadir/zsh
%dir %_datadir/zsh/site-functions/
%_datadir/zsh/site-functions/_psd
%_man1dir/*.1*
%_libexecdir/systemd/user/psd*.*

%changelog
* Thu May 07 2020 Anton Midyukov <antohami@altlinux.org> 6.40-alt1
- new version 6.40

* Sun Apr 19 2020 Cronbuild Service <cronbuild@altlinux.org> 6.37-alt1
- new version 6.37

* Sun Feb 23 2020 Cronbuild Service <cronbuild@altlinux.org> 6.36-alt1
- new version 6.36

* Mon Sep 16 2019 Cronbuild Service <cronbuild@altlinux.org> 6.35-alt1
- new version 6.35

* Sun Dec 23 2018 Cronbuild Service <cronbuild@altlinux.org> 6.34-alt1
- new version 6.34

* Mon Apr 23 2018 Anton Midyukov <antohami@altlinux.org> 6.33-alt2
- fix bash syntax error (Closes: 33902)

* Sun Mar 04 2018 Cronbuild Service <cronbuild@altlinux.org> 6.33-alt1
- new version 6.33

* Sat Feb 18 2017 Anton Midyukov <antohami@altlinux.org> 6.30-alt2
- fix unit file

* Tue Jan 31 2017 Anton Midyukov <antohami@altlinux.org> 6.30-alt1
- new version 6.30

* Mon Oct 10 2016 Cronbuild Service <cronbuild@altlinux.org> 6.28-alt1
- new version 6.28

* Sun Oct 09 2016 Anton Midyukov <antohami@altlinux.org> 6.27-alt1
- new version 6.27

* Mon Oct 03 2016 Cronbuild Service <cronbuild@altlinux.org> 6.26-alt1
- new version 6.26

* Mon Sep 05 2016 Anton Midyukov <antohami@altlinux.org> 6.25-alt1
- new version 6.25
- fix unit files.

* Mon Aug 22 2016 Anton Midyukov <antohami@altlinux.org> 6.22-alt1
- new version 6.22
- added the ability to build using Cronbuild

* Sat May 14 2016 Anton Midyukov <antohami@altlinux.org> 6.21-alt1
- Initial build for ALT Linux Sisyphus
