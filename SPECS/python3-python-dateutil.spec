%global packname python-dateutil
%global rversion 4.0.1
%global packrel 1
%global debug_package %{nil}
%global _python_bytecompile_errors_terminate_build 0

Name:             python3-python-dateutil
Version:          2.8.1
Release:          %{packrel}%{?dist}
Source0:          https://files.pythonhosted.org/packages/be/ed/5bbc91f03fa4c839c4c7360375da77f9659af5f7086b7a7bdda65771c8e0/python-dateutil-2.8.1.tar.gz
License:          Apache Software License, BSD License (Dual License)
URL:              https://pypi.org/project/python-dateutil/
Group:            Applications/Bioinformatics
Summary:          PackYak v0.0.5 build of Python package [python-dateutil] version [2.8.1]
BuildRequires:    python-devel python3-six
Requires:         python-devel python3-six

%description

%prep
%autosetup -p0 -n %{packname}-%{version}
pathfix.py -pni "%{__python3} %{py3_shbang_opts}" .

%build
%py3_build

%install
INSTALLED_FILES=$RPM_BUILD_ROOT/ExtraFiles.list
%py3_install
# --record=%{INSTALLED_FILES}
if ( [ -d %{buildroot}%{_bindir} ] ); then
    pathfix.py -pni "%{__python3} %{py3_shbang_opts}" %{buildroot}%{python3_sitearch} %{buildroot}%{_bindir}/*
fi

%check

%clean
rm -rf $RPM_BUILD_ROOT
rm -fR %{_builddir}/%{packname}*

%files
%{python3_sitelib}


%changelog
* Tue Feb 2 2021 sagrudd <stephen@mnemosyne.co.uk>
- updated [python-dateutil] package version to [2.8.1-1] by PackYak v0.0.5
* Mon Feb 1 2021 sagrudd <stephen@mnemosyne.co.uk>
- updated the R template for usage in Python deployments
* Mon Jan 11 2021 Stephen Rudd <stephen@mnemosyne.co.uk>
- resurrecting the symbioinfo concept for arm64 usage
* Tue Jan 31 2017 Stephen Rudd <stephen@mnemosyne.co.uk>
- This is a first version of the R package specfile for SymBioInfo
- this is based on docs from https://fedoraproject.org/wiki/Packaging:R?rd=Packaging/R
- this is also intended as a template for automation ...
