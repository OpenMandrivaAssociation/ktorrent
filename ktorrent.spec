%define major %version

Name: ktorrent
Version: 3.1
Release: %mkrel 0.beta2.1
Summary: BitTorrent program for KDE
Group: Networking/File transfer
License: GPLv2+
Url: http://ktorrent.org/
Source0: http://ktorrent.org/downloads/%{version}/%{name}-%{version}beta2.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: gmp-devel
BuildRequires: kdelibs4-devel
BuildRequires: qca2-devel
Obsoletes: %{_lib}ktorrent0 
Obsoletes: %{_lib}ktorrent2.1 
Obsoletes: %{_lib}ktorrent2.1.1
Obsoletes: %{_lib}ktorrent2.1.2 
Obsoletes: %{_lib}ktorrent2.1.3
Obsoletes: kde4-ktorrent < 1:3.0.1
Provides:  kde4-ktorrent = 1:%version

%description
KTorrent is a BitTorrent program for KDE. It's main features are:
 o Downloads torrent files
 o Upload speed capping, seeing that most people can't upload
   infinite amounts of data.
 o Internet searching using  The Bittorrent website's search engine
 o UDP Trackers

%post
%update_desktop_database
%update_icon_cache hicolor

%postun
%clean_desktop_database
%clean_icon_cache hicolor

%files -f %{name}.lang
%defattr(-,root,root)
%{_kde_bindir}/*
%{_kde_libdir}/kde4/*
%{_kde_datadir}/apps/%{name}
%{_kde_datadir}/applications/kde4/*
%{_kde_services}/*
%{_kde_servicetypes}/*
%{_kde_iconsdir}/*/*/*/*

#-------------------------------------------------------------------------

%define btcore_major 4
%define libbtcore %mklibname btcore %btcore_major

%package -n %libbtcore
Summary:    Ktorrent libbrary
Group:      System/Libraries
Obsoletes:  %{_lib}btcore1 < 4.0.0-2
Obsoletes:  %{_lib}btcore2 < 3.0-0.rc1.3
Obsoletes:  %{_lib}btcore3 < 3.1-0.beta1.2

%description -n %libbtcore
KTorrent library.

%post -n %libbtcore -p /sbin/ldconfig
%postun -n %libbtcore -p /sbin/ldconfig

%files -n %libbtcore
%defattr(-,root,root)
%{_kde_libdir}/libbtcore.so.%{btcore_major}*

#-------------------------------------------------------------------------

%define ktcore_major 4
%define libktcore %mklibname ktcore %ktcore_major

%package -n %libktcore
Summary:    Ktorrent libbrary
Group:      System/Libraries
Obsoletes:  %{_lib}ktcore1 < 4.0.0-2
Obsoletes:  %{_lib}ktcore2 < 3.0-0.rc1.3
Obsoletes:  %{_lib}ktcore3 < 3.1-0.beta1.2

%description -n %libktcore
KTorrent library.

%post -n %libktcore -p /sbin/ldconfig
%postun -n %libktcore -p /sbin/ldconfig

%files -n %libktcore
%defattr(-,root,root)
%{_kde_libdir}/libktcore.so.%{ktcore_major}*

#-------------------------------------------------------------------------

%define ktupnp_major 1
%define libktupnp %mklibname ktupnp %ktupnp_major

%package -n %libktupnp
Summary: Ktorrent libbrary
Group: System/Libraries

%description -n %libktupnp
KTorrent library.

%post -n %libktupnp -p /sbin/ldconfig
%postun -n %libktupnp -p /sbin/ldconfig

%files -n %libktupnp
%defattr(-,root,root)
%{_kde_libdir}/libktupnp.so.%{ktupnp_major}*

#-------------------------------------------------------------------------

%package devel
Summary: Ktorrent plugin devel headers
Group: Networking/File transfer

%description devel
Ktorrent plugin devel headers.

%files devel
%defattr(-,root,root)
%{_kde_includedir}/*
%{_kde_appsdir}/cmake/*/*
%{_kde_libdir}/*.so

#-------------------------------------------------------------------------

%prep
%setup -q -n %name-%{version}beta2

%build
%cmake_kde4 

%make
 
%install
rm -rf %buildroot

make -C build DESTDIR=%buildroot install  

%find_lang %{name}

%clean
rm -rf %buildroot

