%global packname DT
%global rversion  4.0.3
%global packrel 1
%global debug_package %{nil}

Name:             r_symbioinfo_cran_dt
Version:          0.17
Release:          %{packrel}%{?dist}
Source0:          https://cran.r-project.org/web/packages/DT/../../../src/contrib/DT_0.17.tar.gz
License:          GPL-3 | file LICENSE
URL:              https://cran.r-project.org/web/packages/DT/index.html
Group:            Applications/Bioinformatics
Summary:          PackYak build of R-package [DT] version [0.17]
BuildRequires:    tex(latex) R-core = %{rversion} r_symbioinfo_cran_htmltools r_symbioinfo_cran_htmlwidgets r_symbioinfo_cran_jsonlite r_symbioinfo_cran_magrittr r_symbioinfo_cran_crosstalk r_symbioinfo_cran_promises
Requires:         tex(latex) R-core = %{rversion} r_symbioinfo_cran_htmltools r_symbioinfo_cran_htmlwidgets r_symbioinfo_cran_jsonlite r_symbioinfo_cran_magrittr r_symbioinfo_cran_crosstalk r_symbioinfo_cran_promises

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
- updated [DT] package version to [0.17-1] by PackYak
- updated to R version [4.0.3]
* Mon Jan 11 2021 Stephen Rudd <stephen@mnemosyne.co.uk>
- resurrecting the symbioinfo concept for arm64 usage
* Tue Jan 31 2017 Stephen Rudd <stephen@mnemosyne.co.uk>
- This is a first version of the R package specfile for SymBioInfo
- this is based on docs from https://fedoraproject.org/wiki/Packaging:R?rd=Packaging/R
- this is also intended as a template for automation ...
