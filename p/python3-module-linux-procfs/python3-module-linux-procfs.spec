Name: python3-module-linux-procfs
Version: 0.7.0
Release: alt1

Summary: Linux /proc abstraction classes

License: GPLv2
Group: Development/Python3
URL: https://rt.wiki.kernel.org/index.php/Tuna

# Source-url: https://cdn.kernel.org/pub/software/libs/python/python-linux-procfs/python-linux-procfs-%version.tar.xz
Source: %name-%version.tar

BuildArch: noarch

BuildRequires: python3-dev
#BuildRequires: python3-setuptools
#Requires: python3-module-six

%description
Abstractions to extract information from the Linux kernel /proc files.

%prep
%setup

%build
%python3_build_debug

%install
%python3_install

%files
%_bindir/pflags
%python3_sitelibdir/procfs/
%python3_sitelibdir/python_linux_procfs*.egg-info

%changelog
* Mon Jul 18 2022 Vitaly Lipatov <lav@altlinux.ru> 0.7.0-alt1
- new version 0.7.0 (with rpmrb script)

* Tue Jul 06 2021 Vitaly Lipatov <lav@altlinux.ru> 0.6.3-alt1
- new version 0.6.3 (with rpmrb script)

* Sat Feb 08 2020 Vitaly Lipatov <lav@altlinux.ru> 0.6.1-alt1
- initial build for ALT Sisyphus

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Feb 25 2019 Miro Hrončok <mhroncok@redhat.com> - 0.6.1-2
- Subpackage python2-linux-procfs has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Tue Feb  5 2019 Jiri Kastner <jkastner@redhat.com> - 0.6.1-1
- update to 0.6.1

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.5.1-5
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 25 2018 Iryna Shcherbina <ishcherb@redhat.com> - 0.5.1-3
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Tue Nov 21 2017 Jiri Kastner <jkastner@redhat.com> - 0.5.1-2
- missing defattr for _bindir

* Tue Nov 21 2017 Jiri Kastner <jkastner@redhat.com> - 0.5.1-1
- missed snippet in specfile for python2 only
- added scripts to setup.py, pflags renamed and added to setup.py

* Mon Nov 20 2017 Jiri Kastner <jkastner@redhat.com> - 0.5-1
- update to 0.5

* Sat Aug 19 2017 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.4.10-4
- Python 2 binary package renamed to python2-linux-procfs
  See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.10-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Dec 22 2016 Jiri Kastner <jkastner@redhat.com> - 0.4.10-1
- update to latest release

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.6-7
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Oct 10 2014 Jiri Kastner <jkastner@redhat.com> - 0.4.6-4
- fix source and url

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Jun 14 2013 Jiri Kastner <jkastner@redhat.com> - 0.4.6-1
- updated to 0.4.6

* Thu Jun  6 2013 Jiri Kastner <jkastner@redhat.com> - 0.4.5-1
- Added support for parsing cgroups as a per thread attribute

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Jul 22 2010 David Malcolm <dmalcolm@redhat.com> - 0.4.4-4
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Feb 10 2009 Arnaldo Carvalho de Melo <acme@redhat.com> - 0.4.4-1
- Even more fixes due to the fedora review process

* Mon Feb  9 2009 Arnaldo Carvalho de Melo <acme@redhat.com> - 0.4.3-1
- Fixups due to the fedora review process

* Tue Aug 12 2008 Arnaldo Carvalho de Melo <acme@redhat.com> - 0.4.2-1
- interrupts: Add find_by_user_regex
- process: Always set the "cmdline" array, even if empty
- pidstats: Remove dead processes in find_by_name()
- pidstats: Add process class to catch dict references for late parsing
- pidstats: Move the /proc/PID/{stat,status} parsing to classes
- pidstats: Introduce process_flags method

* Tue Aug 12 2008 Arnaldo Carvalho de Melo <acme@redhat.com> - 0.4-1
- Per process flags needed by tuna

* Fri Jun 13 2008 Arnaldo Carvalho de Melo <acme@redhat.com> - 0.3-1
- Support CPU hotplug

* Mon Feb 25 2008 Arnaldo Carvalho de Melo <acme@redhat.com> - 0.1-1
- package created
