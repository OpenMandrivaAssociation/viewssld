%define name    viewssld
%define version 0.6.0
%define release %mkrel 1

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:    SSL breaking daemon
License:    GPL
Group:      Networking/Other
URL:        http://sourceforge.net/projects/viewssld/
Source:     http://voxel.dl.sourceforge.net/sourceforge/viewssld/%{name}-%{version}.tar.bz2
Patch0:		viewssld-utils-fix.diff
BuildRequires:  libnet1.1.2-devel
BuildRequires:  openssl-devel >= 0.9.7
BuildRequires:  pcap-devel
BuildRequires:  dssl-devel
Requires:	dssl
Requires:	libnet1.1.2
Requires:	libpcap
Requires:	openssl

%if %mdkversion < 200800
BuildRoot:  %{_tmppath}/%{name}-%{version}
%endif

%description
Viewssld is a free and open source non-terminating SSL traffic decryption daemon for Snort and other 
Network Intrusion Detection Systems (IDS).
%prep

%setup -q 
%patch0 -p1 -b .utils_fix_compillation

%build
%configure2_5x
%make


%install

%makeinstall_std

%clean
%{__rm} -rf %{buildroot}


%files
%defattr(0755,root,root)
%doc COPYING INSTALL README
%doc doc/manual.doc doc/manual.pdf
%doc doc/examples/viewssld.conf
%{_sbindir}/viewssld
%dir %{_sysconfdir}/imspector


