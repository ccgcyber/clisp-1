Summary:	Common Lisp (ANSI CL) implementation
Summary(pl):	Implementacja Common Lisp (ANSI CL)
Name:		clisp
Version:	2.28
Release:	2
Icon:		clisp.gif
License:	GPL
Group:		Development/Languages
Source0:	ftp://cvs2.cons.org/pub/lisp/clisp/source/latest/%{name}-%{version}.tar.bz2
#Alternatively http://prdownloads.sourceforge.net/clisp/clisp-2.27.tar.bz2
Patch0:		%{name}-shell.patch
URL:		http://clisp.cons.org/
BuildRequires:	readline-devel
BuildRequires:	gettext-devel
BuildRequires:	ncurses-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Common Lisp is a high-level, all-purpose programming language. CLISP
is a Common Lisp implementation by Bruno Haible of Karlsruhe
University and Michael Stoll of Munich University, both in Germany. It
mostly supports Common Lisp as described in the ANSI CL standard. It
runs on microcomputers (DOS, OS/2, Windows NT, Windows 95, Amiga
500-4000, Acorn RISC PC) as well as on Unix workstations (Linux, SVR4,
Sun4, DEC Alpha OSF, HP-UX, NeXTstep, SGI, AIX, Sun3 and others) and
needs only 2 MB of RAM.

It is free software and may be distributed under the terms of GNU GPL,
while it is possible to distribute commercial applications compiled
with CLISP.

The user interface comes in German, English, French and Spanish. CLISP
includes an interpreter, a compiler, a large subset of CLOS, a foreign
language interface and a socket interface. An X11 interface is
available through CLX and Garnet.

%description -l pl
Common Lisp to wysokopoziomowy j�zyk programowania og�lnego
przeznaczenia. CLISP to implementacja Common Lisp, kt�rej autorami s�
Bruno Haible z Karlsruhe University oraz Michael Stoll z Munich
University (oba w Niemczech). W wi�kszo�ci wspiera Common Lisp opisany
w standardzie ANSI CL. Dzia�a na mikrokomputerach (DOS, OS/2, Windows
NT, Windows 95, Amiga 500-4000, Acorn RICS PC), a tak�e stacjach
uniksowych (Linux, SVR4, Sun4, DEC Alpha OSF, HP-UX, NeXTstep, SGI,
AIX, Sun3 i inne) i wymaga tylko 2 MB RAM.

To jest oprogramowanie wolnodost�pne, na licencji GNU GPL, mo�liwe
jest dystrybuowanie komercyjnych aplikacji skompilowanych CLISP-em.

Interfejs u�ytkownika dost�pny jest po niemiecku, angielsku, francusku
i hiszpa�sku. CLISP zawiera interpreter, kompilator, znaczny podzbi�r
CLOS, interfejs do innych j�zyk�w oraz interfejs do gniazdek.
Interfejs X11 jest dost�pny poprzez CLX i Garnet.

%prep
%setup -q
%patch0 -p1

%build
./configure --prefix=%{_prefix}
cd src
./makemake \
	--prefix=%{_prefix} \
	--with-readline \
	--with-gettext \
	--with-dynamic-ffi \
	--with-module=wildcard \
	--with-module=regexp \
	--with-module=bindings/linuxlibc6 \
	>Makefile
%{__make} config.lisp
%{__make}
#make check

%install
rm -rf $RPM_BUILD_ROOT
cd src
install -d $RPM_BUILD_ROOT{%{_bindir},%{_docdir},%{_libdir},%{_mandir}}
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	lispdocdir=%{_docdir}/%{name}-%{version} \
	mandir=%{_mandir}
cd ..
mkdir $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}/modules
install modules/*/*.dvi $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}/modules

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/clisp
%doc %{_docdir}/%{name}-%{version}
%dir %{_libdir}/clisp
%dir %{_libdir}/clisp/base
%{_libdir}/clisp/base/*.[aho]
%{_libdir}/clisp/base/lispinit.mem
%attr(755,root,root) %{_libdir}/clisp/base/lisp.run
%{_libdir}/clisp/base/makevars
%{_libdir}/clisp/clisp-link
%{_libdir}/clisp/data
%{_libdir}/clisp/full/*.[aho]
%{_libdir}/clisp/full/lispinit.mem
%attr(755,root,root) %{_libdir}/clisp/full/lisp.run
%{_libdir}/clisp/full/makevars
%{_libdir}/clisp/linkkit
%{_datadir}/locale/en/LC_MESSAGES/*
%lang(de) %{_datadir}/locale/de/LC_MESSAGES/*
%lang(es) %{_datadir}/locale/es/LC_MESSAGES/*
%lang(fr) %{_datadir}/locale/fr/LC_MESSAGES/*
%lang(nl) %{_datadir}/locale/nl/LC_MESSAGES/*
%{_mandir}/man[13]/*
