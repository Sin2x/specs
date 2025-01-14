%define _unpackaged_files_terminate_build 1

Name:       puppetserver
Version:    6.20.0
Release:    alt1
Summary:    Server automation framework and application
License:    Apache-2.0
Group:      Other
Url:        https://github.com/puppetlabs/puppetserver

BuildArch: noarch

Source: %name-%version.tar

Source1: puppetserver.init
Source2: jruby-1_7.jar
Source3: jruby-9k.jar

Patch1: puppetserver-6.13.0-alt.patch

BuildPreReq: /proc
BuildPreReq: rpm-build-java
BuildPreReq: rpm-macros-ruby /usr/bin/ruby

Requires: clojure
Requires: puppet
Requires: puppetserver-ca
Requires: gem-multi-json
Requires: gem-deep-merge
Requires: gem-text
Requires: gem-locale
Requires: gem-fast-gettext
Requires: gem-gettext
Requires: gem-semantic-puppet
Requires: gem-concurrent-ruby >= 1.1.6-alt1.1

%description
Puppet Server is the next-generation application for managing Puppet agents.
This platform implements Puppet's server-side components in a more distributed,
service-oriented architecture. We've built Puppet Server on top of the same
technologies that make PuppetDB successful, and which allow us to greatly
improve performance, scalability, advanced metrics collection, and fine-grained
control over the Ruby runtime.

%prep
%setup
%patch1 -p2
sed "s|gem-path: \\[.*\\]|gem-path: [$(echo $(ls /usr/lib/ruby/gems | \
   sed -e "s,^,/usr/lib/ruby/gems/,") | sed "s/ \\+/, /")]|" \
   -i ext/config/conf.d/puppetserver.conf
subst 's|/var/log/puppetlabs|/var/log|' $(find -name '*.xml')
sed '/name.*environments/a \
        }, \
        { \
            match-request: { \
                path: "/puppet/v3/environment_classes" \
                type: path \
                method: get \
            } \
            allow: "*" \
            sort-order: 500 \
            name: "puppetlabs environment_classes"' \
      -i ext/config/conf.d/auth.conf


%install
install -d -m 0755 %buildroot%_datadir/%name
install -d -m 0770 %buildroot%_localstatedir/%name
install -m 0644 puppet-server-release.jar %buildroot%_datadir/%name
install -m 0755 ext/ezbake-functions.sh %buildroot%_datadir/%name
install -m 0644 ext/ezbake.manifest %buildroot%_datadir/%name
install -d -m 0755 %buildroot%_sysconfdir/%name
install -d -m 0755 %buildroot%_sysconfdir/%name/conf.d

install -m 0644 %SOURCE2 %buildroot%_datadir/%name
install -m 0644 %SOURCE3 %buildroot%_datadir/%name
  
install -d -m 0755 %buildroot%_sysconfdir/%name/services.d

install -m 0644 ext/system-config/services.d/bootstrap.cfg %buildroot%_sysconfdir/%name/bootstrap.cfg
    
install -m 0644 ext/config/conf.d/puppetserver.conf %buildroot%_sysconfdir/%name/conf.d/puppetserver.conf
install -m 0644 ext/config/request-logging.xml %buildroot%_sysconfdir/%name/request-logging.xml
install -m 0644 ext/config/logback.xml %buildroot%_sysconfdir/%name/logback.xml
install -m 0644 ext/config/conf.d/global.conf %buildroot%_sysconfdir/%name/conf.d/global.conf
install -m 0644 ext/config/conf.d/web-routes.conf %buildroot%_sysconfdir/%name/conf.d/web-routes.conf
install -m 0644 ext/config/conf.d/auth.conf %buildroot%_sysconfdir/%name/conf.d/auth.conf
install -m 0644 ext/config/conf.d/metrics.conf %buildroot%_sysconfdir/%name/conf.d/metrics.conf
install -m 0644 ext/config/conf.d/webserver.conf %buildroot%_sysconfdir/%name/conf.d/webserver.conf
install -m 0644 ext/config/services.d/ca.cfg %buildroot%_sysconfdir/%name/services.d/ca.cfg

