Summary:	A utility for converting amounts from one unit to another
Summary(de):	Einheitenkonvertierungsprogramm
Summary(es):	Programas de conversión de unidades
Summary(fr):	Programme de conversion d'unités
Summary(pl):	Narzêdzie do konwersji warto¶ci miêdzy jednostkami
Summary(pt_BR):	Programas de conversão de unidades
Summary(ru):	õÔÉÌÉÔÁ ÐÒÅÏÂÒÁÚÏ×ÁÎÉÑ ÅÄÉÎÉÃ ÉÚÍÅÒÅÎÉÑ
Summary(tr):	Birim dönüþtürme programý
Summary(uk):	õÔÉÌ¦ÔÁ ÄÌÑ ËÏÎ×ÅÒÔÁÃ¦§ ÏÄÉÎÉÃØ ×ÉÍ¦ÒÕ
Name:		units
Version:	1.80
Release:	6
License:	GPL
Group:		Applications/Engineering
Source0:	ftp://ftp.gnu.org/pub/gnu/units/%{name}-%{version}.tar.gz
# Source0-md5:	537f0e1fadc7715e1eb15c9aa33c8c64
Patch0:		%{name}-info.patch
Patch1:		%{name}-DESTDIR.patch
Patch2:		%{name}-FHS.patch
Patch3:		%{name}-use_sys_getopt.patch
Patch4:		%{name}-comment_strange_c_code.patch
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	readline-devel >= 4.2
BuildRequires:	texinfo
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
Program units przelicza warto¶ci z jednej jednostki na inn±, albo mówi
jakie operacje matematyczne trzeba przeprowadziæ, aby przeliczyæ
miêdzy jednostkami. Narzêdzie to mo¿e obs³u¿yæ tylko konwersje
multiplikatywne (tzn. nie mo¿e powiedzieæ jak przeliczyæ ze stopni
Celsjusza na Fahrenheita, co wymaga dodawania oprócz mno¿enia).

%description -l pt_BR
O programa units converte expressões de quantidade em várias escalas
para seus equivalentes em outras escalas. Ele somente pode manipular
mudanças multiplicativas de escala.

%description -l ru
ðÒÏÇÒÁÍÍÁ units ÐÒÅÏÂÒÁÚÏ×Ù×ÁÅÔ ËÏÌÉÞÅÓÔ×ÅÎÎÙÅ ×ÙÒÁÖÅÎÉÑ ÍÅÖÄÕ
ÒÁÚÌÉÞÎÙÍÉ ÓÉÓÔÅÍÁÍÉ ÍÅÒ ÉÌÉ ÒÁÓÓËÁÚÙ×ÁÅÔ ËÁËÉÅ ÍÁÔÅÍÁÔÉÞÅÓËÉÅ
ÏÐÅÒÁÃÉÉ ÎÅÏÂÈÏÄÉÍÙ ÄÌÑ ÔÁËÏÇÏ ÐÒÅÏÂÒÁÚÏ×ÁÎÉÑ. üÔÁ ÐÒÏÇÒÁÍÍÁ ÍÏÖÅÔ
ÏÂÒÁÂÁÔÙ×ÁÔØ ÔÏÌØËÏ ÍÕÌØÔÉÐÌÉËÁÔÉ×ÎÙÅ ÉÚÍÅÎÅÎÉÑ ÍÅÒ (ÎÁÐÒÉÍÅÒ, ÏÎÁ ÎÅ
ÍÏÖÅÔ ÒÁÓÓËÁÚÁÔØ ËÁË ËÏÎ×ÅÒÔÉÒÏ×ÁÔØ ÇÒÁÄÕÓÙ ãÅÌØÓÉÑ × ÇÒÁÄÕÓÙ
æÁÒÅÎÇÅÊÔÁ, ÔÁË ËÁË ÜÔÁ ËÏÎ×ÅÒÔÁÃÉÑ ÔÒÅÂÕÅÔ ÓÕÍÍÉÒÏ×ÁÎÉÑ ÄÏÐÏÌÎÉÔÅÌØÎÏ
Ë ÍÕÌØÔÉÐÌÉËÁÔÉ×ÎÏÍÕ ÐÒÅÏÂÒÁÚÏ×ÁÎÉÀ).

þÁÝÅ ×ÓÅÇÏ ÎÅÔ ÎÅÏÂÈÏÄÉÍÏÓÔÉ ÕÓÔÁÎÁ×ÌÉ×ÁÔØ ÜÔÕ ÐÒÏÇÒÁÍÍÕ, ÎÏ ÉÎÏÇÄÁ
ÏÎÁ ÍÏÖÅÔ ÏËÁÚÁÔØÓÑ ÐÏÌÅÚÎÏÊ.

%description -l tr
units programý, çeþitli birimlerdeki büyüklükleri baþka birimlere
çevirir.

%description -l uk
ðÒÏÇÒÁÍÁ units ÐÅÒÅÔ×ÏÒÀ¤ Ë¦ÌØË¦ÓÎ¦ ×ÉÒÁÚÉ Í¦Ö Ò¦ÚÎÉÍÉ ÓÉÓÔÅÍÁÍÉ Í¦Ò
ÁÂÏ ÒÏÚÐÏ×¦ÄÁ¤ ÑË¦ ÍÁÔÅÍÁÔÉÞÎ¦ ÏÐÅÒÁÃ¦§ ÐÏÔÒ¦ÂÎ¦ ÄÌÑ ÔÁËÏÇÏ
ÐÅÒÅÔ×ÏÒÅÎÎÑ. ãÑ ÐÒÏÇÒÁÍÁ ÍÏÖÅ ÏÂÒÏÂÌÑÔÉ ÌÉÛÅ ÍÕÌØÔÉÐÌ¦ËÁÔÉ×Î¦ ÚÍ¦ÎÉ
Í¦Ò (ÎÁÐÒÉËÌÁÄ, ×ÏÎÁ ÎÅ ÍÏÖÅ ÒÏÚÐÏ×¦ÓÔÉ ÑË ËÏÎ×ÅÒÔÕ×ÁÔÉ ÇÒÁÄÕÓÉ
ãÅÌØÓ¦Ñ × ÇÒÁÄÕÓÉ æÁÒÅÎÇÅÊÔÁ, ÂÏ ÃÑ ËÏÎ×ÅÒÔÁÃ¦Ñ ÐÏÔÒÅÂÕ¤ ÄÏÄÁ×ÁÎÎÑ
ÄÏÄÁÔËÏ×Ï ÄÏ ÍÕÌØÔÉÐÌ¦ËÁÔÉ×ÎÏÇÏ ÐÅÒÅÔ×ÏÒÅÎÎÑ).

ñË ÐÒÁ×ÉÌÏ ÎÅÏÂÈ¦ÄÎÏÓÔ¦ ×ÓÔÁÎÏ×ÌÀ×ÁÔÉ ÃÀ ÐÒÏÇÒÁÍÕ ÎÅÍÁ¤, ÁÌÅ ¦ÎÏÄ¦
×ÏÎÁ ÓÔÁ¤ ÎÁ ÐÒÉÇÏÄ¦.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p0

%build
%{__aclocal}
%{__autoconf}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT


%clean
rm -rf $RPM_BUILD_ROOT

%post
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%postun
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%files
%defattr(644,root,root,755)
%doc NEWS README
%attr(755,root,root) %{_bindir}/%{name}
%{_datadir}/misc/%{name}.dat
%{_mandir}/man1/*
%{_infodir}/*info*
