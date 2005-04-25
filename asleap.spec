# TODO: optflags
Summary:	asleap - recovers weak LEAP password
Summary(pl):	asleap - odtwarzanie s�abych hase� LEAP
Name:		asleap
Version:	1.4
Release:	0.1
License:	GPL v2
Group:		Applications/System
Source0:	http://dl.sourceforge.net/asleap/%{name}-%{version}.tgz
# Source0-md5:	805f1e239d9c8b027822aae379eb3a61
URL:		http://asleap.sourceforge.net/
BuildRequires:	libpcap-devel
BuildRequires:	openssl-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This tool is released as a proof-of-concept to demonstrate weaknesses
in the LEAP and PPTP protocols.

%description -l pl
To narz�dzie s�u�y do demonstracji s�abo�ci protoko��w LEAP i PPTP.

%prep
%setup -q -n %{name}

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

install asleap $RPM_BUILD_ROOT%{_bindir}
install genkeys $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc FEATURES README THANKS
%attr(755,root,root) %{_bindir}/*
