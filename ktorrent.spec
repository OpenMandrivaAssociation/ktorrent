%define major %version

Name: ktorrent
Version:	3.0.1
Release:	%mkrel 1
Summary:	BitTorrent program for KDE
Group: Networking/File transfer
License:	GPLv2+
Url:		http://ktorrent.org/
Source0:	http://ktorrent.org/downloads/%{version}/%{name}-%{version}.tar.bz2
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	gmp-devel
BuildRequires:	kdelibs4-devel
Obsoletes:	%{_lib}ktorrent0 %{_lib}ktorrent2.1 %{_lib}ktorrent2.1.1
Obsoletes:	%{_lib}ktorrent2.1.2 %{_lib}ktorrent2.1.3


%description
KTorrent is a BitTorrent program for KDE. It's main features are:
 o Downloads torrent files
 o Upload speed capping, seeing that most people can't upload
   infinite amounts of data.
 o Internet searching using  The Bittorrent website's search engine
 o UDP Trackers

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

%post
/sbin/ldconfig
%update_menus

%postun
/sbin/ldconfig
%clean_menus

%files -f %{name}.lang
%defattr(-,root,root)
%doc AUTHORS README
%{_bindir}/*
%{_libdir}/kde4/*
%{_datadir}/services/*
%{_datadir}/servicetypes/*
%{_datadir}/apps/%{name}
%{_datadir}/applications/kde/*
%{_datadir}/config.kcfg/*.kcfg
%{_iconsdir}/*/*/*/*
