Summary:	Fonts to replace commonly used Microsoft Windows Fonts
Summary(pl.UTF-8):	Fonty zastępujące popularne fonty z Microsoft Windows
Name:		fonts-TTF-RedHat-liberation
Version:	2.00.0
Release:	2
Epoch:		1
License:	OFL
Group:		Fonts
Source0:	https://fedorahosted.org/releases/l/i/liberation-fonts/liberation-fonts-%{version}.tar.gz
# Source0-md5:	5b5055ed755025891f908b7726fea482
Source1:	generate.pe
Source2:	59-liberation-mono.conf
Source3:	59-liberation-sans.conf
Source4:	59-liberation-serif.conf
URL:		https://fedorahosted.org/liberation-fonts/
BuildRequires:	fontforge >= 20090923
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
%setup -q -n liberation-fonts-%{version}
install -m755 %{SOURCE1} .

%build
rm -f *.ttf
./generate.pe src/*.sfd

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_ttffontsdir}
install -d $RPM_BUILD_ROOT%{_sysconfdir}/fonts/conf.avail
install -d $RPM_BUILD_ROOT%{_sysconfdir}/fonts/conf.d

mv LiberationMono.ttf LiberationMono-Regular.ttf
mv LiberationSerif.ttf LiberationSerif-Regular.ttf
mv LiberationSans.ttf LiberationSans-Regular.ttf

cp -a *.ttf $RPM_BUILD_ROOT%{_ttffontsdir}

install %{SOURCE2} $RPM_BUILD_ROOT%{_sysconfdir}/fonts/conf.avail/59-liberation-mono.conf
install %{SOURCE3} $RPM_BUILD_ROOT%{_sysconfdir}/fonts/conf.avail/59-liberation-sans.conf
install %{SOURCE4} $RPM_BUILD_ROOT%{_sysconfdir}/fonts/conf.avail/59-liberation-serif.conf

ln -s ../conf.avail/59-liberation-mono.conf $RPM_BUILD_ROOT%{_sysconfdir}/fonts/conf.d
ln -s ../conf.avail/59-liberation-sans.conf $RPM_BUILD_ROOT%{_sysconfdir}/fonts/conf.d
ln -s ../conf.avail/59-liberation-serif.conf $RPM_BUILD_ROOT%{_sysconfdir}/fonts/conf.d

%clean
rm -rf $RPM_BUILD_ROOT

%post
fontpostinst TTF

%postun
fontpostinst TTF

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README TODO
%{_ttffontsdir}/LiberationMono*.ttf
%{_ttffontsdir}/LiberationSans*.ttf
%{_ttffontsdir}/LiberationSerif*.ttf
%{_sysconfdir}/fonts/conf.avail/59-liberation-*.conf
%{_sysconfdir}/fonts/conf.d/59-liberation-*.conf
