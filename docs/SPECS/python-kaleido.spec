%global packname kaleido
%global pyversion 3.8
%global packrel 1
%global debug_package %{nil}
%global _python_bytecompile_errors_terminate_build 0

%global specfile_lock 1

%undefine __brp_mangle_shebangs

Name:             python-kaleido
Version:          0.1.0
Release:          %{packrel}%{?dist}
Source0:          https://github.com/plotly/Kaleido/releases/download/v0.1.0/kaleido-0.1.0-py2.py3-none-manylinux1_x86_64.whl
Source1:          https://github.com/plotly/Kaleido/releases/download/v0.1.0/kaleido-0.1.0-py2.py3-none-manylinux2014_aarch64.whl
License:          MIT
URL:              https://pypi.org/project/kaleido/
Group:            Applications/Bioinformatics
Summary:          PackYak automated build of package = kaleido (0.1.0)

%global _description %{expand:
This workflow has been prepared by the PackYak and description parsing has not
yet been implemented - this is a TODO
}

%description %_description

%package -n python3-bio-%{packname}
%{?python_provide:%python_provide python3-bio-%{packname}}

Summary:        %{summary}
BuildRequires:    python3.8
Requires:         python3.8

%description -n python3-bio-%{packname} %_description

%prep

%build

%install

%ifarch aarch64

python3.8 -m pip install -I %{SOURCE1} --root %{buildroot} --no-deps --no-index --no-warn-script-location
rm -rfv %{buildroot}/usr/bin/__pycache__

%else

python3.8 -m pip install -I %{SOURCE0} --root %{buildroot} --no-deps --no-index --no-warn-script-location
rm -rfv %{buildroot}/usr/bin/__pycache__

%endif

%check

%clean
rm -rf $RPM_BUILD_ROOT
rm -fR %{_builddir}/%{packname}*

%files -n python3-bio-kaleido
/usr/lib/python%{pyversion}/site-packages/%{packname}*
#/usr/bin/*

%changelog
* Thu Feb 11 2021 sagrudd <stephen@mnemosyne.co.uk>
- first build of [kaleido] version [0.1.0.post1] by PackYak v0.0.6
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
