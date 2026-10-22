Summary:	Thumbnail generator for raw images
Name:		raw-thumbnailer
Version:	51.0.0
Release:	2
License:	GPLv2+
Group:		Graphics
Url:		https://libopenraw.freedesktop.org/wiki/RawThumbnailer
Source0:	https://gitlab.gnome.org/World/gnome-raw-thumbnailer/-/archive/%{version}/gnome-raw-thumbnailer-%{version}.tar.bz2
Source1:  vendor.tar.xz
BuildRequires:  cargo
BuildRequires:  git
BuildRequires:  rust-packaging
BuildRequires:  intltool
BuildRequires:  meson
BuildRequires:  pkgconfig(gdk-pixbuf-2.0)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(libopenraw-gnome-0.3)
Requires:       shared-mime-info

%description
This simple program generates thumbnails of digital camera raw 
image files using libopenraw and GDK. It supports the same file 
formats as libopenraw.This thumbnailer is designed to be small,
lightweight and fast.

%prep
%autosetup -n gnome-%{name}-%{version} -a1 -p1
%cargo_prep -v vendor

cat >>Cargo.toml <<EOF
[source.crates-io]
replace-with = "vendored-sources"

[source.vendored-sources]
directory = "vendor"
EOF

%build
%meson
%meson_build

%install
%meson_install

%files
%license COPYING
%doc NEWS ChangeLog
%{_bindir}/raw-thumbnailer
%dir %{_datadir}/thumbnailers
%{_datadir}/thumbnailers/raw.thumbnailer
%{_datadir}/mime/packages/raw-thumbnailer.xml
