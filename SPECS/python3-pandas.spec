%global packname pandas
%global rversion 4.0.1
%global packrel 1
%global debug_package %{nil}
%global _python_bytecompile_errors_terminate_build 0

Name:             python3-pandas
Version:          1.2.1
Release:          %{packrel}%{?dist}
Source0:          https://files.pythonhosted.org/packages/11/1c/b0bc154996617eae877ff267fcf84e55e6c6808dbade0da206f0419dd483/pandas-1.2.1.tar.gz
License:          BSD
URL:              https://pypi.org/project/pandas/
Group:            Applications/Bioinformatics
Summary:          PackYak v0.0.5 build of Python package [pandas] version [1.2.1]
BuildRequires:    python-devel python3-numpy python3-python-dateutil python3-pytz python3-six
Requires:         python-devel python3-numpy python3-python-dateutil python3-pytz python3-six

%description

%prep
%autosetup -p0 -n %{packname}-%{version}
pathfix.py -pni "%{__python3} %{py3_shbang_opts}" .

%build
%py3_build

%install
%{__python3} setup.py install --root=%{buildroot} --record=filelist
# --record=%{INSTALLED_FILES}
if ( [ -d %{buildroot}%{_bindir} ] ); then
    pathfix.py -pni "%{__python3} %{py3_shbang_opts}" %{buildroot}%{python3_sitearch} %{buildroot}%{_bindir}/*
fi

%check

%clean
rm -rf $RPM_BUILD_ROOT
rm -fR %{_builddir}/%{packname}*

%files
/usr/lib64/python3.9/site-packages/%{packname}*
#/usr/lib64/python3.9/site-packages/
# WRT to the above I haven't found a clean fix for identifying if files vanish into lib or lib64 at build time

%changelog
* Tue Feb 2 2021 sagrudd <stephen@mnemosyne.co.uk>
- updated [pandas] package version to [1.2.1-1] by PackYak v0.0.5
* Mon Feb 1 2021 sagrudd <stephen@mnemosyne.co.uk>
- updated the R template for usage in Python deployments
* Mon Jan 11 2021 Stephen Rudd <stephen@mnemosyne.co.uk>
- resurrecting the symbioinfo concept for arm64 usage
* Tue Jan 31 2017 Stephen Rudd <stephen@mnemosyne.co.uk>
- This is a first version of the R package specfile for SymBioInfo
- this is based on docs from https://fedoraproject.org/wiki/Packaging:R?rd=Packaging/R
- this is also intended as a template for automation ...
