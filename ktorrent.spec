Name:		ktorrent
Version:	4.3.1
Release:	1
Summary:	BitTorrent program for KDE
Group:		Networking/File transfer
License:	GPLv2+
Url:		http://ktorrent.org/
Source0:	http://ktorrent.org/downloads/%{version}/%{name}-%{version}.tar.bz2
Patch0:		ktorrent-4.3.1-add-missing-linkage.patch
BuildRequires:	gmp-devel
BuildRequires:	kdepimlibs4-devel
BuildRequires:	kdebase4-workspace-devel
BuildRequires:	qca2-devel >= 2.0.1
BuildRequires:	boost-devel
BuildRequires:	pkgconfig(taglib)
BuildRequires:	libktorrent-devel >= 1.3.0

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

%define ktcore_major 14
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
%patch0 -p1 -b .link~

%build
%cmake_kde4
%make

%install
%makeinstall_std -C build

# make it preferred over kget:
echo "InitialPreference=5" >> %{buildroot}%{_kde_applicationsdir}/ktorrent.desktop

%find_lang %{name} --with-html

%changelog
* Wed Jun 27 2012 Alexander Khrukin <akhrukin@mandriva.org> 4.2.1-1
+ Revision: 807186
- version update 4.2.1

* Tue Mar 06 2012 Bernhard Rosenkraenzer <bero@bero.eu> 4.2.0-1
+ Revision: 782332
- 4.2.0

* Thu Oct 27 2011 vsinitsyn <vsinitsyn> 4.1.1-3
+ Revision: 707647
- Updated Russian translation

* Mon May 23 2011 Funda Wang <fwang@mandriva.org> 4.1.1-2
+ Revision: 677497
- rebuild for updated mimehandler

* Thu Apr 28 2011 Funda Wang <fwang@mandriva.org> 4.1.1-1
+ Revision: 659823
- new version 4.1.1

* Wed Mar 16 2011 Funda Wang <fwang@mandriva.org> 4.1.0-1
+ Revision: 645475
- 4.1.0 final

* Sun Feb 06 2011 Funda Wang <fwang@mandriva.org> 4.1-0.rc1.1
+ Revision: 636482
- update file list
- 4.1 rc1

* Wed Dec 29 2010 Funda Wang <fwang@mandriva.org> 4.0.5-1mdv2011.0
+ Revision: 625976
- new version 4.0.5

* Mon Oct 18 2010 Funda Wang <fwang@mandriva.org> 4.0.4-1mdv2011.0
+ Revision: 586559
- new version 4.0.4

  + Shlomi Fish <shlomif@mandriva.org>
    - Fix a typo in the description.

* Mon Aug 30 2010 Funda Wang <fwang@mandriva.org> 4.0.3-1mdv2011.0
+ Revision: 574271
- update to new version 4.0.3

* Sat Jul 10 2010 Funda Wang <fwang@mandriva.org> 4.0.2-2mdv2011.0
+ Revision: 549967
- rebuild for new libktorrent

* Fri Jul 09 2010 Funda Wang <fwang@mandriva.org> 4.0.2-1mdv2011.0
+ Revision: 549883
- dso fix merged upstream
- new version 4.0.2

  + Ahmad Samir <ahmadsamir@mandriva.org>
    - it requires kde >= 4.4.0

* Wed Jun 16 2010 Ahmad Samir <ahmadsamir@mandriva.org> 4.0.1-3mdv2010.1
+ Revision: 548145
+ rebuild (emptylog)

* Wed Jun 16 2010 Ahmad Samir <ahmadsamir@mandriva.org> 4.0.1-2mdv2010.1
+ Revision: 548136
- make ktorrent preferred over kget for .torrents

  + Funda Wang <fwang@mandriva.org>
    - new version 4.0.1
      (crashes fixing, reduce disk activities when downloding)

* Tue May 25 2010 Funda Wang <fwang@mandriva.org> 4.0.0-1mdv2010.1
+ Revision: 545840
- new version 4.0.0 final

* Tue May 04 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 4.0-0.rc1.1mdv2010.1
+ Revision: 542035
- Update to 4.0Rc1
  Update buildrequires ( add libktorrent-devel )

