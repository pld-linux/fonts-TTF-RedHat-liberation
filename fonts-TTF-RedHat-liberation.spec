Summary:	Fonts to replace commonly used Microsoft Windows Fonts
Summary(pl.UTF-8):	Fonty zastępujące popularne fonty z Microsoft Windows
Name:		fonts-TTF-RedHat-liberation
Version:	2.00.1
Release:	5
Epoch:		1
License:	OFL
Group:		Fonts
Source0:	https://fedorahosted.org/releases/l/i/liberation-fonts/liberation-fonts-%{version}.tar.gz
# Source0-md5:	a0dfdcffcd0398afe5f57269198846e9
Source1:	30-0-liberation-mono.conf
Source2:	30-0-liberation-sans.conf
Source3:	30-0-liberation-serif.conf
URL:		https://fedorahosted.org/liberation-fonts/
BuildRequires:	fontforge >= 20090923
BuildRequires:	fonttools
Suggests:	fontpostinst
Obsoletes:	liberation-fonts-ttf
Conflicts:	fontconfig < 1:2.10.1
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_ttffontsdir	%{_fontsdir}/TTF

%description
The Liberation Fonts are intended to be replacements for the three
most commonly used fonts on Microsoft systems.

There are three sets: Sans (a substitute for Arial, Albany, Helvetica,
Nimbus Sans L, and Bitstream Vera Sans), Serif (a substitute for Times
New Roman, Thorndale, Nimbus Roman, and Bitstream Vera Serif) and Mono
(a substitute for Courier New, Cumberland, Courier, Nimbus Mono L, and
Bitstream Vera Sans Mono).

%description -l pl.UTF-8
Fonty Liberation mają być zamiennikami trzech najczęściej używanych
fontów z systemów Microsoftu.

Pakiet zawiera trzy zestawy: Sans (zamiennik dla Arial, Albany,
Helvetica, Nimbus Sans L i Bitstream Vera Sans), Serif (zamiennik dla
Times New Roman, Thorndale, Nimbus Roman i Bitstream Vera Serif) i
Mono (zamiennik dla Courier New, Cumberland, Courier, Nimbus Mono L i
Bitstream Vera Sans Mono).

%prep
%setup -q -n liberation-fonts-%{version}

%build
%{__make}
mv liberation-fonts-ttf-%{version}/* .

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_ttffontsdir},%{_sysconfdir}/fonts/conf.d,%{_datadir}/fontconfig/conf.avail}

cp -p *.ttf $RPM_BUILD_ROOT%{_ttffontsdir}

cp -p %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/fontconfig/conf.avail/30-0-liberation-mono.conf
cp -p %{SOURCE2} $RPM_BUILD_ROOT%{_datadir}/fontconfig/conf.avail/30-0-liberation-sans.conf
cp -p %{SOURCE3} $RPM_BUILD_ROOT%{_datadir}/fontconfig/conf.avail/30-0-liberation-serif.conf

ln -s %{_datadir}/fontconfig/conf.avail/30-0-liberation-mono.conf $RPM_BUILD_ROOT%{_sysconfdir}/fonts/conf.d
ln -s %{_datadir}/fontconfig/conf.avail/30-0-liberation-sans.conf $RPM_BUILD_ROOT%{_sysconfdir}/fonts/conf.d
ln -s %{_datadir}/fontconfig/conf.avail/30-0-liberation-serif.conf $RPM_BUILD_ROOT%{_sysconfdir}/fonts/conf.d

%clean
rm -rf $RPM_BUILD_ROOT

%triggerin -- fontpostinst
if [ "$1" = "1" ] && [ "$2" = "1" ]; then
	fontpostinst TTF
fi

%triggerun -- fontpostinst
if [ "$1" = "0" ] || [ "$2" = "0" ]; then
	fontpostinst TTF
fi

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README TODO
%{_ttffontsdir}/LiberationMono*.ttf
%{_ttffontsdir}/LiberationSans*.ttf
%{_ttffontsdir}/LiberationSerif*.ttf
%{_datadir}/fontconfig/conf.avail/30-0-liberation-*.conf
%{_sysconfdir}/fonts/conf.d/30-0-liberation-*.conf
