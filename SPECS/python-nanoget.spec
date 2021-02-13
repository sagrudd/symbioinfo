%global packname nanoget
%global pyversion 3.8
%global packrel 1
%global debug_package %{nil}
%global _python_bytecompile_errors_terminate_build 0
%define __brp_python_bytecompile %{nil}

Name:             python-nanoget
Version:          1.15.0
Release:          %{packrel}%{?dist}
Source0:          https://files.pythonhosted.org/packages/2b/7a/b87c809a2d08cb48ddaefa9e1e45b4cfd3a071417155e5b514dc9d74d7f2/nanoget-1.15.0.tar.gz
License:          GNU General Public License v3 (GPLv3) (GPLv3)
URL:              https://pypi.org/project/nanoget/
Group:            Applications/Bioinformatics
Summary:          PackYak automated build of package = nanoget (1.15.0)

%global _description %{expand:
This workflow has been prepared by the PackYak and description parsing has not
yet been implemented - this is a TODO
}

%description %_description

%package -n python3-bio-%{packname}
%{?python_provide:%python_provide python3-bio-%{packname}}

Summary:        %{summary}
Provides:         python3.8dist(nanoget)
BuildRequires:    python3.8
BuildRequires:    python3-bio-six
BuildRequires:    python3-bio-pytz
BuildRequires:    python3-bio-python-dateutil
BuildRequires:    python3-bio-pysam
BuildRequires:    python3-bio-pandas
BuildRequires:    python3-bio-numpy
BuildRequires:    python3-bio-biopython
Requires:         python3.8
Requires:         python3-bio-six
Requires:         python3-bio-pytz
Requires:         python3-bio-python-dateutil
Requires:         python3-bio-pysam
Requires:         python3-bio-pandas
Requires:         python3-bio-numpy
Requires:         python3-bio-biopython

%description -n python3-bio-%{packname} %_description

%prep
%autosetup -p1 -n %{packname}-%{version}
pathfix.py -pni "/usr/bin/python%{pyversion} -s" .

%build
CFLAGS="${CFLAGS:-${RPM_OPT_FLAGS}}" LDFLAGS="${LDFLAGS:-${RPM_LD_FLAGS}}"\
  /usr/bin/python%{pyversion} setup.py  build --executable="/usr/bin/python%{pyversion} -s"

%install
CFLAGS="${CFLAGS:-${RPM_OPT_FLAGS}}" LDFLAGS="${LDFLAGS:-${RPM_LD_FLAGS}}"\
  /usr/bin/python%{pyversion} setup.py install --single-version-externally-managed -O1 --root=$RPM_BUILD_ROOT --record=INSTALLED_FILES

%check

%clean
rm -rf $RPM_BUILD_ROOT
rm -fR %{_builddir}/%{packname}*

%files -n  python3-bio-nanoget -f INSTALLED_FILES
%defattr(-,root,root)

%changelog
* Sat Feb 13 2021 sagrudd <stephen@mnemosyne.co.uk>
- first build of [nanoget] version [1.15.0] by PackYak v0.0.7
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
