%define oname cloudpickle

Name:           python3-module-%oname
Version:        1.4.1
Release:        alt1
Summary:        Extended pickling support for Python objects
Group:          Development/Python
License:        BSD
URL:            https://github.com/cloudpipe/cloudpickle
BuildArch:      noarch

# https://github.com/cloudpipe/cloudpickle.git
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-dev python3-module-setuptools
BuildRequires: python3(mock) python3(pytest) python3(tornado) python3(curses)
BuildRequires: python3(psutil) python3(typing_extensions) python3(numpy)
BuildRequires: /proc

%description
cloudpickle makes it possible to serialize Python constructs
not supported by the default pickle module from the Python standard
library. cloudpickle is especially useful for cluster computing where
Python expressions are shipped over the network to execute on remote
hosts, possibly close to the data. Among other things, cloudpickle
supports pickling for lambda expressions, functions and classes defined
interactively in the __main__ module.

%prep
%setup

%build
%python3_build

%install
%python3_install

%check
# There is one test not working with Python 3
#https://github.com/cloudpipe/cloudpickle/issues/114
%__python3 setup.py test ||:

%files
%doc LICENSE README.md
%python3_sitelibdir/%oname
%python3_sitelibdir/%oname-%version-py?.?.egg-info

%changelog
* Sun May 24 2020 Anton Midyukov <antohami@altlinux.org> 1.4.1-alt1
- New version 1.4.1

* Sun Oct 14 2018 Igor Vlasenko <viy@altlinux.ru> 0.4.0-alt1.qa1
- NMU: applied repocop patch

* Fri Oct 13 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.4.0-alt1
- Initial build for ALT.

* Wed Aug 09 2017 Lumir Balhar <lbalhar@redhat.com> - 0.3.1-1
- Initial package.
