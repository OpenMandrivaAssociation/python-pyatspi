%define name python-pyatspi
%define version 0.3.6
%define release %mkrel 1
%define oname pyatspi

Summary: D-Bus AT-SPI - Python bindings
Name: %{name}
Version: %{version}
Release: %{release}
Source0: ftp://ftp.gnome.org/pub/GNOME/sources/%{oname}/%{oname}-%{version}.tar.bz2
License: LGPLv2
Group: Development/Python
Url: http://www.linuxfoundation.org/en/AT-SPI_on_D-Bus
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildArch: noarch
BuildRequires:	python-devel
BuildRequires:  dbus-glib-devel
BuildRequires:  gtk+2-devel
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
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README AUTHORS
%py_puresitedir/%{oname}
