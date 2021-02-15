%define debug_package %{nil}

Name:		spoa
Version:	4.0.7
Release:	1%{?dist}
Summary:	spoa
Group:          Applications/Bioinformatics
License:	MIT License 
URL:		https://github.com/rvaser/spoa/
Source0:        https://github.com/rvaser/spoa/archive/4.0.7.tar.gz

BuildRequires:	gcc
Requires:	gcc

%define debug_package %{nil}
%define	_bindir	/usr/bin/
%define _libdir /usr/lib64/
%define _mandir /man
%define _datarootdir /

%description    
Spoa (SIMD POA) is a c++ implementation of the partial order alignment (POA) algorithm (as described in 10.1093/bioinformatics/18.3.452) which is used to generate consensus sequences (as described in 10.1093/bioinformatics/btg109). It supports three alignment modes: local (Smith-Waterman), global (Needleman-Wunsch) and semi-global alignment (overlap), and three gap modes: linear, affine and convex (piecewise affine). It also supports Intel SSE4.1+ and AVX2 vectorization (marginally faster due to high latency shifts), SIMDe and dispatching.


%prep
rm -fR spoa-4.0.7
git clone --recursive https://github.com/rvaser/spoa.git spoa-4.0.7

%build
cd spoa-4.0.7
%set_build_flags
mkdir build && cd build
cmake -Dspoa_build_executable=ON -DCMAKE_BUILD_TYPE=Release ..
make

%install
cd spoa-4.0.7
%{__install} -d %{buildroot}%{_bindir}
%{__install} -m0755 build/bin/spoa %{buildroot}%{_bindir}
%{__install} -d %{buildroot}/%{_libdir}
%{__install} -m0755 build/lib/libspoa.a %{buildroot}/%{_libdir}/

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%{_bindir}/spoa
%{_libdir}/libspoa.a

%clean
rm -rf $RPM_BUILD_ROOT
rm -fR %{buildroot}
rm -fR %{_builddir}/%{name}-%{version}


%changelog
* Fri Jan 22 2021 sagrudd <stephen@mnemosyne.co.uk>
- updated to include the libminimap2.a into /usr/lib64/minimap2
- using this in the Nanopolish build
* Mon Jan 18 2021 sagrudd <stephen@mnemosyne.co.uk>
- updated version to 2.17 - build for aarch64
- note hasindu's comments on arm64 at https://github.com/hasindu2008/minimap2-arm
* Fri Dec 9 2016 Stephen Rudd <stephen@mnemosyne.co.uk>
- appended %define debug_package %{nil} to header of SPEC file
* Wed Feb 03 2016 Stephen Rudd <stephen@mnemosyne.co.uk>
- first version of a minimap RPM for the Heikisho distribution in development
- this builds upon documentation from Mothur website and in makefiles

