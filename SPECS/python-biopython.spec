%global packname biopython
%global pyversion 3.8
%global packrel 1
%global debug_package %{nil}
%global _python_bytecompile_errors_terminate_build 0
%define __brp_python_bytecompile %{nil}
%define __brp_mangle_shebangs %{nil}

%global specfile_lock 1

Name:             python-biopython
Version:          1.77
Release:          %{packrel}%{?dist}
Source0:          https://files.pythonhosted.org/packages/3d/2f/d9df24de05d651c5e686ee8fea3afe3985c03ef9ca02f4cc1e7ea10aa31e/biopython-1.77.tar.gz
License:          Freely Distributable
URL:              https://pypi.org/project/biopython/
Group:            Applications/Bioinformatics
Summary:          PackYak automated build of package = biopython (1.77)

%global _description %{expand:
This workflow has been prepared by the PackYak and description parsing has not
yet been implemented - this is a TODO
}

%description %_description

%package -n python3-bio-%{packname}
%{?python_provide:%python_provide python3-bio-%{packname}}

Summary:        %{summary}
BuildRequires:    python3.8
BuildRequires:    python3-bio-numpy
Requires:         python3.8
Requires:         python3-bio-numpy

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

%files -n  python3-bio-biopython -f INSTALLED_FILES
%defattr(-,root,root)

%changelog
* Tue Feb 16 2021 sagrudd <stephen@mnemosyne.co.uk>
- downgrade of biopython to 1.77 as required by Medaka
* Fri Feb 12 2021 sagrudd <stephen@mnemosyne.co.uk>
- first build of [biopython] version [1.78] by PackYak v0.0.7
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
