%define _unpackaged_files_terminate_build 1
%define pypi_name mkdocs

%def_with check

Name: python3-module-%pypi_name
Version: 1.4.1
Release: alt2

Summary: Python tool to create HTML documentation from markdown sources
License: BSD-2-Clause
Group: Development/Python3
Url: https://pypi.org/project/mkdocs/

BuildArch: noarch

Source: %name-%version.tar
Patch0: %name-%version-alt.patch

BuildRequires(pre): rpm-build-python3
BuildRequires: fonts-font-awesome

# build backend and its deps
BuildRequires: python3(hatchling)

# build MO from PO (similar to msgfmt)
BuildRequires: python3(babel)

%if_with check
# install_requires:
BuildRequires: python3(click)
BuildRequires: python3(jinja2)
BuildRequires: python3(markdown)
BuildRequires: python3(yaml)
BuildRequires: python3(watchdog)
BuildRequires: python3-module-ghp-import
BuildRequires: python3(yaml_env_tag)
BuildRequires: python3(packaging)
BuildRequires: python3(mergedeep)
%endif

%description
MkDocs is a fast, simple and downright gorgeous static site generator
that's geared towards building project documentation. Documentation
source files are written in Markdown, and configured with a single YAML
configuration file.

%prep
%setup
%autopatch -p1

%build
%pyproject_build

%install
%pyproject_install
rm -r %buildroot%python3_sitelibdir/mkdocs/tests/

# unbundle font-awesome fonts
FONT_AWESOME_FONTS='%_datadir/fonts-font-awesome/fonts'

fonts_bundled=
for f in $(find -P %buildroot%python3_sitelibdir/mkdocs/themes/*/fonts/ -name 'fontawesome-webfont.*' -type f);
do
    printf "Found fontawesome font: '%%s'\n" "$f"
    font_name="$(basename "$f")"
    system_font="$FONT_AWESOME_FONTS/$font_name"
    if [ ! -f "$system_font" ]; then
        # raise to be sure we have synced fonts (bundled vs system)
        printf "Unknown font name: '%%s'\n" "$font_name"
        exit 1
    fi

    ln -sfT "$system_font" "$f"
    fonts_bundled=yes
done
[ "$fonts_bundled" != "yes" ] && exit 1

%check
cat > tox.ini <<'EOF'
[testenv]
commands =
    # see tool.hatch.envs.test.scripts.test
    python -m unittest discover -p '*tests.py' mkdocs --top-level-directory .
EOF
%tox_check_pyproject

%files
%_bindir/mkdocs
%python3_sitelibdir/mkdocs/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Fri Oct 21 2022 Stanislav Levin <slev@altlinux.org> 1.4.1-alt2
- Fixed build without check.

* Mon Oct 17 2022 Stanislav Levin <slev@altlinux.org> 1.4.1-alt1
- 1.4.0 -> 1.4.1.

* Fri Oct 07 2022 Stanislav Levin <slev@altlinux.org> 1.4.0-alt1
- 1.3.1 -> 1.4.0.

* Fri Sep 23 2022 Stanislav Levin <slev@altlinux.org> 1.3.1-alt1
- 1.3.0 -> 1.3.1.

* Thu May 19 2022 Fr. Br. George <george@altlinux.org> 1.3.0-alt1
- 1.2.3 -> 1.3.0
- Hack in external coverage call in tests

* Mon Jan 24 2022 Stanislav Levin <slev@altlinux.org> 1.2.3-alt1
- 1.2.2 -> 1.2.3 (closes: #41685).

* Sat Aug 21 2021 Vitaly Lipatov <lav@altlinux.ru> 1.2.2-alt2
- fix build requires

* Mon Jul 19 2021 Stanislav Levin <slev@altlinux.org> 1.2.2-alt1
- 1.0.4 -> 1.2.2.
- Enabled testing.

* Thu Jun 24 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.0.4-alt4
- drop excessive python3-module-jinja2-tests BR

* Mon Jun 01 2020 Andrey Bychkov <mrdrew@altlinux.org> 1.0.4-alt3
- Requires fixed.

* Tue Apr 14 2020 Andrey Bychkov <mrdrew@altlinux.org> 1.0.4-alt2
- Build for python2 disabled.

* Wed Apr 24 2019 Fr. Br. George <george@altlinux.ru> 1.0.4-alt1
- Autobuild version bump to 1.0.4

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.16.1-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Mon May 29 2017 Lenar Shakirov <snejok@altlinux.ru> 0.16.1-alt1
- 0.16.1

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.11.1-alt1.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.11.1-alt1.1
- NMU: Use buildreq for BR.

* Sat Nov 22 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.11.1-alt1
- Initial build for Sisyphus

