%global packname snakemake
%global pyversion 3.8
%global packrel 1
%global debug_package %{nil}
%global _python_bytecompile_errors_terminate_build 0
%define __brp_python_bytecompile %{nil}

Name:             python-snakemake
Version:          5.32.2
Release:          %{packrel}%{?dist}
Source0:          https://files.pythonhosted.org/packages/d3/c9/d99121a040f9984495367cdc47d75305fc4993f2411d7fb5becd696a1b3d/snakemake-5.32.2.tar.gz
License:          MIT License (MIT)
URL:              https://pypi.org/project/snakemake/
Group:            Applications/Bioinformatics
Summary:          PackYak automated build of package = snakemake (5.32.2)

%global _description %{expand:
This workflow has been prepared by the PackYak and description parsing has not
yet been implemented - this is a TODO
}

%description %_description

%package -n python3-bio-%{packname}
%{?python_provide:%python_provide python3-bio-%{packname}}

Summary:        %{summary}
Provides:         python3.8dist(snakemake)
BuildRequires:    python3.8
BuildRequires:    python3-bio-pyparsing
BuildRequires:    python3-bio-smmap
BuildRequires:    python3-bio-urllib3
BuildRequires:    python3-bio-idna
BuildRequires:    python3-bio-chardet
BuildRequires:    python3-bio-certifi
BuildRequires:    python3-bio-amply
BuildRequires:    python3-bio-traitlets
BuildRequires:    python3-bio-jupyter-core
BuildRequires:    python3-bio-ipython-genutils
BuildRequires:    python3-bio-six
BuildRequires:    python3-bio-setuptools
BuildRequires:    python3-bio-pyrsistent
BuildRequires:    python3-bio-attrs
BuildRequires:    python3-bio-gitdb
BuildRequires:    python3-bio-wrapt
BuildRequires:    python3-bio-toposort
BuildRequires:    python3-bio-requests
BuildRequires:    python3-bio-ratelimiter
BuildRequires:    python3-bio-PyYAML
BuildRequires:    python3-bio-PuLP
BuildRequires:    python3-bio-psutil
BuildRequires:    python3-bio-nbformat
BuildRequires:    python3-bio-jsonschema
BuildRequires:    python3-bio-GitPython
BuildRequires:    python3-bio-docutils
BuildRequires:    python3-bio-datrie
BuildRequires:    python3-bio-ConfigArgParse
BuildRequires:    python3-bio-appdirs
Requires:         python3.8
Requires:         python3-bio-pyparsing
Requires:         python3-bio-smmap
Requires:         python3-bio-urllib3
Requires:         python3-bio-idna
Requires:         python3-bio-chardet
Requires:         python3-bio-certifi
Requires:         python3-bio-amply
Requires:         python3-bio-traitlets
Requires:         python3-bio-jupyter-core
Requires:         python3-bio-ipython-genutils
Requires:         python3-bio-six
Requires:         python3-bio-setuptools
Requires:         python3-bio-pyrsistent
Requires:         python3-bio-attrs
Requires:         python3-bio-gitdb
Requires:         python3-bio-wrapt
Requires:         python3-bio-toposort
Requires:         python3-bio-requests
Requires:         python3-bio-ratelimiter
Requires:         python3-bio-PyYAML
Requires:         python3-bio-PuLP
Requires:         python3-bio-psutil
Requires:         python3-bio-nbformat
Requires:         python3-bio-jsonschema
Requires:         python3-bio-GitPython
Requires:         python3-bio-docutils
Requires:         python3-bio-datrie
Requires:         python3-bio-ConfigArgParse
Requires:         python3-bio-appdirs

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

%files -n  python3-bio-snakemake -f INSTALLED_FILES
%defattr(-,root,root)

%changelog
* Mon Feb 15 2021 sagrudd <stephen@mnemosyne.co.uk>
- first build of [snakemake] version [5.32.2] by PackYak v0.0.7
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
