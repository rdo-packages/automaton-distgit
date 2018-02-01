%{!?upstream_version: %global upstream_version %{version}%{?milestone}}
%global pypi_name automaton
 
%if 0%{?fedora}
%global with_python3 1
%endif

Name:           python-%{pypi_name}
Version:        XXX
Release:        XXX
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
BuildRequires:  python2-pbr
BuildRequires:  git
BuildRequires:  graphviz
BuildRequires:  python2-sphinx
BuildRequires:  python2-openstackdocstheme
BuildRequires:  python2-oslo-sphinx
BuildRequires:  python2-prettytable

Requires: python2-pbr >= 2.0.0
Requires: python2-six >= 1.10.0
Requires: python2-prettytable

%description -n python2-%{pypi_name}
Friendly state machines for python.

%if 0%{?with_python3}
%package -n python3-%{pypi_name}
Summary:        Friendly state machines for python
%{?python_provide:%python_provide python3-%{pypi_name}}
BuildRequires:  python3-devel
BuildRequires:  python3-pbr

Requires: python3-pbr >= 2.0.0
Requires: python3-six >= 1.10.0
Requires: python3-prettytable

%description -n python3-%{pypi_name}
Friendly state machines for python.
%endif

%package -n python-%{pypi_name}-doc
Summary:        Friendly state machines for python - documentation

%description -n python-%{pypi_name}-doc
Friendly state machines for python (documentation)

%prep
%autosetup -n %{pypi_name}-%{upstream_version} -S git

%build
%if 0%{?with_python3}
%py3_build
%endif
%py2_build

# generate html docs 
%{__python2} setup.py build_sphinx -b html
# remove the sphinx-build leftovers
rm -rf doc/build/html/.{doctrees,buildinfo}

%install
%if 0%{?with_python3}
%py3_install
%endif
%py2_install

%files -n python2-%{pypi_name}
%doc README.rst
%license LICENSE
%{python2_sitelib}/%{pypi_name}
%{python2_sitelib}/*.egg-info

%if 0%{?with_python3}
%files -n python3-%{pypi_name}
%doc README.rst
%license LICENSE
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/*.egg-info
%endif

%files -n python-%{pypi_name}-doc
%doc doc/build/html
%license LICENSE

%changelog
