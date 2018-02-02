#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : python-pkgconfig
Version  : 1.2.2
Release  : 12
URL      : https://pypi.debian.net/pkgconfig/pkgconfig-1.2.2.tar.gz
Source0  : https://pypi.debian.net/pkgconfig/pkgconfig-1.2.2.tar.gz
Summary  : Interface Python with pkg-config
Group    : Development/Tools
License  : MIT
Requires: python-pkgconfig-legacypython
Requires: python-pkgconfig-python3
Requires: python-pkgconfig-python
BuildRequires : nose
BuildRequires : pbr
BuildRequires : pip
BuildRequires : python-dev
BuildRequires : python3-dev
BuildRequires : setuptools

%description
=========

%package legacypython
Summary: legacypython components for the python-pkgconfig package.
Group: Default
Requires: python-core

%description legacypython
legacypython components for the python-pkgconfig package.


%package python
Summary: python components for the python-pkgconfig package.
Group: Default
Requires: python-pkgconfig-legacypython
Requires: python-pkgconfig-python3

%description python
python components for the python-pkgconfig package.


%package python3
Summary: python3 components for the python-pkgconfig package.
Group: Default
Requires: python3-core

%description python3
python3 components for the python-pkgconfig package.


%prep
%setup -q -n pkgconfig-1.2.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1507170341
python2 setup.py build -b py2
python3 setup.py build -b py3

%install
export SOURCE_DATE_EPOCH=1507170341
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot} --force
python3 -tt setup.py build -b py3 install --root=%{buildroot} --force
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files legacypython
%defattr(-,root,root,-)
/usr/lib/python2*/*

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
