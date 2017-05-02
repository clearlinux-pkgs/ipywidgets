#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : ipywidgets
Version  : 6.0.0
Release  : 3
URL      : https://pypi.python.org/packages/99/26/daf5c44c8b2a4cbe80b4cafced8cc2c3c2a4b8f035e4ef53b037f47e8897/ipywidgets-6.0.0.tar.gz
Source0  : https://pypi.python.org/packages/99/26/daf5c44c8b2a4cbe80b4cafced8cc2c3c2a4b8f035e4ef53b037f47e8897/ipywidgets-6.0.0.tar.gz
Summary  : IPython HTML widgets for Jupyter
Group    : Development/Tools
License  : BSD-3-Clause-Clear
Requires: ipywidgets-python
Requires: Sphinx
Requires: ipykernel
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
[![Build Status](https://travis-ci.org/ipython/ipywidgets.svg?branch=master)](https://travis-ci.org/ipython/ipywidgets)
[![Documentation Status](http://readthedocs.org/projects/ipywidgets/badge/?version=latest)](https://ipywidgets.readthedocs.io/en/latest/?badge=latest)
[![Join the chat at https://gitter.im/ipython/ipywidgets](https://badges.gitter.im/Join%20Chat.svg)](https://gitter.im/ipython/ipywidgets?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)

%package python
Summary: python components for the ipywidgets package.
Group: Default

%description python
python components for the ipywidgets package.


%prep
%setup -q -n ipywidgets-6.0.0

%build
export LANG=C
export SOURCE_DATE_EPOCH=1490541712
python2 setup.py build -b py2
python3 setup.py build -b py3

%install
export SOURCE_DATE_EPOCH=1490541712
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot} --force
python3 -tt setup.py build -b py3 install --root=%{buildroot} --force
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)
/usr/lib/python2*/*
/usr/lib/python3*/*
