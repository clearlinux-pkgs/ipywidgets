#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : ipywidgets
Version  : 7.1.2
Release  : 15
URL      : https://pypi.python.org/packages/00/6e/1bcda14078d8ebee6cff0c67ccba1a528a5ec636954ebe0af5fdebf9b6bf/ipywidgets-7.1.2.tar.gz
Source0  : https://pypi.python.org/packages/00/6e/1bcda14078d8ebee6cff0c67ccba1a528a5ec636954ebe0af5fdebf9b6bf/ipywidgets-7.1.2.tar.gz
Summary  : IPython HTML widgets for Jupyter
Group    : Development/Tools
License  : BSD-3-Clause-Clear
Requires: ipywidgets-python3
Requires: ipywidgets-python
Requires: Sphinx
Requires: ipykernel
Requires: ipywidgets
Requires: jupyter_client
BuildRequires : pbr
BuildRequires : pip
BuildRequires : python-dev
BuildRequires : python3-dev
BuildRequires : setuptools

%description
# ipywidgets: Interactive HTML Widgets
[![Version](https://img.shields.io/pypi/v/ipywidgets.svg)](https://pypi.python.org/pypi/ipywidgets)
[![Downloads](https://img.shields.io/pypi/dm/ipywidgets.svg)](https://pypi.python.org/pypi/ipywidgets)
[![Build Status](https://travis-ci.org/jupyter-widgets/ipywidgets.svg?branch=master)](https://travis-ci.org/jupyter-widgets/ipywidgets)
[![Documentation Status](http://readthedocs.org/projects/ipywidgets/badge/?version=latest)](https://ipywidgets.readthedocs.io/en/latest/?badge=latest)
[![Join the chat at https://gitter.im/ipython/ipywidgets](https://badges.gitter.im/Join%20Chat.svg)](https://gitter.im/jupyter-widgets/Lobby)

%package legacypython
Summary: legacypython components for the ipywidgets package.
Group: Default
Requires: python-core

%description legacypython
legacypython components for the ipywidgets package.


%package python
Summary: python components for the ipywidgets package.
Group: Default
Requires: ipywidgets-python3

%description python
python components for the ipywidgets package.


%package python3
Summary: python3 components for the ipywidgets package.
Group: Default
Requires: python3-core

%description python3
python3 components for the ipywidgets package.


%prep
%setup -q -n ipywidgets-7.1.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1518789589
python2 setup.py build -b py2
python3 setup.py build -b py3

%install
export SOURCE_DATE_EPOCH=1518789589
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
