Group: Other
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:             adobe-mappings-pdf
Summary:          PDF mapping resources from Adobe
Version:          20180407
Release:          alt1_4
License:          BSD

URL:              https://www.adobe.com/
Source:           https://github.com/adobe-type-tools/mapping-resources-pdf/archive/%{version}.tar.gz#/mapping-resources-pdf-%{version}.tar.gz

BuildArch:        noarch
BuildRequires:    git
Source44: import.info

%description
Mapping resources for PDF have a variety of functions, such as mapping CIDs
(Character IDs) to character codes, or mapping character codes to other
character codes.

These mapping resources for PDF should not be confused with CMap resources.
While both types of resources share the same file structure and syntax, they
have very different functions.

These PDF mapping resources are useful for some applications (e.g. Ghostscript)
to function properly.

# === SUBPACKAGES =============================================================

%package devel
Group: Other
Summary:          RPM macros for Adobe's PDF mapping resources
Requires:         %{name} = %{version}-%{release}

%description devel
This package is useful for Fedora development purposes only. It installs RPM
macros useful for building packages against %{name},
as well as all the fonts contained in this font set.


# === BUILD INSTRUCTIONS ======================================================

# NOTE: This package provides only resource files, which are already
#       "pre-compiled" to smallest size possible, but they still remain in
#       postscript format as intended. That's why there is no %%build phase.

%prep
%setup -q -n mapping-resources-pdf-%{version}


%install
%makeinstall_std prefix=%{_prefix}

# Generate the macro containing the root path to our mappings files:
install -m 0755 -d %{buildroot}%{_rpmmacrosdir}

cat > %{buildroot}%{_rpmmacrosdir}/macros.%{name} << _EOF
%%adobe_mappings_rootpath     %{_datadir}/adobe/resources/mapping/
_EOF

# === PACKAGING INSTRUCTIONS ==================================================

%files
%doc README.md
%doc --no-dereference LICENSE.txt

%dir %{_datadir}/adobe
%dir %{_datadir}/adobe/resources
%dir %{_datadir}/adobe/resources/mapping

%{_datadir}/adobe/resources/mapping/pdf2other
%{_datadir}/adobe/resources/mapping/pdf2unicode

%files devel
%{_rpmmacrosdir}/macros.%{name}

# =============================================================================

%changelog
* Sun Sep 29 2019 Igor Vlasenko <viy@altlinux.ru> 20180407-alt1_4
- new version

