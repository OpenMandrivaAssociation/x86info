%define	name	x86info
%define	version	1.30
%define realver	%{version}
#define cvsdate	20050420

Summary:	Show x86 CPU information
Name:		%{name}
Version:	%{version}
Release:	2
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




%changelog
* Mon Mar 12 2012 Alexander Khrukin <akhrukin@mandriva.org> 1.30-1
+ Revision: 784333
- version update 1.30

* Sun Sep 20 2009 Thierry Vignaud <tv@mandriva.org> 1.23-2mdv2010.0
+ Revision: 445863
- rebuild

* Thu Jan 22 2009 Giuseppe Ghibò <ghibo@mandriva.com> 1.23-1mdv2009.1
+ Revision: 332630
- Release 1.23.
- Disable parallel building (deps errors on some 8 core building host).

* Sun Aug 03 2008 Thierry Vignaud <tv@mandriva.org> 1.21-4mdv2009.0
+ Revision: 262227
- rebuild

* Thu Jul 31 2008 Thierry Vignaud <tv@mandriva.org> 1.21-3mdv2009.0
+ Revision: 256561
- rebuild
- fix no-buildroot-tag
- kill re-definition of %%buildroot on Pixel's request

* Tue Nov 27 2007 Thierry Vignaud <tv@mandriva.org> 1.21-1mdv2008.1
+ Revision: 113388
- new release

  + Erwan Velu <erwan@mandriva.org>
    - Fixing url

