# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl rpm-build-python3 rpm-build-ruby
BuildRequires: /usr/bin/pcre-config /usr/bin/perl libruby-devel perl(DynaLoader.pm) perl(Exporter.pm) perl(base.pm) perl(overload.pm) perl-podlators
# END SourceDeps(oneline)
BuildRequires: libltdl7-devel
Group: System/Libraries
%add_optflags %optflags_shared
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%global major                   28
%global cppmajor                12

# Notes about rpmlint
# - crypto-policy-non-compliance-gnutls-{1,2} fixed with patch
#   libprelude-5.2.0-gnutls_priority_set_direct.patch

Name:           libprelude
Version:        5.2.0
Release:        alt1_3
Summary:        Secure Connections between all Sensors and the Prelude Manager
License:        LGPL-2.1+
URL:            https://www.prelude-siem.org/
Source0:        https://www.prelude-siem.org/pkg/src/5.2.0/%{name}-%{version}.tar.gz
# https://www.prelude-siem.org/issues/860
Patch0:         libprelude-5.2.0-ruby_vendorarchdir.patch
# https://www.prelude-siem.org/issues/862
Patch1:         libprelude-5.2.0-gnutls_priority_set_direct.patch
# https://www.prelude-siem.org/issues/863
Patch2:         libprelude-5.2.0-fsf_address.patch
# https://www.prelude-siem.org/issues/865
Patch3:         libprelude-5.2.0-fix_timegm.patch
# https://www.prelude-siem.org/issues/885
Patch4:         libprelude-5.2.0-fix_pthread_atfork.patch
# https://www.prelude-siem.org/issues/887
Patch5:         libprelude-5.2.0-fix_prelude_tests_timer.patch
Patch6:         libprelude-5.2.0-fix_gtkdoc_1.32.patch
Patch7:         libprelude-5.2.0-linking.patch
Patch8:         libprelude-5.2.0-fix_libprelude-error_on_gnu.patch
Patch9:         libprelude-5.2.0-disable_test-poll_on_kfreebsd.patch
Patch10:        libprelude-5.2.0-fix-test_rwlock1.patch
# https://github.com/swig/swig/issues/1689
# https://github.com/swig/swig/pull/1692
# For now, add a minimum patch to support ruby2.7
Patch11:        libprelude-5.2.0-ruby27.patch
# Remove unneded libraries from libprelude-config --libs (bz#1830473)
Patch12:        libprelude-5.2.0-clean_libprelude-config.patch
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  bison
BuildRequires:  chrpath
BuildRequires:  flex
BuildRequires:  gtk-doc gtk-doc-mkpdf
BuildRequires:  glib2-devel libgio libgio-devel
BuildRequires:  swig
BuildRequires:  libgpg-error-devel
BuildRequires:  libltdl7-devel
BuildRequires:  perl-devel
BuildRequires:  rpm-build-perl
BuildRequires:  python3-devel
BuildRequires:  pkgconfig(gnutls)
BuildRequires:  pkgconfig(lua) >= 5.2
BuildRequires:  pkgconfig(ruby)
BuildRequires:  pkgconfig(zlib)

%ifnarch s390 ppc64 ppc64le
BuildRequires:  valgrind
%endif

# Upstream do not use explicit version of gnulib, just checkout
# and update files. In libprelude 5.2.0, the checkout has been done
# on 2018-09-03
Provides:       bundled(gnulib) = 20180903
Source44: import.info
Patch33: libprelude-1.0.0-alt-extern-libltdl.patch

%description
Libprelude is a collection of generic functions providing communication
between all Sensors, like IDS (Intrusion Detection System), and the Prelude
Manager. It provides a convenient interface for sending and receiving IDMEF
(Information and Event Message Exchange Format) alerts to Prelude Manager with
transparent SSL, fail-over and replication support, asynchronous events and
timer interfaces, an abstracted configuration API (hooking at the command-line,
the configuration line, or wide configuration, available from the Manager), and
a generic plugin API. It allows you to easily turn your favorite security
program into a Prelude sensor.

