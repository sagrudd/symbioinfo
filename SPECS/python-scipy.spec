%global packname scipy
%global pyversion 3.8
%global packrel 1
%global debug_package %{nil}
%global _python_bytecompile_errors_terminate_build 0

Name:             python-scipy
Version:          1.6.0
Release:          %{packrel}%{?dist}
Source0:          https://files.pythonhosted.org/packages/16/48/ff7026d26dfd92520f00b109333e22c05a235f0c9115a5a2d7679cdf39ef/scipy-1.6.0.tar.gz
License:          BSD License (BSD)
URL:              https://pypi.org/project/scipy/
Group:            Applications/Bioinformatics
Summary:          PackYak v0.0.6 build of Python package [scipy] version [1.6.0]

%global _description %{expand:
This workflow has been prepared by the PackYak and description parsing has not
yet been implemented - this is a TODO
}

%description %_description

%package -n python3-bio-%{packname}
%{?python_provide:%python_provide python3-bio-%{packname}}

Summary:          PackYak v0.0.6 build of Python package [scipy] version [1.6.0]
BuildRequires:    python3.8 python3-bio-numpy gcc-fortran swig gcc-c++ qhull-devel fftw-devel suitesparse-devel openblas-devel
Requires:         python3.8 python3-bio-numpy

%description -n python3-bio-%{packname} %_description

%prep
%autosetup -p1 -n %{packname}-%{version}
pathfix.py -pni "/usr/bin/python%{pyversion} -s" .

%build
#CFLAGS="${CFLAGS:-${RPM_OPT_FLAGS}}" LDFLAGS="${LDFLAGS:-${RPM_LD_FLAGS}}"\
CFLAGS="$RPM_OPT_FLAGS -lm" FFLAGS="$RPM_OPT_FLAGS -fPIC -fallow-argument-mismatch"     OPENBLAS=%{_libdir} \
    FFTW=%{_libdir} BLAS=%{_libdir} LAPACK=%{_libdir} \
    /usr/bin/python%{pyversion} setup.py config_fc \
    --fcompiler=gnu95 --noarch  build

%install
CFLAGS="${CFLAGS:-${RPM_OPT_FLAGS}}" LDFLAGS="${LDFLAGS:-${RPM_LD_FLAGS}}"\
  /usr/bin/python%{pyversion} setup.py  install -O1 --skip-build --root %{buildroot}
if ( [ -d %{buildroot}%{_bindir} ] ); then
    pathfix.py -pni "/usr/bin/python%{pyversion} -s" %{buildroot}/usr/lib/python%{pyversion}/site-packages/ %{buildroot}%{_bindir}/*
fi

%check

%clean
rm -rf $RPM_BUILD_ROOT
rm -fR %{_builddir}/%{packname}*

%files -n python3-bio-scipy
/usr/lib64/python%{pyversion}/site-packages/%{packname}*
#/usr/bin/*

%changelog
* Thu Feb 4 2021  <>
- updated [scipy] package version to [1.6.0-1] by PackYak v0.0.6
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
