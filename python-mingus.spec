%define 	module	mingus
Summary:	Python package for making and investigating music
Name:		python-%{module}
Version:	0.4.2.3
Release:	0.1
License:	GPLv3
Group:		Development/Languages/Python
Source0:	http://mingus.googlecode.com/files/%{module}-%{version}.tar.gz
# Source0-md5:	
URL:		http://code.google.com/p/mingus/
BuildRequires:	python-devel
BuildRequires:	rpm-pythonprov
# if py_postclean is used
BuildRequires:	rpmbuild(macros) >= 1.219
Requires:	python-modules
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
mingus is a package for Python used by programmers, musicians, composers and
researchers to make and investigate music. At the core of mingus is music
theory, which includes topics like intervals, chords, scales and progressions.
These components are rigurously tested and can be used to generate and
recognize musical elements using convenient shorthand where possible (for
example some acceptable chords are: "CM7", "Am6", "Ab7", "G7").


%prep
%setup -q -n %{module}-%{version}

%build
export CFLAGS="%{rpmcflags}"
%{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}

%{__python} setup.py install \
	--optimize=2 \
	--root=$RPM_BUILD_ROOT

%py_ocomp $RPM_BUILD_ROOT%{py_sitescriptdir}
%py_comp $RPM_BUILD_ROOT%{py_sitescriptdir}
%py_postclean

mv $RPM_BUILD_ROOT%{_prefix}/mingus_examples $RPM_BUILD_ROOT%{_examplesdir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS CHANGELOG README THANKS
%{py_sitescriptdir}/mingus
%if "%{py_ver}" > "2.4"
%{py_sitescriptdir}/*.egg-info
%endif
%{_examplesdir}/*
