Summary: A utility for converting amounts from one unit to another.
Name: units
Version: 1.0
Release: 12
Source: ftp://lth.se/pub/usenet/comp.sources.misc/volume38/units/part01.gz
Patch0: units-1.0-makefile.patch
Patch1: units-1.0-jbj.patch
Copyright: freely distributable
Group: Applications/Engineering
BuildRoot: /var/tmp/units-root

%description
Units converts an amount from one unit to another, or tells you what
mathematical operation you need to perform to convert from one unit to
another.  Units can only handle multiplicative scale changes (i.e., it
can't tell you how to convert from Celsius to Fahrenheit, which requires
an additive step in addition to the multiplicative conversion).

Units is a handy little program which contains a large number of
conversions, from au's to parsecs and tablespoons to cups.  You probably
don't need to install it, but it comes in handy sometimes.

%prep
%setup -q -T -c
cd $RPM_BUILD_DIR/units-1.0
zcat $RPM_SOURCE_DIR/part01.gz | tail -1683 | sh
%patch0 -p1
%patch1 -p1

%build
make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/{bin,lib,man/man1}

install -s -m 755 units $RPM_BUILD_ROOT/usr/bin
install -m 644 units.lib $RPM_BUILD_ROOT/usr/lib
install -m 644 units.1 $RPM_BUILD_ROOT/usr/man/man1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
/usr/bin/units
/usr/lib/units.lib
/usr/man/man1/units.1

%changelog
* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com> 
- auto rebuild in the new build environment (release 12)

* Thu Dec 17 1998 Michael Maher <mike@redhat.com>
- built package for 6.0

* Sun Aug 23 1998 Jeff Johnson <jbj@redhat.com>
- units.lib corrections (problem #685)

* Tue Aug 11 1998 Jeff Johnson <jbj@redhat.com>
- build root

* Mon Apr 27 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Tue Oct 21 1997 Donnie Barnes <djb@redhat.com>
- spec file cleanups

* Mon Jul 21 1997 Erik Troan <ewt@redhat.com>
- built against glibc
