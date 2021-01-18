
%global debug_package %{nil}

Name:           ncbi-blast
Version:        2.2.26
Release:        1%{?dist}
Summary:        BLAST by NCBI

Group:          Applications/Bioinformatics
License:        GPLv3
URL:            https://ftp.ncbi.nlm.nih.gov/blast/executables/legacy.NOTSUPPORTED/2.2.26/ncbi.tar.gz
Source0:        https://ftp.ncbi.nlm.nih.gov/blast/executables/legacy.NOTSUPPORTED/2.2.26/ncbi.tar.gz
BuildRequires:  gcc
Requires:       gcc
AutoReqProv:    no

%description    
NCBI blast is a collection of tools for comparing DNA and protein sequences

%prep
%setup -q -n ncbi

%build
cd ..
./ncbi/make/makedis.csh


%install
mkdir -p %{buildroot}/usr/local/bin
cd build
%{__install} -m0755 asn2ff asn2gb asn2idx asn2xml asndhuff asntool bl2seq blastall blastcl3 blastclust blastpgp cdscan checksub copymat debruijn errhdr formatrpsdb idfetch megablast seqtest fa2htgs gene2xml impala ncbisort taxblast fastacmd getmesh indexpub tbl2asn vecscreen dosimple findspl getpub makemat rpsblast entrcmd formatdb gil2bin makeset seedtop %{buildroot}/usr/local/bin

%clean
rm -fR %{_builddir}/ncbi
rm -fR %{buildroot}

%files
%defattr(-,root,root,-)
/usr/local/bin/


%changelog
* Mon Jan 18 2021 sagrudd <stephen@mnemosyne.co.uk>
- rollback to ancient 2.2.26 release (pre +) for use on aarch64
* Thu Feb 16 2017 Stephen Rudd <stephen@mnemosyne.co.uk>
- update to version 2.6.0+
- update of the modulefile metafile to the EOF based framework
- simple patch of the Makefile reference to correct some wierd installation eror
* Fri Dec 9 2016 Stephen Rudd <stephen@mnemosyne.co.uk>
- updated to 2.5.0+
* Sun Mar 13 2016 Stephen Rudd <stephen@mnemosyne.co.uk>
- updated version of BLAST - aimed to integrate into Sprai workflow
* Tue Mar 24 2015 Stephen Rudd <stephen@mnemosyne.co.uk>
- a first NCBI blast rpm for BioNinja
