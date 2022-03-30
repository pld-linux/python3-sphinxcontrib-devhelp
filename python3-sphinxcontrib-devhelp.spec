#
# Conditional build:
%bcond_with	tests	# unit tests (failing?)

Summary:	Sphinx extension which outputs Devhelp documents
Summary(pl.UTF-8):	Rozszerzenie Sphinksa zapisujące dokumenty Devhelpa
Name:		python3-sphinxcontrib-devhelp
Version:	1.0.2
Release:	5
License:	BSD
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/sphinxcontrib-devhelp/
Source0:	https://files.pythonhosted.org/packages/source/s/sphinxcontrib-devhelp/sphinxcontrib-devhelp-%{version}.tar.gz
# Source0-md5:	94069c5cdb5079c445f5477fa6107016
URL:		https://pypi.org/project/sphinxcontrib-devhelp/
BuildRequires:	python3-modules >= 1:3.5
BuildRequires:	python3-setuptools
%if %{with tests}
BuildRequires:	python3-Sphinx
BuildRequires:	python3-pytest
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
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
%setup -q -n sphinxcontrib-devhelp-%{version}

%build
%py3_build

%if %{with tests}
PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 \
%{__python3} -m pytest tests
%endif

%install
rm -rf $RPM_BUILD_ROOT

%py3_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES LICENSE README.rst
%{py3_sitescriptdir}/sphinxcontrib/devhelp
%{py3_sitescriptdir}/sphinxcontrib_devhelp-%{version}-py*.egg-info
%{py3_sitescriptdir}/sphinxcontrib_devhelp-%{version}-py*-nspkg.pth
