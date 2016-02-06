%if 0%{?fedora}
%global with_python3 1
%endif

%global pypi_name automaton

Name:           python-%{pypi_name}
Version:        1.1.0
Release:        3%{?dist}
Summary:        Friendly state machines for python

License:        ASL 2.0
URL:            https://wiki.openstack.org/wiki/Oslo#automaton
Source0:        https://pypi.python.org/packages/source/a/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
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
BuildRequires:  python-setuptools

#Required for tests
BuildRequires:  python-debtcollector
BuildRequires:  python-hacking
BuildRequires:  python-coverage
BuildRequires:  python-subunit
BuildRequires:  python-oslotest
BuildRequires:  python-prettytable
BuildRequires:  python-testrepository
BuildRequires:  python-testscenarios
BuildRequires:  python-testtools

Requires: python-pbr >= 1.6
Requires: python-six >= 1.9.0
Requires: python-debtcollector >= 0.3.0
Requires: python-prettytable

%description -n python2-%{pypi_name}
Friendly state machines for python.

%package -n python-%{pypi_name}-doc
Summary:        Friendly state machines for python - documentation

%description -n python-%{pypi_name}-doc
Friendly state machines for python (documentation)

%if 0%{?with_python3}
%package -n python3-%{pypi_name}
Summary:        Friendly state machines for python
%{?python_provide:%python_provide python3-%{pypi_name}}

BuildRequires:  python3-devel
BuildRequires:  python3-pbr
BuildRequires:  python3-sphinx
BuildRequires:  python3-oslo-sphinx
BuildRequires:  python3-setuptools

#Required for tests
BuildRequires:  python3-debtcollector
BuildRequires:  python3-hacking
BuildRequires:  python3-coverage
BuildRequires:  python3-subunit
BuildRequires:  python3-oslotest
BuildRequires:  python3-prettytable
BuildRequires:  python3-testrepository
BuildRequires:  python3-testscenarios
BuildRequires:  python3-testtools

Requires: python3-pbr >= 1.6
Requires: python3-six >= 1.9.0
Requires: python3-debtcollector >= 0.3.0
Requires: python3-prettytable

%description -n python3-%{pypi_name}
Friendly state machines for python.
%endif

%prep
%setup -q -n %{pypi_name}-%{version}

%build
%{py_build}

%if 0%{?with_python3}
%{py3_build}
%endif

%install
%{py2_install}

# generate html docs 
sphinx-build doc/source html
# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}

%if 0%{?with_python3}
%{py3_install}
%endif


%check
%{__python2} setup.py test

%if 0%{?with_python3}
rm -rf .testrepository
%{__python3} setup.py test
%endif

%files -n python2-%{pypi_name}
%doc README.rst
%license LICENSE
%{python2_sitelib}/%{pypi_name}
%{python2_sitelib}/*.egg-info

%files -n python-%{pypi_name}-doc
%doc html
%license LICENSE

%if 0%{?with_python3}
%files -n python3-%{pypi_name}
%doc html README.rst
%license LICENSE
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/*.egg-info

%endif

%changelog
* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-3
- Test

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Dec 22 2015 jpena <jpena@redhat.com> - 1.1.0-1
- Updated to upstream release 1.1.0

* Tue Nov 24 2015 jpena <jpena@redhat.com> - 1.0.0-1
- Updated to upstream release 1.0.0

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.0-2
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Fri Sep 18 2015 jpena <jpena@redhat.com> - 0.7.0-1
- Initial package.
