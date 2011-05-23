%define name ghex
%define major 0
%define libname %mklibname gtkhex %major
%define libnamedev %mklibname -d gtkhex

Name: %name
Summary: GNOME Hexadecimal Editor
Version: 2.24.0
Release: %mkrel 3
License: GPLv2+
Group: Editors
Url: http://pluton.ijs.si/~jaka/gnome.html#GHEX
Source: ftp://ftp.gnome.org/pub/GNOME/sources/%{name}/%{name}-%{version}.tar.bz2
Patch: ghex-2.24.0-format-strings.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-buildroot
BuildRequires: libgnomeprintui-devel >= 2.2
BuildRequires: libglade2.0-devel
BuildRequires: libgail-devel
BuildRequires: libgnomeui2-devel
BuildRequires: gnome-doc-utils
BuildRequires: scrollkeeper
BuildRequires: intltool
BuildRequires: desktop-file-utils
Requires(post): scrollkeeper >= 0.3
Requires(postun): scrollkeeper >= 0.3

%description
GHex allows the user to load data from any file, view and edit it in either
hex or ascii. A must for anyone playing games that use non-ascii format for
saving.

%package -n %libname
Summary: Shared library of the GNOME Hexadecimal Editor
Group: System/Libraries

%description -n %libname
GHex allows the user to load data from any file, view and edit it in either
hex or ascii. A must for anyone playing games that use non-ascii format for
saving.

This contains the shared library needed by ghex.
 
%package -n %libnamedev
Summary: Development files for the GNOME Hexadecimal Editor library 
Group: Development/C
Requires: %libname = %version
Provides: libgtkhex-devel = %version-%release
Obsoletes: %mklibname -d gtkhex 0

%description -n %libnamedev
GHex allows the user to load data from any file, view and edit it in either
hex or ascii. A must for anyone playing games that use non-ascii format for
saving.

This contains the development files needed to compile applications with 
libghex

%prep
%setup -q
%patch -p1 -b .format-strings

%build
%configure2_5x
%make

%install
rm -rf %buildroot %name-2.0.lang

GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL=1 %makeinstall_std

desktop-file-install --vendor="" \
  --remove-category="Application" \
  --add-category="X-MandrivaLinux-MoreApplications-Editors" \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications $RPM_BUILD_ROOT%{_datadir}/applications/*


%{find_lang} %name-2.0 --with-gnome --all-name

%post
%if %mdkversion < 200900
%update_scrollkeeper
%post_install_gconf_schemas ghex2
%update_icon_cache hicolor
%endif

%if %mdkversion < 200900
%{update_menus}
%endif

%preun
%preun_uninstall_gconf_schemas ghex2

%if %mdkversion < 200900
%postun
%{clean_scrollkeeper}
%{clean_menus}
%clean_icon_cache hicolor
%endif

%if %mdkversion < 200900
%post -n %libname -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %libname -p /sbin/ldconfig
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}-2.0.lang
%defattr(-, root, root)
%doc AUTHORS README ChangeLog
%config(noreplace) %{_sysconfdir}/gconf/schemas/*
%{_bindir}/*
%{_datadir}/applications/*
%_datadir/icons/hicolor/*/apps/*ghex.*
%{_datadir}/gnome-2.0/ui/*

%files -n %libname
%defattr(-, root, root)
%_libdir/libgtkhex.so.%{major}*

%files -n %libnamedev
%defattr(-, root, root)
%_libdir/libgtkhex.so
%_libdir/libgtkhex.a
%attr(644,root,root) %_libdir/libgtkhex.la
%_libdir/pkgconfig/gtkhex.pc
%_includedir/gtkhex/