%description -l ru_RU.UTF-8
Библиотека Prelude содержит коллекцию общих функций, обеспечивающих
коммуникацию между компонентами Prelude Hybrid IDS. Она обеспечивает
интерфейс для пересылки предупреждений менеджеру Prelude используя
SSL, отказоустойчивость и поддержку репликаций, асинхронные события и
интерфейсы таймера, абстрактный конфигурационный API и общий API для
дополнений. Это позволит вам легко интегрировать вашу программу
безопасности в датчик Prelude.

%description -l uk_UA.UTF-8
Бібліотека Prelude містить колекцію спільних функцій, що забезпечують
комунікацію між компонентами Prelude Hybrid IDS. Вона забезпечує
інтерфейс для надсилання попереджень менеджеру Prelude використовуючи
SSL, відмовостійкість і підтримку реплікацій, асинхронні події та
інтерфейси таймера, абстрактний конфігураційний API та загальний API
для доповнень. Це дозволить вам легко інтегрувати вашу програму
безпеки в датчик Prelude.

%package devel
Group: Development/C
Summary:        Libraries and headers for developing Prelude sensors
Requires:       %{name} = %{version}-%{release}
Requires:       pkgconfig(gnutls)
Provides:       prelude-devel = %{version}-%{release}

%description devel
Libraries and headers you can use to develop Prelude sensors using the Prelude
Library. Libprelude is a collection of generic functions providing
communication between all Sensors, like IDS (Intrusion Detection System),
and the Prelude Manager. It provides a convenient interface for sending and
receiving IDMEF (Information and Event Message Exchange Format) alerts to
Prelude Manager with transparent SSL, fail-over and replication support,
asynchronous events and timer interfaces, an abstracted configuration API
(hooking at the command-line, the configuration line, or wide configuration,
available from the Manager), and a generic plugin API. It allows you to easily
turn your favorite security program into a Prelude sensor.

%description -l ru_RU.UTF-8 devel
Библиотеки, заголовочные файлы и т.п вы можете использовать для
разработки датчиков Prelude IDS. Библиотека Prelude содержит коллекцию
общих функций, обеспечивающих коммуникацию между компонентами Prelude
Hybrid IDS. Она обеспечивает интерфейс для пересылки предупреждений
менеджеру Prelude используя SSL, отказоустойчивость и поддержку
репликаций, асинхронные события и интерфейсы таймера, абстрактный
конфигурационный API и общий API для дополнений. Это позволит вам
легко интегрировать вашу программу безопасности в датчик Prelude.

%description -l uk_UA.UTF-8 devel
Бібліотеки, файли заголовків і т.п ви можете використовувати для
розробки датчиків Prelude IDS. Бібліотека Prelude містить колекцію
спільних функцій, що забезпечують комунікацію між компонентами Prelude
Hybrid IDS. Вона забезпечує інтерфейс для надсилання попереджень
менеджеру Prelude використовуючи SSL, відмовостійкість і підтримку
реплікацій, асинхронні події та інтерфейси таймера, абстрактний
конфігураційний API та загальний API для доповнень. Це дозволить вам
легко інтегрувати вашу програму безпеки в датчик Prelude.

%package -n prelude-tools
Group: System/Libraries
Summary:        Command-line tools for %{name}
Requires:       %{name} = %{version}-%{release}

%description -n prelude-tools
Provides a convenient interface for sending alerts to Prelude
Manager.

%package -n python3-module-prelude
Group: System/Libraries
Summary:        Python 3 bindings for prelude
Requires:       %{name} = %{version}-%{release}
%{?python_provide:%python_provide python3-prelude}

%description -n python3-module-prelude
Provides python 3 bindings for prelude.

%package -n perl-prelude
Group: System/Libraries
Summary:        Perl bindings for prelude
Requires:       %{name} = %{version}-%{release}

%description -n perl-prelude
Provides perl bindings for prelude.

%package -n ruby-prelude
Group: System/Libraries
Summary:        Ruby bindings for prelude
Requires:       %{name} = %{version}-%{release}

%description -n ruby-prelude
Provides ruby bindings for prelude.

%package -n lua-prelude
Group: System/Libraries
Summary:        Lua bindings for prelude
Requires:       %{name} = %{version}-%{release}
Requires:       lua5.3

