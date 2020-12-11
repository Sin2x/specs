Name: trinity
Version: 1.9
Release: alt2
Summary: System call fuzz tester

License: GPL-2.0
Group: Development/Other
Url: http://codemonkey.org.uk/projects/%name/

Packager: Pavel Vasenkov <pav@altlinux.org>

Source0: http://codemonkey.org.uk/projects/%name/%name-%version.tar.xz
# Fix crash due to walking off the end of the net_protocols array
Patch0: %name-net-protocols.patch
Patch1: %name-rm-definition.patch

%description
Trinity makes syscalls at random, with random arguments.  Where Trinity
differs from other fuzz testers is that the arguments it passes are not
purely random.

We found some bugs in the past by just passing random values, but once
the really dumb bugs were found, these dumb fuzzers would just run and
run.  The problem was if a syscall took for example a file descriptor as
an argument, one of the first things it would try to do was validate
that fd.  Being garbage, the kernel would just reject it as -EINVAL of
course.  So on startup, Trinity creates a list of file descriptors, by
opening pipes, scanning sysfs, procfs, /dev, and creates a bunch of
sockets using random network protocols.  Then when a syscall needs an
fd, it gets passed one of these at random.

File descriptors aren't the only thing Trinity knows about.  Every
syscall has its arguments annotated, and where possible it tries to
provide something at least semi-sensible. "Length" arguments for example
get passed one of a whole bunch of potentially interesting values.
(Powers of 2 +/-1 are a good choice for triggering off-by-one bugs it
seems).

Trinity also shares those file descriptors between multiple threads,
which causes havoc sometimes.

If a child process successfully creates an mmap, the pointer is stored,
and fed to subsequent syscalls, sometimes with hilarious results.

%prep
%setup
%patch0 -p0
%patch1 -p2

%build
%configure
%make_build include/version.h

%install
# Install the main binary
%makeinstall_std install DESTDIR=%buildroot%prefix

# Install helper scripts
install -Dm0755 scripts/* -t %buildroot%_libexecdir/%name

%files
%doc COPYING README Documentation/*
%_bindir/%name
%_libexecdir/%name/

%changelog
* Fri Dec 11 2020 Pavel Vasenkov <pav@altlinux.org> 1.9-alt2
- Remove multiple defined variables

* Fri Feb 25 2020 Pavel Vasenkov <pav@altlinux.org> 1.9-alt1
- Removed %{?_smp_mflags} option from %make_build macro.
- Changed prefix INSTALL="/bin/install -p" to install
- Set build and installation settings to common type
- Cleaned spec file

* Fri Feb 21 2020 Pavel Vasenkov <pav@altlinux.org> 1.9-alt0.1.beta
- change spec

* Thu Feb 20 2020 Pavel Vasenkov <pav@altlinux.org> 1.9-alt0.1
- initial build
