%global packname google-auth
%global pyversion 3.8
%global packrel 1
%global debug_package %{nil}
%global _python_bytecompile_errors_terminate_build 0

Name:             python-google-auth
Version:          1.25.0
Release:          %{packrel}%{?dist}
Source0:          https://files.pythonhosted.org/packages/cf/8c/cb8431e8ac65d88fd5e5a834dad5add3700de03abacba45531e0326294d4/google-auth-1.25.0.tar.gz
License:          Apache Software License (Apache 2.0)
URL:              https://pypi.org/project/google-auth/
Group:            Applications/Bioinformatics
Summary:          PackYak v0.0.6 build of Python package [google-auth] version [1.25.0]

%global _description %{expand:
This workflow has been prepared by the PackYak and description parsing has not
yet been implemented - this is a TODO
}

%description %_description

%package -n python3-bio-%{packname}
%{?python_provide:%python_provide python3-bio-%{packname}}

Summary:          PackYak v0.0.6 build of Python package [google-auth] version [1.25.0]
BuildRequires:    python3.8 python3-bio-cachetools python3-bio-pyasn1-modules python3-bio-rsa python3-bio-setuptools python3-bio-six python3-bio-pyasn1
Requires:         python3.8 python3-bio-cachetools python3-bio-pyasn1-modules python3-bio-rsa python3-bio-setuptools python3-bio-six python3-bio-pyasn1

%description -n python3-bio-%{packname} %_description

%prep
%autosetup -p1 -n %{packname}-%{version}
pathfix.py -pni "/usr/bin/python%{pyversion} -s" .

%build
CFLAGS="${CFLAGS:-${RPM_OPT_FLAGS}}" LDFLAGS="${LDFLAGS:-${RPM_LD_FLAGS}}"\
  /usr/bin/python%{pyversion} setup.py  build --executable="/usr/bin/python%{pyversion} -s"

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

%files -n python3-bio-google-auth
/usr/lib/python%{pyversion}/site-packages/google*
#/usr/bin/*

%changelog
* Fri Feb 5 2021 sagrudd <stephen@mnemosyne.co.uk>
- updated [google-auth] package version to [1.25.0-1] by PackYak v0.0.6
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
