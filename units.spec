Summary:	A utility for converting amounts from one unit to another
Summary(de.UTF-8):	Einheitenkonvertierungsprogramm
Summary(es.UTF-8):	Programas de conversión de unidades
Summary(fr.UTF-8):	Programme de conversion d'unités
Summary(pl.UTF-8):	Narzędzie do konwersji wartości między jednostkami
Summary(pt_BR.UTF-8):	Programas de conversão de unidades
Summary(ru.UTF-8):	Утилита преобразования единиц измерения
Summary(tr.UTF-8):	Birim dönüştürme programı
Summary(uk.UTF-8):	Утиліта для конвертації одиниць виміру
Name:		units
Version:	1.85
Release:	1
License:	GPL
Group:		Applications/Engineering
Source0:	ftp://ftp.gnu.org/pub/gnu/units/%{name}-%{version}.tar.gz
# Source0-md5:	e2856ebf1082a8ed4f83d791e5a0b90b
Patch0:		%{name}-info.patch
Patch1:		%{name}-DESTDIR.patch
Patch2:		%{name}-FHS.patch
Patch3:		%{name}-use_sys_getopt.patch
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

%description -l de.UTF-8
Das Programm 'units' konvertiert Mengenausdrücke in verschiedenen
Maßstäben in die entsprechenden Werte des anderen Maßstabs um. Das
Programm kann nur multiplikative Maßstabsänderungen verarbeiten.

%description -l es.UTF-8
El programa units convierte expresiones de cantidad en varias escalas
para sus equivalentes en otras escalas. Solamente puede manipular
cambios multiplicativos de escala.

%description -l fr.UTF-8
Le programme units convertit des quantités exprimées en différents
systèmes en leur équivalents sous d'autres systèmes. Il ne peut gérer
que les changements multiplicatifs de systèmes.

%description -l pl.UTF-8
Program units przelicza wartości z jednej jednostki na inną, albo mówi
jakie operacje matematyczne trzeba przeprowadzić, aby przeliczyć
między jednostkami. Narzędzie to może obsłużyć tylko konwersje
multiplikatywne (tzn. nie może powiedzieć jak przeliczyć ze stopni
Celsjusza na Fahrenheita, co wymaga dodawania oprócz mnożenia).

%description -l pt_BR.UTF-8
O programa units converte expressões de quantidade em várias escalas
para seus equivalentes em outras escalas. Ele somente pode manipular
mudanças multiplicativas de escala.

%description -l ru.UTF-8
Программа units преобразовывает количественные выражения между
различными системами мер или рассказывает какие математические
операции необходимы для такого преобразования. Эта программа может
обрабатывать только мультипликативные изменения мер (например, она не
может рассказать как конвертировать градусы Цельсия в градусы
Фаренгейта, так как эта конвертация требует суммирования дополнительно
к мультипликативному преобразованию).

Чаще всего нет необходимости устанавливать эту программу, но иногда
она может оказаться полезной.

%description -l tr.UTF-8
units programı, çeşitli birimlerdeki büyüklükleri başka birimlere
çevirir.

%description -l uk.UTF-8
Програма units перетворює кількісні вирази між різними системами мір
або розповідає які математичні операції потрібні для такого
перетворення. Ця програма може обробляти лише мультиплікативні зміни
мір (наприклад, вона не може розповісти як конвертувати градуси
Цельсія в градуси Фаренгейта, бо ця конвертація потребує додавання
додатково до мультиплікативного перетворення).

Як правило необхідності встановлювати цю програму немає, але іноді
вона стає на пригоді.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
%{__aclocal}
%{__autoconf}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -j1 install \
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
