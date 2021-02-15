%global packname pyarrow
%global pyversion 3.8
%global packrel 1
%global debug_package %{nil}
%global _python_bytecompile_errors_terminate_build 0
%define __brp_python_bytecompile %{nil}

Name:             python-pyarrow
Version:          3.0.0
Release:          %{packrel}%{?dist}
Source0:          https://files.pythonhosted.org/packages/62/d3/a482d8a4039bf931ed6388308f0cc0541d0cab46f0bbff7c897a74f1c576/pyarrow-3.0.0.tar.gz
License:          Apache Software License (Apache License, Version 2.0)
URL:              https://pypi.org/project/pyarrow/
Group:            Applications/Bioinformatics
Summary:          PackYak automated build of package = pyarrow (3.0.0)

%global _description %{expand:
This workflow has been prepared by the PackYak and description parsing has not
yet been implemented - this is a TODO
}

%description %_description

%package -n python3-bio-%{packname}
%{?python_provide:%python_provide python3-bio-%{packname}}

Summary:        %{summary}
Provides:         python3.8dist(pyarrow)
Provides:       libarrow.so.400()(64bit)
Provides:       libarrow_python.so.400()(64bit)
BuildRequires:    python3.8
BuildRequires:    python3-bio-numpy
Requires:         python3.8
Requires:         python3-bio-numpy

%description -n python3-bio-%{packname} %_description

%prep
%autosetup -p1 -n %{packname}-%{version}
pathfix.py -pni "/usr/bin/python%{pyversion} -s" .

%build

git clone https://github.com/apache/arrow.git
pushd arrow
git submodule init
git submodule update
export PARQUET_TEST_DATA="${PWD}/cpp/submodules/parquet-testing/data"
export ARROW_TEST_DATA="${PWD}/testing/data"
popd

export ARROW_HOME=$(pwd)/dist
export LD_LIBRARY_PATH=$(pwd)/dist/lib:$LD_LIBRARY_PATH

mkdir arrow/cpp/build
pushd arrow/cpp/build

cmake -DCMAKE_INSTALL_PREFIX=$ARROW_HOME       -DCMAKE_INSTALL_LIBDIR=lib       -DARROW_WITH_BZ2=ON       -DARROW_WITH_ZLIB=ON       -DARROW_WITH_ZSTD=ON       -DARROW_WITH_LZ4=ON       -DARROW_WITH_SNAPPY=ON       -DARROW_WITH_BROTLI=ON       -DARROW_PARQUET=ON       -DARROW_PYTHON=ON       -DARROW_BUILD_TESTS=OFF -DPython3_EXECUTABLE=/usr/bin/python3.8  ..
make -j4
make install 
popd

CFLAGS="${CFLAGS:-${RPM_OPT_FLAGS}}" LDFLAGS="${LDFLAGS:-${RPM_LD_FLAGS}}"\
  /usr/bin/python%{pyversion} setup.py  bdist_wheel

%install


%ifarch aarch64

python3.8 -m pip install -I dist/pyarrow-3.0.0-cp38-cp38-linux_aarch64.whl --root %{buildroot} --no-deps --no-index --no-warn-script-location
rm -rfv %{buildroot}/usr/bin/__pycache__

%else

python3.8 -m pip install -I dist/pyarrow-3.0.0-cp38-cp38-linux_x86_64.whl --root %{buildroot} --no-deps --no-index --no-warn-script-location
rm -rfv %{buildroot}/usr/bin/__pycache__

%endif

%check

%clean
rm -rf $RPM_BUILD_ROOT
rm -fR %{_builddir}/%{packname}*

%files -n  python3-bio-pyarrow
/usr/lib64/python%{pyversion}/site-packages/%{packname}*
/usr/bin/*
%defattr(-,root,root)

%changelog
* Fri Feb 12 2021 sagrudd <stephen@mnemosyne.co.uk>
- first build of [pyarrow] version [3.0.0] by PackYak v0.0.7
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
