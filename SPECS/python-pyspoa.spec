%global packname pyspoa
%global pyversion 3.8
%global packrel 2
%global debug_package %{nil}
%global _python_bytecompile_errors_terminate_build 0
%global specfile_lock 1

Name:             python-pyspoa
Version:          0.0.5
Release:          %{packrel}%{?dist}
License:          MPL-2.0
URL:              https://github.com/nanoporetech/pyspoa/
Group:            Applications/Bioinformatics
Summary:          PackYak v0.0.6 build of Python package [pyspoa] version [0.0.4]

%global _description %{expand:
This workflow has been prepared by the PackYak and description parsing has not
yet been implemented - this is a TODO
}

%description %_description

%package -n python3-bio-%{packname}
%{?python_provide:%python_provide python3-bio-%{packname}}

Summary:          PackYak v0.0.6 build of Python package [pyspoa] version [0.0.5]
BuildRequires:    python3.8
Requires:         python3.8

%description -n python3-bio-%{packname} %_description

%prep
rm -fR %{packname}-%{version}
git clone --recursive https://github.com/nanoporetech/pyspoa.git %{packname}-%{version}
cd %{packname}-%{version}
pathfix.py -pni "/usr/bin/python%{pyversion} -s" .

%build
cd %{packname}-%{version}

mkdir -p src/build
cd src/build && cmake -D spoa_optimize_for_portability=OFF -DCMAKE_BUILD_TYPE=Release -D CMAKE_CXX_FLAGS="-I ../vendor/cereal/include/ -fPIC" .. && make
cd ../..

CFLAGS="${CFLAGS:-${RPM_OPT_FLAGS}}" LDFLAGS="${LDFLAGS:-${RPM_LD_FLAGS}}"\
  /usr/bin/python%{pyversion} setup.py build

%install
cd %{packname}-%{version}
CFLAGS="${CFLAGS:-${RPM_OPT_FLAGS}}" LDFLAGS="${LDFLAGS:-${RPM_LD_FLAGS}}"\
  /usr/bin/python%{pyversion} setup.py  install -O1 --root %{buildroot}
if ( [ -d %{buildroot}%{_bindir} ] ); then
    pathfix.py -pni "/usr/bin/python%{pyversion} -s" %{buildroot}/usr/lib/python%{pyversion}/site-packages/ %{buildroot}%{_bindir}/*
fi

%check

%clean
rm -rf $RPM_BUILD_ROOT
rm -fR %{_builddir}/%{packname}*

%files -n python3-bio-pyspoa
/usr/lib64/python%{pyversion}/site-packages/%{packname}*
/usr/lib64/python%{pyversion}/site-packages/spoa*

%changelog
* Sat Feb 13 2021 sagrudd <stephen@mnemosyne.co.uk>
- manual update to version 0.0.5
* Thu Feb 4 2021 sagrudd <stephen@mnemosyne.co.uk>
- updated [pyspoa] package version to [v0.0.4] by PackYak v0.0.6
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
