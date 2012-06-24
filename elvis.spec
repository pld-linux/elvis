Summary:	Elvis is a clone of vi/ex
Summary(pl):	Elvis jest klonem edytora vi
Name:		elvis
Version:	2.2_0
Release:	2
Epoch:		1
License:	Artistic (see LICENSE.html)
Group:		Applications/Editors
Source0:	ftp://ftp.cs.pdx.edu/pub/elvis/%{name}-%{version}.tar.gz
# Source0-md5:	6831b8df3e4a530395e66c2889783752
URL:		http://elvis.vi-editor.org/
BuildRequires:	XFree86-devel
BuildRequires:	glibc-static
BuildRequires:	ncurses-devel >= 5.0
BuildRequires:	ncurses-static
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Obsoletes:	elvis-X11

%description
Elvis is one of the most popular Vi clones. Its swift, well
documented and has many features.

%description -l pl
Elvis to jeden z popularniejszych klon�w edytora vi. Jest szybki,
posiada bogate mo�liwo�ci i bardzo dobr� dokumentacj�.

%package static
Summary:	Static elvis
Summary(pl):	elvis skompilowany statycznie
Group:		Applications/Editors
Provides:	vi
Obsoletes:	vi
Obsoletes:	vim-static
Obsoletes:	nvi

%description static
The classic unix /bin/vi - small, statically linked editor which is
useful as a rescue tool.

%description static -l pl
Klasyczny uniksowy /bin/vi - ma�y, skompilowany statycznie edytor,
kt�ry przydaje si� przy awarii systemu.

%prep
%setup -q

%build
CC="%{__cc} %{rpmcflags}"; export CC
%configure \
	--without-x \
	--datadir=%{_datadir}/elvis

%{__make} \
	LIBS="%{rpmldflags} -static -ltinfo"
mv -f elvis elvis.static

%{__make} clean

%configure \
	--with-x \
	--datadir=%{_datadir}/elvis

%{__make} \
	LIBS="%{rpmldflags} -ltinfo -lXft -lXpm -lX11 -L/usr/X11R6/%{_lib}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{/bin,%{_bindir},%{_mandir}/man1,%{_datadir}/elvis}

install elvis ref $RPM_BUILD_ROOT%{_bindir}
install elvis.static $RPM_BUILD_ROOT/bin/vi

for f in doc/{elv*,ref}.man ; do
	install $f $RPM_BUILD_ROOT%{_mandir}/man1/`basename $f .man`.1
done

cp -rf data/* $RPM_BUILD_ROOT%{_datadir}/elvis

mv -f doc/license.html LICENSE.html

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Announce* BUGS COPYING LICENSE.html README.html doc/howto.html
%attr(755,root,root) %{_bindir}/elvis
%attr(755,root,root) %{_bindir}/ref
%{_mandir}/man1/*
%{_datadir}/elvis

%files static
%defattr(644,root,root,755)
%attr(755,root,root) /bin/vi
