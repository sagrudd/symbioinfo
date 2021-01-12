%global packname roxygen2
%global rversion  4.0.3
%global packrel 1
%global debug_package %{nil}

Name:             r_symbioinfo_cran_roxygen2
Version:          7.1.1
Release:          %{packrel}%{?dist}
Source0:          https://cran.r-project.org/web/packages/roxygen2/../../../src/contrib/roxygen2_7.1.1.tar.gz
License:          GPL-2 | GPL-3 [expanded from: GPL (≥ 2)]
URL:              https://cran.r-project.org/web/packages/roxygen2/index.html
Group:            Applications/Bioinformatics
Summary:          PackYak build of R-package [roxygen2] version [7.1.1]
BuildRequires:    tex(latex) R-core = %{rversion} r_symbioinfo_cran_brew r_symbioinfo_cran_commonmark r_symbioinfo_cran_desc r_symbioinfo_cran_digest r_symbioinfo_cran_knitr r_symbioinfo_cran_pkgload r_symbioinfo_cran_purrr r_symbioinfo_cran_r6 r_symbioinfo_cran_rcpp r_symbioinfo_cran_rlang r_symbioinfo_cran_stringi r_symbioinfo_cran_stringr r_symbioinfo_cran_xml2
Requires:         tex(latex) R-core = %{rversion} r_symbioinfo_cran_brew r_symbioinfo_cran_commonmark r_symbioinfo_cran_desc r_symbioinfo_cran_digest r_symbioinfo_cran_knitr r_symbioinfo_cran_pkgload r_symbioinfo_cran_purrr r_symbioinfo_cran_r6 r_symbioinfo_cran_rcpp r_symbioinfo_cran_rlang r_symbioinfo_cran_stringi r_symbioinfo_cran_stringr r_symbioinfo_cran_xml2

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
* Tue Jan 12 2021 sagrudd <stephen@mnemosyne.co.uk>
- updated [roxygen2] package version to [7.1.1-1] by PackYak
- updated to R version [4.0.3]
* Mon Jan 11 2021 Stephen Rudd <stephen@mnemosyne.co.uk>
- resurrecting the symbioinfo concept for arm64 usage
* Tue Jan 31 2017 Stephen Rudd <stephen@mnemosyne.co.uk>
- This is a first version of the R package specfile for SymBioInfo
- this is based on docs from https://fedoraproject.org/wiki/Packaging:R?rd=Packaging/R
- this is also intended as a template for automation ...
