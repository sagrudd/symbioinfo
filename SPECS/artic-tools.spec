%define debug_package %{nil}

Name:		artic-tools
Version:	0.3.0
Release:	1%{?dist}
Summary:	artic-tools
Group:          Applications/Bioinformatics
License:	MIT
URL:		https://github.com/will-rowe/artic-tools

BuildRequires:	gcc
Requires:	gcc

%description    
tools to accompany the artic fieldbioinformatics

%prep
rm -fR artic-tools
git clone --recursive https://github.com/will-rowe/artic-tools

%build
cd artic-tools
mkdir build
cd build
cmake ..
make -j4


%install
cd artic-tools
mkdir -p %{buildroot}/usr/local/bin/

%{__install} -d %{buildroot}/usr/local/bin/
%{__install} -m0755 ./bin/artic-tools %{buildroot}/usr/local/bin/

%files
%defattr(-,root,root,-)
/usr/local/bin/artic-tools

%clean
rm -rf $RPM_BUILD_ROOT
rm -fR %{buildroot}
rm -fR %{_builddir}/%{name}-%{version}


%changelog
* Mon Feb 22 2021 sagrudd <stephen@mnemosyne.co.uk>
- first hacktogether of artic-tools to support FieldBioinformatics 1.3.0
