%define debug_package %{nil}

Name:		isal
Version:	2.30.0
Release:	1%{?dist}
Summary:	spoa
Group:          Applications/Bioinformatics
License:	BSD-3
URL:		https://github.com/intel/isa-l/
Source0:        https://github.com/intel/isa-l/archive/v2.30.0.tar.gz

BuildRequires:	gcc
Requires:	gcc

%define debug_package %{nil}
%define	_bindir	/usr/bin/
%define _libdir /usr/lib64/
%define _mandir /man
%define _datarootdir /

%description    


%prep
%setup -q -n isa-l-2.30.0


%build

%set_build_flags

./autogen.sh
./configure
make
# sudo make install


%install

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

