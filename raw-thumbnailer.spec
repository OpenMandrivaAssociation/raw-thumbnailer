Summary:	Thumbnail generator for raw images
Name:		raw-thumbnailer
Version:	0.2
Release:	%mkrel 4
License:	GPLv2+
Group:		Graphics
Url:		http://code.google.com/p/raw-thumbnailer/
Source0:	http://code.google.com/p/raw-thumbnailer/downloads/%{name}-%{version}.tar.bz2
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

%files
%defattr(-,root,root)
%{_bindir}/%{name}