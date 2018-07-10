#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : ipywidgets
Version  : 7.2.1
Release  : 28
URL      : https://pypi.python.org/packages/18/8c/d19f7bef501c2cc217f52f7656eb98e04f236b1511192657de74a8abf6c1/ipywidgets-7.2.1.tar.gz
Source0  : https://pypi.python.org/packages/18/8c/d19f7bef501c2cc217f52f7656eb98e04f236b1511192657de74a8abf6c1/ipywidgets-7.2.1.tar.gz
Summary  : IPython HTML widgets for Jupyter
Group    : Development/Tools
License  : BSD-3-Clause-Clear
Requires: ipywidgets-python3
Requires: ipywidgets-license
Requires: ipywidgets-python
Requires: Sphinx
Requires: ipykernel
Requires: ipywidgets
Requires: jupyter_client
Requires: nbsphinx
Requires: sphinx_rtd_theme
BuildRequires : pbr
BuildRequires : pip
BuildRequires : python3-dev
BuildRequires : setuptools

%description
# ipywidgets: Interactive HTML Widgets
[![Version](https://img.shields.io/pypi/v/ipywidgets.svg)](https://pypi.python.org/pypi/ipywidgets)
[![Build Status](https://travis-ci.org/jupyter-widgets/ipywidgets.svg?branch=master)](https://travis-ci.org/jupyter-widgets/ipywidgets)
[![Documentation Status](http://readthedocs.org/projects/ipywidgets/badge/?version=latest)](https://ipywidgets.readthedocs.io/en/latest/?badge=latest)
[![Join the chat at https://gitter.im/ipython/ipywidgets](https://badges.gitter.im/Join%20Chat.svg)](https://gitter.im/jupyter-widgets/Lobby)

%package license
Summary: license components for the ipywidgets package.
Group: Default

%description license
license components for the ipywidgets package.


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
%setup -q -n ipywidgets-7.2.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1530396604
python3 setup.py build -b py3

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/doc/ipywidgets
cp COPYING.md %{buildroot}/usr/share/doc/ipywidgets/COPYING.md
python3 -tt setup.py build -b py3 install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(-,root,root,-)
/usr/share/doc/ipywidgets/COPYING.md

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
