Name: nagios-plugins-check_monit
Version: 1.4
Release: alt1

Summary: Nagios(R) plug-in for checking monit status
License: GPL
Group: Monitoring

Url: https://code.google.com/p/nagios-monit-plugin/

Source: %name-%version.tar

BuildArchitectures: noarch

Requires: nagios-nrpe

# nagios uses /usr/lib for plugins in any arch
%define pluginsdir %_prefix/lib/nagios/plugins

%description
Nagios plugin for checking all monit services,
all warnings and "unmonitored" states are shown.

%prep
%setup

sed -i 's|#!/usr/bin/env python|#!/usr/bin/env python3|' \
$(find ./ -name '*.py')

%install
mkdir -p %buildroot%pluginsdir/
install -m755 check_monit.py %buildroot%pluginsdir/

%files
%pluginsdir/check_monit.py
%doc README check_monit.cfg

%changelog
* Mon Oct 21 2019 Andrey Bychkov <mrdrew@altlinux.org> 1.4-alt1
- Version updated to 1.4
- python2 -> python3

* Thu Feb 12 2015 Vitaly Lipatov <lav@altlinux.ru> 1.3-alt1
- the plugin updated to fit to new monit versions (5.8.1+)

* Mon Oct 14 2013 Vitaly Lipatov <lav@altlinux.ru> 1.0-alt2
- cleanup spec

* Mon Oct 14 2013 Anton Agapov <anton@etersoft.ru> 1.0-alt1
- initial build for ALT Linux Sisyphus
