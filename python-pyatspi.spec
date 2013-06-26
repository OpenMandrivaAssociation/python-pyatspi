%define oname pyatspi

Summary: D-Bus AT-SPI - Python bindings
Name:    python-pyatspi
Version: 0.4.1
Release: 3
Source0: ftp://ftp.gnome.org/pub/GNOME/sources/%{oname}/%{oname}-%{version}.tar.bz2
License: LGPLv2
Group: Development/Python
Url: http://www.linuxfoundation.org/en/AT-SPI_on_D-Bus
BuildArch: noarch
BuildRequires:	python-devel
BuildRequires:  dbus-glib-devel
BuildRequires:  pkgconfig(gtk+-2.0)
BuildRequires:  libxml2-devel
BuildRequires:  python-dbus
Requires:  python-dbus

%description
This version of at-spi is a major break from previous versions.  It
has been completely rewritten to use D-Bus rather than ORBIT / CORBA
for its transport protocol.

%prep
%setup -q -n %oname-%version

%build
./configure --prefix=%_prefix
%make

%install
%makeinstall_std

%files
%doc README AUTHORS
%py_puresitedir/%{oname}_dbus


%changelog
* Thu May 05 2011 Oden Eriksson <oeriksson@mandriva.com> 0.4.1-2mdv2011.0
+ Revision: 668023
- mass rebuild

* Tue Nov 16 2010 Götz Waschk <waschk@mandriva.org> 0.4.1-1mdv2011.0
+ Revision: 597896
- update to new version 0.4.1

* Fri Nov 05 2010 Götz Waschk <waschk@mandriva.org> 0.4.0-2mdv2011.0
+ Revision: 593735
- rebuild for new python 2.7

* Tue Sep 28 2010 Götz Waschk <waschk@mandriva.org> 0.4.0-1mdv2011.0
+ Revision: 581617
- update to new version 0.4.0

* Tue Aug 31 2010 Götz Waschk <waschk@mandriva.org> 0.3.91-1mdv2011.0
+ Revision: 574616
- new version
- update file list

* Tue Aug 17 2010 Götz Waschk <waschk@mandriva.org> 0.3.90-1mdv2011.0
+ Revision: 570823
- update to new version 0.3.90

* Tue Aug 03 2010 Götz Waschk <waschk@mandriva.org> 0.3.6-1mdv2011.0
+ Revision: 565403
- update to new version 0.3.6

* Fri Jul 30 2010 Götz Waschk <waschk@mandriva.org> 0.3.4-1mdv2011.0
+ Revision: 563403
- new version
- rename python module

* Wed Mar 31 2010 Götz Waschk <waschk@mandriva.org> 0.1.8-1mdv2010.1
+ Revision: 530225
- update to new version 0.1.8

* Fri Feb 19 2010 Götz Waschk <waschk@mandriva.org> 0.1.7-1mdv2010.1
+ Revision: 508296
- update to new version 0.1.7

* Tue Feb 09 2010 Götz Waschk <waschk@mandriva.org> 0.1.6-1mdv2010.1
+ Revision: 502692
- new version
- update file list

* Mon Jan 11 2010 Götz Waschk <waschk@mandriva.org> 0.1.5-1mdv2010.1
+ Revision: 489821
- update to new version 0.1.5

* Tue Dec 22 2009 Götz Waschk <waschk@mandriva.org> 0.1.4-1mdv2010.1
+ Revision: 481262
- import python-pyatspi