install -d -m 0755 %buildroot%_datadir/%name/cli
install -d -m 0755 %buildroot%_datadir/%name/cli/apps
install -d -m 0755 %buildroot%_bindir
install -m 0755 ext/bin/puppetserver %buildroot%_bindir/%name
install -m 0755 ext/cli/reload %buildroot%_datadir/%name/cli/apps/reload
install -m 0755 ext/cli/stop %buildroot%_datadir/%name/cli/apps/stop
install -m 0755 ext/cli/gem %buildroot%_datadir/%name/cli/apps/gem
install -m 0755 ext/cli/irb %buildroot%_datadir/%name/cli/apps/irb
install -m 0755 ext/cli/foreground %buildroot%_datadir/%name/cli/apps/foreground
install -m 0755 ext/cli/ruby %buildroot%_datadir/%name/cli/apps/ruby
install -m 0755 ext/cli/start %buildroot%_datadir/%name/cli/apps/start
install -m 0755 ext/cli/ca %buildroot%_datadir/%name/cli/apps/ca

install -m 0755 ext/cli_defaults/cli-defaults.sh %buildroot%_datadir/%name/cli/

install -d -m 0755 %buildroot%_var/run/%name
install -d -m 0700 %buildroot%_var/log/%name
install -d -m 0700 %buildroot%_localstatedir/%name/jars

install -d -m 0755 %buildroot%_sysconfdir/default
install -m 0644 ext/default %buildroot%_sysconfdir/default/%name

install -d -m 0755 %buildroot%_sysconfdir/init.d
install -m 0755 %SOURCE1 %buildroot%_sysconfdir/init.d/%name

mkdir -p %buildroot%_tmpfilesdir
install -m 0644 ext/puppetserver.tmpfiles.conf %buildroot%_tmpfilesdir/

mkdir -p %buildroot%_sysconfdir/logrotate.d
install -m 0644 ext/puppetserver.logrotate.conf %buildroot%_sysconfdir/logrotate.d/

%pre
getent group puppet > /dev/null || \
	groupadd -r puppet || :
	if getent passwd puppet > /dev/null; then
		usermod --gid puppet --home "/var/lib/puppetserver" \
		--comment "puppetserver daemon" puppet || :
	else
		useradd -r --gid puppet --home "/var/lib/puppetserver" --shell $(which nologin) \
		--comment "puppetserver daemon"  puppet || :
	fi

%post
install --directory %_sysconfdir/puppet/ssl
install --directory %_sysconfdir/puppet/code

chown -R puppet:puppet %_sysconfdir/puppet/ssl
chown -R puppet:puppet %_sysconfdir/puppet/code

find %_sysconfdir/puppet/ssl -type d -print0 | xargs -0 chmod 0770
find %_sysconfdir/puppet/code -type d -print0 | xargs -0 chmod 0770

chown puppet:puppet /var/log/puppetserver
chmod 0700 /var/log/puppetserver
chown puppet:puppet /var/lib/puppetserver
chmod 0770 /var/lib/puppetserver
chown puppet:puppet /etc/puppetserver
chmod 0750 /etc/puppetserver
chown puppet:puppet /var/run/puppetserver
chmod 0755 /var/run/puppetserver
chown puppet:puppet /var/lib/puppetserver/jars
chmod 0700 /var/lib/puppetserver/jars

