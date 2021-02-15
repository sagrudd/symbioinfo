%global packname usethis
%global rversion  4.0.3
%global packrel 1
%global debug_package %{nil}

Name:             r_usethis
Version:          2.0.1
Release:          %{packrel}%{?dist}
Source0:          https://cran.r-project.org/web/packages/usethis/../../../src/contrib/usethis_2.0.1.tar.gz
License:          MIT + file LICENSE
URL:              https://cran.r-project.org/web/packages/usethis/index.html
Group:            Applications/Bioinformatics
Summary:          PackYak v0.0.8 build of R package [usethis] version [2.0.1]
Provides:         R(%{packname})
BuildRequires:    tex(latex) R-core = %{rversion} r_cli r_clipr r_crayon r_curl r_desc r_fs r_gert r_gh r_glue r_jsonlite r_lifecycle r_purrr r_rappdirs r_rlang r_rprojroot r_rstudioapi r_whisker r_withr r_yaml
Requires:         tex(latex) R-core = %{rversion} r_cli r_clipr r_crayon r_curl r_desc r_fs r_gert r_gh r_glue r_jsonlite r_lifecycle r_purrr r_rappdirs r_rlang r_rprojroot r_rstudioapi r_whisker r_withr r_yaml

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
* Mon Feb 15 2021 sagrudd <stephen@mnemosyne.co.uk>
- updated [usethis] package version to [2.0.1-1] by PackYak v0.0.8
* Fri Jan 15 2021 sagrudd <stephen@mnemosyne.co.uk>
- updated [usethis] package version to [2.0.0-1] by PackYak v0.0.2
- updated to R version [4.0.3]
* Mon Jan 11 2021 Stephen Rudd <stephen@mnemosyne.co.uk>
- resurrecting the symbioinfo concept for arm64 usage
* Tue Jan 31 2017 Stephen Rudd <stephen@mnemosyne.co.uk>
- This is a first version of the R package specfile for SymBioInfo
- this is based on docs from https://fedoraproject.org/wiki/Packaging:R?rd=Packaging/R
- this is also intended as a template for automation ...
