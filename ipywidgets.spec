#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : ipywidgets
Version  : 7.5.0
Release  : 40
URL      : https://files.pythonhosted.org/packages/53/93/708cdb1feda1ec2d55ee9357d319a92f4d9adb61e5822a323aac9a6af8e6/ipywidgets-7.5.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/53/93/708cdb1feda1ec2d55ee9357d319a92f4d9adb61e5822a323aac9a6af8e6/ipywidgets-7.5.0.tar.gz
Summary  : IPython HTML widgets for Jupyter
Group    : Development/Tools
License  : BSD-3-Clause
Requires: ipywidgets-license = %{version}-%{release}
Requires: ipywidgets-python = %{version}-%{release}
Requires: ipywidgets-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3

%description
# ipywidgets: Interactive HTML Widgets
[![Version](https://img.shields.io/pypi/v/ipywidgets.svg)](https://pypi.python.org/pypi/ipywidgets)
[![Build Status](https://travis-ci.org/jupyter-widgets/ipywidgets.svg?branch=master)](https://travis-ci.org/jupyter-widgets/ipywidgets)
[![Documentation Status](http://readthedocs.org/projects/ipywidgets/badge/?version=latest)](https://ipywidgets.readthedocs.io/en/latest/?badge=latest)
[![Join the chat at https://gitter.im/ipython/ipywidgets](https://badges.gitter.im/Join%20Chat.svg)](https://gitter.im/jupyter-widgets/Lobby)
[![Binder](https://mybinder.org/badge.svg)](https://mybinder.org/v2/gh/jupyter-widgets/ipywidgets/master?filepath=docs%2Fsource%2Fexamples)

%package license
Summary: license components for the ipywidgets package.
Group: Default

%description license
license components for the ipywidgets package.


%package python
Summary: python components for the ipywidgets package.
Group: Default
Requires: ipywidgets-python3 = %{version}-%{release}

%description python
python components for the ipywidgets package.


%package python3
Summary: python3 components for the ipywidgets package.
Group: Default
Requires: python3-core

%description python3
python3 components for the ipywidgets package.


%prep
%setup -q -n ipywidgets-7.5.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1562031760
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/ipywidgets
cp LICENSE %{buildroot}/usr/share/package-licenses/ipywidgets/LICENSE
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/ipywidgets/LICENSE

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
