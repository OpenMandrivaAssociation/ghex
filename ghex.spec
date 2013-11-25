%define api		3
%define major		0
%define libname		%mklibname gtkhex %{api} %{major}
%define develname	%mklibname -d gtkhex

Summary:	GNOME Hexadecimal Editor
Name:		ghex
Version:	3.10.0
Release:	1
License:	GPLv2+
Group:		Editors
Url:		http://live.gnome.org/Ghex
Source0:	ftp://ftp.gnome.org:21/pub/GNOME/sources/ghex/3.10/%{name}-%{version}.tar.xz

BuildRequires:	gettext
BuildRequires:	intltool
BuildRequires:	itstool
BuildRequires:	perl-XML-Parser
BuildRequires:	desktop-file-utils
BuildRequires:	pkgconfig(gail-3.0)
BuildRequires:	pkgconfig(gconf-2.0)
BuildRequires:	pkgconfig(gnome-doc-utils)
BuildRequires:	pkgconfig(gtk+-3.0) >= 3.0
BuildRequires:	pkgconfig(xml2po)

%description
GHex allows the user to load data from any file, view and edit it in either
hex or ascii. A must for anyone playing games that use non-ascii format for
saving.

%package -n %{libname}
Summary:	Shared library of the GNOME Hexadecimal Editor
Group:		System/Libraries

%description -n %{libname}
This contains the shared library needed by ghex.
 
%package -n %{develname}
Summary:	Development files for the GNOME Hexadecimal Editor library 
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description -n %{develname}
This contains the development files needed to compile applications with 
libghex.

%prep
%setup -q

%build
%configure2_5x \
	--disable-static \
	--disable-rpath \
	--disable-scrollkeeper

%make

%install
%makeinstall_std

