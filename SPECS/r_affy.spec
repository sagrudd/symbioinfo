%global packname affy
%global rversion  4.0.3
%global packrel 1
%global debug_package %{nil}

Name:             r_affy
Version:          1.68.0
Release:          %{packrel}%{?dist}
Source0:          https://www.bioconductor.org/packages/release/bioc/html/../src/contrib/affy_1.68.0.tar.gz
License:          LGPL (>= 2.0)
URL:              https://www.bioconductor.org/packages/release/bioc/html/affy.html
Group:            Applications/Bioinformatics
Summary:          PackYak v0.0.2 build of R-package [affy] version [1.68.0]
BuildRequires:    tex(latex) R-core = %{rversion} r_biocgenerics r_biobase r_affyio r_biocmanager r_preprocesscore r_zlibbioc
Requires:         tex(latex) R-core = %{rversion} r_biocgenerics r_biobase r_affyio r_biocmanager r_preprocesscore r_zlibbioc

%description

%prep
echo "BUILDROOT = $RPM_BUILD_ROOT"
%setup -q -c -n %{packname}_%{version}

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/lib64/R/library
%{_bindir}/R CMD INSTALL -l $RPM_BUILD_ROOT/usr/lib64/R/library/ %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -rf $RPM_BUILD_ROOT%{_libdir}/R/library/R.css

%check

%clean
rm -rf $RPM_BUILD_ROOT
rm -fR %{_builddir}/%{packname}*

%files
#%dir /usr/lib64/R/library/%{packname}
/usr/lib64/R/library/%{packname}

%changelog
* Sat Jan 16 2021 sagrudd <stephen@mnemosyne.co.uk>
- updated [affy] package version to [1.68.0-1] by PackYak v0.0.2
- updated to R version [4.0.3]
* Mon Jan 11 2021 Stephen Rudd <stephen@mnemosyne.co.uk>
- resurrecting the symbioinfo concept for arm64 usage
* Tue Jan 31 2017 Stephen Rudd <stephen@mnemosyne.co.uk>
- This is a first version of the R package specfile for SymBioInfo
- this is based on docs from https://fedoraproject.org/wiki/Packaging:R?rd=Packaging/R
- this is also intended as a template for automation ...