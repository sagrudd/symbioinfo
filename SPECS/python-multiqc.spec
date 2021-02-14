%global packname multiqc
%global pyversion 3.8
%global packrel 1
%global debug_package %{nil}
%global _python_bytecompile_errors_terminate_build 0
%define __brp_python_bytecompile %{nil}

Name:             python-multiqc
Version:          1.9
Release:          %{packrel}%{?dist}
Source0:          https://files.pythonhosted.org/packages/c8/2d/f0a6be15f861c5d165726d7afecd823ca158dff530b566379623a0e4534b/multiqc-1.9.tar.gz
License:          GNU General Public License v3 (GPLv3) (GPLv3)
URL:              https://pypi.org/project/multiqc/
Group:            Applications/Bioinformatics
Summary:          PackYak automated build of package = multiqc (1.9)

%global _description %{expand:
This workflow has been prepared by the PackYak and description parsing has not
yet been implemented - this is a TODO
}

%description %_description

%package -n python3-bio-%{packname}
%{?python_provide:%python_provide python3-bio-%{packname}}

Summary:        %{summary}
Provides:         python3.8dist(multiqc)
BuildRequires:    python3.8
BuildRequires:    python3-bio-six
BuildRequires:    python3-bio-colormath
BuildRequires:    python3-bio-urllib3
BuildRequires:    python3-bio-idna
BuildRequires:    python3-bio-chardet
BuildRequires:    python3-bio-certifi
BuildRequires:    python3-bio-decorator
BuildRequires:    python3-bio-python-dateutil
BuildRequires:    python3-bio-pyparsing
BuildRequires:    python3-bio-Pillow
BuildRequires:    python3-bio-kiwisolver
BuildRequires:    python3-bio-cycler
BuildRequires:    python3-bio-MarkupSafe
BuildRequires:    python3-bio-humanfriendly
BuildRequires:    python3-bio-spectra
BuildRequires:    python3-bio-simplejson
BuildRequires:    python3-bio-requests
BuildRequires:    python3-bio-PyYAML
BuildRequires:    python3-bio-numpy
BuildRequires:    python3-bio-networkx
BuildRequires:    python3-bio-matplotlib
BuildRequires:    python3-bio-Markdown
BuildRequires:    python3-bio-lzstring
BuildRequires:    python3-bio-Jinja2
BuildRequires:    python3-bio-future
BuildRequires:    python3-bio-coloredlogs
BuildRequires:    python3-bio-click
Requires:         python3.8
Requires:         python3-bio-six
Requires:         python3-bio-colormath
Requires:         python3-bio-urllib3
Requires:         python3-bio-idna
Requires:         python3-bio-chardet
Requires:         python3-bio-certifi
Requires:         python3-bio-decorator
Requires:         python3-bio-python-dateutil
Requires:         python3-bio-pyparsing
Requires:         python3-bio-Pillow
Requires:         python3-bio-kiwisolver
Requires:         python3-bio-cycler
Requires:         python3-bio-MarkupSafe
Requires:         python3-bio-humanfriendly
Requires:         python3-bio-spectra
Requires:         python3-bio-simplejson
Requires:         python3-bio-requests
Requires:         python3-bio-PyYAML
Requires:         python3-bio-numpy
Requires:         python3-bio-networkx
Requires:         python3-bio-matplotlib
Requires:         python3-bio-Markdown
Requires:         python3-bio-lzstring
Requires:         python3-bio-Jinja2
Requires:         python3-bio-future
Requires:         python3-bio-coloredlogs
Requires:         python3-bio-click

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

%files -n  python3-bio-multiqc -f INSTALLED_FILES
%defattr(-,root,root)

%changelog
* Sun Feb 14 2021 sagrudd <stephen@mnemosyne.co.uk>
- first build of [multiqc] version [1.9] by PackYak v0.0.7
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