desktop-file-install --vendor="" \
	--remove-category="Application" \
	--add-category="X-MandrivaLinux-MoreApplications-Editors" \
	--dir %{buildroot}%{_datadir}/applications \
	%{buildroot}%{_datadir}/applications/*

%find_lang %{name}-%{api} --with-gnome --all-name

%files -f %{name}-%{api}.lang
%doc AUTHORS README
%{_bindir}/*
%{_datadir}/applications/*
%{_datadir}/icons/hicolor/*/apps/*ghex.*
%{_datadir}/icons/HighContrast/*/apps/*ghex.*
%{_datadir}/GConf/gsettings/ghex.convert
%{_datadir}/glib-2.0/schemas/org.gnome.GHex.gschema.xml
%{_datadir}/appdata/ghex.appdata.xml

%files -n %{libname}
%{_libdir}/libgtkhex-%{api}.so.%{major}*

%files -n %{develname}
%{_libdir}/libgtkhex-%{api}.so
%{_libdir}/pkgconfig/gtkhex-%{api}.pc
%{_includedir}/gtkhex-%{api}


%changelog
* Fri Oct  5 2012 Arkady L. Shane <ashejn@rosalab.ru> 3.6.0-1
- update to 3.6.0

* Wed May 16 2012 Matthew Dawkins <mattydaw@mandriva.org> 3.4.1-1
+ Revision: 799232
- update to new version 3.4.1

* Sat May 05 2012 Alexander Khrukin <akhrukin@mandriva.org> 3.4.0-1
+ Revision: 796838
- BR: gettext gnome-doc-utils perl-XML-Parser
- BR: xsltproc
- version update 3.4.0

* Mon May 23 2011 Funda Wang <fwang@mandriva.org> 2.24.0-3
+ Revision: 677704
- rebuild to add gconftool as req

* Fri Sep 11 2009 Thierry Vignaud <tv@mandriva.org> 2.24.0-2mdv2011.0
+ Revision: 437687
- rebuild

* Thu Feb 19 2009 Götz Waschk <waschk@mandriva.org> 2.24.0-1mdv2009.1
+ Revision: 342790
- new version
- fix format strings

* Mon Nov 10 2008 Funda Wang <fwang@mandriva.org> 2.22.0-3mdv2009.1
+ Revision: 301804
- rebuild for new xcb

* Thu Aug 07 2008 Thierry Vignaud <tv@mandriva.org> 2.22.0-2mdv2009.0
+ Revision: 266843
- rebuild early 2009.0 package (before pixel changes)

  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Thu Apr 10 2008 Götz Waschk <waschk@mandriva.org> 2.22.0-1mdv2009.0
+ Revision: 192555
- new version

* Wed Feb 27 2008 Götz Waschk <waschk@mandriva.org> 2.21.92-1mdv2008.1
+ Revision: 175671
- new version

* Wed Jan 30 2008 Götz Waschk <waschk@mandriva.org> 2.21.90-1mdv2008.1
+ Revision: 160364
- new version

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

* Sat Dec 22 2007 Götz Waschk <waschk@mandriva.org> 2.21.4-1mdv2008.1
+ Revision: 136788
- new version

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Mon Dec 10 2007 Götz Waschk <waschk@mandriva.org> 2.20.1-1mdv2008.1
+ Revision: 116876
- new version

* Tue Sep 18 2007 Götz Waschk <waschk@mandriva.org> 2.20.0-1mdv2008.0
+ Revision: 89456
- new version

* Tue Aug 28 2007 Götz Waschk <waschk@mandriva.org> 2.19.91-1mdv2008.0
+ Revision: 72476
- new version

* Tue Aug 14 2007 Götz Waschk <waschk@mandriva.org> 2.19.90-1mdv2008.0
+ Revision: 63194
- new version

* Wed Aug 08 2007 Götz Waschk <waschk@mandriva.org> 2.19.0-1mdv2008.0
+ Revision: 60433
- fix buildrequires
- Import ghex



* Wed Aug  8 2007 Götz Waschk <waschk@mandriva.org> 2.19.0-1mdv2008.0
- drop legacy menu
- new devel name
- add new icons
- remove gnome help
- New version 2.19.0

* Thu Aug 03 2006 Frederic Crozat <fcrozat@mandriva.com> 2.8.2-4mdv2007.0
- Rebuild with latest dbus

* Thu Jul 13 2006 Frederic Crozat <fcrozat@mandriva.com> 2.8.2-3mdv2007.0
- Rebuild with latest gail
- switch to xdg menu
- use macros

* Wed Mar  8 2006 Götz Waschk <waschk@mandriva.org> 2.8.2-2mdk
- replace prereq

* Wed Mar 08 2006 Götz Waschk <waschk@mandriva.org> 2.8.2-1mdk
- New release 2.8.2
- use mkrel

* Sun Nov 20 2005 Götz Waschk <waschk@mandriva.org> 2.8.1-2mdk
- rebuild for new openssl

* Tue Oct 19 2004 Götz Waschk <waschk@linux-mandrake.com> 2.8.1-1mdk
- New release 2.8.1

* Tue Oct 12 2004 Götz Waschk <waschk@linux-mandrake.com> 2.8.0-1mdk
- add omf files to lang
- New release 2.8.0

* Fri Aug 20 2004 Götz Waschk <waschk@linux-mandrake.com> 2.6.1-3mdk
- really fix to new menu

* Thu Aug 19 2004 Götz Waschk <waschk@linux-mandrake.com> 2.6.1-2mdk
- rebuild for new menu

* Thu May 27 2004 Götz Waschk <waschk@linux-mandrake.com> 2.6.1-1mdk
- enable parallel build
- reenable libtoolize
- New release 2.6.1

* Mon Apr 26 2004 Götz Waschk <waschk@linux-mandrake.com> 2.6.0-1mdk
- new version

* Wed Apr  7 2004 Götz Waschk <waschk@linux-mandrake.com> 2.5.2-1mdk
- fix menu
- fix intltool build
- new version

* Sat Oct 11 2003 Götz Waschk <waschk@linux-mandrake.com> 2.5.0-1mdk
- new version

* Thu Sep 11 2003 Götz Waschk <waschk@linux-mandrake.com> 2.4.0.1-1mdk
- new version

* Tue Sep 09 2003 Frederic Crozat <fcrozat@mandrakesoft.com> 2.4.0-1mdk
- Release 2.4.0
- Remove patch0 (merged upstream)

* Tue Jul 15 2003 Götz Waschk <waschk@linux-mandrake.com> 2.3.0-4mdk
- don't uninstall schemas on upgrade

* Fri Jul 11 2003 Götz Waschk <waschk@linux-mandrake.com> 2.3.0-3mdk
- add schemas uninstallation
- patch to fix varargs syntax error caught by new gcc 

* Mon Apr 28 2003 Götz Waschk <waschk@linux-mandrake.com> 2.3.0-2mdk
- fix distriblint warning

* Wed Apr 16 2003 Götz Waschk <waschk@linux-mandrake.com> 2.3.0-1mdk
- libify the package
- disable parallel build, there are some missing deps
- new version

* Thu Jan 16 2003 Frederic Crozat <fcrozat@mandrakesoft.com> 2.2.0-2mdk
- Recompiled against latest openssl

* Tue Jan  7 2003 Frederic Crozat <fcrozat@mandrakesoft.com> 2.2.0-1mdk
- Release 2.2.0
- Remove patch0 (merged upstream) (was gnomeprint 2.2 support)

* Tue Dec 31 2002 Frederic Crozat <fcrozat@mandrakesoft.com> 1.99.90-1mdk
- Release 1.99.90 (GNOME 2 port)
- Remove patch0 (merged upstream)

* Mon Aug  5 2002 Frederic Crozat <fcrozat@mandrakesoft.com> 1.2.1-5mdk
- Patch0: use DTD compliant OMF file

* Mon Jun 17 2002 Olivier Thauvin <thauvin@aerov.jussieu.fr> 1.2.1-4mdk
- png icons (out xpm!)

* Fri Oct 05 2001 Lenny Cartier <lenny@mandrakesoft.com> 1.2.1-3mdk
- fixes from Götz Waschk <waschk@linux-mandrake.com> :
	- find_lang --with-gnome for help files

* Mon Jul 16 2001 Lenny Cartier <lenny@mandrakesoft.com> 1.2.1-2mdk
- add url

* Wed Jun 27 2001 Frederic Crozat <fcrozat@mandrakesoft.com> 1.2.1-1mdk
- Release 1.2.1

* Wed Mar 14 2001 Frederic Crozat <fcrozat@mandrakesoft.com> 1.2-2mdk
- Correct dependencies on scrollkeeper

* Wed Mar 14 2001 Frederic Crozat <fcrozat@mandrakesoft.com> 1.2-1mdk
- Release 1.2
- Use scrollkeeper to maintain help database

* Wed Mar  7 2001 Frederic Crozat <fcrozat@mandrakesoft.com> 1.2-0.2mdk
- Recompiled against latest gnome-print
- add help

* Tue Feb 27 2001 Lenny Cartier <lenny@mandrakesoft.com> 1.2-0.1mdk
- correct release
- used srpm from Götz Waschk <waschk@linux-mandrake.com

* Wed Feb 21 2001 Götz Waschk <waschk@linux-mandrake.com> 1.2-0.1mdk
- 1.2-beta1

* Thu Nov 16 2000 Lenny Cartier <lenny@mandrakesoft.com> 1.1.4-1mdk 
- used srpm from Götz Waschk <waschk@linux-mandrake.com> :
	- new release

* Thu Jul 20 2000 Götz Waschk <waschk@linux-mandrake.com> 1.1.3-1mdk
- initial Mandrake package


