%define debug_package %{nil}

Name:		minimap2
Version:	2.17
Release:	1%{?dist}
Summary:	minimap
Group:          Applications/Bioinformatics
License:	GPLv3
URL:		https://github.com/lh3/minimap2
Source0:        https://github.com/lh3/minimap2/releases/download/v2.17/minimap2-2.17.tar.bz2

BuildRequires:	gcc
Requires:	gcc

%define debug_package %{nil}
%define	_bindir	/bin
%define _libdir /lib
%define _mandir /man
%define _datarootdir /
%description    
Minimap is an experimental tool to efficiently find multiple approximate mapping positions between two sets of long sequences, such as between reads and reference genomes, between genomes and between long noisy reads. By default, it is tuned to have high sensitivity to 2kb matches around 20% divergence but with low specificity. Minimap does not generate alignments as of now and because of this, it is usually tens of times faster than mainstream aligners. With four CPU cores, minimap can map 1.6Gbp PacBio reads to human in 2.5 minutes, 1Gbp PacBio E. coli reads to pre-indexed 9.6Gbp bacterial genomes in 3 minutes, to pre-indexed >100Gbp nt database in ~1 hour (of which ~20 minutes are spent on loading index from the network filesystem; peak RAM: 10GB), map 2800 bacteria to themselves in 1 hour, and map 1Gbp E. coli reads against themselves in a couple of minutes.

Minimap does not replace mainstream aligners, but it can be useful when you want to quickly identify long approximate matches at moderate divergence among a huge collection of sequences. For this task, it is much faster than most existing tools.

%prep
%setup


%build

make arm_neon=1 aarch64=1

%install
mkdir -p %{buildroot}/usr/local/bin/

%{__install} -d %{buildroot}/usr/local/bin/
%{__install} -m0755 minimap2 %{buildroot}/usr/local/bin/


%files
%defattr(-,root,root,-)
/usr/local/bin/

%clean
rm -rf $RPM_BUILD_ROOT
rm -fR %{buildroot}
rm -fR %{_builddir}/%{name}-%{version}


%changelog
* Mon Jan 18 2021 sagrudd <stephen@mnemosyne.co.uk>
- updated version to 2.17 - build for aarch64
- note hasindu's comments on arm64 at https://github.com/hasindu2008/minimap2-arm
* Fri Dec 9 2016 Stephen Rudd <stephen@mnemosyne.co.uk>
- appended %define debug_package %{nil} to header of SPEC file
* Wed Feb 03 2016 Stephen Rudd <stephen@mnemosyne.co.uk>
- first version of a minimap RPM for the Heikisho distribution in development
- this builds upon documentation from Mothur website and in makefiles

