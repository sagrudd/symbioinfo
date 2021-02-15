%global packname packyak
%global rversion  4.0.3
%global packrel 2
%global debug_package %{nil}

Name:             r_packyak
Version:          0.0.8
Release:          %{packrel}%{?dist}
License:          MPL-2.0
URL:              https://github.com/sagrudd/packyak
Group:            Applications/Bioinformatics
Summary:          PackYak v0.0.8
Provides:         R(%{packname})
BuildRequires:    tex(latex) R-core = %{rversion} r_cli r_stringr r_r6 r_httr r_rvest r_lubridate r_git2r r_yaml r_tibble
Requires:         tex(latex) R-core = %{rversion} r_cli r_stringr r_r6 r_httr r_rvest r_lubridate r_git2r r_yaml r_tibble

%description

%build
git clone https://github.com/sagrudd/%{packname}

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
* Mon Feb 15 2021 sagrudd <stephen@mnemosyne.co.uk>
- manual version bump to 0.0.8
* Thu Jan 21 2021 sagrudd <stephen@mnemosyne.co.uk>
- manual version bump from git to 0.0.5 (lodestar)
* Mon Jan 18 2021 sagrudd <stephen@mnemosyne.co.uk>
- changed build script to just use a git clone as source ...
* Wed Jan 13 2021 sagrudd <stephen@mnemosyne.co.uk>
- copied an existing autogenerated SPEC file and modified for PackYak
- updated to R version [4.0.3]
* Mon Jan 11 2021 Stephen Rudd <stephen@mnemosyne.co.uk>
- resurrecting the symbioinfo concept for arm64 usage
* Tue Jan 31 2017 Stephen Rudd <stephen@mnemosyne.co.uk>
- This is a first version of the R package specfile for SymBioInfo
- this is based on docs from https://fedoraproject.org/wiki/Packaging:R?rd=Packaging/R
- this is also intended as a template for automation ...

