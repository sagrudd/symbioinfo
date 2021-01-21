
%global debug_package %{nil}

Name:           ncbi-blast
Version:        2.10.1+
Release:        1%{?dist}
Summary:        BLAST by NCBI

Group:          Applications/Bioinformatics
License:        GPLv3
URL:            https://ftp.ncbi.nlm.nih.gov/blast/executables/blast+/2.10.1/ncbi-blast-2.10.1+-src.tar.gz
Source0:        https://ftp.ncbi.nlm.nih.gov/blast/executables/blast+/2.10.1/ncbi-blast-2.10.1+-src.tar.gz
Source1:        ncbi-blast-Makefile
Patch0:		blast+fix_x86isms.patch
Patch1:         blast+bm-6.4.0.patch
Patch2:         blast+enable_clean_after_failed_compile.patch
Patch3:         blast+fix_configure.patch
Patch4:         blast+fix_lib_deps.patch
Patch5:         blast+fix_unit_tests.patch
Patch6:         blast+hurd_fixes.patch
Patch7:         blast+legacy_rename_rpsblast.patch
Patch8:         blast+no_multiarch_rpath.patch
Patch9:         blast+optionally_keep_sequence.patch
Patch10:        blast+reprobuild.patch
Patch11:        blast+run_perl_directly.patch
Patch13:        blast+skip_services_unit_test.patch
Patch14:        blast+spelling.patch
Patch15:        blast+support_gcc10.patch
Patch16:        blast+support_x32.patch
Patch17:        blast+suppress_gnutls_version_check.patch
Patch18:        blast+system_mbedtls_only.patch
Patch19:        blast+tune_lmdb_defaults.patch
Patch20:        blast+use_pie_for_apps.patch
BuildRequires:  gcc mbedtls
Requires:       gcc
AutoReqProv:    no

%description    
NCBI blast is a collection of tools for comparing DNA and protein sequences

%prep
%setup -q -n %{name}-%{version}-src 
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1
%patch10 -p1
%patch11 -p1
%patch13 -p1
%patch14 -p1
%patch15 -p1
%patch16 -p1
%patch17 -p1
%patch18 -p1
%patch19 -p1
%patch20 -p1
cp %{SOURCE1} %{_builddir}/%{name}-%{version}-src/c++/src/build-system/Makefile.app.in

%build
%set_build_flags
cd c++
./configure --without-autodep --without-makefile-auto-update --with-flat-makefile --without-caution --without-dbapi --without-lzo --without-debug --without-downloaded-vdb --without-sse42 --with-mbedtls
cd ReleaseMT/build
make -j4 -f Makefile.flat

%install
mkdir -p %{buildroot}/usr/local/bin
cd c++/ReleaseMT/bin
%{__install} -m0755 get_species_taxids.sh blastn blastp blastx makeblastdb %{buildroot}/usr/local/bin

%clean
rm -fR %{_builddir}/ncbi-blast*
rm -fR %{buildroot}

%files
%defattr(-,root,root,-)
/usr/local/bin/


%changelog
* Wed Jan 20 2021 sagrudd <stephen@mnemosyne.co.uk>
- BLAST+ is PITA on aarch64 - borrowed patches from debian files
- please note the non-standard build file specified
- CMD_BASEARGS modified to remove -pie -fPIE and only retain -fPIC
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
