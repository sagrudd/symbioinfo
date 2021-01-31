%define debug_package %{nil}

Name:		muscle
Version:	3.8.1551
Release:	2%{?dist}
Summary:	MUSCLE: multiple sequence alignment with high accuracy and high throughput

Group:          Applications/Bioinformatics
License:	Public Domain
URL:		http://www.drive5.com/muscle/
Source0:	http://www.drive5.com/muscle/muscle_src_3.8.1551.tar.gz
Patch0:		muscle_src_3.8.1551.patch
BuildRequires:	gcc
AutoReqProv:	no


%description    
MUSCLE is one of the best-performing multiple alignment programs according to published benchmark tests, with accuracy and speed that are consistently better than CLUSTALW. MUSCLE can align hundreds of sequences in seconds. Most users learn everything they need to know about MUSCLE in a few minutes—only a handful of command-line options are needed to perform common alignment tasks.

%prep
rm -fR %{name}-%{version}
mkdir %{name}-%{version}
cd %{name}-%{version}
tar -zxvpf %{SOURCE0}
#cd ..
%patch0 -p1 

%build
cd %{name}-%{version}
make

%install
cd %{name}-%{version}
mkdir -p %{buildroot}%{_bindir}
%{__install} -m0755 muscle %{buildroot}%{_bindir}

%clean
rm -fR %{_builddir}/%{name}-%{version}
rm -fR %{buildroot}

%files
%defattr(-,root,root,-)
%{_bindir}/muscle



%changelog
* Sun Jan 31 2021 sagrudd <stephen@mnemosyne.co.uk>
- stripped modulefiles dependency - build for aarch64+x86_64
* Fri Dec 9 2016 Stephen Rudd <stephen@mnemosyne.co.uk>
- appended %define debug_package %{nil} to header of SPEC file
* Tue Apr 26 2016 Stephen Rudd <stephen@mnemosyne.co.uk>
- a first muscle installation - still requires testing and documentation