* Sun Apr 04 2010 Ahmad Samir <ahmadsamir@mandriva.org> 4.0-0.beta2.1mdv2010.1
+ Revision: 531458
- new upstream release 4.0-0.beta2

  + Funda Wang <fwang@mandriva.org>
    - obsoletes old libs

* Tue Feb 09 2010 Funda Wang <fwang@mandriva.org> 4.0-0.beta1.2mdv2010.1
+ Revision: 503366
- rebuild for new gmp

* Tue Dec 22 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 4.0-0.beta1.1mdv2010.1
+ Revision: 481586
- 4.0 beta1

* Thu Dec 17 2009 Funda Wang <fwang@mandriva.org> 3.3.2-1mdv2010.1
+ Revision: 479621
- new version 3.3.2

* Tue Nov 24 2009 Funda Wang <fwang@mandriva.org> 3.3.1-1mdv2010.1
+ Revision: 469410
- new version 3.3.1

* Thu Nov 12 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 3.3-3mdv2010.1
+ Revision: 465246
- Rebuild against new Qt

  + Raphaël Gertz <rapsys@mandriva.org>
    - Replace with real obsolete version
    - Obsolete old libraries

* Mon Nov 09 2009 Frederik Himpe <fhimpe@mandriva.org> 3.3-1mdv2010.1
+ Revision: 463714
- Update to new version 3.3

* Mon Nov 09 2009 Funda Wang <fwang@mandriva.org> 3.2.5-1mdv2010.1
+ Revision: 463295
- new version 3.2.5

* Thu Sep 24 2009 Frederik Himpe <fhimpe@mandriva.org> 3.2.4-1mdv2010.0
+ Revision: 448461
- Update to new version 3.2.4
- Remove patch integrated upstream

* Thu Aug 13 2009 Raphaël Gertz <rapsys@mandriva.org> 3.2.3-2mdv2010.0
+ Revision: 415794
- Add unbackported upstream patch to avoid startup crash

* Tue Aug 11 2009 Funda Wang <fwang@mandriva.org> 3.2.3-1mdv2010.0
+ Revision: 414521
- new version 3.2.3

* Tue Jun 02 2009 Funda Wang <fwang@mandriva.org> 3.2.2-1mdv2010.0
+ Revision: 382100
- New version 3.2.2

* Fri May 01 2009 Funda Wang <fwang@mandriva.org> 3.2.1-1mdv2010.0
+ Revision: 369387
- New version 3.2.1

* Sat Feb 28 2009 Anssi Hannula <anssi@mandriva.org> 3.2-2mdv2009.1
+ Revision: 346192
- 3.2 final

  + Helio Chissini de Castro <helio@mandriva.com>
    - Recompile against new kdelibs

* Sat Jan 31 2009 Funda Wang <fwang@mandriva.org> 3.2-0.rc1.1mdv2009.1
+ Revision: 335758
- New version 3.2 rc1

* Thu Jan 29 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 3.2-0.beta1.4mdv2009.1
+ Revision: 335046
- Rebuild against new kde4

* Sun Jan 18 2009 Funda Wang <fwang@mandriva.org> 3.2-0.beta1.3mdv2009.1
+ Revision: 330973
- use upstream method to satisfy kde 4.1 and 4.2

  + Nicolas Lécureuil <nlecureuil@mandriva.com>
    - Fix link of ktorrent plasma applet
    - Enable plasmoids

* Sat Jan 17 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 3.2-0.beta1.2mdv2009.1
+ Revision: 330434
- Fix CMakeLists.txt for new kde 4.2
- Rebuild against new kde4

  + Funda Wang <fwang@mandriva.org>
    - patch not needed any more

* Tue Nov 18 2008 Funda Wang <fwang@mandriva.org> 3.2-0.beta1.1mdv2009.1
+ Revision: 304135
- New version 3.2 beta 1

* Sun Nov 16 2008 Funda Wang <fwang@mandriva.org> 3.1.5-1mdv2009.1
+ Revision: 303643
- New version 3.1.5

* Wed Oct 29 2008 Funda Wang <fwang@mandriva.org> 3.1.4-1mdv2009.1
+ Revision: 298552
- New version 3.1.4

* Mon Sep 29 2008 Helio Chissini de Castro <helio@mandriva.com> 3.1.3-1mdv2009.0
+ Revision: 289895
- New upstream bugfix release

