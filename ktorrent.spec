%define major %version

Name: ktorrent
Version: 3.0.1
Release: %mkrel 1
Summary: BitTorrent program for KDE
Group: Networking/File transfer
License: GPLv2+
Url: http://ktorrent.org/
Source0: http://ktorrent.org/downloads/%{version}/%{name}-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: gmp-devel
BuildRequires: kdelibs4-devel
BuildRequires: qca2-devel
Obsoletes: %{_lib}ktorrent0 %{_lib}ktorrent2.1 %{_lib}ktorrent2.1.1
Obsoletes: %{_lib}ktorrent2.1.2 %{_lib}ktorrent2.1.3

%description
KTorrent is a BitTorrent program for KDE. It's main features are:
 o Downloads torrent files
 o Upload speed capping, seeing that most people can't upload
   infinite amounts of data.
 o Internet searching using  The Bittorrent website's search engine
 o UDP Trackers

%post
%update_menus

%postun
%clean_menus

%files -f %{name}.lang
%defattr(-,root,root)
%{_kde_bindir}/*
%{_kde_libdir}/kde4/*
%{_kde_datadir}/apps/%{name}
%{_kde_datadir}/applications/kde4/*
%{_kde_services}/*
%{_kde_servicetypes}/*
%{_iconsdir}/*/*/*/*

#-------------------------------------------------------------------------

%define libbtcore %mklibname btcore 3

%package -n %libbtcore
Summary: Ktorrent libbrary
Group: System/Libraries

%description -n %libbtcore
KTorrent library.

%post -n %libbtcore -p /sbin/ldconfig
%postun -n %libbtcore -p /sbin/ldconfig

%files -n %libbtcore
%defattr(-,root,root)
%{_kde_libdir}/libbtcore.so.*

#-------------------------------------------------------------------------

%define libktcore %mklibname ktcore 3

%package -n %libktcore
Summary: Ktorrent libbrary
Group: System/Libraries

%description -n %libktcore
KTorrent library.

%post -n %libktcore -p /sbin/ldconfig
%postun -n %libktcore -p /sbin/ldconfig

%files -n %libktcore
%defattr(-,root,root)
%{_kde_libdir}/libktcore.so.*

#-------------------------------------------------------------------------

%define libktupnp %mklibname ktupnp 1

%package -n %libktupnp
Summary: Ktorrent libbrary
Group: System/Libraries

%description -n %libktupnp
KTorrent library.

%post -n %libktupnp -p /sbin/ldconfig
%postun -n %libktupnp -p /sbin/ldconfig

%files -n %libktupnp
%defattr(-,root,root)
%{_kde_libdir}/libktupnp.so.*

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

%prep
%setup -q

%build
%cmake_kde4 

%make
 
%install
rm -rf %buildroot

make -C build DESTDIR=%buildroot install  

%find_lang %{name}

%clean
rm -rf %buildroot

