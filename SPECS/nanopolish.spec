%define debug_package %{nil}

Name:		nanopolish
Version:	0.13.2
Release:	1%{?dist}
Summary:	Signal-level algorithms for MinION data
Group:          Applications/Bioinformatics
License:	MIT
URL:		https://github.com/jts/nanopolish
BuildRequires:	gcc gcc-c++ hdf5-mpich-devel eigen3-devel minimap2 samtools htslib-devel
Requires:	gcc

%description    
Software package for signal-level analysis of Oxford Nanopore sequencing data. Nanopolish can calculate an improved consensus sequence for a draft genome assembly, detect base modifications, call SNPs and indels with respect to a reference genome and more

%configure

%build
# %set_build_flags
rm -fR nanopolish
git clone --recursive https://github.com/jts/nanopolish.git
cd nanopolish
make -j5 HDF5=noinstall EIGEN=noinstall HTS=noinstall MINIMAP2=noinstall  H5_INCLUDE=-I/usr/include/mpich-%{_arch}/ EIGEN_INCLUDE=-I/usr/include/eigen3/ MINIMAP2_INCLUDE=-I/usr/include/minimap2


%install
mkdir -p %{buildroot}/usr/local/bin/
cd nanopolish
%{__install} -m0755 nanopolish %{buildroot}/usr/local/bin/

%files
%defattr(-,root,root,-)
/usr/local/bin/nanopolish

%clean
rm -fR %{_builddir}/nanopolish
rm -fR %{buildroot}


%changelog
* Fri Jan 22 2021 sagrudd <stephen@mnemosyne.co.uk>
- first build of Nanopolish
- has required rejig of minimap2 - not exhaustively tested

