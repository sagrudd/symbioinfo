%global packname devtools
%global rversion  4.0.3
%global packrel 1
%global debug_package %{nil}

Name:             r_symbioinfo_cran_devtools
Version:          2.3.2
Release:          %{packrel}%{?dist}
Source0:          https://cran.r-project.org/web/packages/devtools/../../../src/contrib/devtools_2.3.2.tar.gz
License:          GPL-2 | GPL-3 [expanded from: GPL (≥ 2)]
URL:              https://cran.r-project.org/web/packages/devtools/index.html
Group:            Applications/Bioinformatics
Summary:          PackYak build of R-package [devtools] version [2.3.2]
BuildRequires:    tex(latex) R-core = %{rversion} r_symbioinfo_cran_callr r_symbioinfo_cran_cli r_symbioinfo_cran_covr r_symbioinfo_cran_desc r_symbioinfo_cran_dt r_symbioinfo_cran_ellipsis r_symbioinfo_cran_httr r_symbioinfo_cran_jsonlite r_symbioinfo_cran_memoise r_symbioinfo_cran_pkgbuild r_symbioinfo_cran_pkgload r_symbioinfo_cran_rcmdcheck r_symbioinfo_cran_remotes r_symbioinfo_cran_rlang r_symbioinfo_cran_roxygen2 r_symbioinfo_cran_rstudioapi r_symbioinfo_cran_rversions r_symbioinfo_cran_sessioninfo r_symbioinfo_cran_testthat r_symbioinfo_cran_withr r_symbioinfo_cran_usethis
Requires:         tex(latex) R-core = %{rversion} r_symbioinfo_cran_callr r_symbioinfo_cran_cli r_symbioinfo_cran_covr r_symbioinfo_cran_desc r_symbioinfo_cran_dt r_symbioinfo_cran_ellipsis r_symbioinfo_cran_httr r_symbioinfo_cran_jsonlite r_symbioinfo_cran_memoise r_symbioinfo_cran_pkgbuild r_symbioinfo_cran_pkgload r_symbioinfo_cran_rcmdcheck r_symbioinfo_cran_remotes r_symbioinfo_cran_rlang r_symbioinfo_cran_roxygen2 r_symbioinfo_cran_rstudioapi r_symbioinfo_cran_rversions r_symbioinfo_cran_sessioninfo r_symbioinfo_cran_testthat r_symbioinfo_cran_withr r_symbioinfo_cran_usethis

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
- updated [devtools] package version to [2.3.2-1] by PackYak
- updated to R version [4.0.3]
* Mon Jan 11 2021 Stephen Rudd <stephen@mnemosyne.co.uk>
- resurrecting the symbioinfo concept for arm64 usage
* Tue Jan 31 2017 Stephen Rudd <stephen@mnemosyne.co.uk>
- This is a first version of the R package specfile for SymBioInfo
- this is based on docs from https://fedoraproject.org/wiki/Packaging:R?rd=Packaging/R
- this is also intended as a template for automation ...
