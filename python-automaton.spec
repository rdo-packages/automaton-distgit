# Macros for py2/py3 compatibility
%if 0%{?fedora} || 0%{?rhel} > 7
%global pyver %{python3_pkgversion}
%else
%global pyver 2
%endif
%global pyver_bin python%{pyver}
%global pyver_sitelib %python%{pyver}_sitelib
%global pyver_install %py%{pyver}_install
%global pyver_build %py%{pyver}_build
# End of macros for py2/py3 compatibility
%{!?upstream_version: %global upstream_version %{version}%{?milestone}}
%global pypi_name automaton

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

%package -n python%{pyver}-%{pypi_name}
Summary:        Friendly state machines for python
%{?python_provide:%python_provide python%{pyver}-%{pypi_name}}
BuildRequires:  python%{pyver}-devel
BuildRequires:  python%{pyver}-pbr
BuildRequires:  git
BuildRequires:  graphviz
BuildRequires:  python%{pyver}-sphinx
BuildRequires:  python%{pyver}-openstackdocstheme
BuildRequires:  python%{pyver}-prettytable

Requires: python%{pyver}-pbr >= 2.0.0
Requires: python%{pyver}-six >= 1.10.0
Requires: python%{pyver}-prettytable

%description -n python%{pyver}-%{pypi_name}
Friendly state machines for python.

%package -n python-%{pypi_name}-doc
Summary:        Friendly state machines for python - documentation

%description -n python-%{pypi_name}-doc
Friendly state machines for python (documentation)

%prep
%autosetup -n %{pypi_name}-%{upstream_version} -S git

%build
%{pyver_build}

# generate html docs 
%{pyver_bin} setup.py build_sphinx -b html
# remove the sphinx-build-%{pyver} leftovers
rm -rf doc/build/html/.{doctrees,buildinfo}

%install
%{pyver_install}

%files -n python%{pyver}-%{pypi_name}
%doc README.rst
%license LICENSE
%{pyver_sitelib}/%{pypi_name}
%{pyver_sitelib}/*.egg-info

%files -n python-%{pypi_name}-doc
%doc doc/build/html
%license LICENSE

%changelog
