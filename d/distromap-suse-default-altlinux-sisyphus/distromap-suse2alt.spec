%define orepo suse
%define obranch default
%define module %orepo-%obranch-altlinux-sisyphus

Name: distromap-%module
Version: 0.055
Release: alt1
BuildArch: noarch
Packager: Igor Yu. Vlasenko <viy@altlinux.org>

Summary: %module DistroMap database
Group: Development/Other
License: GPLv2+ or Artistic-2.0
Source: %name-%version.tar
Url: http://repocop.altlinux.org/

Requires: distromap-generic-default-altlinux-sisyphus
Requires: distrodb-static-altlinux-sisyphus

%description
%summary

%prep
%setup

%build

%install
destdir=%buildroot/usr/share/distromap/%orepo/%obranch/altlinux/sisyphus
for type in source binary group-strict group-approx; do
    if [ -d $type ] && stat -t $type/* >/dev/null 2>&1 ; then
	install -m755 -d $destdir/$type
	install -m644 $type/* $destdir/$type/
    fi
done
for type in binary source ; do
    for flag in flags/$type/* ; do
	if [ -d $flag ] && stat -t $flag/* >/dev/null 2>&1 ; then
	    install -m755 -d $destdir/$flag
	    install -m644 $flag/* $destdir/$flag/
	fi
    done
done
ln -s default %buildroot/usr/share/distromap/%orepo/tumbleweed
ln -s %orepo %buildroot/usr/share/distromap/open%orepo

%files
/usr/share/distromap/*

%changelog
* Thu Oct 06 2022 Igor Vlasenko <viy@altlinux.org> 0.055-alt1
- db update

* Sun Jul 03 2022 Igor Vlasenko <viy@altlinux.org> 0.054-alt1
- db update

* Fri Jan 21 2022 Igor Vlasenko <viy@altlinux.org> 0.053-alt1
- db update

* Thu Dec 16 2021 Igor Vlasenko <viy@altlinux.org> 0.052-alt1
- db update

* Wed Oct 20 2021 Igor Vlasenko <viy@altlinux.org> 0.051-alt1
- db update

* Mon Jun 07 2021 Igor Vlasenko <viy@altlinux.org> 0.050-alt1
- db update

* Thu Nov 26 2020 Igor Vlasenko <viy@altlinux.ru> 0.049-alt1
- db update

* Fri Sep 11 2020 Igor Vlasenko <viy@altlinux.ru> 0.048-alt1
- db update

* Fri Jun 12 2020 Igor Vlasenko <viy@altlinux.ru> 0.047-alt1
- db update

* Sat Mar 28 2020 Igor Vlasenko <viy@altlinux.ru> 0.046-alt1
- db update

* Fri Jan 03 2020 Igor Vlasenko <viy@altlinux.ru> 0.045-alt1
- db update

* Thu Oct 31 2019 Igor Vlasenko <viy@altlinux.ru> 0.044-alt1
- db update

* Thu Oct 17 2019 Igor Vlasenko <viy@altlinux.ru> 0.043-alt1
- db update

* Sun Sep 29 2019 Igor Vlasenko <viy@altlinux.ru> 0.042-alt1
- db update

* Thu Sep 12 2019 Igor Vlasenko <viy@altlinux.ru> 0.041-alt1
- db update

* Fri Jul 05 2019 Igor Vlasenko <viy@altlinux.ru> 0.040-alt1
- db update

* Fri Jun 28 2019 Igor Vlasenko <viy@altlinux.ru> 0.039-alt1
- db update

* Sat Apr 13 2019 Igor Vlasenko <viy@altlinux.ru> 0.038-alt1
- db update

* Wed Mar 20 2019 Igor Vlasenko <viy@altlinux.ru> 0.037-alt1
- db update

* Mon Mar 04 2019 Igor Vlasenko <viy@altlinux.ru> 0.036-alt1
- db update

* Tue Feb 19 2019 Igor Vlasenko <viy@altlinux.ru> 0.035-alt1
- db update

* Sat Dec 29 2018 Igor Vlasenko <viy@altlinux.ru> 0.034-alt1
- db update

* Mon Jul 30 2018 Igor Vlasenko <viy@altlinux.ru> 0.033-alt1
- db update

* Sun Jul 15 2018 Igor Vlasenko <viy@altlinux.ru> 0.032-alt1
- db update

* Tue Jun 26 2018 Igor Vlasenko <viy@altlinux.ru> 0.031-alt1
- db update

* Mon Jun 18 2018 Igor Vlasenko <viy@altlinux.ru> 0.030-alt1
- db update

* Sat Jun 02 2018 Igor Vlasenko <viy@altlinux.ru> 0.029-alt1
- db update

* Fri May 18 2018 Igor Vlasenko <viy@altlinux.ru> 0.028-alt1
- db update

* Fri Apr 13 2018 Igor Vlasenko <viy@altlinux.ru> 0.027-alt1
- db update

* Sat Mar 24 2018 Igor Vlasenko <viy@altlinux.ru> 0.026-alt1
- db update

* Fri Mar 16 2018 Igor Vlasenko <viy@altlinux.ru> 0.025-alt1
- db update

* Wed Mar 07 2018 Igor Vlasenko <viy@altlinux.ru> 0.024-alt1
- db update

* Thu Dec 15 2016 Igor Vlasenko <viy@altlinux.ru> 0.023-alt1
- db update

* Thu Nov 03 2016 Igor Vlasenko <viy@altlinux.ru> 0.022-alt1
- added packman
- db update

* Thu Oct 27 2016 Igor Vlasenko <viy@altlinux.ru> 0.021-alt1
- db update

* Mon Oct 17 2016 Igor Vlasenko <viy@altlinux.ru> 0.02-alt1
- db update

* Sun Jan 08 2012 Igor Vlasenko <viy@altlinux.ru> 0.01-alt1
- new version
