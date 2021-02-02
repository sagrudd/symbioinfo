%global packname numpy
%global rversion 4.0.1
%global packrel 1
%global debug_package %{nil}
%global _python_bytecompile_errors_terminate_build 0

Name:             python3-numpy
Version:          1.20.0
Release:          %{packrel}%{?dist}
Source0:          https://files.pythonhosted.org/packages/c3/97/fd507e48f8c7cab73a9f002e52e15983b5636b4ac6cf69b83ae240324b44/numpy-1.20.0.zip
License:          BSD License (BSD)
URL:              https://pypi.org/project/numpy/
Group:            Applications/Bioinformatics
Summary:          PackYak v0.0.5 build of Python package [numpy] version [1.20.0]
BuildRequires:    python-devel
Requires:         python-devel

%description

%prep
%autosetup -p0 -n %{packname}-%{version}
pathfix.py -pni "%{__python3} %{py3_shbang_opts}" .

%build
%{__python3} setup.py build

%install
INSTALLED_FILES=$RPM_BUILD_ROOT/ExtraFiles.list
%{__python3} setup.py install --root=%{buildroot} --record=%{INSTALLED_FILES}

# attempt the pathfix using conditional if the binary directory has been created
if ([ -d %{buildroot}%{_bindir} ]); then
    pathfix.py -pni "%{__python3} %{py3_shbang_opts}" %{buildroot}%{python3_sitearch} %{buildroot}%{_bindir}/*
fi

echo "checking for presence of /usr/lib"
if ([ -d %{buildroot}/usr/lib/ ]); then
  echo "/usr/lib/python3.9/site-packages/"
  %define libhome "/usr/lib/python3.9/site-packages/"
fi
if ([ -d %{buildroot}/usr/lib64/ ]); then
  echo "/usr/lib64/python3.9/site-packages/"
  %define libhome "/usr/lib64/python3.9/site-packages/"
fi
echo %{libhome}

%check

%clean
rm -rf $RPM_BUILD_ROOT
rm -fR %{_builddir}/%{packname}*

%files -f %{INSTALLED_FILES}
%{libhome}

%changelog
* Tue Feb 2 2021 sagrudd <stephen@mnemosyne.co.uk>
- updated [numpy] package version to [1.20.0-1] by PackYak v0.0.5
* Mon Feb 1 2021 sagrudd <stephen@mnemosyne.co.uk>
- updated the R template for usage in Python deployments
* Mon Jan 11 2021 Stephen Rudd <stephen@mnemosyne.co.uk>
- resurrecting the symbioinfo concept for arm64 usage
* Tue Jan 31 2017 Stephen Rudd <stephen@mnemosyne.co.uk>
- This is a first version of the R package specfile for SymBioInfo
- this is based on docs from https://fedoraproject.org/wiki/Packaging:R?rd=Packaging/R
- this is also intended as a template for automation ...
