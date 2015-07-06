%{!?_licensedir:%global license %%doc}
%global pypi_name automaton

Name:           python-%{pypi_name}
Version:        XXX
Release:        XXX
Summary:        Friendly state machines for python

License:        ASL 2.0
URL:            https://wiki.openstack.org/wiki/Oslo#automaton
Source0:        https://pypi.python.org/packages/source/a/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
 
BuildRequires:  python2-devel
BuildRequires:  python-pbr
BuildRequires:  python-sphinx
BuildRequires:  python-oslo-sphinx

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
%{python2_sitelib}/ 
%{python2_sitelib}/*.egg-info

%changelog
