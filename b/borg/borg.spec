Name: borg
Version: 1.1.13
Release: alt2

Summary: Deduplicating backup program with compression and authenticated encryption

License: BSD-3-Clause
Group: File tools
Url: https://borgbackup.github.io/borgbackup/

# Source-url: https://github.com/borgbackup/borg/archive/%version.tar.gz
Source: %name-%version.tar
Patch1: borg-unbundle-xxhash-1.1.10.patch

BuildRequires(pre): rpm-build-python3

BuildRequires: gcc-c++
BuildRequires: libacl-devel ipython3 python3-module-Cython libssl-devel python3-dev
BuildRequires: python3-module-setuptools_scm
BuildRequires: liblz4-devel libzstd-devel libb2-devel libxxhash-devel

#Requires: python3-module-msgpack >= 0.4.6
Requires: python3-module-zmq

%description
BorgBackup (short: Borg) is a deduplicating backup program.
Optionally, it supports compression and authenticated encryption.

The main goal of Borg is to provide an efficient and secure way to backup data.
The data deduplication technique used makes Borg suitable for daily backups
since only changes are stored.

The authenticated encryption technique makes it suitable for backups to not
fully trusted targets.

%prep
%setup
%patch1 -p1
rm -rfv src/borg/algorithms/{lz4,xxh64,zstd,blake2}/
# TODO: remove with the patch after 1.2.0
%__subst "s|xxh64/xxhash.c|xxhash.h|" src/borg/algorithms/checksums.pyx

%build
export SETUPTOOLS_SCM_PRETEND_VERSION=%version
%python3_build

%install
export SETUPTOOLS_SCM_PRETEND_VERSION=%version
%python3_install
rm -rfv %buildroot%python3_sitelibdir/borg/testsuite/

%files
%doc LICENSE AUTHORS CHANGES.rst README.rst
%_bindir/borg
%_bindir/borgfs
%python3_sitelibdir/borg/
%python3_sitelibdir/borgbackup-*.egg-info/

%changelog
* Fri Oct 30 2020 Vitaly Lipatov <lav@altlinux.ru> 1.1.13-alt2
- NMU: don't pack testsuite

* Thu Jun 11 2020 Dmitriy D. Shadrinov <shadrinov@altlinux.org> 1.1.13-alt1
- 1.1.13 release

* Fri Mar 27 2020 Dmitriy D. Shadrinov <shadrinov@altlinux.org> 1.1.11-alt1
- update version to 1.1.11

* Sun Oct 20 2019 Vitaly Lipatov <lav@altlinux.ru> 1.1.10-alt2
- remove source code of the bundled libraries
- build with external blake2
- build with external xxhash (ALT bug 36408)

* Wed Jun 05 2019 Vitaly Lipatov <lav@altlinux.ru> 1.1.10-alt1
- borgbackup 1.1.10 bug fix release (now bundling msgpack)
- gcc-c++ used

* Sun Mar 31 2019 Dmitriy D. Shadrinov <shadrinov@altlinux.org> 1.1.9-alt2
- rebuilder with external libzstd

* Sun Feb 24 2019 Dmitriy D. Shadrinov <shadrinov@altlinux.org> 1.1.9-alt1
- update version to 1.1.9

* Tue Dec 25 2018 Dmitriy D. Shadrinov <shadrinov@altlinux.org> 1.1.8-alt1
- update version to 1.1.8

* Wed Aug 29 2018 Grigory Ustinov <grenka@altlinux.org> 1.1.7-alt1.1
- NMU: Rebuild with new openssl 1.1.0.

* Tue Aug 14 2018 Dmitriy D. Shadrinov <shadrinov@altlinux.org> 1.1.7-alt1
- update version to 1.1.7

* Thu Jun 14 2018 Dmitriy D. Shadrinov <shadrinov@altlinux.org> 1.1.6-alt1
- update version to 1.1.6

* Mon May 21 2018 Dmitriy D. Shadrinov <shadrinov@altlinux.org> 1.1.5-alt1
- update version to 1.1.5

* Thu Mar 22 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 1.1.4-alt1.1
- (NMU) Rebuilt with python-3.6.4.

* Fri Jan 12 2018 Dmitriy D. Shadrinov <shadrinov@altlinux.org> 1.1.4-alt1
- update version to 1.1.4

* Thu Dec 07 2017 Dmitriy D. Shadrinov <shadrinov@altlinux.org> 1.1.3-alt1
- update version to 1.1.3

* Fri Nov 17 2017 Dmitriy D. Shadrinov <shadrinov@altlinux.org> 1.1.2-alt1
- update version to 1.1.2

* Mon Oct 30 2017 Dmitriy D. Shadrinov <shadrinov@altlinux.org> 1.1.1-alt1
- update version to 1.1.1

* Sat Oct 14 2017 Dmitriy D. Shadrinov <shadrinov@altlinux.org> 1.1.0-alt2
- update version to 1.1.0

* Tue Oct 03 2017 Dmitriy D. Shadrinov <shadrinov@altlinux.org> 1.1.0-alt1.rc4
- update version to 1.1.0rc4

* Tue Sep 19 2017 Dmitriy D. Shadrinov <shadrinov@altlinux.org> 1.1.0-alt1.rc3
- update version to 1.1.0rc3

* Mon Aug 28 2017 Dmitriy D. Shadrinov <shadrinov@altlinux.org> 1.1.0-alt1.rc2
- update version to 1.1.0rc2

* Tue Aug 15 2017 Dmitriy D. Shadrinov <shadrinov@altlinux.org> 1.1.0-alt1.rc1
- update version to 1.1.0rc1

* Fri Aug 05 2016 Vitaly Lipatov <lav@altlinux.ru> 1.0.6-alt1
- new version 1.0.6 (with rpmrb script)

* Tue Jul 26 2016 Vitaly Lipatov <lav@altlinux.ru> 1.0.5-alt1
- new version 1.0.5 (with rpmrb script)

* Thu Mar 17 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.24.0-alt1.1
- (NMU) rebuild with python3-3.5 & rpm-build-python3-0.1.10
  (for ABI dependence and new python3(*) reqs)

* Fri Aug 14 2015 Vitaly Lipatov <lav@altlinux.ru> 0.24.0-alt1
- initial build for ALT Linux Sisyphus
