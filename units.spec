Summary:	A utility for converting amounts from one unit to another.
Name:		units
Version:	1.0
Release:	12
Source:		ftp://lth.se/pub/usenet/comp.sources.misc/volume38/units/part01.gz
Patch0:		units-1.0-makefile.patch
Patch1:		units-1.0-jbj.patch
Copyright:	freely distributable
Group:		Applications/Engineering
BuildRoot:	/tmp/%{name}-%{version}-root

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
install -d $RPM_BUILD_ROOT{%{_bindir},%{_libdir},%{_mandir}/man1}

install -s units $RPM_BUILD_ROOT%{_bindir}
install units.lib $RPM_BUILD_ROOT%{_libdir}
install units.1 $RPM_BUILD_ROOT%{_mandir}/man1

gzip -9nf  $RPM_BUILD_ROOT%{_mandir}/man1/*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/units
%{_libdir}/units.lib
%{_mandir}/man1/units.1.gz
