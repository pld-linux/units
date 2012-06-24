Summary:	A utility for converting amounts from one unit to another
Summary(de):	Einheitenkonvertierungsprogramm
Summary(fr):	Programme de conversion d'unit�s
Summary(tr):	Birim d�n��t�rme program�
Name:		units
Version:	1.55
Release:	11
License:	GPL
Group:		Applications/Engineering
Group(de):	Applikationen/Ingenieurwesen
Group(pl):	Aplikacje/In�ynierskie
Source0:	ftp://ftp.gnu.org/pub/gnu/units/%{name}-%{version}.tar.gz
Patch0:		%{name}-info.patch
Patch1:		%{name}-DESTDIR.patch
BuildRequires:	readline-devel >= 4.2
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

%description -l de
Das Programm 'units' konvertiert Mengenausdr�cke in verschiedenen
Ma�st�ben in die entsprechenden Werte des anderen Ma�stabs um. Das
Programm kann nur multiplikative Ma�stabs�nderungen verarbeiten.

%description -l fr
Le programme units convertit des quantit�s exprim�es en diff�rents
syst�mes en leur �quivalents sous d'autres syst�mes. Il ne peut g�rer
que les changements multiplicatifs de syst�mes.

%description -l tr
units program�, �e�itli birimlerdeki b�y�kl�kleri ba�ka birimlere
�evirir.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
aclocal
autoconf
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf NEWS README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/units
%{_datadir}/units.dat
%{_mandir}/man1/*
%{_infodir}/*info*
