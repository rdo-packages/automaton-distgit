%{!?_licensedir:%global license %%doc}
%global pypi_name automaton

%{!?upstream_version: %global upstream_version %{version}%{?milestone}}

Name:           python-%{pypi_name}
Version:        1.2.0
Release:        1%{?dist}
Summary:        Friendly state machines for python

License:        ASL 2.0
URL:            https://wiki.openstack.org/wiki/Oslo#automaton
Source0:        https://pypi.python.org/packages/source/a/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
 
BuildRequires:  python2-devel
BuildRequires:  python-pbr
BuildRequires:  python-sphinx
BuildRequires:  python-oslo-sphinx

Requires: python-pbr >= 0.11
Requires: python-six >= 1.9.0
Requires: python-debtcollector >= 0.3.0
Requires: python-prettytable

%description
Friendly state machines for python.

%prep
%setup -q -n %{pypi_name}-%{upstream_version}

%build
%{__python2} setup.py build

# generate html docs 
sphinx-build doc/source html
# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}

%install
%{__python2} setup.py install --skip-build --root %{buildroot}

%files
%doc html README.rst
%license LICENSE
%{python2_sitelib}/%{pypi_name}
%{python2_sitelib}/*.egg-info

%changelog
* Wed Mar 23 2016 Haikel Guemar <hguemar@fedoraproject.org> 1.2.0-
- Update to 1.2.0

