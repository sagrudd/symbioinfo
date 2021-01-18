%global packname rhdf5filters
%global rversion  4.0.3
%global packrel 1
%global debug_package %{nil}

Name:             r_rhdf5filters
Version:          1.2.0
Release:          %{packrel}%{?dist}
Source0:          https://www.bioconductor.org/packages/release/bioc/html/../src/contrib/rhdf5filters_1.2.0.tar.gz
License:          BSD_2_clause + file LICENSE
URL:              https://www.bioconductor.org/packages/release/bioc/html/rhdf5filters.html
Group:            Applications/Bioinformatics
Summary:          PackYak v0.0.2 build of R-package [rhdf5filters] version [1.2.0]
BuildRequires:    tex(latex) R-core = %{rversion} r_rhdf5lib
Requires:         tex(latex) R-core = %{rversion} r_rhdf5lib

%description

%prep
echo "BUILDROOT = $RPM_BUILD_ROOT"
%setup -q -c -n %{packname}_%{version}

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/lib64/R/library

%ifarch aarch64
%{_bindir}/R CMD INSTALL --configure-args="ax_cv_gcc_check_x86_cpu_init=yes ax_cv_gcc_x86_cpu_supports_sse2=no" -l $RPM_BUILD_ROOT/usr/lib64/R/library/ %{packname}
%else
%{_bindir}/R CMD INSTALL -l $RPM_BUILD_ROOT/usr/lib64/R/library/ %{packname}
%endif

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
* Mon Jan 18 2021 sagrudd <stephen@mnemosyne.co.uk>
- updated build script with conditionals to accommodate different compiler flags
- compiler flags borrowed from the debian install script
* Sat Jan 16 2021 sagrudd <stephen@mnemosyne.co.uk>
- updated [rhdf5filters] package version to [1.2.0-1] by PackYak v0.0.2
- updated to R version [4.0.3]
* Mon Jan 11 2021 Stephen Rudd <stephen@mnemosyne.co.uk>
- resurrecting the symbioinfo concept for arm64 usage
* Tue Jan 31 2017 Stephen Rudd <stephen@mnemosyne.co.uk>
- This is a first version of the R package specfile for SymBioInfo
- this is based on docs from https://fedoraproject.org/wiki/Packaging:R?rd=Packaging/R
- this is also intended as a template for automation ...
