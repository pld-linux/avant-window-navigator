Summary:	Fully customisable dock-like window navigator for GNOME
Summary(pl.UTF-8):	W pełni konfigurowalny dokowy nawigator okien dla GNOME
Name:		avant-window-navigator
Version:	0.2.1
Release:	1
License:	GPL v2+
Group:		X11/Applications
Source0:	https://launchpad.net/awn/0.2/%{version}/+download/avant-window-navigator-%{version}.tar
# Source0-md5:	59733ce392d58236338736f6726cac9d
URL:		https://launchpad.net/awn/
BuildRequires:	GConf2-devel >= 2.14.0
BuildRequires:	autoconf
BuildRequires:	automake >= 1:1.8
BuildRequires:	dbus-glib-devel >= 0.30
BuildRequires:	gettext-devel
BuildRequires:	gnome-desktop-devel >= 2.0
BuildRequires:	gnome-doc-utils >= 0.7.1
BuildRequires:	gnome-vfs2-devel >= 2.0
BuildRequires:	gtk+2-devel >= 2:2.10.0
BuildRequires:	intltool >= 0.34
BuildRequires:	libglade2-devel >= 1:2.6.0
BuildRequires:	libtool
BuildRequires:	libwnck-devel >= 2.20.0
BuildRequires:	pkgconfig
BuildRequires:	python-devel >= 2.3.5
BuildRequires:	python-gnome-devel
BuildRequires:	python-pycairo-devel >= 1.0.2
BuildRequires:	python-pygtk-devel >= 2:2.8.0
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.311
BuildRequires:	xorg-lib-libXcomposite-devel
BuildRequires:	xorg-lib-libXdamage-devel
BuildRequires:	xorg-lib-libXrender-devel
Requires(post,postun):	/sbin/ldconfig
Requires(post,postun):	gtk+2 >= 2:2.10.0
Requires(post,postun):	hicolor-icon-theme
Requires:	python-pycairo >= 1.0.2
Requires:	python-pygtk-gtk >= 2:2.8.0
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
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	GConf2-devel >= 2.14.0
Requires:	dbus-glib-devel >= 0.30
Requires:	gnome-desktop-devel >= 2.0
Requires:	gnome-vfs2-devel >= 2.0
Requires:	gtk+2-devel >= 2:2.10.0
Requires:	libglade2-devel >= 1:2.6.0
Requires:	libwnck-devel >= 2.20.0
Requires:	xorg-lib-libXcomposite-devel
Requires:	xorg-lib-libXdamage-devel
Requires:	xorg-lib-libXrender-devel

%description devel
Headers for avant window navigator library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki nawigatora okien avant.

%package static
Summary:	Static avant window navigator library
Summary(pl.UTF-8):	Statyczna biblioteka nawigatora okien avant
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static avant window navigator library.

%description static -l pl.UTF-8
Statyczna biblioteka nawigatora okien avant.

%prep
%setup -q

%build
%{__intltoolize}
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# there are more complete de,fi,fr,it,ru,nb already
rm -r $RPM_BUILD_ROOT%{_datadir}/locale/{de_DE,fi_FI,fr_FR,it_IT,ru_RU,no_NO}

rm -f $RPM_BUILD_ROOT%{py_sitedir}/awn/awn.{la,a}
%py_postclean

%find_lang %{name} --with-gnome --all-name

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
%doc AUTHORS ChangeLog README TODO
%attr(755,root,root) %{_bindir}/avant-window-navigator
%attr(755,root,root) %{_bindir}/awn-applet-activation
%attr(755,root,root) %{_bindir}/awn-manager
%attr(755,root,root) %{_libdir}/libawn.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libawn.so.0
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

%files static
%defattr(644,root,root,755)
%{_libdir}/libawn.a
