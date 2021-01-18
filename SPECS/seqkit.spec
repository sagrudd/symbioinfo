
%global debug_package %{nil}

Name:           seqkit
Version:        0.15.0
Release:        1%{?dist}
Summary:        SeqKit - a cross-platform and ultrafast toolkit for FASTA/Q file manipulation

Group:          Applications/Bioinformatics
License:        GPLv3
URL:            https://github.com/shenwei356/seqkit
BuildRequires:  wget
AutoReqProv:    no

%description    
FASTA and FASTQ are basic and ubiquitous formats for storing nucleotide and protein sequences. Common manipulations of FASTA/Q file include converting, searching, filtering, deduplication, splitting, shuffling, and sampling. Existing tools only implement some of these manipulations, and not particularly efficiently, and some are only available for certain operating systems. Furthermore, the complicated installation process of required packages and running environments can render these programs less user friendly.

This project describes a cross-platform ultrafast comprehensive toolkit for FASTA/Q processing. SeqKit provides executable binary files for all major operating systems, including Windows, Linux, and Mac OS X, and can be directly used without any dependencies or pre-configurations. SeqKit demonstrates competitive performance in execution time and memory usage compared to similar tools. The efficiency and usability of SeqKit enable researchers to rapidly accomplish common FASTA/Q file manipulations.


%prep


%build


%install
# mkdir -p %{buildroot}/usr/local/bin
%ifarch aarch64
wget https://github.com/shenwei356/seqkit/releases/download/v0.15.0/seqkit_linux_arm64.tar.gz
tar -zxvpf seqkit_linux_arm64.tar.gz
%else
wget https://github.com/shenwei356/seqkit/releases/download/v0.15.0/seqkit_linux_amd64.tar.gz
tar -zxvpf seqkit_linux_amd64.tar.gz
%endif
%{__install} -d %{buildroot}/usr/local/bin/
%{__install} -m0755 seqkit %{buildroot}/usr/local/bin/

%clean
rm -fR %{_builddir}
rm -fR %{buildroot}

%files
%defattr(-,root,root,-)
/usr/local/bin/


%changelog
* Mon Jan 18 2021 sagrudd <stephen@mnemosyne.co.uk>
- first attempt of a seqkit RPM using the prebuild binaries
