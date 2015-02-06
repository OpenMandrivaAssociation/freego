Summary:	Easier access to your personal data on free.fr
Name:		freego
Version:	4.5
Release:	3
License:	GPLv2+
Group:		Networking/Other
Url:		http://www.freego.fr/
Source0:	http://www.freego.fr/logiciel/linux/FreeGo%{version}.zip
Patch0:		freego-4-prefix.patch
Patch1:		freego-4-desktopfile.patch
Patch2:		freego-4-gcc45.patch
BuildRequires:	qt4-devel
Requires:	vlc

%description
FreeGo makes it easier to access your personal data on the french ISP Free.

%files
%doc *.pdf
%{_bindir}/*
%{_datadir}/applications/*.desktop
%{_datadir}/icons/hicolor/*/apps/*.png

#----------------------------------------------------------------------------

%prep
%setup -q -c Freego%{version}
%patch0 -p0 -b .prefix
%patch1 -p0 -b .desktopfile
%patch2 -p0 -b .gcc

%build
%qmake_qt4
%make

%install
%makeinstall INSTALL_ROOT=%{buildroot}
install -p -m 755 -D FreeGo %{buildroot}%{_bindir}/FreeGo

desktop-file-install  \
	--dir %{buildroot}%{_datadir}/applications\
	--delete-original\
	%{buildroot}%{_datadir}/applications/*.desktop

