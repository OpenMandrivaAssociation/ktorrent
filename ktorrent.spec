Name: ktorrent
Version: 4.2.1
Release: 1
Summary: BitTorrent program for KDE
Group: Networking/File transfer
License: GPLv2+
Url: http://ktorrent.org/
Source0: http://ktorrent.org/downloads/%{version}/%{name}-%{version}.tar.bz2
BuildRequires: gmp-devel
BuildRequires: kdepimlibs4-devel
BuildRequires: kdebase4-workspace-devel >= 4.4.0
BuildRequires: qca2-devel >= 2.0.1
BuildRequires: boost-devel
BuildRequires: taglib-devel
BuildRequires: libktorrent-devel >= 1.1
Obsoletes: %{_lib}ktorrent0 
Obsoletes: %{_lib}ktorrent2.1 
Obsoletes: %{_lib}ktorrent2.1.1
Obsoletes: %{_lib}ktorrent2.1.2 
Obsoletes: %{_lib}ktorrent2.1.3
Obsoletes: kde4-ktorrent < 1:%version-%release
Provides:  kde4-ktorrent = 1:%version-%release

%description
KTorrent is a BitTorrent program for KDE. Its main features are:
 o Downloads torrent files
 o Upload speed capping, seeing that most people can't upload
   infinite amounts of data.
 o Internet searching using  The Bittorrent website's search engine
 o UDP Trackers

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

%define ktcore_major 13
%define libktcore %mklibname ktcore %ktcore_major

%package -n %libktcore
Summary:    Ktorrent libbrary
Group:      System/Libraries
Obsoletes:  %{_lib}ktcore1 < 4.0.0-2
Obsoletes:  %{_lib}ktcore2 < 3.0-0.rc1.3
Obsoletes:  %{_lib}ktcore3 < 3.1-0.beta1.2
Obsoletes:  %{_lib}ktcore4 < 3.1-0.beta2.1
Obsoletes:  %{_lib}btcore8 < 3.2
Obsoletes:  %{_lib}btcore9 < 4.0

%description -n %libktcore
KTorrent library.

%files -n %libktcore
%defattr(-,root,root)
%{_kde_libdir}/libktcore.so.%{ktcore_major}*

#-------------------------------------------------------------------------

%package devel
Summary: Ktorrent plugin devel headers
Group: Networking/File transfer
Requires: %{libktcore} = %{version}

%description devel
Ktorrent plugin devel headers.

%files devel
%defattr(-,root,root)
%{_kde_libdir}/*.so

#-------------------------------------------------------------------------

%prep
%setup -q -n %name-%version

%build
%cmake_kde4 
%make
 
%install
rm -rf %buildroot
%makeinstall_std -C build

# make it preferred over kget:
echo "InitialPreference=5" >> %{buildroot}%{_kde_applicationsdir}/ktorrent.desktop

%find_lang %{name} --with-html

%clean
rm -rf %buildroot
