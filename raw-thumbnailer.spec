Summary:	Thumbnail generator for raw images
Name:		raw-thumbnailer
Version:	0.99.1
Release:	%mkrel 1
License:	GPLv2+
Group:		Graphics
Url:		http://libopenraw.freedesktop.org/wiki/RawThumbnailer
Source0:	http://libopenraw.freedesktop.org/download/%{name}-%{version}.tar.bz2
BuildRequires:	libopenraw-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
This simple program generates thumbnails of digital camera raw 
image files using libopenraw and GDK. It supports the same file 
formats as libopenraw.This thumbnailer is designed to be small,
lightweight and fast. 

Usage: raw-thumbnailer -i input_file -o output_file -s size

%prep
%setup -q

%build
%configure2_5x

%make

%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%makeinstall_std

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%post
%post_install_gconf_schemas %{name}

%preun
%preun_uninstall_gconf_schemas %{name}

%files
%defattr(-,root,root)
%{_bindir}/%{name}
%{_sysconfdir}/gconf/schemas/raw-thumbnailer.schemas
%{_datadir}/mime/packages/raw-thumbnailer.xml
