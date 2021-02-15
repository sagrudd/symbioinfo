%global packname methplotlib
%global pyversion 3.8
%global packrel 1
%global debug_package %{nil}
%global _python_bytecompile_errors_terminate_build 0
%define __brp_python_bytecompile %{nil}

%undefine __brp_mangle_shebangs

Name:             python-methplotlib
Version:          0.17.0
Release:          %{packrel}%{?dist}
Source0:          https://files.pythonhosted.org/packages/c7/a1/154c3b7e600726f090e85a58ccbdc90f5036f4f0f04121e5f1b913a31950/methplotlib-0.17.0.tar.gz
License:          MIT License (MIT)
URL:              https://pypi.org/project/methplotlib/
Group:            Applications/Bioinformatics
Summary:          PackYak automated build of package = methplotlib (0.17.0)

%global _description %{expand:
This workflow has been prepared by the PackYak and description parsing has not
yet been implemented - this is a TODO
}

%description %_description

%package -n python3-bio-%{packname}
%{?python_provide:%python_provide python3-bio-%{packname}}

Summary:        %{summary}
Provides:         python3.8dist(methplotlib)
BuildRequires:    python3.8
BuildRequires:    python3-bio-threadpoolctl
BuildRequires:    python3-bio-scipy
BuildRequires:    python3-bio-joblib
BuildRequires:    python3-bio-scikit-learn
BuildRequires:    python3-bio-tabulate
BuildRequires:    python3-bio-sorted-nearest
BuildRequires:    python3-bio-pyrle
BuildRequires:    python3-bio-ncls
BuildRequires:    python3-bio-natsort
BuildRequires:    python3-bio-Cython
BuildRequires:    python3-bio-setuptools
BuildRequires:    python3-bio-six
BuildRequires:    python3-bio-retrying
BuildRequires:    python3-bio-pytz
BuildRequires:    python3-bio-python-dateutil
BuildRequires:    python3-bio-sklearn
BuildRequires:    python3-bio-pysam
BuildRequires:    python3-bio-pyranges
BuildRequires:    python3-bio-pyfaidx
BuildRequires:    python3-bio-plotly
BuildRequires:    python3-bio-pandas
BuildRequires:    python3-bio-numpy
BuildRequires:    python3-bio-fisher
BuildRequires:    python3-bio-biopython
Requires:         python3.8
Requires:         python3-bio-threadpoolctl
Requires:         python3-bio-scipy
Requires:         python3-bio-joblib
Requires:         python3-bio-scikit-learn
Requires:         python3-bio-tabulate
Requires:         python3-bio-sorted-nearest
Requires:         python3-bio-pyrle
Requires:         python3-bio-ncls
Requires:         python3-bio-natsort
Requires:         python3-bio-Cython
Requires:         python3-bio-setuptools
Requires:         python3-bio-six
Requires:         python3-bio-retrying
Requires:         python3-bio-pytz
Requires:         python3-bio-python-dateutil
Requires:         python3-bio-sklearn
Requires:         python3-bio-pysam
Requires:         python3-bio-pyranges
Requires:         python3-bio-pyfaidx
Requires:         python3-bio-plotly
Requires:         python3-bio-pandas
Requires:         python3-bio-numpy
Requires:         python3-bio-fisher
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

%files -n  python3-bio-methplotlib -f INSTALLED_FILES
%defattr(-,root,root)

%changelog
* Mon Feb 15 2021 sagrudd <stephen@mnemosyne.co.uk>
- first build of [methplotlib] version [0.17.0] by PackYak v0.0.7
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