%description -n lua-prelude
Provides Lua bindings for prelude generated by SWIG.

%package doc
Group: System/Libraries
Summary:        Documentation for prelude
BuildArch:      noarch

%description doc
Provides documentation for prelude generated by gtk-doc.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1
%patch10 -p1
%patch11 -p1
%patch12 -p1
%patch33 -p0


%build
%autoreconf
%configure \
    --disable-rpath \
    --disable-static \
    --enable-shared \
    --with-swig \
    --without-python2 \
    --with-python3 \
    --with-ruby \
    --with-lua \
    --with-perl-installdirs=vendor \
    --without-included-regex \
    --includedir=%{_includedir}/%{name} \
    --enable-gtk-doc \
    --with-html-dir=%{_docdir}/%{name}-devel
sed -i -e 's! -shared ! -Wl,--as-needed\0!g' libtool
# remove bundled libltld 
rm -fR libltdl
sed -i 's|^\(CFLAGS =.*\)|\1 -include %_includedir/stdio.h|' \
	$(find ./ -name Makefile)

%make_build

%install
%makeinstall_std

chrpath -d %{buildroot}%{_libdir}/*.so.*

find %{buildroot} -name '*.la' -delete
find %{buildroot} -name 'perllocal.pod' -delete
find %{buildroot} -name '.packlist' -delete

# Enable test again after fixing #1629893
#%check
#make check



%files
%{_libdir}/%{name}.so.%{major}
%{_libdir}/%{name}.so.%{major}.*
%{_libdir}/%{name}cpp.so.%{cppmajor}
%{_libdir}/%{name}cpp.so.%{cppmajor}.*
%doc --no-dereference COPYING LICENSE.README HACKING.README
%doc AUTHORS README NEWS

%files devel
%{_datadir}/%{name}
%{_bindir}/%{name}-config
%{_libdir}/%{name}.so
%{_libdir}/%{name}cpp.so
%{_libdir}/pkgconfig/%{name}.pc
%{_includedir}/%{name}
%{_datadir}/aclocal/%{name}.m4
%{_mandir}/man1/%{name}-config.1*

%files -n prelude-tools
# Force default attrs because libprelude force others
%defattr(- , root, root, 755)
%{_bindir}/prelude-adduser
%{_bindir}/prelude-admin
%{_mandir}/man1/prelude-admin.1*
%dir %{_sysconfdir}/prelude
%dir %{_sysconfdir}/prelude/default
%dir %{_sysconfdir}/prelude/profile
%config(noreplace) %{_sysconfdir}/prelude/default/client.conf
%config(noreplace) %{_sysconfdir}/prelude/default/global.conf
%config(noreplace) %{_sysconfdir}/prelude/default/idmef-client.conf
%config(noreplace) %{_sysconfdir}/prelude/default/tls.conf
%dir %{_var}/spool/prelude

%files -n python3-module-prelude
%{python3_sitelibdir}/_prelude.*so
%{python3_sitelibdir}/__pycache__/prelude.cpython-*.*pyc
%{python3_sitelibdir}/prelude-%{version}-py%{__python3_version}.egg-info
%{python3_sitelibdir}/prelude.py

%files -n perl-prelude
%{perl_vendor_archlib}/Prelude.pm
%dir %{perl_vendor_archlib}/auto/Prelude
# Force attrs because libprelude set it to 555
%attr(755, root, root) %{perl_vendor_archlib}/auto/Prelude/Prelude.so

%files -n ruby-prelude
%{ruby_sitearchdir}/Prelude.so

%files -n lua-prelude
%{_libdir}/lua/*/prelude.so

%files doc
%{_docdir}/%{name}-devel
%doc --no-dereference COPYING LICENSE.README HACKING.README
%doc AUTHORS ChangeLog README NEWS

%changelog
* Mon Jan 25 2021 Igor Vlasenko <viy@altlinux.ru> 5.2.0-alt1_3
- update to new release by fcimport

* Wed Nov 18 2020 Igor Vlasenko <viy@altlinux.ru> 5.2.0-alt1_2
- update to new release by fcimport

* Fri Apr 03 2020 Pavel Skrylev <majioa@altlinux.org> 5.1.1-alt2
- - disable ruby

