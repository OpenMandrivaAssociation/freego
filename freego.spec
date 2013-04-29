Name:		freego
Version:	4.5
Release:	2
Summary:	Easier access to your personal data on free.fr
Summary(fr):	Simplifie l'accès à vos données personnelles Free.fr

Group:		Networking/Other
License:	GPLv2
URL:		http://www.freego.fr/
Source0:	http://www.freego.fr/logiciel/linux/FreeGo%{version}.zip
Patch0:		freego-4-prefix.patch
Patch1:		freego-4-desktopfile.patch
Patch2:		freego-4-gcc45.patch

BuildRequires:	qt4-devel >= 4.4.0
Requires:	vlc

%description
FreeGo makes it easier to access your personal data on the french
ISP Free.

# %description(fr)
# FreeGo simplifie l'accès à vos données personnelles Free. De plus,
# cet outil vous permet en un clic d'être informé de l'état du réseau,
# des innovations de votre fournisseur d'accès, de tester votre débit,
# de consulter vos e-mails et bien plus encore.

%prep
%setup -q -c Freego%{version}
%patch0 -p0 -b .prefix
%patch1 -p0 -b .desktopfile
%patch2 -p0 -b .gcc

%build
%qmake_qt4
%make

%install
%makeinstall INSTALL_ROOT=%buildroot
%__install -p -m 755 -D FreeGo %buildroot%{_bindir}/FreeGo

desktop-file-install  \
       --dir %buildroot/%{_datadir}/applications\
       --delete-original\
       %buildroot/%{_datadir}/applications/*.desktop


%files
%defattr(-,root,root,-)
%doc *.pdf
%{_bindir}/*
%{_datadir}/applications/*.desktop
%{_datadir}/icons/hicolor/*/apps/*.png


%changelog
* Mon Dec 06 2010 Stéphane Téletchéa <steletch@mandriva.org> 4.5-1mdv2011.0
+ Revision: 612670
- Update Freego to version 4.5, using svn snapshot (personal communication) since some files were missing
- Fix spaces and tabs mixing

* Mon Dec 06 2010 Funda Wang <fwang@mandriva.org> 4.0-3mdv2011.0
+ Revision: 611688
- fix build

  + Oden Eriksson <oeriksson@mandriva.com>
    - rebuild

* Fri Sep 11 2009 Thierry Vignaud <tv@mandriva.org> 4.0-2mdv2010.1
+ Revision: 437590
- rebuild

* Thu Feb 05 2009 Jerome Martin <jmartin@mandriva.org> 4.0-1mdv2009.1
+ Revision: 337712
- import freego


