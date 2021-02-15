%global packname NanoComp
%global pyversion 3.8
%global packrel 1
%global debug_package %{nil}
%global _python_bytecompile_errors_terminate_build 0
%define __brp_python_bytecompile %{nil}

Name:             python-NanoComp
Version:          1.13.1
Release:          %{packrel}%{?dist}
Source0:          https://files.pythonhosted.org/packages/25/61/b268f64c3adfa92b59b5ff5521b6fb246bec0019bcb6aac4156c7200ad68/NanoComp-1.13.1.tar.gz
License:          GNU General Public License v3 (GPLv3) (GPLv3)
URL:              https://pypi.org/project/NanoComp/
Group:            Applications/Bioinformatics
Summary:          PackYak automated build of package = NanoComp (1.13.1)

%global _description %{expand:
This workflow has been prepared by the PackYak and description parsing has not
yet been implemented - this is a TODO
}

%description %_description

%package -n python3-bio-%{packname}
%{?python_provide:%python_provide python3-bio-%{packname}}

Summary:        %{summary}
Provides:         python3.8dist(NanoComp)
BuildRequires:    python3.8
BuildRequires:    python3-bio-threadpoolctl
BuildRequires:    python3-bio-joblib
BuildRequires:    python3-bio-scikit-learn
BuildRequires:    python3-bio-six
BuildRequires:    python3-bio-retrying
BuildRequires:    python3-bio-pytz
BuildRequires:    python3-bio-Python-Deprecated
BuildRequires:    python3-bio-pyparsing
BuildRequires:    python3-bio-Pillow
BuildRequires:    python3-bio-kiwisolver
BuildRequires:    python3-bio-cycler
BuildRequires:    python3-bio-scipy
BuildRequires:    python3-bio-python-dateutil
BuildRequires:    python3-bio-pysam
BuildRequires:    python3-bio-pauvre
BuildRequires:    python3-bio-kaleido
BuildRequires:    python3-bio-biopython
BuildRequires:    python3-bio-seaborn
BuildRequires:    python3-bio-pyarrow
BuildRequires:    python3-bio-psutil
BuildRequires:    python3-bio-plotly
BuildRequires:    python3-bio-pandas
BuildRequires:    python3-bio-numpy
BuildRequires:    python3-bio-nanomath
BuildRequires:    python3-bio-nanoget
BuildRequires:    python3-bio-matplotlib
BuildRequires:    python3-bio-joypy
BuildRequires:    python3-bio-NanoPlot
Requires:         python3.8
Requires:         python3-bio-threadpoolctl
Requires:         python3-bio-joblib
Requires:         python3-bio-scikit-learn
Requires:         python3-bio-six
Requires:         python3-bio-retrying
Requires:         python3-bio-pytz
Requires:         python3-bio-Python-Deprecated
Requires:         python3-bio-pyparsing
Requires:         python3-bio-Pillow
Requires:         python3-bio-kiwisolver
Requires:         python3-bio-cycler
Requires:         python3-bio-scipy
Requires:         python3-bio-python-dateutil
Requires:         python3-bio-pysam
Requires:         python3-bio-pauvre
Requires:         python3-bio-kaleido
Requires:         python3-bio-biopython
Requires:         python3-bio-seaborn
Requires:         python3-bio-pyarrow
Requires:         python3-bio-psutil
Requires:         python3-bio-plotly
Requires:         python3-bio-pandas
Requires:         python3-bio-numpy
Requires:         python3-bio-nanomath
Requires:         python3-bio-nanoget
Requires:         python3-bio-matplotlib
Requires:         python3-bio-joypy
Requires:         python3-bio-NanoPlot

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
rm -f $RPM_BUILD_ROOT/usr/lib/python3.8/site-packages/scripts/test.sh
sed -i '/site-packages\/scripts\/test.sh/d' ./INSTALLED_FILES

%check

%clean
rm -rf $RPM_BUILD_ROOT
rm -fR %{_builddir}/%{packname}*

%files -n  python3-bio-NanoComp -f INSTALLED_FILES
%defattr(-,root,root)

%changelog
* Mon Feb 15 2021 sagrudd <stephen@mnemosyne.co.uk>
- first build of [NanoComp] version [1.13.1] by PackYak v0.0.7
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
