%define		_name	liberation-fonts
Summary:	Fonts to replace commonly used Microsoft Windows Fonts
Name:		fonts-TTF-RedHat-liberation
Version:	0.1
Release:	1
License:	GPL v2 + exceptions
Group:		Fonts
Source0:	%{_name}-%{version}.tar.gz
# Source0-md5:	a874631c4641e8496cd9be5c7da74b48
URL:		https://www.redhat.com/promo/fonts/
Requires(post,postun):	fontpostinst
Requires:	%{_fontsdir}/TTF
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_ttffontsdir	%{_fontsdir}/TTF

%description
The Liberation Fonts are intended to be replacements for the three
most commonly used fonts on Microsoft systems: Times New Roman,
Arial, and Courier New.

%prep
%setup -c -n %{_name}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_ttffontsdir}

install *.ttf $RPM_BUILD_ROOT%{_ttffontsdir}

%clean
rm -rf $RPM_BUILD_ROOT

%post
fontpostinst TTF

%postun
fontpostinst TTF

%files
%defattr(644,root,root,755)
%{_ttffontsdir}/*
