%global packname readr
%global rversion  4.0.3
%global packrel 1
%global debug_package %{nil}

Name:             r_symbioinfo_cran_readr
Version:          1.4.0
Release:          %{packrel}%{?dist}
Source0:          https://cran.r-project.org/web/packages/readr/../../../src/contrib/readr_1.4.0.tar.gz
License:          GPL-2 | GPL-3 | file LICENSE [expanded from: GPL (≥ 2) | file LICENSE]
URL:              https://cran.r-project.org/web/packages/readr/index.html
Group:            Applications/Bioinformatics
Summary:          PackYak build of R-package [readr] version [1.4.0]
BuildRequires:    tex(latex) R-core = %{rversion} r_symbioinfo_cran_cli r_symbioinfo_cran_clipr r_symbioinfo_cran_crayon r_symbioinfo_cran_hms r_symbioinfo_cran_rlang r_symbioinfo_cran_r6 r_symbioinfo_cran_tibble r_symbioinfo_cran_lifecycle
Requires:         tex(latex) R-core = %{rversion} r_symbioinfo_cran_cli r_symbioinfo_cran_clipr r_symbioinfo_cran_crayon r_symbioinfo_cran_hms r_symbioinfo_cran_rlang r_symbioinfo_cran_r6 r_symbioinfo_cran_tibble r_symbioinfo_cran_lifecycle

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
- updated [readr] package version to [1.4.0-1] by PackYak
- updated to R version [4.0.3]
* Mon Jan 11 2021 Stephen Rudd <stephen@mnemosyne.co.uk>
- resurrecting the symbioinfo concept for arm64 usage
* Tue Jan 31 2017 Stephen Rudd <stephen@mnemosyne.co.uk>
- This is a first version of the R package specfile for SymBioInfo
- this is based on docs from https://fedoraproject.org/wiki/Packaging:R?rd=Packaging/R
- this is also intended as a template for automation ...
