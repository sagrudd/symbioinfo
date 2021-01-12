%global packname rcmdcheck
%global rversion  4.0.3
%global packrel 1
%global debug_package %{nil}

Name:             r_symbioinfo_cran_rcmdcheck
Version:          1.3.3
Release:          %{packrel}%{?dist}
Source0:          https://cran.r-project.org/web/packages/rcmdcheck/../../../src/contrib/rcmdcheck_1.3.3.tar.gz
License:          MIT + file LICENSE
URL:              https://cran.r-project.org/web/packages/rcmdcheck/index.html
Group:            Applications/Bioinformatics
Summary:          PackYak build of R-package [rcmdcheck] version [1.3.3]
BuildRequires:    tex(latex) R-core = %{rversion} r_symbioinfo_cran_callr r_symbioinfo_cran_cli r_symbioinfo_cran_crayon r_symbioinfo_cran_desc r_symbioinfo_cran_digest r_symbioinfo_cran_pkgbuild r_symbioinfo_cran_prettyunits r_symbioinfo_cran_r6 r_symbioinfo_cran_rprojroot r_symbioinfo_cran_sessioninfo r_symbioinfo_cran_withr r_symbioinfo_cran_xopen
Requires:         tex(latex) R-core = %{rversion} r_symbioinfo_cran_callr r_symbioinfo_cran_cli r_symbioinfo_cran_crayon r_symbioinfo_cran_desc r_symbioinfo_cran_digest r_symbioinfo_cran_pkgbuild r_symbioinfo_cran_prettyunits r_symbioinfo_cran_r6 r_symbioinfo_cran_rprojroot r_symbioinfo_cran_sessioninfo r_symbioinfo_cran_withr r_symbioinfo_cran_xopen

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
- updated [rcmdcheck] package version to [1.3.3-1] by PackYak
- updated to R version [4.0.3]
* Mon Jan 11 2021 Stephen Rudd <stephen@mnemosyne.co.uk>
- resurrecting the symbioinfo concept for arm64 usage
* Tue Jan 31 2017 Stephen Rudd <stephen@mnemosyne.co.uk>
- This is a first version of the R package specfile for SymBioInfo
- this is based on docs from https://fedoraproject.org/wiki/Packaging:R?rd=Packaging/R
- this is also intended as a template for automation ...
