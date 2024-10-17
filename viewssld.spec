%define name    viewssld
%define version 0.6.0
%define release %mkrel 5

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:    SSL breaking daemon
License:    GPL
Group:      Networking/Other
URL:        https://sourceforge.net/projects/viewssld/
Source:     http://voxel.dl.sourceforge.net/sourceforge/viewssld/%{name}-%{version}.tar.bz2
Patch0:		viewssld-utils-fix.diff
Patch1:		viewssld-make-docs.diff
BuildRequires:	net-devel >= 1.1.3
BuildRequires:  openssl-devel >= 0.9.7
BuildRequires:  pcap-devel
BuildRequires:  dssl-devel
Requires:	dssl
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
%patch1 -p1 -b .dont_install_etc_viewssld_conf

%build
export LIBS="-lnet -ldssl -lssl"
%configure2_5x
%make


%install
%{__mkdir_p}  %{buildroot}/%{_sysconfdir}
%{__mv} doc/examples/viewssld.conf %{buildroot}/%{_sysconfdir}
%makeinstall_std

%clean
%{__rm} -rf %{buildroot}


%files
%defattr(0755,root,root)
%doc COPYING INSTALL README
%doc doc/manual.doc doc/manual.pdf
%{_sysconfdir}/viewssld.conf
%{_sbindir}/viewssld


%changelog
* Wed Mar 11 2009 Daniel Lucio <dlucio@mandriva.org> 0.6.0-1mdv2009.1
- Import

