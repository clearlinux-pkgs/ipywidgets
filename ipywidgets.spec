#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : ipywidgets
Version  : 7.4.2
Release  : 35
URL      : https://files.pythonhosted.org/packages/88/8d/c5d3ac1bdcd74c7327c733c9d02354ff12d7d72744f262ed1e26560962b2/ipywidgets-7.4.2.tar.gz
Source0  : https://files.pythonhosted.org/packages/88/8d/c5d3ac1bdcd74c7327c733c9d02354ff12d7d72744f262ed1e26560962b2/ipywidgets-7.4.2.tar.gz
Summary  : IPython HTML widgets for Jupyter
Group    : Development/Tools
License  : BSD-3-Clause
Requires: ipywidgets-python3
Requires: ipywidgets-license
Requires: ipywidgets-python
Requires: Sphinx
Requires: ipykernel
Requires: ipywidgets
Requires: jupyter_client
Requires: nbsphinx
Requires: recommonmark
Requires: sphinx_rtd_theme
BuildRequires : buildreq-distutils3

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
%setup -q -n ipywidgets-7.4.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1536974474
python3 setup.py build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/doc/ipywidgets
cp LICENSE %{buildroot}/usr/share/doc/ipywidgets/LICENSE
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(-,root,root,-)
/usr/share/doc/ipywidgets/LICENSE

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
