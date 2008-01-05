#
# TODO: Complete buildrequires, -devel deps
#
Summary:	Fully customisable dock-like window navigator for GNOME
Summary(pl.UTF-8):	W pełni konfigurowalny dokowy nawigator okien dla GNOME
Name:		avant-window-navigator
Version:	0.2
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	https://launchpad.net/awn/0.2/0.2/+download/avant-window-navigator-0.2.tar
# Source0-md5:	ca6e741c833ca99a5dc4a8ad1d024147
URL:		https://launchpad.net/awn
BuildRequires:	GConf2-devel >= 2.14.0
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	gnome-common >= 2.12.0
BuildRequires:	gnome-desktop-devel
BuildRequires:	gnome-doc-utils >= 0.7.1
BuildRequires:	gtk+2-devel >= 2:2.10.0
BuildRequires:	intltool >= 0.35
BuildRequires:	libglade2-devel >= 1:2.6.0
BuildRequires:	libtool
BuildRequires:	libwnck-devel
BuildRequires:	pkgconfig
BuildRequires:	python-gnome-devel
BuildRequires:	python-pycairo-devel
BuildRequires:	rpmbuild(macros) >= 1.311
Requires(post,postun):	/sbin/ldconfig
Requires(post,postun):	gtk+2 >= 2:2.10.0
Requires(post,postun):	hicolor-icon-theme
Requires(post,preun):	GConf2 >= 2.14.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Avant Window Navigator (Awn) is a dock-like bar which sits at the
bottom of the screen (in all its composited-goodness) tracking open
windows.

%description -l pl.UTF-8
Avant Window Navigator (Awn) to pasek podobny do doku umiejscowiony na
dole ekranu śledzący otwarte okna.

%package devel
Summary:	Headers for avant window manager library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki zarządcy okien avant
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Headers for avant window manager library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki zarządcy okien avant.

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
	--disable-schemas-install
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL=1

#mv $RPM_BUILD_ROOT%{_datadir}/locale/de{_DE,}
#mv $RPM_BUILD_ROOT%{_datadir}/locale/el{_GR,}
#mv $RPM_BUILD_ROOT%{_datadir}/locale/fi{_FI,}
#mv $RPM_BUILD_ROOT%{_datadir}/locale/fr{_FR,}
#mv $RPM_BUILD_ROOT%{_datadir}/locale/it{_IT,}

rm -f $RPM_BUILD_ROOT%{py_sitedir}/awn/awn.la

%find_lang %{name} --with-gnome --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/ldconfig
#%%gconf_schema_install %{name}.schemas
%update_icon_cache hicolor

%preun
#%%gconf_schema_uninstall switcher.schemas trash.schemas

%postun
%update_icon_cache hicolor
/sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
#%{_sysconfdir}/gconf/schemas/switcher.schemas
#%{_sysconfdir}/gconf/schemas/trash.schemas
%attr(755,root,root) %{_bindir}/avant-window-navigator
%attr(755,root,root) %{_bindir}/awn-applet-activation
%attr(755,root,root) %{_bindir}/awn-manager
%attr(755,root,root) %{_libdir}/libawn.so.*.*.*
%dir %{_libdir}/awn
%dir %{_libdir}/awn/applets
%{_libdir}/awn/applets/*.desktop
%{_datadir}/avant-window-navigator
%{_desktopdir}/awn-manager.desktop
%{_desktopdir}/avant-window-navigator.desktop
%dir %{py_sitedir}/awn
%{py_sitedir}/awn/*.py[co]
%attr(755,root,root) %{py_sitedir}/awn/awn.so

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libawn.so
%{_libdir}/libawn.la
%{_includedir}/libawn
%{_pkgconfigdir}/awn.pc
