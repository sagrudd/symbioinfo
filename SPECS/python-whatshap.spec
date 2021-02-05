%global packname whatshap
%global pyversion 3.8
%global packrel 1
%global debug_package %{nil}
%global _python_bytecompile_errors_terminate_build 0

Name:             python-whatshap
Version:          1.0
Release:          %{packrel}%{?dist}
Source0:          https://files.pythonhosted.org/packages/c0/c8/98036e04fb95249128d6b49ca61691e1d8eea484dd94611f90efb5857174/whatshap-1.0.tar.gz
License:          MIT License (MIT)
URL:              https://pypi.org/project/whatshap/
Group:            Applications/Bioinformatics
Summary:          PackYak v0.0.6 build of Python package [whatshap] version [1.0]

%global _description %{expand:
This workflow has been prepared by the PackYak and description parsing has not
yet been implemented - this is a TODO
}

%description %_description

%package -n python3-bio-%{packname}
%{?python_provide:%python_provide python3-bio-%{packname}}

Summary:          PackYak v0.0.6 build of Python package [whatshap] version [1.0]
BuildRequires:    python3.8 python3-bio-biopython python3-bio-networkx python3-bio-pyfaidx python3-bio-pysam python3-bio-scipy python3-bio-xopen python3-bio-numpy python3-bio-decorator python3-bio-setuptools python3-bio-six python3-bio-isal
Requires:         python3.8 python3-bio-biopython python3-bio-networkx python3-bio-pyfaidx python3-bio-pysam python3-bio-scipy python3-bio-xopen python3-bio-numpy python3-bio-decorator python3-bio-setuptools python3-bio-six python3-bio-isal

%description -n python3-bio-%{packname} %_description

%prep
%autosetup -p1 -n %{packname}-%{version}
pathfix.py -pni "/usr/bin/python%{pyversion} -s" .

sed -i -E 's/.include <set>/#include <set>\n#include <stdint.h>/g' src/polyphase/trianglesparsematrix.h

%build

/usr/bin/python%{pyversion} setup.py  build

%install
CXXFLAGS="${CXXFLAGS}" LDFLAGS="${LDFLAGS}"\
  /usr/bin/python%{pyversion} setup.py  install -O1 --skip-build --root %{buildroot}
if ( [ -d %{buildroot}%{_bindir} ] ); then
    pathfix.py -pni "/usr/bin/python%{pyversion} -s" %{buildroot}/usr/lib64/python%{pyversion}/site-packages/ %{buildroot}%{_bindir}/*
fi

%check

%clean
rm -rf $RPM_BUILD_ROOT
rm -fR %{_builddir}/%{packname}*

%files -n python3-bio-whatshap
/usr/lib64/python%{pyversion}/site-packages/%{packname}*
/usr/bin/*

%changelog
* Fri Feb 5 2021 sagrudd <stephen@mnemosyne.co.uk>
- updated [whatshap] package version to [1.0-1] by PackYak v0.0.6
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
