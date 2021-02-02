%global packname clint
%global rversion 4.0.1
%global packrel 1
%global debug_package %{nil}
%global _python_bytecompile_errors_terminate_build 0

Name:             python3-clint
Version:          0.5.1
Release:          %{packrel}%{?dist}
Source0:          https://files.pythonhosted.org/packages/3d/b4/41ecb1516f1ba728f39ee7062b9dac1352d39823f513bb6f9e8aeb86e26d/clint-0.5.1.tar.gz
License:          ISC License (ISCL) (ISC)
URL:              https://pypi.org/project/clint/
Group:            Applications/Bioinformatics
Summary:          PackYak v0.0.5 build of Python package [clint] version [0.5.1]
BuildRequires:    python-devel python3-args
Requires:         python-devel python3-args

%description

%prep
%autosetup -p0 -n %{packname}-%{version}
pathfix.py -pni "%{__python3} %{py3_shbang_opts}" .

%build
%py3_build

%install
%py3_install
if ( [ -d %{buildroot}%{_bindir} ] ); then
    pathfix.py -pni "%{__python3} %{py3_shbang_opts}" %{buildroot}%{python3_sitearch} %{buildroot}%{_bindir}/*
fi

%check

%clean
rm -rf $RPM_BUILD_ROOT
rm -fR %{_builddir}/%{packname}*

%files
#/usr/lib64/python3.9/site-packages/%{packname}*
/usr/lib/python3.9/site-packages/%{packname}*
#/usr/bin/*

%changelog
* Tue Feb 2 2021 sagrudd <stephen@mnemosyne.co.uk>
- updated [clint] package version to [0.5.1-1] by PackYak v0.0.5
* Mon Feb 1 2021 sagrudd <stephen@mnemosyne.co.uk>
- updated the R template for usage in Python deployments
* Mon Jan 11 2021 Stephen Rudd <stephen@mnemosyne.co.uk>
- resurrecting the symbioinfo concept for arm64 usage
* Tue Jan 31 2017 Stephen Rudd <stephen@mnemosyne.co.uk>
- This is a first version of the R package specfile for SymBioInfo
- this is based on docs from https://fedoraproject.org/wiki/Packaging:R?rd=Packaging/R
- this is also intended as a template for automation ...
