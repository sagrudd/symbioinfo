%global packname medaka
%global pyversion 3.8
%global packrel 1
%global debug_package %{nil}
%global _python_bytecompile_errors_terminate_build 0
%define __brp_python_bytecompile %{nil}

Name:             python-medaka
Version:          1.2.3
Release:          %{packrel}%{?dist}
Source0:          https://files.pythonhosted.org/packages/d4/6c/0e57302fd3dcb1438541d16b6d3a6aa0d2b0e4c946101556776929faa734/medaka-1.2.3.tar.gz
License:          undefined
URL:              https://pypi.org/project/medaka/
Group:            Applications/Bioinformatics
Summary:          PackYak automated build of package = medaka (1.2.3)

%global _description %{expand:
This workflow has been prepared by the PackYak and description parsing has not
yet been implemented - this is a TODO
}

%description %_description

%package -n python3-bio-%{packname}
%{?python_provide:%python_provide python3-bio-%{packname}}

Summary:        %{summary}
Provides:         python3.8dist(medaka)
BuildRequires:    openssl-static
BuildRequires:    python3.8
BuildRequires:    python3-bio-pyasn1
BuildRequires:    python3-bio-oauthlib
BuildRequires:    python3-bio-rsa
BuildRequires:    python3-bio-pyasn1-modules
BuildRequires:    python3-bio-cachetools
BuildRequires:    python3-bio-requests-oauthlib
BuildRequires:    python3-bio-isal
BuildRequires:    python3-bio-decorator
BuildRequires:    python3-bio-Werkzeug
BuildRequires:    python3-bio-tensorboard-plugin-wit
BuildRequires:    python3-bio-setuptools
BuildRequires:    python3-bio-Markdown
BuildRequires:    python3-bio-google-auth
BuildRequires:    python3-bio-google-auth-oauthlib
BuildRequires:    python3-bio-pyparsing
BuildRequires:    python3-bio-xopen
BuildRequires:    python3-bio-pyfaidx
BuildRequires:    python3-bio-networkx
BuildRequires:    python3-bio-wrapt
BuildRequires:    python3-bio-wheel
BuildRequires:    python3-bio-termcolor
BuildRequires:    python3-bio-tensorflow-estimator
BuildRequires:    python3-bio-tensorboard
BuildRequires:    python3-bio-scipy
BuildRequires:    python3-bio-protobuf
BuildRequires:    python3-bio-opt-einsum
BuildRequires:    python3-bio-Keras-Preprocessing
BuildRequires:    python3-bio-google-pasta
BuildRequires:    python3-bio-gast
BuildRequires:    python3-bio-astunparse
BuildRequires:    python3-bio-absl-py
BuildRequires:    python3-bio-urllib3
BuildRequires:    python3-bio-idna
BuildRequires:    python3-bio-chardet
BuildRequires:    python3-bio-certifi
BuildRequires:    python3-bio-pybind11
BuildRequires:    python3-bio-progressbar33
BuildRequires:    python3-bio-packaging
BuildRequires:    python3-bio-sortedcontainers
BuildRequires:    python3-bio-six
BuildRequires:    python3-bio-pycparser
BuildRequires:    python3-bio-whatshap
BuildRequires:    python3-bio-tensorflow
BuildRequires:    python3-bio-requests
BuildRequires:    python3-bio-pyspoa
BuildRequires:    python3-bio-pysam
BuildRequires:    python3-bio-parasail
BuildRequires:    python3-bio-ont-fast5-api
BuildRequires:    python3-bio-numpy
BuildRequires:    python3-bio-mappy
BuildRequires:    python3-bio-intervaltree
BuildRequires:    python3-bio-h5py
BuildRequires:    python3-bio-grpcio
BuildRequires:    python3-bio-edlib
BuildRequires:    python3-bio-cffi
BuildRequires:    python3-bio-biopython
Requires:         python3.8
Requires:         python3-bio-pyasn1
Requires:         python3-bio-oauthlib
Requires:         python3-bio-rsa
Requires:         python3-bio-pyasn1-modules
Requires:         python3-bio-cachetools
Requires:         python3-bio-requests-oauthlib
Requires:         python3-bio-isal
Requires:         python3-bio-decorator
Requires:         python3-bio-Werkzeug
Requires:         python3-bio-tensorboard-plugin-wit
Requires:         python3-bio-setuptools
Requires:         python3-bio-Markdown
Requires:         python3-bio-google-auth
Requires:         python3-bio-google-auth-oauthlib
Requires:         python3-bio-pyparsing
Requires:         python3-bio-xopen
Requires:         python3-bio-pyfaidx
Requires:         python3-bio-networkx
Requires:         python3-bio-wrapt
Requires:         python3-bio-wheel
Requires:         python3-bio-termcolor
Requires:         python3-bio-tensorflow-estimator
Requires:         python3-bio-tensorboard
Requires:         python3-bio-scipy
Requires:         python3-bio-protobuf
Requires:         python3-bio-opt-einsum
Requires:         python3-bio-Keras-Preprocessing
Requires:         python3-bio-google-pasta
Requires:         python3-bio-gast
Requires:         python3-bio-astunparse
Requires:         python3-bio-absl-py
Requires:         python3-bio-urllib3
Requires:         python3-bio-idna
Requires:         python3-bio-chardet
Requires:         python3-bio-certifi
Requires:         python3-bio-pybind11
Requires:         python3-bio-progressbar33
Requires:         python3-bio-packaging
Requires:         python3-bio-sortedcontainers
Requires:         python3-bio-six
Requires:         python3-bio-pycparser
Requires:         python3-bio-whatshap
Requires:         python3-bio-tensorflow
Requires:         python3-bio-requests
Requires:         python3-bio-pyspoa
Requires:         python3-bio-pysam
Requires:         python3-bio-parasail
Requires:         python3-bio-ont-fast5-api
Requires:         python3-bio-numpy
Requires:         python3-bio-mappy
Requires:         python3-bio-intervaltree
Requires:         python3-bio-h5py
Requires:         python3-bio-grpcio
Requires:         python3-bio-edlib
Requires:         python3-bio-cffi
Requires:         python3-bio-biopython

%description -n python3-bio-%{packname} %_description

%prep
%autosetup -p1 -n %{packname}-%{version}
pathfix.py -pni "/usr/bin/python%{pyversion} -s" .

%build

sed -i -E 's/tensorflow==2.2.0/tensorflow>=2.2.0/g' requirements.txt
sed -i -E 's/biopython>=1.73,<1.77.*/biopython>=1.73/g' requirements.txt
sed -i -E 's/h5py<3.0.0/h5py/g' requirements.txt

CFLAGS="${CFLAGS:-${RPM_OPT_FLAGS}}" LDFLAGS="${LDFLAGS:-${RPM_LD_FLAGS}}"\
  /usr/bin/python%{pyversion} setup.py  build --executable="/usr/bin/python%{pyversion} -s"

%install
CFLAGS="${CFLAGS:-${RPM_OPT_FLAGS}}" LDFLAGS="${LDFLAGS:-${RPM_LD_FLAGS}}"\
  /usr/bin/python%{pyversion} setup.py install --single-version-externally-managed -O1 --root=$RPM_BUILD_ROOT --record=INSTALLED_FILES

%check

%clean
rm -rf $RPM_BUILD_ROOT
rm -fR %{_builddir}/%{packname}*

%files -n  python3-bio-medaka -f INSTALLED_FILES
%defattr(-,root,root)

%changelog
* Tue Feb 16 2021 sagrudd <stephen@mnemosyne.co.uk>
- first build of [medaka] version [1.2.3] by PackYak v0.0.8
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
