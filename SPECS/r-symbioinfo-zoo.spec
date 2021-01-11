%global packname zoo
%global packrel 1
%global rversion 4.0.3
%global debug_package %{nil}

Name:	          r-symbioinfo-zoo
Version:	  1.8.8
Release:          1%{?dist}
Source0:	  https://cran.r-project.org/src/contrib/%{packname}_1.8-8.tar.gz
License:	  GPL-2 | GPL-3
URL:	          http://cran.rstudio.com/web/packages/zoo/index.html
Group:            Applications/Bioinformatics
Summary:	  Automated Build of package = zoo (1.8.8) 
BuildRequires:    tex(latex) R-core = %{rversion} 
Requires:         tex(latex) R-core = %{rversion}

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
* Mon Jan 11 2021 Stephen Rudd <stephen@mnemosyne.co.uk>
- resurrecting the symbioinfo concept for arm64 usage
* Fri Feb 3 2017 Stephen Rudd <stephen@mnemosyne.co.uk>
- Automated Build of package = zoo (1.7.14) for R 3.3.2
* Thu Feb 2 2017 Stephen Rudd <stephen@mnemosyne.co.uk>
- changed the installation path to a plugins folder of the modules location
- this is ugly and not entirely compliant ... but ...
* Tue Jan 31 2017 Stephen Rudd <stephen@mnemosyne.co.uk>
- This is a first version of the R package specfile for SymBioInfo
- this is based on docs from https://fedoraproject.org/wiki/Packaging:R?rd=Packaging/R
- this is also intended as a template for automation ...

