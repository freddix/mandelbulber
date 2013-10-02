Summary:	3D fractal generator
Name:		mandelbulber
Version:	1.17
Release:	1
License:	GPL v3
Group:		X11/Applications
Source0:	http://mandelbulber.googlecode.com/files/%{name}%{version}.orig.tar.gz
# Source0-md5:	2d2b216ea6e72d2fd21d9de860647af8
BuildRequires:	gtk+-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel
BuildRequires:	libstdc++-devel
BuildRequires:	pkg-config
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Mandelbulb is a three-dimensional analogue of the Mandelbrot set.

%prep
%setup -qn %{name}%{version}.orig

%build
%{__make} -C makefiles all \
	CXXFLAGS="%{rpmcxxflags} %{rpmldflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_datadir}/%{name},%{_desktopdir},%{_pixmapsdir}}

install makefiles/mandelbulber $RPM_BUILD_ROOT%{_bindir}
cp -aR usr/share/* $RPM_BUILD_ROOT%{_datadir}/%{name}

install usr/share/icons/mandelbulber.png \
	$RPM_BUILD_ROOT%{_pixmapsdir}

cat > $RPM_BUILD_ROOT%{_desktopdir}/%{name}.desktop <<EOF
[Desktop Entry]
Type=Application
Exec=mandelbulber
Icon=mandelbulber
Terminal=false
Name=Mandelbulber
Comment=3D fractal generator
StartupNotify=true
Categories=GTK;Graphics;3DGraphics;
EOF

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc NEWS README
%attr(755,root,root) %{_bindir}/mandelbulber
%{_datadir}/%{name}
%{_desktopdir}/mandelbulber.desktop
%{_pixmapsdir}/mandelbulber.png

