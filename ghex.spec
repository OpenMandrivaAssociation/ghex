%define api		4
%define major		1
%define libname		%mklibname gtkhex %{api} %{major}
%define girname		%mklibname gtkhex-gir %{api}
%define develname	%mklibname -d gtkhex

%define _disable_rebuild_configure 1
%global url_ver %%(echo %{version} | cut -d. -f1)

Summary:	GNOME Hexadecimal Editor

Name:		ghex
Version:	46.2
Release:	1
License:	GPLv2+
Group:		Editors
Url:		https://live.gnome.org/Ghex
Source0:	https://download.gnome.org/sources/ghex/%{ulr_ver}/%{name}-%{version}.tar.xz

BuildRequires:	meson
BuildRequires:	gettext
BuildRequires:	intltool
BuildRequires:	itstool
BuildRequires:	perl-XML-Parser
BuildRequires:	desktop-file-utils
BuildRequires:	pkgconfig(gobject-introspection-1.0)
BuildRequires:	pkgconfig(gail-3.0)
BuildRequires:	pkgconfig(gnome-doc-utils)
BuildRequires:	pkgconfig(gtk4)
BuildRequires:	pkgconfig(xml2po)
BuildRequires:  pkgconfig(libadwaita-1)

Requires:	%{libname} = %{version}-%{release}

%description
GHex allows the user to load data from any file, view and edit it in either
hex or ascii. A must for anyone playing games that use non-ascii format for
saving.

%package -n %{libname}
Summary:	Shared library of the GNOME Hexadecimal Editor

Group:		System/Libraries

%description -n %{libname}
This contains the shared library needed by ghex.

%package -n %{girname}
Summary:	GObject Introspection interface description for Hex
Group:		System/Libraries
Requires:	%{libname} = %{version}-%{release}

%description -n %{girname}
GObject Introspection interface description for Hex.
 
%package -n %{develname}
Summary:	Development files for the GNOME Hexadecimal Editor library 

Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
Requires:	%{girname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description -n %{develname}
This contains the development files needed to compile applications with 
libghex.

%prep
%setup -q -n %{name}-%{version}

%build
%meson
%meson_build

%install
%meson_install

desktop-file-install --vendor="" \
	--remove-category="Application" \
	--add-category="X-MandrivaLinux-MoreApplications-Editors" \
	--dir %{buildroot}%{_datadir}/applications \
	%{buildroot}%{_datadir}/applications/*

%find_lang %{name}-%{api} --with-gnome --all-name

%files -f %{name}-%{api}.lang
%doc README.md
%{_bindir}/*
%{_datadir}/applications/*
%{_datadir}/glib-2.0/schemas/org.gnome.GHex.gschema.xml
%{_datadir}/metainfo/org.gnome.GHex.appdata.xml
%{_iconsdir}/hicolor/scalable/apps/org.gnome.GHex.Devel.svg
%{_iconsdir}/hicolor/scalable/apps/org.gnome.GHex.svg
%{_iconsdir}/hicolor/symbolic/apps/org.gnome.GHex-symbolic.svg

%files -n %{libname}
%{_libdir}/libgtkhex-%{api}.so.%{major}*
%{_libdir}/gtkhex-%{api}.0/libhex-buffer-mmap.so
%{_libdir}/gtkhex-4.0/libhex-buffer-direct.so

%files -n %{girname}
%{_libdir}/girepository-1.0/Hex-%{api}.typelib

%files -n %{develname}
%{_libdir}/libgtkhex-%{api}.so
%{_libdir}/pkgconfig/gtkhex-%{api}.pc
%{_includedir}/gtkhex-%{api}
%{_datadir}/gir-1.0/Hex-%{api}.gir
