%define pkg_name multipip
%define version 0.1
%define unmangled_version 0.1
%define release 1

Summary: multipip and py2rpm
Name: python-multipip
Version: %{version}
Release: %{release}%{?dist}
Source0: %{pkg_name}-%{unmangled_version}.tar.gz
License: Apache License (2.0)
Group: Development/Libraries
BuildRoot: %{_tmppath}/%{pkg_name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
BuildArch: noarch
Vendor: Alessio Ababilov <ilovegnulinux@gmail.com>
Url: https://github.com/aababilov/multipip
Requires: rpm-build
Requires: python-setuptools
Requires: python-pip
Requires: python-argparse

%description
Tools for building RPMs for Python packages.

%prep
%setup -n %{pkg_name}-%{unmangled_version}

%build
python setup.py build

%install
python setup.py install -O1 --root=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README* LICENSE
%{_bindir}/*
%{python_sitelib}/*
