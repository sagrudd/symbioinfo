%global packname testthat
%global rversion  4.0.3
%global packrel 1
%global debug_package %{nil}

Name:             r_testthat
Version:          3.0.1
Release:          %{packrel}%{?dist}
Source0:          https://cran.r-project.org/web/packages/testthat/../../../src/contrib/testthat_3.0.1.tar.gz
License:          MIT + file LICENSE
URL:              https://cran.r-project.org/web/packages/testthat/index.html
Group:            Applications/Bioinformatics
Summary:          PackYak v0.0.2 build of R-package [testthat] version [3.0.1]
BuildRequires:    tex(latex) R-core = %{rversion} r_brio r_callr r_cli r_crayon r_desc r_digest r_ellipsis r_evaluate r_jsonlite r_lifecycle r_magrittr r_pkgload r_praise r_processx r_ps r_r6 r_rlang r_waldo r_withr
Requires:         tex(latex) R-core = %{rversion} r_brio r_callr r_cli r_crayon r_desc r_digest r_ellipsis r_evaluate r_jsonlite r_lifecycle r_magrittr r_pkgload r_praise r_processx r_ps r_r6 r_rlang r_waldo r_withr

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
* Fri Jan 15 2021 sagrudd <stephen@mnemosyne.co.uk>
- updated [testthat] package version to [3.0.1-1] by PackYak v0.0.2
- updated to R version [4.0.3]
* Mon Jan 11 2021 Stephen Rudd <stephen@mnemosyne.co.uk>
- resurrecting the symbioinfo concept for arm64 usage
* Tue Jan 31 2017 Stephen Rudd <stephen@mnemosyne.co.uk>
- This is a first version of the R package specfile for SymBioInfo
- this is based on docs from https://fedoraproject.org/wiki/Packaging:R?rd=Packaging/R
- this is also intended as a template for automation ...
