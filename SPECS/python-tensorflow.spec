%global packname tensorflow
%global pyversion 3.8
%global packrel 1
%global debug_package %{nil}
%global _python_bytecompile_errors_terminate_build 0
%define __brp_python_bytecompile %{nil}

Name:             python-tensorflow
Version:          2.4.1
Release:          %{packrel}%{?dist}
Source0:          https://github.com/tensorflow/tensorflow/archive/v2.4.1.tar.gz
License:          Apache Software License (Apache 2.0)
URL:              https://pypi.org/project/tensorflow/
Group:            Applications/Bioinformatics
Summary:          PackYak automated build of package = tensorflow (2.4.1)

%global _description %{expand:
This workflow has been prepared by the PackYak and description parsing has not
yet been implemented - this is a TODO
}

%description %_description

%package -n python3-bio-%{packname}
%{?python_provide:%python_provide python3-bio-%{packname}}

Summary:        %{summary}
Provides:         python3.8dist(tensorflow)
BuildRequires:    python3.8
BuildRequires:    python3-bio-pyasn1
BuildRequires:    python3-bio-oauthlib
BuildRequires:    python3-bio-urllib3
BuildRequires:    python3-bio-idna
BuildRequires:    python3-bio-chardet
BuildRequires:    python3-bio-certifi
BuildRequires:    python3-bio-rsa
BuildRequires:    python3-bio-pyasn1-modules
BuildRequires:    python3-bio-cachetools
BuildRequires:    python3-bio-requests-oauthlib
BuildRequires:    python3-bio-Werkzeug
BuildRequires:    python3-bio-tensorboard-plugin-wit
BuildRequires:    python3-bio-setuptools
BuildRequires:    python3-bio-requests
BuildRequires:    python3-bio-Markdown
BuildRequires:    python3-bio-google-auth
BuildRequires:    python3-bio-google-auth-oauthlib
BuildRequires:    python3-bio-wrapt
BuildRequires:    python3-bio-wheel
BuildRequires:    python3-bio-typing-extensions
BuildRequires:    python3-bio-termcolor
BuildRequires:    python3-bio-tensorflow-estimator
BuildRequires:    python3-bio-tensorboard
BuildRequires:    python3-bio-six
BuildRequires:    python3-bio-protobuf
BuildRequires:    python3-bio-opt-einsum
BuildRequires:    python3-bio-numpy
BuildRequires:    python3-bio-Keras-Preprocessing
BuildRequires:    python3-bio-h5py
BuildRequires:    python3-bio-grpcio
BuildRequires:    python3-bio-google-pasta
BuildRequires:    python3-bio-gast
BuildRequires:    python3-bio-flatbuffers
BuildRequires:    python3-bio-astunparse
BuildRequires:    python3-bio-absl-py
Requires:         python3.8
Requires:         python3-bio-pyasn1
Requires:         python3-bio-oauthlib
Requires:         python3-bio-urllib3
Requires:         python3-bio-idna
Requires:         python3-bio-chardet
Requires:         python3-bio-certifi
Requires:         python3-bio-rsa
Requires:         python3-bio-pyasn1-modules
Requires:         python3-bio-cachetools
Requires:         python3-bio-requests-oauthlib
Requires:         python3-bio-Werkzeug
Requires:         python3-bio-tensorboard-plugin-wit
Requires:         python3-bio-setuptools
Requires:         python3-bio-requests
Requires:         python3-bio-Markdown
Requires:         python3-bio-google-auth
Requires:         python3-bio-google-auth-oauthlib
Requires:         python3-bio-wrapt
Requires:         python3-bio-wheel
Requires:         python3-bio-typing-extensions
Requires:         python3-bio-termcolor
Requires:         python3-bio-tensorflow-estimator
Requires:         python3-bio-tensorboard
Requires:         python3-bio-six
Requires:         python3-bio-protobuf
Requires:         python3-bio-opt-einsum
Requires:         python3-bio-numpy
Requires:         python3-bio-Keras-Preprocessing
Requires:         python3-bio-h5py
Requires:         python3-bio-grpcio
Requires:         python3-bio-google-pasta
Requires:         python3-bio-gast
Requires:         python3-bio-flatbuffers
Requires:         python3-bio-astunparse
Requires:         python3-bio-absl-py

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

%files -n  python3-bio-tensorflow -f INSTALLED_FILES
%defattr(-,root,root)

%changelog
* Sat Feb 13 2021 sagrudd <stephen@mnemosyne.co.uk>
- first build of [tensorflow] version [2.4.1] by PackYak v0.0.7
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