* Thu Dec 05 2019 Igor Vlasenko <viy@altlinux.ru> 5.1.1-alt1_2
- update to new release by fcimport

* Wed Apr 10 2019 Grigory Ustinov <grenka@altlinux.org> 5.0.0-alt2
- (NMU) Rebuild for python3.7.

* Sat Mar 16 2019 Igor Vlasenko <viy@altlinux.ru> 5.0.0-alt1_1
- update to new release by fcimport

* Sun Feb 17 2019 Igor Vlasenko <viy@altlinux.ru> 4.1.0-alt1_10
- new version

* Thu Jan 24 2019 Igor Vlasenko <viy@altlinux.ru> 4.0.0-alt1_3.4
- rebuild with new perl 5.28.1

* Tue Apr 03 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 4.0.0-alt1_3.3.1
- (NMU) Rebuilt with python-3.6.4.

* Fri Mar 30 2018 Andrey Cherepanov <cas@altlinux.org> 4.0.0-alt1_3.3
- rebuild with Ruby 2.5.1

* Tue Mar 13 2018 Andrey Cherepanov <cas@altlinux.org> 4.0.0-alt1_3.2
- rebuild with Ruby 2.5.0

* Fri Dec 15 2017 Igor Vlasenko <viy@altlinux.ru> 4.0.0-alt1_3.1
- rebuild with new perl 5.26.1

* Sat Nov 25 2017 Igor Vlasenko <viy@altlinux.ru> 4.0.0-alt1_3
- new version

* Mon Sep 25 2017 Andrey Cherepanov <cas@altlinux.org> 3.1.0-alt2_29.4
- Rebuild with Ruby 2.4.2

* Sun Sep 10 2017 Andrey Cherepanov <cas@altlinux.org> 3.1.0-alt2_29.3
- Rebuild with Ruby 2.4.1

* Sat Mar 11 2017 Andrey Cherepanov <cas@altlinux.org> 3.1.0-alt2_29.2
- Rebuild with new %%ruby_sitearchdir location

* Fri Feb 03 2017 Igor Vlasenko <viy@altlinux.ru> 3.1.0-alt2_29.1
- rebuild with new perl 5.24.1

* Thu Feb 02 2017 Igor Vlasenko <viy@altlinux.ru> 3.1.0-alt2_29
- changed python names to be the same for python3 and 2

* Wed Feb 01 2017 Igor Vlasenko <viy@altlinux.ru> 3.1.0-alt1_29
- converted for ALT Linux by srpmconvert tools

* Sat Apr 16 2016 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 1.2.6rc1-alt1.git20140916.qa4
- NMU: rebuilt with libgnutls.so.28 -> libgnutls.so.30.

* Wed Nov 25 2015 Igor Vlasenko <viy@altlinux.ru> 1.2.6rc1-alt1.git20140916.1.1.1
- rebuild with new perl 5.22.0

