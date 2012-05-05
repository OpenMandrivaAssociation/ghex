%define url_ver %(echo %{version} | cut -d. -f1,2)

%define api		3
%define major		0
%define libname		%mklibname gtkhex %{api} %{major}
%define libnamedev	%mklibname -d gtkhex

Name:		ghex
Summary:	GNOME Hexadecimal Editor
Version:	3.4.0
Release:	1
License:	GPLv2+
Group:		Editors
Url:		http://live.gnome.org/Ghex
Source0:	http://download.gnome.org/sources/%{name}/%{url_ver}/%{name}-%{version}.tar.xz
BuildRequires:	intltool
BuildRequires:	desktop-file-utils
BuildRequires:	pkgconfig(gtk+-3.0) >= 3.0
BuildRequires:	pkgconfig(gconf-2.0)
BuildRequires:	pkgconfig(gail-3.0)
BuildRequires:	pkgconfig(xml2po)
BuildRequires:	gnome-doc-utils
BuildRequires:	gettext
BuildRequires:	perl-XML-Parser

%description
GHex allows the user to load data from any file, view and edit it in either
hex or ascii. A must for anyone playing games that use non-ascii format for
saving.

%package -n %{libname}
Summary:	Shared library of the GNOME Hexadecimal Editor
Group:		System/Libraries

%description -n %{libname}
GHex allows the user to load data from any file, view and edit it in either
hex or ascii. A must for anyone playing games that use non-ascii format for
saving.

This contains the shared library needed by ghex.
 
%package -n %{libnamedev}
Summary:	Development files for the GNOME Hexadecimal Editor library 
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
Provides:	libgtkhex-devel = %{version}-%{release}

%description -n %{libnamedev}
GHex allows the user to load data from any file, view and edit it in either
hex or ascii. A must for anyone playing games that use non-ascii format for
saving.

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
  --dir %{buildroot}%{_datadir}/applications %{buildroot}%{_datadir}/applications/*

%{find_lang} %{name}-%{api} --with-gnome --all-name

#for omf in %{buildroot}%{_datadir}/omf/*/*-??*.omf;do 
#echo "%lang($(basename $omf|sed -e s/.*-// -e s/.omf//)) $(echo $omf|sed -e s!%{buildroot}!!)" >> %{name}-%{api}.lang
#done

#we don't want these
rm -rf %{buildroot}%{_libdir}/*.la


%files -f %{name}-%{api}.lang
%doc AUTHORS README ChangeLog
%{_bindir}/*
%{_datadir}/applications/*
%{_datadir}/icons/hicolor/*/apps/*ghex.*
%{_datadir}/GConf/gsettings/ghex.convert
%{_datadir}/glib-2.0/schemas/org.gnome.GHex.gschema.xml

%files -n %{libname}
%{_libdir}/libgtkhex-%{api}.so.%{major}*

%files -n %{libnamedev}
%{_libdir}/libgtkhex-%{api}.so
%{_libdir}/pkgconfig/gtkhex-%{api}.pc
%{_includedir}/gtkhex-%{api}
