#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : ipywidgets
Version  : 7.6.3
Release  : 57
URL      : https://files.pythonhosted.org/packages/3e/52/85aa3969401115cd81d71d60cebf003f84256626e37e0f836b0adf9f3784/ipywidgets-7.6.3.tar.gz
Source0  : https://files.pythonhosted.org/packages/3e/52/85aa3969401115cd81d71d60cebf003f84256626e37e0f836b0adf9f3784/ipywidgets-7.6.3.tar.gz
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
Provides: pypi(ipywidgets)
Requires: pypi(ipykernel)
Requires: pypi(ipython)
Requires: pypi(jupyterlab_widgets)
Requires: pypi(nbformat)
Requires: pypi(traitlets)
Requires: pypi(widgetsnbextension)

%description python3
python3 components for the ipywidgets package.


%prep
%setup -q -n ipywidgets-7.6.3
cd %{_builddir}/ipywidgets-7.6.3

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1610042273
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/ipywidgets
cp %{_builddir}/ipywidgets-7.6.3/LICENSE %{buildroot}/usr/share/package-licenses/ipywidgets/5dc7e0ef3878c3d4a92a7233208e6f91553de266
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/ipywidgets/5dc7e0ef3878c3d4a92a7233208e6f91553de266

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
