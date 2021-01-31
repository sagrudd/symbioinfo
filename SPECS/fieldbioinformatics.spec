%define debug_package %{nil}

Name:		fieldbioinformatics
Version:	1.2.1
Release:	1%{?dist}
Summary:	artic fieldbioinformatics
Group:          Applications/Bioinformatics
License:	GPLv3
URL:		https://github.com/artic-network/fieldbioinformatics
Source0:        https://github.com/artic-network/fieldbioinformatics/archive/1.2.1.tar.gz

BuildRequires:	gcc
Requires:	gcc muscle

%define debug_package %{nil}
%define	_bindir	/usr/local/bin/
%define _libdir /usr/lib64/
%define _mandir /man
%define _datarootdir /
%description    
artic is a pipeline and set of accompanying tools for working with viral nanopore sequencing data, generated from tiling amplicon schemes.

It is designed to help run the artic bioinformatics protocols; for example the SARS-CoV-2 coronavirus protocol.

Features include:

    read filtering
    primer trimming
    amplicon coverage normalisation
    variant calling
    consensus building

There are two workflows baked into this pipeline, one which uses signal data (via nanopolish) and one that does not (via medaka).


%prep
%setup

%build
%set_build_flags

CFLAGS="$RPM_OPT_FLAGS -fPIE -pie"
CXXFLAGS="$RPM_OPT_FLAGS -fPIE -pie"

export CFLAGS
export CXXFLAGS


%ifarch aarch64
sed -i -E 's/CFLAGS=.+/CFLAGS=         -g -Wall -O2 -Wc++-compat -fPIE -pie -Wextra/g' Makefile
make arm_neon=1 aarch64=1
%else
sed -i -E 's/CFLAGS=.+/CFLAGS=         -g -Wall -O2 -Wc++-compat -fPIE -pie -Wextra/g' Makefile
make
%endif

%install
mkdir -p %{buildroot}/usr/local/bin/

%{__install} -d %{buildroot}%{_bindir}
%{__install} -m0755 minimap2 %{buildroot}%{_bindir}
%{__install} -d %{buildroot}%{_includedir}/%{name}
%{__install} -m0644 *.h %{buildroot}%{_includedir}/%{name}/
%{__install} -d %{buildroot}/%{_libdir}
%{__install} -m0755 libminimap2.a %{buildroot}/%{_libdir}/

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%{_bindir}/minimap2
%{_includedir}/%{name}/*
%{_libdir}/libminimap2.a

%clean
rm -rf $RPM_BUILD_ROOT
rm -fR %{buildroot}
rm -fR %{_builddir}/%{name}-%{version}


%changelog
* Fri Jan 22 2021 sagrudd <stephen@mnemosyne.co.uk>
- updated to include the libminimap2.a into /usr/lib64/minimap2
- using this in the Nanopolish build
* Mon Jan 18 2021 sagrudd <stephen@mnemosyne.co.uk>
- updated version to 2.17 - build for aarch64
- note hasindu's comments on arm64 at https://github.com/hasindu2008/minimap2-arm
* Fri Dec 9 2016 Stephen Rudd <stephen@mnemosyne.co.uk>
- appended %define debug_package %{nil} to header of SPEC file
* Wed Feb 03 2016 Stephen Rudd <stephen@mnemosyne.co.uk>
- first version of a minimap RPM for the Heikisho distribution in development
- this builds upon documentation from Mothur website and in makefiles

