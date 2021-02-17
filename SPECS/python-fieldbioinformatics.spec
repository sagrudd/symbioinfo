%global packname fieldbioinformatics
%global pyversion 3.8
%global packrel 1
%global debug_package %{nil}
%global _python_bytecompile_errors_terminate_build 0
%define __brp_python_bytecompile %{nil}

Name:             python-fieldbioinformatics
Version:          1.2.1
Release:          %{packrel}%{?dist}
Source0:          https://github.com/artic-network/fieldbioinformatics/archive/1.2.1.tar.gz
License:          MIT
URL:              https://github.com/artic-network/fieldbioinformatics
Group:            Applications/Bioinformatics
Summary:          PackYak automated build of package = medaka (1.2.3)

%global _description %{expand:
artic is a pipeline and set of accompanying tools for working with viral nanopore sequencing data, generated from tiling amplicon schemes.

It is designed to help run the artic bioinformatics protocols; for example the SARS-CoV-2 coronavirus protocol.

Features include:

    read filtering
    primer trimming
    amplicon coverage normalisation
    variant calling
    consensus building

There are 2 workflows baked into this pipeline, one which uses signal data (via nanopolish) and one that does not (via medaka).
}

%description %_description

%package -n python3-bio-%{packname}
%{?python_provide:%python_provide python3-bio-%{packname}}

Summary:        %{summary}
Provides:         python3.8dist(fieldbioinformatics)
BuildRequires:    python3.8
BuildRequires:    python3-bio-medaka
Requires:         python3.8
Requires:         python3-bio-medaka

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

%files -n  python3-bio-fieldbioinformatics -f INSTALLED_FILES
%defattr(-,root,root)

%changelog
* Tue Feb 16 2021 sagrudd <stephen@mnemosyne.co.uk>
- first build of [fieldbioinformatics] version [1.2.1] - borrowed from PackYak template
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
