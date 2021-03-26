Group: Text tools
# BEGIN SourceDeps(oneline):
BuildRequires: unzip
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name: hunspell-eu
Summary: Basque hunspell dictionaries
Version: 5.1
Release: alt1_1
Source0: http://xuxen.eus/static/hunspell/xuxen_%{version}_hunspell.zip
URL: http://xuxen.eus
License: GPLv3
BuildArch: noarch

Requires: hunspell
Source44: import.info

%description
Basque hunspell dictionaries.

%prep
%setup -q -c -n hunspell-eu

%build

%install
mkdir -p %{buildroot}%{_datadir}/myspell
cp -p eu_ES.dic %{buildroot}%{_datadir}/myspell/eu_ES.dic
cp -p eu_ES.aff %{buildroot}%{_datadir}/myspell/eu_ES.aff


%files
%doc --no-dereference LICENSE.txt
%{_datadir}/myspell/*

%changelog
* Thu Mar 25 2021 Igor Vlasenko <viy@altlinux.org> 5.1-alt1_1
- update to new release by fcimport

* Wed Sep 27 2017 Igor Vlasenko <viy@altlinux.ru> 0.20080507-alt2_14
- update to new release by fcimport

* Thu Mar 16 2017 Igor Vlasenko <viy@altlinux.ru> 0.20080507-alt2_13
- update to new release by fcimport

* Mon Mar 07 2016 Igor Vlasenko <viy@altlinux.ru> 0.20080507-alt2_12
- update to new release by fcimport

* Mon Feb 15 2016 Igor Vlasenko <viy@altlinux.ru> 0.20080507-alt2_11
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 0.20080507-alt2_10
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 0.20080507-alt2_9
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 0.20080507-alt2_8
- update to new release by fcimport

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 0.20080507-alt2_7
- update to new release by fcimport

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 0.20080507-alt2_6
- update to new release by fcimport

* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 0.20080507-alt2_5
- update to new release by fcimport

* Fri May 20 2011 Igor Vlasenko <viy@altlinux.ru> 0.20080507-alt2_4
- Group: should be Text tools

* Fri May 20 2011 Igor Vlasenko <viy@altlinux.ru> 0.20080507-alt1_4
- import from Fedora by fcimport

