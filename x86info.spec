%define	name	x86info
%define	version	1.23
%define realver	%{version}
#define cvsdate	20050420

Summary:	Show x86 CPU information
Name:		%{name}
Version:	%{version}
Release:	%mkrel 2
License:	GPL
Group:		System/Kernel and hardware
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
URL:		http://www.codemonkey.org.uk/projects/x86info/
Source0:	%{name}-%{realver}%{?cvsdate:-%{cvsdate}}.tar.bz2
Patch0:		x86info-1.17-intel-flags.patch
Patch1:		x86info-1.17-intel-caches.patch
Patch2:		x86info-1.17-cpuid-with-ecx-input.patch
Patch3:		x86info-1.17-intel-multicore-htt.patch
Patch4:		x86info-1.17-intel-caches-cpuid4.patch
Patch5:		x86info-1.17-amd-multicore.patch

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
rm -rf %{buildroot}
install -d %{buildroot}%{_bindir}
install -d %{buildroot}%{_mandir}/man1
install -m755 %{name} %{buildroot}%{_bindir}/
install -m755 %{name}.1 %{buildroot}%{_mandir}/man1/

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README TODO
%{_bindir}/*
%{_mandir}/man1/*


