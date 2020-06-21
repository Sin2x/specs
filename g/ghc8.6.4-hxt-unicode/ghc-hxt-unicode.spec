%define ghc_version 8.6.4
%define hsc_name ghc
%define hsc_version %ghc_version
%define hsc_namever %hsc_name%hsc_version
%define h_pkg_name hxt-unicode
%define f_pkg_name hxt-unicode
%define pkg_libdir %_libdir/%hsc_name-%hsc_version/%h_pkg_name-%version

Name: %hsc_namever-%f_pkg_name
Version: 9.0.2.4
Release: alt1
License: MIT
Packager: Denis Smirnov <mithraen@altlinux.ru>
Group: Development/Haskell
Url: https://github.com/UweSchmidt/hxt
Source: %name-%version.tar
Patch: %name-%version-%release.patch
Summary: Unicode en-/decoding functions for utf8, iso-latin-* and other encodings

BuildPreReq: haskell(abi) = %ghc_version


# Automatically added by buildreq on Sun Jun 21 2020 (-bb)
# optimized out: bashrc elfutils ghc8.6.4 ghc8.6.4-aeson ghc8.6.4-aeson-pretty ghc8.6.4-ansi-terminal ghc8.6.4-ansi-wl-pprint ghc8.6.4-asn1-encoding ghc8.6.4-asn1-types ghc8.6.4-async ghc8.6.4-attoparsec ghc8.6.4-base-compat ghc8.6.4-base16-bytestring ghc8.6.4-base64-bytestring ghc8.6.4-basement ghc8.6.4-bitarray ghc8.6.4-cereal ghc8.6.4-chronos ghc8.6.4-clock ghc8.6.4-co-log-core ghc8.6.4-colour ghc8.6.4-conduit ghc8.6.4-contravariant ghc8.6.4-cryptohash-sha256 ghc8.6.4-digest ghc8.6.4-dlist ghc8.6.4-ed25519 ghc8.6.4-exceptions ghc8.6.4-hashable ghc8.6.4-hourglass ghc8.6.4-integer-logarithms ghc8.6.4-ldap ghc8.6.4-memory ghc8.6.4-mono-traversable ghc8.6.4-network ghc8.6.4-network-uri ghc8.6.4-old-locale ghc8.6.4-old-time ghc8.6.4-parsec ghc8.6.4-polyparse ghc8.6.4-primitive ghc8.6.4-random ghc8.6.4-regex-base ghc8.6.4-resourcet ghc8.6.4-scientific ghc8.6.4-semigroups ghc8.6.4-split ghc8.6.4-statevar ghc8.6.4-tagged ghc8.6.4-tar ghc8.6.4-th-abstraction ghc8.6.4-time-locale-compat ghc8.6.4-torsor ghc8.6.4-transformers-compat ghc8.6.4-typerep-map ghc8.6.4-unix-compat ghc8.6.4-unliftio-core ghc8.6.4-unordered-containers ghc8.6.4-uuid-types ghc8.6.4-vector ghc8.6.4-vector-algorithms ghc8.6.4-zlib glibc-kernheaders-generic glibc-kernheaders-x86 libffi-devel libgmp-devel perl pkg-config python-modules python2-base python3 python3-base python3-dev rpm-build-haskell rpm-build-python3 sh4
BuildRequires: ghc8.6.4-adldap ghc8.6.4-asn1-parse ghc8.6.4-base-noprelude ghc8.6.4-blaze-builder ghc8.6.4-bytestring-encoding ghc8.6.4-case-insensitive ghc8.6.4-cmark-gfm ghc8.6.4-co-log ghc8.6.4-common ghc8.6.4-cpphs ghc8.6.4-cryptonite ghc8.6.4-data-default-class ghc8.6.4-doc ghc8.6.4-echo ghc8.6.4-edit-distance ghc8.6.4-entropy ghc8.6.4-filemanip ghc8.6.4-generic-deriving ghc8.6.4-glob ghc8.6.4-hackage-security ghc8.6.4-haddock-library ghc8.6.4-hfuse ghc8.6.4-hscolour ghc8.6.4-hslogger ghc8.6.4-hslua ghc8.6.4-hsyaml ghc8.6.4-http ghc8.6.4-hxt-charproperties ghc8.6.4-ipynb ghc8.6.4-juicypixels ghc8.6.4-markdown-unlit ghc8.6.4-mime-types ghc8.6.4-optparse-applicative ghc8.6.4-pem ghc8.6.4-regex-tdfa ghc8.6.4-relude ghc8.6.4-resolv ghc8.6.4-safe ghc8.6.4-sandi ghc8.6.4-sha ghc8.6.4-socks ghc8.6.4-splitmix ghc8.6.4-streaming-commons ghc8.6.4-syb ghc8.6.4-tagsoup ghc8.6.4-temporary ghc8.6.4-unicode-transforms ghc8.6.4-utf8-string ghc8.6.4-xml ghc8.6.4-zip-archive libdb4-devel python-modules-compiler python3-module-mpl_toolkits python3-module-yieldfrom

%description
Unicode encoding and decoding functions for utf8, iso-latin-* and somes
other encodings, used in the Haskell XML Toolbox. ISO Latin 1 - 16, utf8,
utf16, ASCII are supported. Decoding is done with lazy functions, errors
may be detected or ignored.

%prep
%setup
%patch -p1

%build
%hs_configure2
%hs_build

%install
%hs_install
%hs_gen_filelist

%files -f %name-files.all

%changelog
* Sun Jun 21 2020 Denis Smirnov <mithraen@altlinux.ru> 9.0.2.4-alt1
- Spec created by cabal2rpm 0.20_10
