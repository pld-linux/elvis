Summary:	Elvis is a clone of vi/ex
Summary(pl):	Elvis jest klonem edytora vi
Name:		elvis
Version:	2.1
Release:	1
Copyright:	Artistic License
Group:		Applications/Editors
Group(pl):	Aplikacje/Edytory
Source:		ftp://ftp.cs.pdx.edu/pub/elvis/%{name}-%{version}.tar.gz
BuildRoot:   	/tmp/%{name}-%{version}-root

%description
Vi clone.

%description -l pl
Elvis to jeden z popularniejszych klonów edytora vi. Jest szybki, posiada
bogate mo¿liwo¶ci i bardzo dobr± dokumentacjê.

%package static
Summary:	Static elvis
Summary(pl):	elvis skompilowany statycznie
Group:		Applications/Editors
Group(pl):	Aplikacje/Edytory
Provides:	vi
Obsoletes:	vi

%description static
The classic unix /bin/vi - small, static compiled editor which is useful
as a rescue tool.

%description static -l pl
Klasyczny unixowy /bin/vi - ma³y, skompilowany statycznie edytor, który
przydaje siê przy awarii systemu.

%prep
%setup -q

%build
CC="cc $RPM_OPT_FLAGS" LDFLAGS="-static -s" \
./configure \
	--prefix=/usr \
	--without-x \
	linux
make LIBS="-lncurses"
mv elvis elvis.static

make clean

CC="cc $RPM_OPT_FLAGS" LDFLAGS="-s" \
./configure \
	--prefix=/usr \
	--with-x \
	linux
make LIBS="-lncurses -lX11 -L/usr/X11R6/lib"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/{bin,usr/{bin,man/man1,lib/elvis}}

install -s elvis	$RPM_BUILD_ROOT/usr/bin
install -s elvis.static	$RPM_BUILD_ROOT/bin/vi
install -s ref		$RPM_BUILD_ROOT/usr/bin/
install lib/ref.man	$RPM_BUILD_ROOT/usr/man/man1

rm -f	lib/*.man
mv lib/license .
install	lib/*		$RPM_BUILD_ROOT/usr/lib/elvis

gzip -9nf $RPM_BUILD_ROOT/usr/man/man*/* \
	lib/license BUGS

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {license,BUGS}.gz README.html
%attr(755,root,root) /usr/bin/elvis
%attr(755,root,root) /usr/bin/ref
/usr/man/man1/*
/usr/lib/elvis

%files static
%attr(755,root,root) /bin/vi

%changelog
* Tue Apr 27 1999 Micha³ Kuratczyk <kura@pld.org.pl>
  [2.1-1]
- built for PLD
