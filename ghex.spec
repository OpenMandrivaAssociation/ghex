%define api		3
%define major		0
%define libname		%mklibname gtkhex %{api} %{major}
%define develname	%mklibname -d gtkhex

%define _disable_rebuild_configure 1

Summary:	GNOME Hexadecimal Editor

Name:		ghex
Version:	3.41.0
Release:	1
License:	GPLv2+
Group:		Editors
Url:		http://live.gnome.org/Ghex
Source0:	https://download.gnome.org/sources/ghex/3.10/%{name}-%{version}.tar.xz

BuildRequires:	meson
BuildRequires:	gettext
BuildRequires:	intltool
BuildRequires:	itstool
BuildRequires:	perl-XML-Parser
BuildRequires:	desktop-file-utils
BuildRequires:	pkgconfig(gail-3.0)
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
%doc AUTHORS README
%{_bindir}/*
%{_datadir}/applications/*
%{_datadir}/icons/hicolor/*/apps/org.gnome.GHex.png
%{_datadir}/icons//hicolor/scalable/apps/org.gnome.GHex-symbolic.svg
#{_datadir}/GConf/gsettings/ghex.convert
%{_datadir}/glib-2.0/schemas/org.gnome.GHex.gschema.xml
%{_datadir}/metainfo/org.gnome.GHex.appdata.xml 

%files -n %{libname}
%{_libdir}/libgtkhex-%{api}.so.%{major}*

%files -n %{develname}
%{_libdir}/libgtkhex-%{api}.so
%{_libdir}/pkgconfig/gtkhex-%{api}.pc
%{_includedir}/gtkhex-%{api}



