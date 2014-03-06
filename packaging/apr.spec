Name:		apr
Version:	1.5.0
Release:	0
Summary:	Apache Portable Runtime
License:	Apache-2.0
Group:		Application Framework/Libraries
URL:		http://apr.apache.org/
Source:		%name-%version.tar.xz
Source1001: 	apr.manifest
BuildRequires:	autoconf >= 2.64, automake >= 1.11
BuildRequires:	libtool >= 2.2

%description
Software libraries that provide a predictable and consistent interface
to underlying platform-specific implementations. The primary goal is
to provide an API to which software developers may code and be assured
of predictable if not identical behaviour regardless of the platform
on which their software is built, relieving them of the need to code
special-case conditions to work around or take advantage of
platform-specific deficiencies or features.

%package devel
Summary:	Development files for the Apache Portable Runtime
Group:		Application Framework/Libraries
Requires:       %name = %version

%description devel
Development files, including headers, for the APR library.

%prep
%setup -q
cp %{SOURCE1001} .

%build
autoreconf
%configure --disable-static
make %{?_smp_mflags}

%install
%make_install

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%manifest %{name}.manifest
%license LICENSE
%defattr(-,root,root)
%{_libdir}/*.so.*

%files devel
%manifest %{name}.manifest
%defattr(-,root,root)
%{_bindir}/apr-1-config
%{_includedir}/*.h
%{_libdir}/apr.exp
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
%{_datadir}/build-1/*
