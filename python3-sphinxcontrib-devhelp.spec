#
# Conditional build:
%bcond_with	tests	# unit tests (failing?)

Summary:	Sphinx extension which outputs Devhelp documents
Summary(pl.UTF-8):	Rozszerzenie Sphinksa zapisujące dokumenty Devhelpa
Name:		python3-sphinxcontrib-devhelp
Version:	2.0.0
Release:	3
License:	BSD
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/sphinxcontrib-devhelp/
Source0:	https://pypi.debian.net/sphinxcontrib-devhelp/sphinxcontrib_devhelp-%{version}.tar.gz
# Source0-md5:	79ef5937b8397f724f4fb065073cd24c
URL:		https://pypi.org/project/sphinxcontrib-devhelp/
BuildRequires:	python3-modules >= 1:3.5
BuildRequires:	python3-build
BuildRequires:	python3-installer
%if %{with tests}
BuildRequires:	python3-Sphinx
BuildRequires:	python3-pytest
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 2.044
Requires:	python3-modules >= 1:3.5
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
sphinxcontrib-devhelp is a sphinx extension which outputs
Devhelp documents.

%description -l pl.UTF-8
sphinxcontrib-devhelp to rozszerzenie Sphinksa, zapisujące
dokumenty Devhelpa.

%prep
%setup -q -n sphinxcontrib_devhelp-%{version}

%build
%py3_build_pyproject

%if %{with tests}
PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 \
%{__python3} -m pytest tests
%endif

%install
rm -rf $RPM_BUILD_ROOT

%py3_install_pyproject

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES.rst LICENCE.rst README.rst
%{py3_sitescriptdir}/sphinxcontrib/devhelp
%{py3_sitescriptdir}/sphinxcontrib_devhelp-%{version}.dist-info
