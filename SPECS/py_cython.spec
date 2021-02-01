%global packname Cython
%global rversion 4.0.1
%global packrel 1
%global debug_package %{nil}
%global _python_bytecompile_errors_terminate_build 0

Name:             py_cython
Version:          0.29.21
Release:          %{packrel}%{?dist}
Source0:          https://files.pythonhosted.org/packages/6c/9f/f501ba9d178aeb1f5bf7da1ad5619b207c90ac235d9859961c11829d0160/Cython-0.29.21.tar.gz
License:          Apache Software License (Apache)
URL:              https://pypi.org/project/Cython/
Group:            Applications/Bioinformatics
Summary:          PackYak v0.0.5 build of Python package [Cython] version [0.29.21]
BuildRequires:    python-devel
BuildRequires:    /usr/bin/pathfix.py
Requires:         python-devel

%define python3_sitelib /usr/lib64/python3.9/site-packages/
%define __python /usr/bin/python3
%description

%prep
%autosetup -p0 -n %{packname}-%{version}
pathfix.py -pni "%{__python3} %{py3_shbang_opts}" . 

%build
%{__python} setup.py build

%install

%{__python} setup.py install --root=%{buildroot} --record=FILELIST
pathfix.py -pni "%{__python3} %{py3_shbang_opts}" %{buildroot}%{python3_sitearch} %{buildroot}%{_bindir}/*

%check

%clean
rm -rf $RPM_BUILD_ROOT
rm -fR %{_builddir}/%{packname}*

%files
%{python3_sitelib}/*
%{_bindir}/*

%changelog
* Mon Feb 1 2021 sagrudd <stephen@mnemosyne.co.uk>
- updated [Cython] package version to [0.29.21-1] by PackYak v0.0.5
- updated the R template for usage in Python deployments
* Mon Jan 11 2021 Stephen Rudd <stephen@mnemosyne.co.uk>
- resurrecting the symbioinfo concept for arm64 usage
* Tue Jan 31 2017 Stephen Rudd <stephen@mnemosyne.co.uk>
- This is a first version of the R package specfile for SymBioInfo
- this is based on docs from https://fedoraproject.org/wiki/Packaging:R?rd=Packaging/R
- this is also intended as a template for automation ...
