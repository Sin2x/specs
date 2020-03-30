Group: System/Fonts/True type
%define oldname paktype-ajrak-fonts
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%global priority 67
%global fontname paktype-ajrak
%global fontconf %{priority}-%{fontname}

Name:	fonts-ttf-paktype-ajrak
Version:     5.0
Release:     alt1_1
Summary:     Fonts for Arabic from PakType

License:     GPLv2 with exceptions
URL:	https://sourceforge.net/projects/paktype/
Source0:	https://sourceforge.net/projects/paktype/files/PakType-Release-2019-03-11.tar.gz#/%{oldname}-%{version}.tar.gz
Source1:	%{fontconf}.conf
BuildArch:   noarch
BuildRequires:	fontpackages-devel
Source44: import.info

%description 
The paktype-ajrak-fonts package contains fonts for the display of \
Arabic from the PakType by Lateef Sagar.

%prep
%setup -n %{oldname}-%{version} -q -c
rm -rf Code
# get rid of the white space (' ')
mv License\ files/PakType\ Ajrak\ License.txt  PakType_Ajrak_License.txt
mv Features/PakType\ Ajrak\ Features.pdf PakTypeAjrakFeatures.pdf

sed -i 's/\r//' PakType_Ajrak_License.txt
chmod a-x PakType_Ajrak_License.txt PakTypeAjrakFeatures.pdf


%build
echo "Nothing to do in Build."

%install
install -m 0755 -d $RPM_BUILD_ROOT%{_fontdir}
install -m 0644 -p PakTypeAjrak.ttf $RPM_BUILD_ROOT%{_fontdir}

install -m 0755 -d %{buildroot}%{_fontconfig_templatedir} \
		%{buildroot}%{_fontconfig_confdir}

install -m 0644 -p %{SOURCE1} \
	%{buildroot}%{_fontconfig_templatedir}/%{fontconf}.conf

ln -s %{_fontconfig_templatedir}/%{fontconf}.conf \
      %{buildroot}%{_fontconfig_confdir}/%{fontconf}.conf
# generic fedora font import transformations
# move fonts to corresponding subdirs if any
for fontpatt in OTF TTF TTC otf ttf ttc pcf pcf.gz bdf afm pfa pfb; do
    case "$fontpatt" in 
	pcf*|bdf*) type=bitmap;;
	tt*|TT*) type=ttf;;
	otf|OTF) type=otf;;
	afm*|pf*) type=type1;;
    esac
    find $RPM_BUILD_ROOT/usr/share/fonts -type f -name '*.'$fontpatt | while read i; do
	j=`echo "$i" | sed -e s,/usr/share/fonts/,/usr/share/fonts/$type/,`;
	install -Dm644 "$i" "$j";
	rm -f "$i";
	olddir=`dirname "$i"`;
	mv -f "$olddir"/{encodings.dir,fonts.{dir,scale,alias}} `dirname "$j"`/ 2>/dev/null ||:
	rmdir -p "$olddir" 2>/dev/null ||:
    done
done
# kill invalid catalogue links
if [ -d $RPM_BUILD_ROOT/etc/X11/fontpath.d ]; then
    find -L $RPM_BUILD_ROOT/etc/X11/fontpath.d -type l -print -delete ||:
    # relink catalogue
    find $RPM_BUILD_ROOT/usr/share/fonts -name fonts.dir | while read i; do
	pri=10;
	j=`echo $i | sed -e s,$RPM_BUILD_ROOT/usr/share/fonts/,,`; type=${j%%%%/*}; 
	pre_stem=${j##$type/}; stem=`dirname $pre_stem|sed -e s,/,-,g`;
	case "$type" in 
	    bitmap) pri=10;;
	    ttf|ttf) pri=50;;
	    type1) pri=40;;
	esac
	ln -s /usr/share/fonts/$j $RPM_BUILD_ROOT/etc/X11/fontpath.d/"$stem:pri=$pri"
    done ||:
fi


%files
%{_fontconfig_templatedir}/%{fontconf}.conf
%config(noreplace) %{_fontconfig_confdir}/%{fontconf}.conf
%dir %{_fontbasedir}/*/%{_fontstem}/
%{_fontbasedir}/*/%{_fontstem}/PakTypeAjrak.ttf

%doc PakType_Ajrak_License.txt PakTypeAjrakFeatures.pdf 

%changelog
* Mon Mar 30 2020 Igor Vlasenko <viy@altlinux.ru> 5.0-alt1_1
- update

* Mon Oct 23 2017 Igor Vlasenko <viy@altlinux.ru> 4.1-alt1_7
- update to new release by fcimport

* Thu Jun 26 2014 Igor Vlasenko <viy@altlinux.ru> 4.1-alt1_3
- update to new release by fcimport

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 4.0-alt1_3
- update to new release by fcimport

* Sat Nov 24 2012 Igor Vlasenko <viy@altlinux.ru> 4.0-alt1_2
- update to new release by fcimport

* Wed Nov 21 2012 Igor Vlasenko <viy@altlinux.ru> 4.0-alt1_1
- update to new release by fcimport

* Mon Sep 10 2012 Igor Vlasenko <viy@altlinux.ru> 2.1-alt1_1
- update to new release by fcimport

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 2.0-alt3_7
- update to new release by fcimport

* Wed Mar 21 2012 Igor Vlasenko <viy@altlinux.ru> 2.0-alt3_6
- rebuild to get rid of #27020

* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 2.0-alt2_6
- update to new release by fcimport

* Wed Aug 24 2011 Igor Vlasenko <viy@altlinux.ru> 2.0-alt2_5
- rebuild with new rpm-build-fonts

* Sat Aug 06 2011 Igor Vlasenko <viy@altlinux.ru> 2.0-alt1_5
- initial release by fcimport

