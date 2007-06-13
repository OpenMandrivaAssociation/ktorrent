
%define	name	ktorrent
%define	version 2.1.4
%define	rel	2



# Note that this package does not follow the library policy as the
# main package includes the libktorrent shared object. This is done
# because 1) the library is only used internally by ktorrent, and so
# it does never need to be installed separately, and 2) the %major
# follows %version, thus resulting in one unuseful library package
# in every ktorrent version upgrade. The only downside of not
# following the library policy on this particular package I know is
# rpmlint going nuts.
#
# Feel free to flame me if you do not like this...
# -Anssi

%define major	%version

Summary:	BitTorrent program for KDE
Name:		%{name}
Version:	%{version}
Release:	%mkrel %{rel}
Group:		Networking/File transfer
License:	GPL
Url:		http://ktorrent.org/
Source0:	http://ktorrent.org/downloads/%{version}/%{name}-%{version}.tar.bz2
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	gmp-devel
BuildRequires:	kdelibs-devel
Obsoletes:	%{_lib}ktorrent0 %{_lib}ktorrent2.1 %{_lib}ktorrent2.1.1
Obsoletes:	%{_lib}ktorrent2.1.2 %{_lib}ktorrent2.1.3

%description
KTorrent is a BitTorrent program for KDE. It's main features are:
 o Downloads torrent files
 o Upload speed capping, seeing that most people can't upload
   infinite amounts of data.
 o Internet searching using  The Bittorrent website's search engine
 o UDP Trackers

%files -f %{name}.lang
%defattr(-,root,root)
%doc AUTHORS README
%{_bindir}/*
%{_libdir}/kde3/*
%{_libdir}/libktorrent-%major.so
%{_datadir}/services/*
%{_datadir}/servicetypes/*
%{_datadir}/apps/%{name}
%{_menudir}/%{name}
%{_datadir}/applications/kde/%{name}.desktop
%{_datadir}/config.kcfg/*.kcfg
%{_iconsdir}/hicolor/scalable/apps/%{name}.svgz
%{_miconsdir}/%{name}.png
%{_iconsdir}/%{name}.png
%{_liconsdir}/%{name}.png
%{_iconsdir}/hicolor/*/apps/*.png
%{_iconsdir}/hicolor/*/mimetypes/*.png
%{_iconsdir}/hicolor/*/mimetypes/*.svgz

%prep
%setup -q

%build
make -f admin/Makefile.common cvs
%configure2_5x	--disable-debug \
		--enable-mt \
		--disable-static \
		--enable-shared \
		--disable-objprelink \
		--with-pic \
		--with-gnu-ld \
		--disable-rpath \
		--disable-embedded \
		--enable-fast-install=yes \
%if "%{_lib}" != "lib"
    --enable-libsuffix="%(A=%{_lib}; echo ${A/lib/})" \
%endif
		--with-qt-dir=%{_prefix}/lib/qt3 \
		--with-xinerama \
		--enable-final
%make
 
%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

install -d $RPM_BUILD_ROOT%{_menudir}
kdedesktop2mdkmenu.pl %{name} "Internet/File transfer" $RPM_BUILD_ROOT%{_datadir}/applications/kde/%name.desktop $RPM_BUILD_ROOT%{_menudir}/%{name}

install -m644 apps/ktorrent/hi16-app-ktorrent.png -D $RPM_BUILD_ROOT%{_miconsdir}/%{name}.png
install -m644 apps/ktorrent/hi32-app-ktorrent.png -D $RPM_BUILD_ROOT%{_iconsdir}/%{name}.png
install -m644 apps/ktorrent/hi48-app-ktorrent.png -D $RPM_BUILD_ROOT%{_liconsdir}/%{name}.png

%find_lang %{name}
rm -f $RPM_BUILD_ROOT%{_libdir}/libktorrent.{so,la}

#Fix Conflictss with kdelibs-common
rm -f $RPM_BUILD_ROOT%{_datadir}/mimelnk/application/x-bittorrent.desktop

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/ldconfig
%update_menus
%update_desktop_database
%update_icon_cache hicolor

%postun
/sbin/ldconfig
%clean_menus
%clean_desktop_database
%clean_icon_cache hicolor

# This is a workaround for #27417

