Summary:	BitTorrent program for KDE
Name:		ktorrent
Version:	4.3.1
Release:	11
Group:		Networking/File transfer
License:	GPLv2+
Url:		http://ktorrent.org/
Source0:	http://ktorrent.org/downloads/%{version}/%{name}-%{version}.tar.bz2
Patch0:		ktorrent-4.3.1-add-missing-linkage.patch
# enable DHT by default as it's strongly recommended for magnet links which
# have now become more common than .torrent files, while ktorrent also behaves
# better now with DHT enabled than in the past
Patch1:		ktorrent-4.3.1-enable-dht-by-default.patch

BuildRequires:	boost-devel
BuildRequires:	gmp-devel
BuildRequires:	kdebase4-workspace-devel
BuildRequires:	kdepimlibs4-devel
BuildRequires:	libktorrent-devel >= 1.3.0
BuildRequires:	pkgconfig(qca2)
BuildRequires:	pkgconfig(taglib)

%description
KTorrent is a BitTorrent program for KDE. Its main features are:
 o Downloads torrent files
 o Upload speed capping, seeing that most people can't upload
   infinite amounts of data.
 o Internet searching using  The Bittorrent website's search engine
 o UDP Trackers

%files -f %{name}.lang
%{_kde_bindir}/*
%{_kde_libdir}/kde4/*
%{_kde_datadir}/apps/%{name}
%{_kde_datadir}/applications/kde4/*
%{_kde_services}/*
%{_kde_servicetypes}/*
%{_kde_iconsdir}/*/*/*/*

#-------------------------------------------------------------------------

%define ktcore_major 15
%define libktcore %mklibname ktcore %{ktcore_major}

%package -n %{libktcore}
Summary:	Ktorrent libbrary
Group:		System/Libraries

%description -n %{libktcore}
KTorrent library.

%files -n %{libktcore}
%{_kde_libdir}/libktcore.so.%{ktcore_major}*

%prep
%setup -q
%apply_patches

%build
%cmake_kde4  -DCMAKE_MINIMUM_REQUIRED_VERSION=2.6
%make

%install
%makeinstall_std -C build

# make it preferred over kget:
echo "InitialPreference=5" >> %{buildroot}%{_kde_applicationsdir}/ktorrent.desktop

%find_lang %{name} --with-html

