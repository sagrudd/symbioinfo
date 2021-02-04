%global packname numpy
%global pyversion 3.8
%global packrel 1
%global debug_package %{nil}
%global _python_bytecompile_errors_terminate_build 0

Name:             python-numpy
Version:          1.20.0
Release:          %{packrel}%{?dist}
Source0:          https://files.pythonhosted.org/packages/c3/97/fd507e48f8c7cab73a9f002e52e15983b5636b4ac6cf69b83ae240324b44/numpy-1.20.0.zip
License:          BSD License (BSD)
URL:              https://pypi.org/project/numpy/
Group:            Applications/Bioinformatics
Summary:          PackYak v0.0.6 build of Python package [numpy] version [1.20.0]

%global blaslib flexiblas
	
%global blasvar %{nil}

%global _description %{expand:
This workflow has been prepared by the PackYak and description parsing has not
yet been implemented - this is a TODO
}

%description %_description

%package -n python3-bio-%{packname}
%{?python_provide:%python_provide python3-bio-%{packname}}

Summary:          PackYak v0.0.6 build of Python package [numpy] version [1.20.0]
BuildRequires:    python3.8 lapack-devel atlas-devel
Requires:         python3.8

%description -n python3-bio-%{packname} %_description

%prep
%autosetup -p1 -n %{packname}-%{version}
pathfix.py -pni "/usr/bin/python%{pyversion} -s" .
cat >> site.cfg <<EOF
[openblas]
libraries = %{blaslib}%{blasvar}
library_dirs = %{_libdir}	
EOF


%build
	
%set_build_flags

env OPENBLAS=%{_libdir} \
    BLAS=%{_libdir} \
    LAPACK=%{_libdir} CFLAGS="%{optflags}" \
    CFLAGS="${CFLAGS:-${RPM_OPT_FLAGS}}" LDFLAGS="${LDFLAGS:-${RPM_LD_FLAGS}}"\
    /usr/bin/python%{pyversion} setup.py  build --executable="/usr/bin/python%{pyversion} -s"

%install
env OPENBLAS=%{_libdir} \
    FFTW=%{_libdir} BLAS=%{_libdir} \
    LAPACK=%{_libdir} CFLAGS="%{optflags}" \
  /usr/bin/python%{pyversion} setup.py  install --root %{buildroot}
if ( [ -d %{buildroot}%{_bindir} ] ); then
    pathfix.py -pni "/usr/bin/python%{pyversion} -s" %{buildroot}/usr/lib64/python%{pyversion}/site-packages/ %{buildroot}%{_bindir}/*
fi

%check

%clean
rm -rf $RPM_BUILD_ROOT
rm -fR %{_builddir}/%{packname}*

%files -n python3-bio-numpy
/usr/lib64/python%{pyversion}/site-packages/%{packname}*
/usr/bin/*

%changelog
* Thu Feb 4 2021 sagrudd <stephen@mnemosyne.co.uk>
- updated [numpy] package version to [1.20.0-1] by PackYak v0.0.6
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
