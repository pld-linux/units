Summary:	A utility for converting amounts from one unit to another.
Name:		units
Version:	1.55
Release:	1
Source0:	ftp://ftp.gnu.org/pub/gnu/units/%{name}-%{version}.tar.gz
License:	GPL
Group:		Applications/Engineering
Group(pl):	Aplikacje/In¿ynierskie
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Units converts an amount from one unit to another, or tells you what
mathematical operation you need to perform to convert from one unit to
another. Units can only handle multiplicative scale changes (i.e., it
can't tell you how to convert from Celsius to Fahrenheit, which
requires an additive step in addition to the multiplicative
conversion).

Units is a handy little program which contains a large number of
conversions, from au's to parsecs and tablespoons to cups. You
probably don't need to install it, but it comes in handy sometimes.

%prep
%setup -q

%build
LDFLAGS="-s"; export LDFLAGS
aclocal
autoconf
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_datadir},%{_mandir}/man1,%{_infodir}}

install units $RPM_BUILD_ROOT%{_bindir}
install units.dat $RPM_BUILD_ROOT%{_datadir}
install units.1 $RPM_BUILD_ROOT%{_mandir}/man1
install units.info $RPM_BUILD_ROOT%{_infodir}

gzip -9nf $RPM_BUILD_ROOT{%{_mandir}/man1/*,%{_infodir}/*} \
	NEWS README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/units
%{_datadir}/units.dat
%{_mandir}/man1/*.gz
%{_infodir}/*.gz
%doc *.gz
