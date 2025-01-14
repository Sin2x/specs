Name: dblatex
Version: 0.3.12
Release: alt1

Summary: DocBook to LaTeX/ConTeXt Publishing
License: GPL-2.0-or-later and MIT and W3C
Group: Text tools
Url: http://dblatex.sourceforge.net/
Packager: Kirill Maslinsky <kirill@altlinux.org>

Source: %name-%version.tar

# ImageMagick-tools or GraphicsMagick-ImageMagick-compat
Requires: /usr/bin/convert
Requires: xsltproc docbook-dtds

BuildRequires(pre): rpm-build-python3 rpm-build-tex
BuildRequires: python3-devel texlive-latex-extra xsltproc
BuildRequires: transfig

BuildArch: noarch

# this is xelatex's sty, skip to workaround texmf dep tracing unefficiency
%add_texmf_req_skip xecyr.sty
# 4Suite python2 only, xsltproc will be used
%filter_from_requires /Ft\./d

%define _dblatex_datadir %_datadir/%name
%define _dblatex_texdir %_texmfmain/tex/latex/%name

%description
Dblatex started as a DB2LaTeX clone, but since then many things have changed
and new features have been added or (hopefully) improved. Now, the portion of
shared code is small if any, and the dblatex purpose is different from DB2LaTeX
on these points:

    * The project is end-user oriented, that is, it tries to hide as much as
    * possible the latex compiling stuff by providing a single clean script to
    * produce directly DVI, PostScript and PDF output.  The actual output
    * rendering is done not only by the XSL stylesheets transformation, but
    * also by a dedicated LaTeX package. The goal is to allow a deep LaTeX
    * customisation without changing the XSL stylesheets.  Post-processing is
    * done by Python, to make publication faster, convert the images if needed,
    * and do the whole compilation.

This project is splitted in two instances working on the same principles. Both
instances are intended to produce DVI, PostScript, PDF documents from DocBook
SGML or XML sources, by converting first to a high level set of TeX macros.

%prep
%setup
# \cyrchar is not defined, attempts to use it are unjustified
sed -i 's/\\cyrchar//g' lib/dbtexmf/dblatex/unient.py
# invalid inkscape parameters order
sed -i '/inkscape.*format, *input, *output/s/input, *output/output, input/' lib/dbtexmf/core/imagedata.py

#fix shebangs
sed -i 's|\(/usr/bin/\)env \(python\)$|\1\23|' \
scripts/dblatex tools/pdfscan.py \
lib/dbtexmf/dblatex/xetex/*.py lib/contrib/which/which.py \
lib/contrib/debian/dblatex

%build
%python3_build

%install 
%python3_install

mkdir -p %buildroot/%_dblatex_texdir
mv %buildroot/%_dblatex_datadir/latex/{contrib,misc/multirow2.sty,style} %buildroot/%_dblatex_texdir
rm -rvf %buildroot/%_dblatex_datadir/latex/misc

#mkdir -p %buildroot/%_dblatex_datadir
#cp -a buildroot/%_dblatex_datadir/xsl %buildroot/%_dblatex_datadir

mkdir -p %buildroot/%_dblatex_datadir/latex
#cp -a buildroot/%_dblatex_datadir/latex/{graphics,scripts,specs} %buildroot/%_dblatex_datadir/latex
ln -s ../../texmf/tex/latex/dblatex/contrib %buildroot/%_dblatex_datadir/latex/contrib
mv %buildroot/%_dblatex_datadir/latex/graphics %buildroot/%_dblatex_texdir

mv %buildroot%_docdir/%name %buildroot%_docdir/%name-%version
cp COPYRIGHT %buildroot%_docdir/%name-%version

# another fix shebang
sed -i 's|\(/usr/bin/\)env \(python\)$|\1\23|' %buildroot%_bindir/%name

%pre
[ -h %_datadir/%name/latex/contrib ] || rm -rf %_datadir/%name/latex/contrib

%files 
%_bindir/%name
%_dblatex_datadir
%_dblatex_texdir
%python3_sitelibdir/dbtexmf/
%python3_sitelibdir/*.egg-info
%_docdir/%name-%version
%_man1dir/%name.1*


%changelog
* Tue Sep 14 2021 Grigory Ustinov <grenka@altlinux.org> 0.3.12-alt1
- Build new version.

* Mon Nov 09 2020 Vitaly Lipatov <lav@altlinux.ru> 0.3.11-alt2
- NMU: require /usr/bin/convert instead of ImageMagick-tools

* Tue Jun 16 2020 Yuri N. Sedunov <aris@altlinux.org> 0.3.11-alt1
- 0.3.11 (Python3 version: https://downloads.sf.net/dblatex/dblatex-0.3.11py3.tar.bz2)
- fixed License tag

* Tue Oct 02 2018 Grigory Ustinov <grenka@altlinux.org> 0.3.10-alt2
- Remove dependency on ImageMagick.

* Tue May 29 2018 Grigory Ustinov <grenka@altlinux.org> 0.3.10-alt1
- Build new version (Closes: #34675).

* Mon Mar 05 2018 Igor Vlasenko <viy@altlinux.ru> 0.3-alt2
- NMU: rebuild with rpm-build-tex

* Thu Dec 08 2016 Fr. Br. George <george@altlinux.ru> 0.3-alt1.1.1.1
- Fix inkscape call

* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.3-alt1.1.1
- Rebuild with Python-2.7

* Thu Oct 13 2011 Michael Shigorin <mike@altlinux.org> 0.3-alt1.1
- NMU (fixes by led@):
  + fixed License
  + fixed BuildRequires
  + added URL
- minor spec cleanup

* Tue Aug 23 2011 Kirill Maslinsky <kirill@altlinux.org> 0.3-alt1
- version up

* Tue Jan 19 2010 Kirill Maslinsky <kirill@altlinux.org> 0.2.12-alt2
- Move auxiliary graphics into texmf tree where TeX will find them

* Thu Nov 12 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.12-alt1.1
- Rebuilt with python 2.6

* Wed Sep 02 2009 Kirill Maslinsky <kirill@altlinux.org> 0.2.12-alt1
- 0.2.9 -> 0.2.12
- package is now installable with both texlive and tetex

  Please NOTE that some required latex packages are missing in tetex
  and you may need to install them separately.

* Tue Jul 08 2008 Kirill Maslinsky <kirill@altlinux.org> 0.2.9-alt2
- fixed upgrade failure (closes #16261)

* Thu Jun 26 2008 Kirill Maslinsky <kirill@altlinux.org> 0.2.9-alt1
- 0.2.7 -> 0.2.9 (closes #16169)
- LaTeX styles provided by dblatex are now visible to LaTeX
    + TeX input files moved into texmf hierarchy
    + applyed debian patch to allow user to override TeX paths (see debian bug #470209)
      10_no_TEXINPUTS_manipulation.dpatch 
- BuildRequires minimized
- more requirements added for automatic LaTeX processing

* Thu Jun 19 2008 Kirill Maslinsky <kirill@altlinux.org> 0.2.7-alt2
- add BuildArch: noarch

* Wed Jun 18 2008 Kirill Maslinsky <kirill@altlinux.org> 0.2.7-alt1
- Initial build for Sisyphus
- this package has huge requirements on teTeX and ImageMagick (among others) 
  but it won't be fully finctional without them

