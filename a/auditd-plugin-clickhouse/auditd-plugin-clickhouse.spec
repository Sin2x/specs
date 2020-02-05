%define _unpackaged_files_terminate_build 1

# Recommended versioning scheme for this package:
# 1. If no sources are changed, just increase release.
# 2. If sources are changed, use current date as version in format YYYYMMDD,
#    and increase release for all subsequent versions made on same day.

Name:    auditd-plugin-clickhouse
Version: 20200127
Release: alt1
Summary: Plugin for Auditd daemon for sending data into Clickhouse database
Group:   Monitoring
License: GPLv3+

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-cmake
BuildRequires: gcc-c++ cmake
BuildRequires: boost-complete
BuildRequires: libclickhouse-cpp-devel
BuildRequires: libaudit-devel
BuildRequires: /usr/bin/ctest libgtest-devel

%description
Plugin for Auditd daemon for sending data into Clickhouse database

%prep
%setup

%build
%cmake
%cmake_build

%install
%cmakeinstall_std

mkdir -pv %buildroot%_localstatedir/auditd-plugin-clickhouse

%check
pushd BUILD
ctest
popd

%files
%config(noreplace) %_sysconfdir/audisp/auditd-clickhouse-datatypes.json
%config(noreplace) %_sysconfdir/audisp/auditd-clickhouse.conf
%config(noreplace) %_sysconfdir/audisp/plugins.d/auditd-plugin-clickhouse.conf
%config(noreplace) %_sysconfdir/logrotate.d/auditd-plugin-clickhouse-logrotate.conf
%_prefix/libexec/auditd-plugin-clickhouse
%attr(700,root,root) %_localstatedir/auditd-plugin-clickhouse

%changelog
* Mon Jan 27 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 20200127-alt1
- Fixed excessive logging of writes.
- Fixed memory consumption by logging entries if logging is disabled.
- Fixed memory leak in audit data parsing.
- Fixed issue when some data may be not attempted to be written to DB
  when separate writer thread is used.
- Improved performance by reducing data copying.
- Input data buffer size configuration is removed.

* Thu Jan 16 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 20200116-alt1
- New fields added to database table.
- All unknown fields encountered are saved into database.
- Fixed crash when processing NULL strings.
- Fixed warnings for some audit data types.
- Implemented logging.
- Implemented audit data serialization and temporary storing before sending
  to database.

* Tue Dec 17 2019 Aleksei Nikiforov <darktemplar@altlinux.org> 20191217-alt1
- Initial build for ALT
