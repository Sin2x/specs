Name: python3-module-hass-frontend
Version: 20210407.3
Release: alt1

Summary: Home automation platform -- frontend
License: Apache-2.0
Group: System/Servers
Url: https://www.home-assistant.io/

Source0: hass-frontend-%version.tar

BuildArch: noarch
BuildRequires: rpm-build-python3 python3-module-setuptools

%description
Home Assistant is a home automation platform running on Python 3.
It is able to track and control all devices at home and offer a platform
for automating control.
This package contains frontend part of Home Assistant.

%install
mkdir -p %buildroot%python3_sitelibdir/
tar xf %SOURCE0 -C %buildroot%python3_sitelibdir/

%files
%python3_sitelibdir/hass_frontend
%python3_sitelibdir/home_assistant_frontend-%version-*-info

%changelog
* Tue Apr 13 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 20210407.3-alt1
- 20210407.3

* Fri Apr 09 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 20210407.2-alt1
- 20210407.2

* Tue Mar 16 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 20210302.6-alt1
- 20210302.6

* Fri Feb 19 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 20210127.7-alt1
- 20210127.7

* Fri Jan 29 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 20201229.1-alt1
- 20201229.1

* Mon Nov 23 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 20201111.2-alt1
- 20201111.2

* Mon Nov 02 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 20201021.4-alt1
- 20201021.4

* Fri Oct 16 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 20201001.2-alt1
- 20201001.2

* Wed Sep 30 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 20200918.2-alt1
- 20200918.2

* Tue Sep 22 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 20200918.0-alt1
- 20200918.0

* Tue Aug 18 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 20200811.0-alt1
- 20200811.0

* Tue Jul 21 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 20200702.1-alt1
- 20200702.1

* Tue Jul 07 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 20200702.0-alt1
- 20200702.0

* Wed Mar 04 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 20200220.5-alt1
- 20200220.5

* Wed Feb 12 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 20200130.2-alt1
- 20200130.2

* Mon Jan 20 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 20200108.2-alt1
- 20200108.2

* Thu Jan 16 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 20200108.0-alt1
- 20200108.0

* Tue Jan 14 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 20191204.1-alt1
- initial
