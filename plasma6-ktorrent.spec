%define git 20240218
%define gitbranch release/24.02
%define gitbranchd %(echo %{gitbranch} |sed -e "s,/,-,g")
%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)
Summary:	BitTorrent program for KDE
Name:		plasma6-ktorrent
Version:	24.01.96
Release:	%{?git:0.%{git}.}1
Group:		Networking/File transfer
License:	GPLv2+
Url:		http://ktorrent.org/
%if 0%{?git:1}
Source0:	https://invent.kde.org/network/ktorrent/-/archive/%{gitbranch}/ktorrent-%{gitbranchd}.tar.bz2#/ktorrent-%{git}.tar.bz2
%else
Source0:	http://download.kde.org/%{stable}/release-service/%{version}/src/ktorrent-%{version}.tar.xz
%endif
#Patch0:		ktorrent-4.3.1-add-missing-linkage.patch
# enable DHT by default as it's strongly recommended for magnet links which
# have now become more common than .torrent files, while ktorrent also behaves
# better now with DHT enabled than in the past
Patch1:		ktorrent-4.3.1-enable-dht-by-default.patch
#Patch2:		ktorrent-5.1.1-geoip.patch

BuildRequires:	boost-devel
BuildRequires:	gmp-devel
BuildRequires:	cmake(KTorrent6) >= 2.1
BuildRequires:	pkgconfig(taglib)
BuildRequires:	pkgconfig(geoip)
BuildRequires:	cmake(Qt6Test)
BuildRequires:	cmake(Qt6WebEngineWidgets)
BuildRequires:	cmake(KF6I18n)
BuildRequires:	cmake(KF6Crash)
BuildRequires:	cmake(KF6KIO)
BuildRequires:	cmake(KF6Archive)
BuildRequires:	cmake(KF6NotifyConfig)
BuildRequires:	cmake(KF6KCMUtils)
BuildRequires:	cmake(LibKWorkspace) > 5.90.0
BuildRequires:	cmake(KF6DNSSD)
BuildRequires:	cmake(KF6IconThemes)
BuildRequires:	cmake(KF6Plotting)
BuildRequires:	cmake(KF6Syndication)
BuildRequires:	cmake(Phonon4Qt6)
BuildRequires:	pkgconfig(libmaxminddb)
BuildRequires:	cmake
BuildRequires:	ninja

%description
KTorrent is a BitTorrent program for KDE. Its main features are:
 o Downloads torrent files
 o Upload speed capping, seeing that most people can't upload
   infinite amounts of data.
 o Internet searching using  The Bittorrent website's search engine
 o UDP Trackers

%files -f ktorrent.lang
%{_bindir}/*
%{_qtdir}/plugins/ktorrent_plugins/
%{_datadir}/knotifications6/ktorrent.notifyrc
%{_datadir}/kxmlgui5/ktorrent
%{_datadir}/applications/org.kde.ktorrent.desktop
%{_iconsdir}/*/*/*/*
%{_datadir}/ktorrent
%{_datadir}/metainfo/org.kde.ktorrent.appdata.xml
%{_libdir}/libktcore.so*

%prep
%autosetup -p1 -n ktorrent-%{?git:%{gitbranchd}}%{!?git:%{version}}
%cmake -DWITH_SYSTEM_GEOIP=ON \
	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON \
	-G Ninja

%build
%ninja_build -C build

%install
%ninja_install -C build

# make it preferred over kget:
echo "InitialPreference=10" >> %{buildroot}%{_kde5_applicationsdir}/org.kde.ktorrent.desktop

%find_lang ktorrent --with-html
