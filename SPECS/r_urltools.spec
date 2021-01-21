%global packname urltools
%global rversion  4.0.3
%global packrel 1
%global debug_package %{nil}

Name:             r_urltools
Version:          1.7.3
Release:          %{packrel}%{?dist}
Source0:          https://cran.r-project.org/web/packages/urltools/../../../src/contrib/urltools_1.7.3.tar.gz
License:          MIT + file LICENSE
URL:              https://cran.r-project.org/web/packages/urltools/index.html
Group:            Applications/Bioinformatics
Summary:          PackYak v0.0.4 build of R-package [urltools] version [1.7.3]
BuildRequires:    tex(latex) R-core = %{rversion} r_rcpp r_triebeard
Requires:         tex(latex) R-core = %{rversion} r_rcpp r_triebeard

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
* Thu Jan 21 2021 sagrudd <stephen@mnemosyne.co.uk>
- updated [urltools] package version to [1.7.3-1] by PackYak v0.0.4
- updated to R version [4.0.3]
* Mon Jan 11 2021 Stephen Rudd <stephen@mnemosyne.co.uk>
- resurrecting the symbioinfo concept for arm64 usage
* Tue Jan 31 2017 Stephen Rudd <stephen@mnemosyne.co.uk>
- This is a first version of the R package specfile for SymBioInfo
- this is based on docs from https://fedoraproject.org/wiki/Packaging:R?rd=Packaging/R
- this is also intended as a template for automation ...
