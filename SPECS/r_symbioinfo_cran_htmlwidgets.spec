%global packname htmlwidgets
%global rversion  4.0.3
%global packrel 1
%global debug_package %{nil}

Name:             r_symbioinfo_cran_htmlwidgets
Version:          1.5.3
Release:          %{packrel}%{?dist}
Source0:          https://cran.r-project.org/web/packages/htmlwidgets/../../../src/contrib/htmlwidgets_1.5.3.tar.gz
License:          MIT + file LICENSE
URL:              https://cran.r-project.org/web/packages/htmlwidgets/index.html
Group:            Applications/Bioinformatics
Summary:          PackYak build of R-package [htmlwidgets] version [1.5.3]
BuildRequires:    tex(latex) R-core = %{rversion} r_symbioinfo_cran_htmltools r_symbioinfo_cran_jsonlite r_symbioinfo_cran_yaml
Requires:         tex(latex) R-core = %{rversion} r_symbioinfo_cran_htmltools r_symbioinfo_cran_jsonlite r_symbioinfo_cran_yaml

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
- updated [htmlwidgets] package version to [1.5.3-1] by PackYak
- updated to R version [4.0.3]
* Mon Jan 11 2021 Stephen Rudd <stephen@mnemosyne.co.uk>
- resurrecting the symbioinfo concept for arm64 usage
* Tue Jan 31 2017 Stephen Rudd <stephen@mnemosyne.co.uk>
- This is a first version of the R package specfile for SymBioInfo
- this is based on docs from https://fedoraproject.org/wiki/Packaging:R?rd=Packaging/R
- this is also intended as a template for automation ...
