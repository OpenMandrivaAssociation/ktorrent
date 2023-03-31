%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)
Summary:	BitTorrent program for KDE
Name:		ktorrent
Version:	22.12.3
Release:	2
Group:		Networking/File transfer
License:	GPLv2+
Url:		http://ktorrent.org/
Source0:	http://download.kde.org/%{stable}/release-service/%{version}/src/%{name}-%{version}.tar.xz
#Patch0:		ktorrent-4.3.1-add-missing-linkage.patch
# enable DHT by default as it's strongly recommended for magnet links which
# have now become more common than .torrent files, while ktorrent also behaves
# better now with DHT enabled than in the past
Patch1:		ktorrent-4.3.1-enable-dht-by-default.patch
#Patch2:		ktorrent-5.1.1-geoip.patch

BuildRequires:	boost-devel
BuildRequires:	gmp-devel
BuildRequires:	cmake(KF5Torrent) >= 2.1
BuildRequires:	pkgconfig(qca2-qt5)
BuildRequires:	pkgconfig(taglib)
BuildRequires:	pkgconfig(geoip)
BuildRequires:	cmake(Qt5Script)
BuildRequires:	cmake(Qt5Test)
BuildRequires:	cmake(Qt5WebEngineWidgets)
BuildRequires:	cmake(KF5I18n)
BuildRequires:	cmake(KF5Crash)
BuildRequires:	cmake(KF5KIO)
BuildRequires:	cmake(KF5Archive)
BuildRequires:	cmake(KF5KDE4Support)
BuildRequires:	cmake(KF5NotifyConfig)
BuildRequires:	cmake(KF5KCMUtils)
BuildRequires:	cmake(KF5Kross)
BuildRequires:	cmake(KF5KrossUi)
BuildRequires:	cmake(KF5WebKit)
BuildRequires:	cmake(LibKWorkspace)
BuildRequires:	cmake(KF5DNSSD)
BuildRequires:	cmake(KF5IconThemes)
BuildRequires:	cmake(KF5Plotting)
BuildRequires:	cmake(KF5Syndication)
BuildRequires:	cmake(Phonon4Qt5)
BuildRequires:	pkgconfig(libmaxminddb)
BuildRequires:	cmake
BuildRequires:	ninja
# For 2to3
BuildRequires:	python

%description
KTorrent is a BitTorrent program for KDE. Its main features are:
 o Downloads torrent files
 o Upload speed capping, seeing that most people can't upload
   infinite amounts of data.
 o Internet searching using  The Bittorrent website's search engine
 o UDP Trackers

%files -f %{name}.lang
%{_kde5_bindir}/*
%{_kde5_libdir}/qt5/plugins/%{name}_plugins/
%{_kde5_notificationsdir}/%{name}.notifyrc
%{_kde5_xmlguidir}/%{name}/*.rc
%{_kde5_applicationsdir}/org.kde.ktorrent.desktop
%{_kde5_iconsdir}/*/*/*/*
%{_datadir}/%{name}
%{_datadir}/metainfo/org.kde.ktorrent.appdata.xml


#-------------------------------------------------------------------------

%define ktcore_major 16
%define libktcore %mklibname ktcore %{ktcore_major}

%package -n %{libktcore}
Summary:	Ktorrent libbrary
Group:		System/Libraries

%description -n %{libktcore}
KTorrent library.

%files -n %{libktcore}
%{_kde5_libdir}/libktcore.so.%{ktcore_major}*

%prep
%autosetup -p1
find . -name "*.py" |xargs 2to3 -w

%build
%cmake_kde5 -DWITH_SYSTEM_GEOIP=ON
%ninja

%install
%ninja_install -C build

# make it preferred over kget:
echo "InitialPreference=10" >> %{buildroot}%{_kde5_applicationsdir}/org.kde.ktorrent.desktop

%find_lang %{name} --with-html
