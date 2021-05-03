Name:     daps
Version:  3.0.0
Release:  alt2

Summary:  DocBook Authoring and Publishing Suite (DAPS)
License:  GPL-2.0 or GPL-3.0
Group:    Other
Url:      https://github.com/openSUSE/daps

Packager: Andrey Cherepanov <cas@altlinux.org>

Source:   %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: ImageMagick
BuildRequires: dia
BuildRequires: docbook-dtds
BuildRequires: docbook-style-xsl
BuildRequires: docbook5-schemas
BuildRequires: docbook5-style-xsl
BuildRequires: fop
BuildRequires: ghostscript
BuildRequires: inkscape
BuildRequires: python3-module-libxml2
BuildRequires: python3-module-lxml
BuildRequires: sgml-common
BuildRequires: w3m
BuildRequires: xml-commons-apis
BuildRequires: xmlstarlet
BuildRequires: xsltproc
BuildRequires: zip
BuildRequires: asciidoctor
BuildRequires: epubcheck
BuildRequires: jing
BuildRequires: trang
BuildRequires: perl-Config-IniFiles
BuildRequires: perl-File-Copy-Recursive
BuildRequires: perl-File-Rsync
BuildRequires: perl-Image-ExifTool
BuildRequires: optipng
BuildRequires: xfig

BuildArch: noarch

%description
A complete environment to build HTML, PDF, EPUB and other formats from
DocBook XML. See https://github.com/openSUSE/daps for more information.
Documentation is available from
https://opensuse.github.io/daps/doc/index.html.

%package docs
Summary: Documentation for DAPS
Group: Development/Documentation

%description docs
Documentation for %name.

%prep
%setup

%build
%autoreconf
%configure \
	--disable-edit-rootcatalog
%make_build redhat

%install
%makeinstall_std

%check
%make_build check

%files
%doc AUTHORS README.adoc COPYING
%_sysconfdir/%name
%_bindir/*
%_man1dir/*
%_datadir/%name
%_sysconfdir/xml/catalog.d/daps.xml
%_datadir/bash-completion/completions/daps
%_datadir/emacs/site-lisp/docbook_macros.el
%_datadir/xml/daps/schema/daps-autobuild.rnc

%files docs
%_datadir/doc/%name

%changelog
* Mon May 03 2021 Andrey Cherepanov <cas@altlinux.org> 3.0.0-alt2
- Add rpm-build-python3 to build requirements.

* Thu May 14 2020 Andrey Cherepanov <cas@altlinux.org> 3.0.0-alt1
- Initial build for Sisyphus
