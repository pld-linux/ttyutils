Summary:	Watch and control remote user's terminal session
Summary(pl.UTF-8):	Podgląd i kontrola nad sesją terminalową zdalnego użytkownika
Name:		ttyutils
Version:	3.0.3
Release:	0.1
License:	BSD
Group:		X11/Applications
Source0:	http://downloads.sourceforge.net/ttyutils/%{name}-%{version}.tar.bz2
# Source0-md5:	9baf7cdb7cf111a5ef7dd7a4227627a5
Patch0:		%{name}-ac.patch
Patch1:		%{name}-record_process_write-decl-fix.patch
Patch2:		%{name}-luamod-cflags.patch
Patch3:		%{name}-ttydgen.patch
URL:		http://www.ttyutils.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	glib-devel
BuildRequires:	gtk+2-devel
BuildRequires:	intltool >= 0.35.0
BuildRequires:	libgcrypt-devel >= 1.4.0
BuildRequires:	libtool
BuildRequires:	libzip-devel
BuildRequires:	lua51-devel
BuildRequires:	ncurses-devel
BuildRequires:	perl(XML::Parser)
BuildRequires:	perl-devel
BuildRequires:	readline-devel
BuildRequires:	vte-devel >= 0.24.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
With ttyutils, a user can watch and control a remote user's terminal
session, record the terminal session to a file for later playback, or
write scripts to automate interactive terminal programs such as FTP.

%description -l pl.UTF-8
Za pomocą ttyutils możliwe jest podglądanie i kontrola nad terminalem
zdalnego użytkownika, zapis sesji do pliku do późniejszego odtworzenia
lub tworzenie skryptów do automatyzacji współpracy z niektórymi
interaktywnymi programami.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -rf $RPM_BUILD_ROOT%{_docdir}/%{name}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*.1*
%{_libdir}/ttyutils
%{_datadir}/ttyutils
%dir %{_sysconfdir}/ttyutils
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/%{name}/ttyagent.conf
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/%{name}/ttyrcd.conf
%{_datadir}/glib-2.0/schemas/net.ttyutils.glook.gschema.xml
%{_datadir}/dbus-1/service/net.ttyutils.Agent.service