if [ -d /var/log/puppetlabs/puppetserver ]; then
   find /var/log/puppetlabs/puppetserver/ -name \*.log | while read -r f; do sed "s|/var/log/puppetlabs|/var/log|" -i "$f"; done
   mv -f /var/log/puppetlabs/puppetserver/* /var/log/puppetserver
   rm -rf /var/log/puppetlabs/puppetserver
fi

%files
%_datadir/%name
%config(noreplace) %_sysconfdir/%name
%_var/log/%name
%_var/lib/%name
%_var/run/%name
%_bindir/%name
%_sysconfdir/logrotate.d/*
%_tmpfilesdir/*
%_sysconfdir/init.d/%name
%_sysconfdir/default/%name

%changelog
* Wed Sep 21 2022 Pavel Skrylev <majioa@altlinux.org> 6.20.0-alt1
- ^ 6.13.0 -> 6.20.0
- - remove conflict to gem-oj
- ! fix alt patch to conform ruby new style

* Tue Feb 09 2021 Pavel Skrylev <majioa@altlinux.org> 6.13.0-alt3.1
- ! keeping sysconfig data from an old releases

* Wed Dec 23 2020 Pavel Skrylev <majioa@altlinux.org> 6.13.0-alt3
- + environment_classes to ''auth.conf''
- + replacings for the log folder, removing puppetlabs from it

* Tue Nov 10 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 6.13.0-alt2
- Updated dependencies for p9 compatibility.

* Fri Nov 06 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 6.13.0-alt1
- Updated to upstream version 6.13.0 (Fixes: CVE-2020-7943).

* Fri May 22 2020 Pavel Skrylev <majioa@altlinux.org> 6.5.0-alt3
- ! max memory consumption for JVM by increasing top border an config
  (closes #38519)

* Wed May 13 2020 Pavel Skrylev <majioa@altlinux.org> 6.5.0-alt2.1
- + explicit require dependencies to proper gem packages

* Tue May 12 2020 Pavel Skrylev <majioa@altlinux.org> 6.5.0-alt2
- ! gem paths config

* Mon Aug 26 2019 Andrey Bychkov <mrdrew@altlinux.org> 6.5.0-alt1
- Version updated to 6.5.0

* Sat Jul 06 2019 Igor Vlasenko <viy@altlinux.ru> 6.3.0-alt3
- NMU: remove rpm-build-ubt from BR:

* Tue May 14 2019 Andrey Bychkov <mrdrew@altlinux.org> 6.3.0-alt2
- puppetserver config path fixed

* Wed May 08 2019 Andrey Bychkov <mrdrew@altlinux.org> 6.3.0-alt1
- Version updated to 6.3.0

* Fri Mar 01 2019 Andrey Bychkov <mrdrew@altlinux.org> 6.2.1-alt1
- Version updated to 6.2.1

* Tue Dec 25 2018 Andrey Bychkov <mrdrew@altlinux.org> 6.1.0-alt1
- version updated to 6.1.0

* Fri Dec 07 2018 Andrey Bychkov <mrdrew@altlinux.org> 6.0.2-alt3
- requires fixed

* Fri Nov 30 2018 Andrey Bychkov <mrdrew@altlinux.org> 6.0.2-alt2
- puppetserver ca added

* Mon Nov 19 2018 Andrey Bychkov <mrdrew@altlinux.org> 6.0.2-alt1
- version updated to 6.0.2

* Sun Oct 14 2018 Igor Vlasenko <viy@altlinux.ru> 6.0.0-alt1.qa1%ubt
- NMU: applied repocop patch

* Fri Sep 21 2018 Andrey Bychkov <mrdrew@altlinux.org> 6.0.0-alt1%ubt
- updated version to 6.0.0 from src

* Wed Sep 12 2018 Andrey Bychkov <mrdrew@altlinux.org> 5.3.5-alt2%ubt
- chown puppet/ssl for foreground

* Mon Aug 09 2018 Andrey Bychkov <mrdrew@altlinux.org> 5.3.5-alt1%ubt
- Update version to 5.3.5

* Thu Aug 02 2018 Andrey Bychkov <mrdrew@altlinux.org> 5.3.4-alt1%ubt
- Initial build in Sisyphus