* Tue Aug 05 2008 Funda Wang <fwang@mandriva.org> 3.1.2-1mdv2009.0
+ Revision: 264012
- New version 3.1.2
- Obsoletes old major

* Mon Jul 14 2008 Funda Wang <fwang@mandriva.org> 3.1.1-1mdv2009.0
+ Revision: 234536
- new libmajor of btcore
- New version 3.1.1

* Mon Jun 23 2008 Anssi Hannula <anssi@mandriva.org> 3.1-3mdv2009.0
+ Revision: 228287
- adapt obsoletes for upcoming backports

* Fri Jun 20 2008 Pixel <pixel@mandriva.com> 3.1-2mdv2009.0
+ Revision: 227421
- rebuild for fixed %%update_icon_cache/%%clean_icon_cache/%%post_install_gconf_schemas
- rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

* Tue Jun 17 2008 Funda Wang <fwang@mandriva.org> 3.1-1mdv2009.0
+ Revision: 222098
- New version 3.1 final

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Mon Jun 02 2008 Helio Chissini de Castro <helio@mandriva.com> 3.1-0.rc1.1mdv2009.0
+ Revision: 214405
- New upstream release candidate

* Tue May 20 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 3.1-0.beta2.1mdv2009.0
+ Revision: 209299
- Forgot to bump one major
- Fix majors
  Add obsoletes for older packages
  Clean spec file
- Fix Build
- Update to beta2

* Sun May 18 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 3.1-0.beta1.2mdv2009.0
+ Revision: 208799
-Try to add some obsoletes

* Sun May 11 2008 Anssi Hannula <anssi@mandriva.org> 3.1-0.beta1.1mdv2009.0
+ Revision: 205436
- ensure major correctness
- fix majors
- revert unneeded epoch

  + Nicolas Lécureuil <nlecureuil@mandriva.com>
    - Update to ktorrent 3.1  beta1

  + Funda Wang <fwang@mandriva.org>
    - New version 3.0.2

  + Helio Chissini de Castro <helio@mandriva.com>
    - Added cache back, as pointed by Anssi
    - Obsoletes package kde4-ktorrent lower than 3.0.1 ( need add epoch )
    - Ktorrent 3.0.1 for KDE 4. Main applications now will be oriented to kde4.

* Sun Jan 27 2008 Funda Wang <fwang@mandriva.org> 2.2.5-1mdv2008.1
+ Revision: 158850
- New version 2.2.5

* Thu Jan 03 2008 Oden Eriksson <oeriksson@mandriva.com> 2.2.4-2mdv2008.1
+ Revision: 141741
- rebuilt against openldap-2.4.7 libs

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Thu Nov 22 2007 Funda Wang <fwang@mandriva.org> 2.2.4-1mdv2008.1
+ Revision: 111112
- New version 2.2.4

* Thu Nov 15 2007 Funda Wang <fwang@mandriva.org> 2.2.3-1mdv2008.1
+ Revision: 108895
- New version 2.2.3

* Thu Aug 30 2007 Funda Wang <fwang@mandriva.org> 2.2.2-1mdv2008.0
+ Revision: 75028
- New version 2.2.2

* Tue Jul 24 2007 Anssi Hannula <anssi@mandriva.org> 2.2.1-1mdv2008.0
+ Revision: 55038
- 2.2.1

* Wed Jul 04 2007 Anssi Hannula <anssi@mandriva.org> 2.2-1mdv2008.0
+ Revision: 48110
- use desktop-file-install and drop legacy menu file

  + Helio Chissini de Castro <helio@mandriva.com>
    - Update for new 2.2 version

* Wed Jun 13 2007 Anssi Hannula <anssi@mandriva.org> 2.1.4-2mdv2008.0
+ Revision: 39020
- do not own %%_libdir/kde3 (fixes #31378)

* Wed Apr 25 2007 Anssi Hannula <anssi@mandriva.org> 2.1.4-1mdv2008.0
+ Revision: 18293
- 2.1.4

* Tue Apr 17 2007 Anssi Hannula <anssi@mandriva.org> 2.1.3-2mdv2008.0
+ Revision: 13954
- force -fPIC to prevent build failure
- drop libpackage

