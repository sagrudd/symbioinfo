%global packname whatshap
%global pyversion 3.8
%global packrel 1
%global debug_package %{nil}
%global _python_bytecompile_errors_terminate_build 0
%define __brp_python_bytecompile %{nil}

Name:             python-whatshap
Version:          1.0
Release:          %{packrel}%{?dist}
Source0:          https://files.pythonhosted.org/packages/c0/c8/98036e04fb95249128d6b49ca61691e1d8eea484dd94611f90efb5857174/whatshap-1.0.tar.gz
License:          MIT License (MIT)
URL:              https://pypi.org/project/whatshap/
Group:            Applications/Bioinformatics
Summary:          PackYak automated build of package = whatshap (1.0)

%global _description %{expand:
This workflow has been prepared by the PackYak and description parsing has not
yet been implemented - this is a TODO
}

%description %_description

%package -n python3-bio-%{packname}
%{?python_provide:%python_provide python3-bio-%{packname}}

Summary:        %{summary}
Provides:         python3.8dist(whatshap)
BuildRequires:    python3.8
BuildRequires:    python3-bio-isal
BuildRequires:    python3-bio-six
BuildRequires:    python3-bio-setuptools
BuildRequires:    python3-bio-decorator
BuildRequires:    python3-bio-numpy
BuildRequires:    python3-bio-xopen
BuildRequires:    python3-bio-scipy
BuildRequires:    python3-bio-pysam
BuildRequires:    python3-bio-pyfaidx
BuildRequires:    python3-bio-networkx
BuildRequires:    python3-bio-biopython
Requires:         python3.8
Requires:         python3-bio-isal
Requires:         python3-bio-six
Requires:         python3-bio-setuptools
Requires:         python3-bio-decorator
Requires:         python3-bio-numpy
Requires:         python3-bio-xopen
Requires:         python3-bio-scipy
Requires:         python3-bio-pysam
Requires:         python3-bio-pyfaidx
Requires:         python3-bio-networkx
Requires:         python3-bio-biopython

%description -n python3-bio-%{packname} %_description

%prep
%autosetup -p1 -n %{packname}-%{version}
sed -i -E 's/.include <set>/#include <set>\n#include <stdint.h>/g' src/polyphase/trianglesparsematrix.h


%build

/usr/bin/python%{pyversion} setup.py  build

%install
CFLAGS="${CFLAGS:-${RPM_OPT_FLAGS}}" LDFLAGS="${LDFLAGS:-${RPM_LD_FLAGS}}"\
  /usr/bin/python%{pyversion} setup.py install --single-version-externally-managed -O1 --root=$RPM_BUILD_ROOT --record=INSTALLED_FILES

%check

%clean
rm -rf $RPM_BUILD_ROOT
rm -fR %{_builddir}/%{packname}*

%files -n  python3-bio-whatshap -f INSTALLED_FILES
%defattr(-,root,root)

%changelog
* Sat Feb 13 2021 sagrudd <stephen@mnemosyne.co.uk>
- first build of [whatshap] version [1.0] by PackYak v0.0.7
* Fri Feb 12 2021 sagrudd <stephen@mnemosyne.co.uk>
- rework of the python setup install to be less dependent on manual intervention
  and finding files ...
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
