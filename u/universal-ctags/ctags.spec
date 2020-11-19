# SPDX-License-Identifier: GPL-2.0-only
%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1

Name:    universal-ctags
Version: p5.9.20201115.0
Release: alt1

Summary: Universal Ctags generates an index of language objects found in source
License: GPL-2.0-only
Group:   Development/Other
Url:     https://ctags.io/
Vcs:     https://github.com/universal-ctags/ctags.git
# Docs:  https://docs.ctags.io

Source: %name-%version.tar
BuildRequires: libjansson-devel
BuildRequires: libseccomp-devel
BuildRequires: libxml2-devel
BuildRequires: libyaml-devel
BuildRequires: python3-module-docutils

%description
Universal Ctags generates an index (or tag) file of language objects
found in source files for many popular programming languages. This index
makes it easy for text editors and other tools to locate the indexed
items. Universal Ctags improves on traditional ctags because of its
multilanguage support, its ability for the user to define new languages
searched by regular expressions, and its ability to generate emacs-style
TAGS files.

universal-ctags has the objective of continuing the development from
what existed in the Sourceforge area. Github exuberant-ctags repository
was started by Reza Jelveh and was later moved to the universal-ctags
organization.

The goal of the project is preparing and maintaining common/unified
working space where people interested in making ctags better can work
together.

%prep
%setup

%build
%autoreconf
%configure
%make_build

%install
%makeinstall

%check
%make_build check

%files
%doc COPYING README.md docs/developers.rst docs/news.rst docs/reporting.rst
%doc docs/interactive-mode.rst docs/parser* docs/output*
%_bindir/ctags
%_bindir/readtags
%_man1dir/ctags.1*
%_man1dir/readtags.1*
%_man5dir/tags.5*
%_man7dir/ctags-*.7*

%changelog
* Thu Nov 19 2020 Vitaly Chikunov <vt@altlinux.org> p5.9.20201115.0-alt1
- Initial import of p5.9.20201115.0 (updates: 39176).
