Summary:	Fonts to replace commonly used Microsoft Windows Fonts
Summary(pl.UTF-8):	Fonty zastępujące popularne fonty z Microsoft Windows
Name:		fonts-TTF-RedHat-liberation
Version:	1.05
# https://bugzilla.redhat.com/show_bug.cgi?id=508899
Release:	0.1
Epoch:		1
License:	GPL v2 + exceptions
Group:		Fonts
Source0:	http://github.com/downloads/kaio/liberation-fonts/liberation-fonts-ttf-%{version}.zip
# Source0-md5:	a3237526c7cf0c9a16c0582c5293b38b
Source1:	%{name}.fontconfig
URL:		https://fedorahosted.org/liberation-fonts/
BuildRequires:	unzip
Requires(post,postun):	fontpostinst
Requires:	%{_fontsdir}/TTF
Obsoletes:	liberation-fonts-ttf
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
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_ttffontsdir}
install -d $RPM_BUILD_ROOT%{_sysconfdir}/fonts/conf.avail
install -d $RPM_BUILD_ROOT%{_sysconfdir}/fonts/conf.d

cp -a *.ttf $RPM_BUILD_ROOT%{_ttffontsdir}
install %{SOURCE1} $RPM_BUILD_ROOT%{_sysconfdir}/fonts/conf.avail/60-liberation.conf
ln -s ../conf.avail/60-liberation.conf $RPM_BUILD_ROOT%{_sysconfdir}/fonts/conf.d

%clean
rm -rf $RPM_BUILD_ROOT

%post
fontpostinst TTF

%postun
fontpostinst TTF

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog License.txt README
%{_ttffontsdir}/LiberationMono-*.ttf
%{_ttffontsdir}/LiberationSans-*.ttf
%{_ttffontsdir}/LiberationSerif-*.ttf
%{_sysconfdir}/fonts/conf.avail/60-liberation.conf
%{_sysconfdir}/fonts/conf.d/60-liberation.conf
