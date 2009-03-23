Summary:	Fully customisable dock-like window navigator for GNOME
Summary(pl.UTF-8):	W pełni konfigurowalny dokowy nawigator okien dla GNOME
Name:		avant-window-navigator
Version:	0.3.2
Release:	1
License:	GPL v2+
Group:		X11/Applications
Source0:	https://launchpad.net/awn/0.2/%{version}/+download/%{name}-%{version}.tar.gz
# Source0-md5:	e884bfaf9e3f4a7a99373227d7a24b5f
URL:		https://launchpad.net/awn/
BuildRequires:	GConf2-devel >= 2.14.0
BuildRequires:	autoconf
BuildRequires:	automake >= 1:1.8
BuildRequires:	dbus-glib-devel >= 0.30
BuildRequires:	gettext-devel
BuildRequires:	glib2-devel >= 1:2.16.0
BuildRequires:	gnome-desktop-devel >= 2.0
BuildRequires:	gnome-vfs2-devel >= 2.0
BuildRequires:	gtk+2-devel >= 2:2.10.0
BuildRequires:	gtk-doc >= 1.4
BuildRequires:	intltool >= 0.34
BuildRequires:	libgnome-devel
BuildRequires:	libtool
BuildRequires:	libwnck-devel >= 2.20.0
BuildRequires:	pkgconfig
BuildRequires:	python-devel >= 2.3.5
BuildRequires:	python-pycairo-devel >= 1.0.2
BuildRequires:	python-pygtk-devel >= 2:2.10.0
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.311
BuildRequires:	vala >= 0.5.4
BuildRequires:	xorg-lib-libXcomposite-devel
BuildRequires:	xorg-lib-libXdamage-devel
BuildRequires:	xorg-lib-libXrender-devel
Requires(post,postun):	/sbin/ldconfig
Requires(post,postun):	gtk+2 >= 2:2.10.0
Requires(post,postun):	hicolor-icon-theme
Requires(post,preun):	GConf2
Requires:	python-pycairo >= 1.0.2
Requires:	python-pygtk-glade >= 2:2.10.0
Requires:	python-pygtk-gtk >= 2:2.10.0
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
%{__aclocal}
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

# unsupported(?)
%{__rm} -r $RPM_BUILD_ROOT%{_localedir}/{bs,jv,ku,lv,mk,nds}

%{__rm} $RPM_BUILD_ROOT%{py_sitedir}/awn/awn.{la,a}
%py_postclean

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/ldconfig
%gconf_schema_install awn.schemas
%gconf_schema_install awn-applets-shared.schemas
%update_icon_cache hicolor

%preun
%gconf_schema_uninstall awn.schemas
%gconf_schema_uninstall awn-applets-shared.schemas

%postun
/sbin/ldconfig
%update_icon_cache hicolor

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%{_sysconfdir}/gconf/schemas/awn.schemas
%{_sysconfdir}/gconf/schemas/awn-applets-shared.schemas
%attr(755,root,root) %{_bindir}/avant-window-navigator
%attr(755,root,root) %{_bindir}/awn-autostart
%attr(755,root,root) %{_bindir}/awn-applet-activation
%attr(755,root,root) %{_bindir}/awn-applets-migration
%attr(755,root,root) %{_bindir}/awn-manager
%attr(755,root,root) %{_bindir}/awn-launcher-editor
%attr(755,root,root) %{_bindir}/awn-schema-to-gconf
%attr(755,root,root) %{_libdir}/libawn.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libawn.so.0
%{_datadir}/avant-window-navigator
%{_desktopdir}/awn-manager.desktop
%{_desktopdir}/avant-window-navigator.desktop
%dir %{py_libdir}/site-packages/awn
%dir %{py_sitescriptdir}/awn
%{py_sitescriptdir}/awn/__init__.py[co]
%attr(755,root,root) %{py_libdir}/site-packages/awn/awn.so
%{_iconsdir}/hicolor/24x24/apps/avant-window-navigator.png
%{_iconsdir}/hicolor/32x32/apps/avant-window-navigator.png
%{_iconsdir}/hicolor/48x48/apps/awn-manager.png
%{_iconsdir}/hicolor/48x48/apps/avant-window-navigator.png
%{_iconsdir}/hicolor/scalable/apps/awn-manager.svg
%{_iconsdir}/hicolor/scalable/apps/avant-window-navigator.svg

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libawn.so
%{_libdir}/libawn.la
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
