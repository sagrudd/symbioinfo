%global packname ont-fast5-api
%global pyversion 3.8
%global packrel 1
%global debug_package %{nil}
%global _python_bytecompile_errors_terminate_build 0

Name:             python-ont-fast5-api
Version:          3.2.0
Release:          %{packrel}%{?dist}
Source0:          https://files.pythonhosted.org/packages/80/f8/36f6abb74da2986ad1a2433dc4702392f988fa569ba19eeb928cff4a852c/ont-fast5-api-3.2.0.tar.gz
License:          Mozilla Public License 2.0 (MPL 2.0) (MPL 2.0)
URL:              https://pypi.org/project/ont-fast5-api/
Group:            Applications/Bioinformatics
Summary:          PackYak v0.0.6 build of Python package [ont-fast5-api] version [3.2.0]

%global _description %{expand:
This workflow has been prepared by the PackYak and description parsing has not
yet been implemented - this is a TODO
}

%description %_description

%package -n python3-bio-%{packname}
%{?python_provide:%python_provide python3-bio-%{packname}}

Summary:          PackYak v0.0.6 build of Python package [ont-fast5-api] version [3.2.0]
BuildRequires:    python3.8 python3-bio-h5py python3-bio-numpy python3-bio-packaging python3-bio-progressbar33 python3-bio-pyparsing
Requires:         python3.8 python3-bio-h5py python3-bio-numpy python3-bio-packaging python3-bio-progressbar33 python3-bio-pyparsing
Provides:         ld-linux-aarch64.so.1(GLIBC_2.17)(64bit)
Provides:         ld-linux-aarch64.so.1()(64bit)

%description -n python3-bio-%{packname} %_description

%prep
%autosetup -p1 -n %{packname}-%{version}
pathfix.py -pni "/usr/bin/python%{pyversion} -s" .

%build
CFLAGS="${CFLAGS:-${RPM_OPT_FLAGS}}" LDFLAGS="${LDFLAGS:-${RPM_LD_FLAGS}}"\
  /usr/bin/python%{pyversion} setup.py  build --executable="/usr/bin/python%{pyversion} -s"

%install
CFLAGS="${CFLAGS:-${RPM_OPT_FLAGS}}" LDFLAGS="${LDFLAGS:-${RPM_LD_FLAGS}}"\
  /usr/bin/python%{pyversion} setup.py  install --root %{buildroot}
if ( [ -d %{buildroot}%{_bindir} ] ); then
    pathfix.py -pni "/usr/bin/python%{pyversion} -s" %{buildroot}/usr/lib/python%{pyversion}/site-packages/ %{buildroot}%{_bindir}/*
fi

%check

%clean
rm -rf $RPM_BUILD_ROOT
rm -fR %{_builddir}/%{packname}*

%files -n python3-bio-ont-fast5-api
/usr/lib/python%{pyversion}/site-packages/ont_fast5_api*
/usr/bin/*

%changelog
* Thu Feb 4 2021  <>
- updated [ont-fast5-api] package version to [3.2.0-1] by PackYak v0.0.6
* Thu Feb 4 2021 sagrudd <stephen@mnemosyne.co.uk>
- rejig of all python libraries to use `python3-bio` product suffix
* Mon Feb 1 2021 sagrudd <stephen@mnemosyne.co.uk>
- updated the R template for usage in Python deployments
- somewhat adherent to https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/
* Mon Jan 11 2021 Stephen Rudd <stephen@mnemosyne.co.uk>
- resurrecting the symbioinfo concept for arm64 usage
* Tue Jan 31 2017 Stephen Rudd <stephen@mnemosyne.co.uk>
- This is a first version of the R package specfile for SymBioInfo
- this is based on docs from https://fedoraproject.org/wiki/Packaging:R?rd=Packaging/R
- this is also intended as a template for automation ...
