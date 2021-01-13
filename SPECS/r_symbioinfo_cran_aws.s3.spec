%global packname aws.s3
%global rversion  4.0.3
%global packrel 1
%global debug_package %{nil}

Name:             r_symbioinfo_cran_aws.s3
Version:          0.3.21
Release:          %{packrel}%{?dist}
Source0:          https://cran.r-project.org/web/packages/aws.s3/../../../src/contrib/aws.s3_0.3.21.tar.gz
License:          GPL-2 | GPL-3 [expanded from: GPL (≥ 2)]
URL:              https://cran.r-project.org/web/packages/aws.s3/index.html
Group:            Applications/Bioinformatics
Summary:          PackYak v0.0.1.9005 build of R-package [aws.s3] version [0.3.21]
BuildRequires:    tex(latex) R-core = %{rversion} r_symbioinfo_cran_curl r_symbioinfo_cran_httr r_symbioinfo_cran_xml2 r_symbioinfo_cran_base64enc r_symbioinfo_cran_digest r_symbioinfo_cran_aws.signature
Requires:         tex(latex) R-core = %{rversion} r_symbioinfo_cran_curl r_symbioinfo_cran_httr r_symbioinfo_cran_xml2 r_symbioinfo_cran_base64enc r_symbioinfo_cran_digest r_symbioinfo_cran_aws.signature

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
* Wed Jan 13 2021 sagrudd <stephen@mnemosyne.co.uk>
- updated [aws.s3] package version to [0.3.21-1] by PackYak v0.0.1.9005
- updated to R version [4.0.3]
* Mon Jan 11 2021 Stephen Rudd <stephen@mnemosyne.co.uk>
- resurrecting the symbioinfo concept for arm64 usage
* Tue Jan 31 2017 Stephen Rudd <stephen@mnemosyne.co.uk>
- This is a first version of the R package specfile for SymBioInfo
- this is based on docs from https://fedoraproject.org/wiki/Packaging:R?rd=Packaging/R
- this is also intended as a template for automation ...
