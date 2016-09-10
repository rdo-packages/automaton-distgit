%{!?upstream_version: %global upstream_version %{version}%{?milestone}}
%global pypi_name automaton

%if 0%{?fedora}
%global with_python3 1
%endif

Name:           python-%{pypi_name}
Version:        1.4.0
Release:        2%{?dist}
Summary:        Friendly state machines for python

License:        ASL 2.0
URL:            https://wiki.openstack.org/wiki/Oslo#automaton
Source0:        https://pypi.io/packages/source/a/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

%description
Friendly state machines for python.

%package -n python2-%{pypi_name}
Summary:        Friendly state machines for python
%{?python_provide:%python_provide python2-%{pypi_name}}
BuildRequires:  python2-devel
BuildRequires:  python-pbr
BuildRequires:  python-sphinx
BuildRequires:  python-oslo-sphinx

Requires: python-pbr >= 1.6
Requires: python-six >= 1.9.0
Requires: python-debtcollector >= 1.2.0
Requires: python-prettytable

%description -n python2-%{pypi_name}
Friendly state machines for python.

%if 0%{?with_python3}
%package -n python3-%{pypi_name}
Summary:        Friendly state machines for python
%{?python_provide:%python_provide python3-%{pypi_name}}
BuildRequires:  python3-devel
BuildRequires:  python3-pbr
BuildRequires:  python3-sphinx
BuildRequires:  python3-oslo-sphinx

Requires: python3-pbr >= 1.6
Requires: python3-six >= 1.9.0
Requires: python3-debtcollector >= 1.2.0
Requires: python3-prettytable

%description -n python3-%{pypi_name}
Friendly state machines for python.
%endif

%package -n python-%{pypi_name}-doc
Summary:        Friendly state machines for python - documentation

%description -n python-%{pypi_name}-doc
Friendly state machines for python (documentation)

%prep
%setup -q -n %{pypi_name}-%{upstream_version}

%build
%if 0%{?with_python3}
%py3_build
%endif
%py2_build

# generate html docs 
sphinx-build doc/source html
# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}

%install
%if 0%{?with_python3}
%py3_install
%endif
%py2_install

%files -n python2-%{pypi_name}
%doc html README.rst
%license LICENSE
%{python2_sitelib}/%{pypi_name}
%{python2_sitelib}/*.egg-info

%if 0%{?with_python3}
%files -n python3-%{pypi_name}
%doc html README.rst
%license LICENSE
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/*.egg-info
%endif

%files -n python-%{pypi_name}-doc
%doc html
%license LICENSE

%changelog
* Sat Sep 10 2016 Haïkel Guémar <hguemar@fedoraproject.org> - 1.4.0-2
- Add doc subpackage

* Fri Sep 09 2016 Haikel Guemar <hguemar@fedoraproject.org> 1.4.0-1
- Update to 1.4.0

