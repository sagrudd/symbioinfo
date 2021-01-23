%define debug_package %{nil}

Name:		bedtools
Version:	2.29.2
Release:	1%{?dist}
Summary:	bedtools - a swiss army knife for genome arithmetic
Group:          Applications/Bioinformatics
License:	GPLv2
URL:		https://github.com/arq5x/bedtools2/releases

BuildRequires:	gcc gcc-c++ htslib python
Requires:	gcc htslib samtools

%define	_bindir	/bin
%define _libdir /lib
%define _mandir /man
%define _datarootdir /
%description    
Collectively, the bedtools utilities are a swiss-army knife of tools for a wide-range of genomics analysis tasks. The most widely-used tools enable genome arithmetic: that is, set theory on the genome. For example, bedtools allows one to intersect, merge, count, complement, and shuffle genomic intervals from multiple files in widely-used genomic file formats such as BAM, BED, GFF/GTF, VCF.

%prep


%build
rm -fR bedtools2
git clone https://github.com/arq5x/bedtools2
cd bedtools2
make %{?_smp_mflags}


%install
mkdir -p %{buildroot}/usr/local/bin/
cd bedtools2/bin
%{__install} -m0755 bedtools bamToFastq mapBed shuffleBed bed12ToBed6 bedToBam multiIntersectBed complementBed randomBed tagBam sortBed annotateBed clusterBed fastaFromBed coverageBed bedpeToBam pairToPair subtractBed nucBed expandCols bedToIgv slopBed closestBed windowMaker linksBed getOverlap mergeBed windowBed flankBed pairToBed intersectBed bamToBed multiBamCov unionBedGraphs genomeCoverageBed groupBy maskFastaFromBed %{buildroot}/usr/local/bin/

%files
%defattr(-,root,root,-)
/usr/local/bin

%clean
rm -fR %{_builddir}/bedtools2
rm -fR %{buildroot}


%changelog
* Thu Jan 21 2021 sagrudd <stephen@mnemosyne.co.uk>
- stripped environment modules from the SPEC
- pull code directly from github
- bedtools updated to version 2.29.2 (although this was versioned 2 years ago) - git code is maintained though
* Thu Dec 8 2016 Stephen Rudd <stephen@mnemosyne.co.uk>
- tabix package deprecated and code updated to samtools ...
- updated to version 2.26.0
- removed the debugging from the spec script (%define debug_package %{nil})
* Thu Apr 16 2015 Stephen Rudd <stephen@mnemosyne.co.uk>
- a first attempt at a bedtools rpm installed in modules for BioNinja

