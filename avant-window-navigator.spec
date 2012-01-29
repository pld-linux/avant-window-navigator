Summary:	Fully customisable dock-like window navigator for GNOME
Summary(pl.UTF-8):	W pełni konfigurowalny dokowy nawigator okien dla GNOME
Name:		avant-window-navigator
Version:	0.4.0
Release:	1
License:	GPL v2+
Group:		X11/Applications
Source0:	http://launchpad.net/awn/0.4/%{version}/+download/%{name}-%{version}.tar.gz
# Source0-md5:	03654b45dd95cbb83fa7e112bd00523c
URL:		https://launchpad.net/awn/
BuildRequires:	GConf2-devel >= 2.14.0
BuildRequires:	autoconf
BuildRequires:	automake >= 1:1.8
BuildRequires:	dbus-glib-devel >= 0.80
BuildRequires:	docbook-dtd412-xml
BuildRequires:	gettext-devel
BuildRequires:	glib2-devel >= 1:2.16.0
BuildRequires:	gnome-desktop-devel >= 2.0
BuildRequires:	gnome-vfs2-devel >= 2.0
BuildRequires:	gtk+2-devel >= 2:2.12.0
BuildRequires:	gtk-doc >= 1.4
BuildRequires:	intltool >= 0.34
BuildRequires:	libdesktop-agnostic-devel >= 0.3.9
BuildRequires:	libgnome-devel
BuildRequires:	libtool
BuildRequires:	libwnck2-devel >= 2.22
BuildRequires:	pkgconfig
BuildRequires:	python-devel >= 2.3.5
BuildRequires:	python-pycairo-devel >= 1.0.2
BuildRequires:	python-pygtk-devel >= 2:2.12.0
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.311
BuildRequires:	vala >= 0.7.10
BuildRequires:	xorg-lib-libXcomposite-devel
BuildRequires:	xorg-lib-libXdamage-devel
BuildRequires:	xorg-lib-libXrender-devel
Requires(post,postun):	/sbin/ldconfig
Requires(post,postun):	gtk-update-icon-cache
Requires(post,postun):	hicolor-icon-theme
Requires:	python-pycairo >= 1.0.2
Requires:	python-pygtk-glade >= 2:2.12.0
Requires:	python-pygtk-gtk >= 2:2.12.0
Requires:	python-pyxdg
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Avant Window Navigator (Awn) is a dock-like bar which sits at the
bottom of the screen (in all its composited-goodness) tracking open
windows.

%description -l pl.UTF-8
Avant Window Navigator (Awn) to pasek podobny do doku umiejscowiony na
dole ekranu śledzący otwarte okna.

%package devel
Summary:	Headers for avant window navigator library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki nawigatora okien avant
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	GConf2-devel >= 2.14.0
Requires:	dbus-glib-devel >= 0.30
Requires:	glib2-devel >= 1:2.16.0
Requires:	gnome-desktop-devel >= 2.0
Requires:	gnome-vfs2-devel >= 2.0
Requires:	gtk+2-devel >= 2:2.10.0

%description devel
Headers for avant window navigator library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki nawigatora okien avant.

%package static
Summary:	Static avant window navigator library
Summary(pl.UTF-8):	Statyczna biblioteka nawigatora okien avant
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static avant window navigator library.

%description static -l pl.UTF-8
Statyczna biblioteka nawigatora okien avant.

%package apidocs
Summary:	libawn library API documentation
Summary(pl.UTF-8):	Dokumentacja API biblioteki libawn
Group:		Documentation
Requires:	gtk-doc-common

%description apidocs
libawn library API documentation.

%description apidocs -l pl.UTF-8
Dokumentacja API biblioteki libawn.

%package -n vala-avant-window-navigator
Summary:	Vala bindings to libawn library
Summary(pl.UTF-8):	Wiązania Vala do biblioteki libawn
Group:		Development/Libraries

%description -n vala-avant-window-navigator
Vala bindings to libawn library.

%description -n vala-avant-window-navigator -l pl.UTF-8
Wiązania Vala do biblioteki libawn.

%prep
%setup -q

%build
%{__intltoolize}
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--enable-gtk-doc \
	--with-html-dir=%{_gtkdocdir} \
	--disable-pymod-checks \
	--disable-schemas-install

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# not supported by glibc (as for 2.13-3)
%{__rm} -r $RPM_BUILD_ROOT%{_localedir}/jv

%{__rm} $RPM_BUILD_ROOT%{_libdir}/*.la
%{__rm} $RPM_BUILD_ROOT%{_libdir}/awn/applets/*/*.{a,la}
%{__rm} $RPM_BUILD_ROOT%{py_sitedir}/awn/awn.{la,a}

%py_postclean

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/ldconfig
%update_icon_cache hicolor

%postun
/sbin/ldconfig
%update_icon_cache hicolor

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_bindir}/avant-window-navigator
%attr(755,root,root) %{_bindir}/awn-applet
%attr(755,root,root) %{_bindir}/awn-settings
%attr(755,root,root) %{_libdir}/libawn.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libawn.so.1
%dir %{_libdir}/awn
%dir %{_libdir}/awn/applets
%dir %{_libdir}/awn/applets/expander
%{_libdir}/awn/applets/expander/expander.so
%dir %{_libdir}/awn/applets/quick-prefs
%{_libdir}/awn/applets/quick-prefs/quick-prefs.so
%dir %{_libdir}/awn/applets/separator
%{_libdir}/awn/applets/separator/separator.so
%dir %{_libdir}/awn/applets/taskmanager
%{_libdir}/awn/applets/taskmanager/taskmanager.so
%{_datadir}/avant-window-navigator

%dir %{py_sitedir}/awn
%{py_sitedir}/awn/__init__.py[co]
%attr(755,root,root) %{py_sitedir}/awn/awn.so
%{_desktopdir}/awn-settings.desktop
%{_desktopdir}/avant-window-navigator.desktop
%{_iconsdir}/hicolor/*/apps/awn-settings.*
%{_iconsdir}/hicolor/*/apps/avant-window-navigator.*
%{_iconsdir}/hicolor/scalable/apps/awn-window-fallback.svg
%{_iconsdir}/hicolor/scalable/categories/awn-plugins.svg

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libawn.so
%{_datadir}/pygtk/2.0/defs/awn.defs
%{_includedir}/libawn
%{_pkgconfigdir}/awn.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libawn.a

%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/libawn

%files -n vala-avant-window-navigator
%defattr(644,root,root,755)
%{_datadir}/vala/vapi/awn.deps
%{_datadir}/vala/vapi/awn.vapi
