Summary:	Thumbnail generator for raw images
Name:		raw-thumbnailer
Version:	3.0.0
Release:	1
License:	GPLv2+
Group:		Graphics
Url:		http://libopenraw.freedesktop.org/wiki/RawThumbnailer
Source0:	http://libopenraw.freedesktop.org/download/%{name}-%{version}.tar.bz2
BuildRequires:	pkgconfig(libopenraw-gnome-1.0)
BuildRequires:	intltool

%description
This simple program generates thumbnails of digital camera raw 
image files using libopenraw and GDK. It supports the same file 
formats as libopenraw.This thumbnailer is designed to be small,
lightweight and fast.

%prep
%setup -q

%build
%configure2_5x
%make

%install
%makeinstall_std

%files
%{_bindir}/%{name}
%{_datadir}/mime/packages/raw-thumbnailer.xml
%{_datadir}/thumbnailers/raw.thumbnailer

