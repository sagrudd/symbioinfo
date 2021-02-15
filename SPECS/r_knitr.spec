%global packname knitr
%global rversion  4.0.3
%global packrel 1
%global debug_package %{nil}

Name:             r_knitr
Version:          1.31
Release:          %{packrel}%{?dist}
Source0:          https://cran.r-project.org/web/packages/knitr/../../../src/contrib/knitr_1.31.tar.gz
License:          GPL-2 | GPL-3 [expanded from: GPL]
URL:              https://cran.r-project.org/web/packages/knitr/index.html
Group:            Applications/Bioinformatics
Summary:          PackYak v0.0.5 build of R-package [knitr] version [1.31]
Provides:         R(%{packname})
BuildRequires:    tex(latex) R-core = %{rversion} r_evaluate r_highr r_markdown r_stringr r_yaml r_xfun
Requires:         tex(latex) R-core = %{rversion} r_evaluate r_highr r_markdown r_stringr r_yaml r_xfun

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
* Sun Jan 31 2021 sagrudd <stephen@mnemosyne.co.uk>
- updated [knitr] package version to [1.31-1] by PackYak v0.0.5
* Fri Jan 15 2021 sagrudd <stephen@mnemosyne.co.uk>
- updated [knitr] package version to [1.30-1] by PackYak v0.0.2
- updated to R version [4.0.3]
* Mon Jan 11 2021 Stephen Rudd <stephen@mnemosyne.co.uk>
- resurrecting the symbioinfo concept for arm64 usage
* Tue Jan 31 2017 Stephen Rudd <stephen@mnemosyne.co.uk>
- This is a first version of the R package specfile for SymBioInfo
- this is based on docs from https://fedoraproject.org/wiki/Packaging:R?rd=Packaging/R
- this is also intended as a template for automation ...
