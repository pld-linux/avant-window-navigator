#
# TODO: Complete buildrequires
#
Summary:	Fully customisable dock-like window navigator for GNOME
Summary(pl.UTF-8):	W pełni konfigurowalny dokowy nawigator okien dla GNOME
Name:		avant-window-navigator
%define snap 20070619
Version:	0.1.1
Release:	1.%{snap}
License:	GPL
Group:		X11/Applications
#Source0:	http://avant-window-navigator.googlecode.com/files/%{name}-%{version}-2.tar.gz
Source0:	%{name}-%{version}.tar.gz
# Source0-md5:	97e74929b15f19b8b73edfe9db1912ef
URL:		http://code.google.com/p/avant-window-navigator/
BuildRequires:	GConf2-devel >= 2.14.0
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	gnome-common >= 2.12.0
BuildRequires:	gnome-doc-utils >= 0.7.1
BuildRequires:	gtk+2-devel >= 2:2.10.0
BuildRequires:	intltool >= 0.35
BuildRequires:	libglade2-devel >= 1:2.6.0
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.197
Requires(post,postun):	gtk+2 >= 2:2.10.0
Requires(post,preun):	GConf2 >= 2.14.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Avant Window Navigator (Awn) is a dock-like bar which sits at the
bottom of the screen (in all its composited-goodness) tracking open
windows.

%description -l pl.UTF-8
Avant Window Navigator (Awn) to pasek podobny do doku umiejscowiony na
dole ekranu śledzący otwarte okna.

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

mv $RPM_BUILD_ROOT%{_datadir}/locale/de{_DE,}
mv $RPM_BUILD_ROOT%{_datadir}/locale/el{_GR,}
mv $RPM_BUILD_ROOT%{_datadir}/locale/fi{_FI,}
mv $RPM_BUILD_ROOT%{_datadir}/locale/fr{_FR,}
mv $RPM_BUILD_ROOT%{_datadir}/locale/it{_IT,}

%find_lang %{name} --with-gnome --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%post
%scrollkeeper_update_post
#%%gconf_schema_install %{name}.schemas
gtk-update-icon-cache -qf %{_datadir}/icons/hicolor
/sbin/ldconfig

%preun
%gconf_schema_uninstall switcher.schemas trash.schemas

%postun
%scrollkeeper_update_postun
gtk-update-icon-cache -qf %{_datadir}/icons/hicolor
/sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%{_sysconfdir}/gconf/schemas/switcher.schemas
%{_sysconfdir}/gconf/schemas/trash.schemas
%attr(755,root,root) %{_bindir}/avant-applets
%attr(755,root,root) %{_bindir}/avant-launchers
%attr(755,root,root) %{_bindir}/avant-preferences
%attr(755,root,root) %{_bindir}/avant-window-navigator
%attr(755,root,root) %{_bindir}/awn-applet-activation
%{_desktopdir}/avant-preferences.desktop
%{_desktopdir}/avant-window-navigator.desktop
%dir %{_datadir}/avant-window-navigator
%dir %{_datadir}/avant-window-navigator/active
%{_datadir}/avant-window-navigator/active/*.png
%{_datadir}/avant-window-navigator/*.png
%{_datadir}/avant-window-navigator/*.svg
%{_datadir}/avant-window-navigator/*.glade
%{_libdir}/*.so.*.*.*
%dir %{_libdir}/awn
%dir %{_libdir}/awn/applets
%{_libdir}/awn/applets/*.desktop
%dir %{_libdir}/awn/applets/switcher
%attr(755,root,root) %{_libdir}/awn/applets/switcher/switcher.so
%dir %{_libdir}/awn/applets/trash
%attr(755,root,root) %{_libdir}/awn/applets/trash/trash.so
%{_libdir}/awn/applets/trash/trashapplet.glade
