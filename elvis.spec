Summary:	Elvis is a clone of vi/ex
Summary(pl):	Elvis jest klonem edytora vi
Name:		elvis
Version:	2.2i
Release:	1
License:	Artistic (see LICENSE)
Group:		Applications/Editors
Source0:	ftp://ftp.cs.pdx.edu/pub/elvis/unreleased/%{name}-%{version}.tar.gz
# Source0-md5:	dd53b90614686692d68d27e0223be770
BuildRequires:	ORBit-devel
BuildRequires:	XFree86-devel
BuildRequires:	ncurses-devel >= 5.0
BuildRequires:	ncurses-static
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Obsoletes:	elvis-X11

%define		_libdir		%{_datadir}

%description
Elvis is one of the most popular Vi clones. Its swift, well
documented and has many features.

%description -l pl
Elvis to jeden z popularniejszych klonów edytora vi. Jest szybki,
posiada bogate mo¿liwo¶ci i bardzo dobr± dokumentacjê.

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
Klasyczny unixowy /bin/vi - ma³y, skompilowany statycznie edytor,
który przydaje siê przy awarii systemu.

%prep
%setup -q

%build
CC="%{__cc} %{rpmcflags}"; export CC
LDFLAGS="-static %{rpmldflags}"
%configure \
	--without-x \
	--datadir=%{_datadir}/elvis

%{__make} LIBS="-ltinfo"
mv -f elvis elvis.static

%{__make} clean

LDFLAGS="%{rpmldflags}"
%configure \
	--with-x \
	--datadir=%{_datadir}/elvis

%{__make} LIBS="-ltinfo -lX11 -L/usr/X11R6/lib"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/{bin,%{_bindir},%{_mandir}/man1,%{_datadir}/elvis/themes}

install elvis ref $RPM_BUILD_ROOT%{_bindir}
install elvis.static $RPM_BUILD_ROOT/bin/vi
install lib/*.man $RPM_BUILD_ROOT%{_mandir}/man1

rm -f lib/*.man
mv -f lib/license.html LICENSE.html
install	lib/*.* $RPM_BUILD_ROOT%{_libdir}/elvis
install lib/themes/* $RPM_BUILD_ROOT%{_libdir}/elvis/themes

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE.html BUGS README.html
%attr(755,root,root) %{_bindir}/elvis
%attr(755,root,root) %{_bindir}/ref
%{_mandir}/man1/*
%{_libdir}/elvis

%files static
%defattr(644,root,root,755)
%attr(755,root,root) /bin/vi
