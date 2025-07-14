%define shortname MurrinaBlue
Summary:	A simple blue theme
Name:		gtk2-theme-%{shortname}
Version:	1.0
Release:	2
License:	GPL
Group:		Themes/GTK+
Source0:	http://www.cimitan.com/murrine/files/%{shortname}.tar.bz2
# Source0-md5:	c42534308c8d45a3c953571ea94f50ac
Patch0:		gtk2-theme-MurrinaBlue-hilight.patch
URL:		http://www.cimitan.com/murrine/
Requires:	gtk2-theme-engine-murrine >= 0.90.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A simple blue theme

%prep
%setup -q -n %{shortname}
%patch -P0 -p1

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_datadir}/themes/%{shortname}
cp -R gtk* $RPM_BUILD_ROOT%{_datadir}/themes/%{shortname}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_datadir}/themes/%{shortname}
