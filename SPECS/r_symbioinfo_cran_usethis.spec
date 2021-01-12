%global packname usethis
%global rversion  4.0.3
%global packrel 1
%global debug_package %{nil}

Name:             r_symbioinfo_cran_usethis
Version:          2.0.0
Release:          %{packrel}%{?dist}
Source0:          https://cran.r-project.org/web/packages/usethis/../../../src/contrib/usethis_2.0.0.tar.gz
License:          MIT + file LICENSE
URL:              https://cran.r-project.org/web/packages/usethis/index.html
Group:            Applications/Bioinformatics
Summary:          PackYak build of R-package [usethis] version [2.0.0]
BuildRequires:    tex(latex) R-core = %{rversion} r_symbioinfo_cran_cli r_symbioinfo_cran_clipr r_symbioinfo_cran_crayon r_symbioinfo_cran_curl r_symbioinfo_cran_desc r_symbioinfo_cran_fs r_symbioinfo_cran_gert r_symbioinfo_cran_gh r_symbioinfo_cran_glue r_symbioinfo_cran_jsonlite r_symbioinfo_cran_lifecycle r_symbioinfo_cran_purrr r_symbioinfo_cran_rappdirs r_symbioinfo_cran_rlang r_symbioinfo_cran_rprojroot r_symbioinfo_cran_rstudioapi r_symbioinfo_cran_whisker r_symbioinfo_cran_withr r_symbioinfo_cran_yaml
Requires:         tex(latex) R-core = %{rversion} r_symbioinfo_cran_cli r_symbioinfo_cran_clipr r_symbioinfo_cran_crayon r_symbioinfo_cran_curl r_symbioinfo_cran_desc r_symbioinfo_cran_fs r_symbioinfo_cran_gert r_symbioinfo_cran_gh r_symbioinfo_cran_glue r_symbioinfo_cran_jsonlite r_symbioinfo_cran_lifecycle r_symbioinfo_cran_purrr r_symbioinfo_cran_rappdirs r_symbioinfo_cran_rlang r_symbioinfo_cran_rprojroot r_symbioinfo_cran_rstudioapi r_symbioinfo_cran_whisker r_symbioinfo_cran_withr r_symbioinfo_cran_yaml

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
- updated [usethis] package version to [2.0.0-1] by PackYak
- updated to R version [4.0.3]
* Mon Jan 11 2021 Stephen Rudd <stephen@mnemosyne.co.uk>
- resurrecting the symbioinfo concept for arm64 usage
* Tue Jan 31 2017 Stephen Rudd <stephen@mnemosyne.co.uk>
- This is a first version of the R package specfile for SymBioInfo
- this is based on docs from https://fedoraproject.org/wiki/Packaging:R?rd=Packaging/R
- this is also intended as a template for automation ...
