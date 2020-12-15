#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : python-pkgconfig
Version  : 1.5.1
Release  : 38
URL      : https://files.pythonhosted.org/packages/6e/a9/ff67ef67217dfdf2aca847685fe789f82b931a6957a3deac861297585db6/pkgconfig-1.5.1.tar.gz
Source0  : https://files.pythonhosted.org/packages/6e/a9/ff67ef67217dfdf2aca847685fe789f82b931a6957a3deac861297585db6/pkgconfig-1.5.1.tar.gz
Summary  : Interface Python with pkg-config
Group    : Development/Tools
License  : MIT
Requires: python-pkgconfig-license = %{version}-%{release}
Requires: python-pkgconfig-python = %{version}-%{release}
Requires: python-pkgconfig-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3

%description
pkgconfig
=========
.. image:: https://travis-ci.org/matze/pkgconfig.png?branch=master
:target: https://travis-ci.org/matze/pkgconfig

%package license
Summary: license components for the python-pkgconfig package.
Group: Default

%description license
license components for the python-pkgconfig package.


%package python
Summary: python components for the python-pkgconfig package.
Group: Default
Requires: python-pkgconfig-python3 = %{version}-%{release}

%description python
python components for the python-pkgconfig package.


%package python3
Summary: python3 components for the python-pkgconfig package.
Group: Default
Requires: python3-core
Provides: pypi(pkgconfig)

%description python3
python3 components for the python-pkgconfig package.


%prep
%setup -q -n pkgconfig-1.5.1
cd %{_builddir}/pkgconfig-1.5.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1603402300
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/python-pkgconfig
cp %{_builddir}/pkgconfig-1.5.1/LICENSE %{buildroot}/usr/share/package-licenses/python-pkgconfig/6f33807d1075cf857dc91cf3cf8607894ebd11e0
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/python-pkgconfig/6f33807d1075cf857dc91cf3cf8607894ebd11e0

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
