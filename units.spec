Summary:	A utility for converting amounts from one unit to another
Summary(de):	Einheitenkonvertierungsprogramm
Summary(es):	Programas de conversión de unidades
Summary(fr):	Programme de conversion d'unités
Summary(pl):	Narzêdzie do konwersji warto¶ci miêdzy jednostkami
Summary(pt_BR):	Programas de conversão de unidades
Summary(tr):	Birim dönüþtürme programý
Name:		units
Version:	1.74
Release:	1
License:	GPL
Group:		Applications/Engineering
Group(de):	Applikationen/Ingenieurwesen
Group(pl):	Aplikacje/In¿ynierskie
Source0:	ftp://ftp.gnu.org/pub/gnu/units/%{name}-%{version}.tar.gz
Patch0:		%{name}-info.patch
Patch1:		%{name}-DESTDIR.patch
Patch2:		%{name}-FHS.patch
Patch3:		%{name}-use_sys_geopt.patch
BuildRequires:	autoconf
BuildRequires:	automake
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
Das Programm 'units' konvertiert Mengenausdrücke in verschiedenen
Maßstäben in die entsprechenden Werte des anderen Maßstabs um. Das
Programm kann nur multiplikative Maßstabsänderungen verarbeiten.

%description -l es
El programa units convierte expresiones de cantidad en varias escalas
para sus equivalentes en otras escalas. Solamente puede manipular
cambios multiplicativos de escala.

%description -l fr
Le programme units convertit des quantités exprimées en différents
systèmes en leur équivalents sous d'autres systèmes. Il ne peut gérer
que les changements multiplicatifs de systèmes.

%description -l pl
Program units przelicza warto¶ci z jednej jednostki na inn±, albo
mówi jakie operacje matematyczne trzeba przeprowadziæ, aby przeliczyæ
miêdzy jednostkami. Narzêdzie to mo¿e obs³u¿yæ tylko konwersje
multiplikatywne (tzn. nie mo¿e powiedzieæ jak przeliczyæ ze stopni
Celsjusza na Fahrenheita, co wymaga dodawania oprócz mno¿enia).

%description -l pt_BR
O programa units converte expressões de quantidade em várias escalas
para seus equivalentes em outras escalas. Ele somente pode manipular
mudanças multiplicativas de escala.

%description -l tr
units programý, çeþitli birimlerdeki büyüklükleri baþka birimlere
çevirir.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

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

%post
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%postun
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/units
%{_datadir}/misc/units.dat
%{_mandir}/man1/*
%{_infodir}/*info*