* Fri Oct 09 2015 Sergey V Turchin <zerg@altlinux.org> 1.2.6rc1-alt1.git20140916.1.1
- FTBFS with gcc5
- rebuild with new libgcrypt (ALT#31349)

* Tue Dec 09 2014 Igor Vlasenko <viy@altlinux.ru> 1.2.6rc1-alt1.git20140916.1
- rebuild with new perl 5.20.1

* Tue Sep 23 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.6rc1-alt1.git20140916
- Version 1.2.6rc1

* Fri Aug 30 2013 Vladimir Lettiev <crux@altlinux.ru> 1.0.0-alt3
- built for perl 5.18

* Tue Sep 04 2012 Vladimir Lettiev <crux@altlinux.ru> 1.0.0-alt2
- rebuilt for perl-5.16

* Wed Aug 29 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.0-alt1.7
- Fixed build with new glibc

* Sat Jun 16 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.0-alt1.6
- Fixed build

* Sat Oct 29 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.0.0-alt1.5
- Rebuild with Python-2.7

* Mon Oct 17 2011 Alexey Tourbin <at@altlinux.ru> 1.0.0-alt1.4
- Rebuilt for perl-5.14

* Sat Mar 12 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.0-alt1.3
- Fixed build

* Fri Feb 25 2011 Dmitry V. Levin <ldv@altlinux.org> 1.0.0-alt1.2
- Rebuilt for debuginfo.

* Fri Nov 05 2010 Vladimir Lettiev <crux@altlinux.ru> 1.0.0-alt1.1
- rebuilt with perl 5.12

* Tue Jul 27 2010 Slava Dubrovskiy <dubrsl@altlinux.org> 1.0.0-alt1
- Update to new version 1.0.0

* Wed Jan 13 2010 Slava Dubrovskiy <dubrsl@altlinux.org> 0.9.25-alt1
- Update to new version 0.9.25
- Enable build static lib

* Tue Aug 11 2009 Slava Dubrovskiy <dubrsl@altlinux.org> 0.9.24.1-alt1
- Update to new version 0.9.24.1

* Tue Jun 16 2009 Slava Dubrovskiy <dubrsl@altlinux.ru> 0.9.23-alt2
- Fix dir %_includedir/%name owner (thanks at@)

* Sat Jun 13 2009 Slava Dubrovskiy <dubrsl@altlinux.ru> 0.9.23-alt1
- Update to new version 0.9.23
- Rename python-modules-libprelude to python-module-libprelude

* Fri Jan 16 2009 Slava Dubrovskiy <dubrsl@altlinux.org> 0.9.21.3-alt1
- Update to new version 0.9.21.3

* Fri Dec 26 2008 Slava Dubrovskiy <dubrsl@altlinux.org> 0.9.21.2-alt3
- Rebuild with new gnutls
- Enable build documentation and move it to %_gtk_docdir

* Sat Nov 29 2008 Slava Dubrovskiy <dubrsl@altlinux.org> 0.9.21.2-alt2
- Remmove depricated ldconfig call in post

* Fri Oct 17 2008 Slava Dubrovskiy <dubrsl@altlinux.org> 0.9.21.2-alt1
- Update to new version 0.9.21.2
- Convert spec to UTF-8
- Add lua support

* Sat Jun 28 2008 Slava Dubrovskiy <dubrsl@altlinux.ru> 0.9.17.2-alt1
- Recovery from orfaned
- Update to new version 0.9.17.2
- Update BuildRequires
- Remove ltdl patch
- Add subpackage python-modules-%name and perl-%name
- Update spec

* Sun Dec 19 2004 Serge A. Volkov <vserge at altlinux.ru> 0.8.10-alt1
- Update to new version 0.8.10
- Update BuildRequires
- Reworked ltdl patch - now we try detect ltdl lib

* Thu May 13 2004 Serge A. Volkov <vserge@altlinux.ru> 0.8.8-alt5.1
- Rebuild with openssl-0.9.7d
- Remove configure options "--enable-gtk-doc"

* Mon Feb  2 2004 Serhii Hlodin <hlodin@altlinux.ru> 0.8.8-alt4
- Minor fixes for Sisyphus
- Add patch for remove and use built-in libltdl

* Sat Dec 20 2003 Serhii Hlodin <hlodin@altlinux.ru> 0.8.8-alt3
- Remove .la files

* Thu Nov  6 2003 Serhii Hlodin <hlodin@altlinux.ru> 0.8.8-alt2
- Minor fixes: %name.so transposed to devel package

* Wed Nov  5 2003 Serhii Hlodin <hlodin@altlinux.ru> 0.8.8-alt1
- New release

* Mon Nov 03 2003 Serhii Hlodin <hlodin@altlinux.ru> 0.8.7-alt3
- Minor build fixes in spec

* Sun Oct 12 2003 Aleksandr Blokhin (Sass) <sass@altlinux.ru> 0.8.7-alt2
- Minor fixes in spec

* Wed Oct 08 2003 Serhii Hlodin <hlodin@altlinux.ru> 0.8.7-alt1
- New release

* Mon Jun 16 2003 Serhii Hlodin <hlodin@altlinux.ru> 0.8.5-alt2
- Fixed dependence for directories in spec-file

* Sun May 18 2003 Serhii Hlodin <hlodin@altlinux.ru> 0.8.5-alt1
- Initial build based on original .spec-file
  by Sylvain GIL <prelude-packaging@tootella.org>
