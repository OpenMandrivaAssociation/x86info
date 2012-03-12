%define	name	x86info
%define	version	1.30
%define realver	%{version}
#define cvsdate	20050420

Summary:	Show x86 CPU information
Name:		%{name}
Version:	%{version}
Release:	1
License:	GPL
Group:		System/Kernel and hardware
URL:		http://www.codemonkey.org.uk/projects/x86info/
Source0:	http://codemonkey.org.uk/projects/x86info/%{name}-%{version}.tgz
BuildRequires:	pkgconfig(libpci)

# Will never work on sparc, neither on ppc/alpha...
ExclusiveArch:	%{ix86} x86_64 amd64

%description
Unlike other 'cpuinfo' tools which just parse /proc/cpuinfo, x86info probes
the CPU registers to find out a lot more information. It can discover the
contents of model-specific registers, discover CPU silicon revisions, and
lots more.

%prep
%setup -q -n %{name}-%{realver}

%build
make CFLAGS="%{optflags}"

%install
install -d %{buildroot}%{_bindir}
install -d %{buildroot}%{_mandir}/man1
install -m755 %{name} %{buildroot}%{_bindir}/
install -m755 %{name}.1 %{buildroot}%{_mandir}/man1/

%files
%doc README TODO
%{_bindir}/*
%{_mandir}/man1/*


