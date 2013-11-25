Summary:	Document viewer
Name:		zathura
Version:	0.2.6
Release:	1
License:	BSD-like
Group:		Libraries
Source0:	https://pwmt.org/projects/zathura/download/%{name}-%{version}.tar.gz
# Source0-md5:	d155a66ec1862550dfde5a50e3dd6d01
BuildRequires:	check
BuildRequires:	girara-devel
BuildRequires:	intltool
BuildRequires:	pkg-config
BuildRequires:	sqlite3-devel
Requires:	zathura-plugin
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
zathura is a highly customizable and functional document viewer.
It provides a minimalistic and space saving interface as well as an
easy usage that mainly focuses on keyboard interaction.

# standalone
%package devel
Summary:	Development files for zathura
Group:		Development/Libraries

%description devel
This is the package containing the development files for zathura.

%prep
%setup -q

%{__sed} -i "s/^DFLAGS.*/DFLAGS =/" config.mk
%{__sed} -i "s|^PLUGINDIR.*|PLUGINDIR ?= %{_libdir}/zathura|" config.mk
%{__sed} -i "s|^ZATHURA_GTK_VERSION.*|ZATHURA_GTK_VERSION ?= 2|" config.mk

%build
export CFLAGS="%{rpmcflags}"
export LDFLAGS="%{rpmldflags}"
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_libdir}/zathura

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT	\
	LIBDIR=%{_libdir}

# FIXME: wrong locale dir names
mv $RPM_BUILD_ROOT%{_localedir}/id{_ID,}
mv $RPM_BUILD_ROOT%{_localedir}/ta{_IN,}
mv $RPM_BUILD_ROOT%{_localedir}/uk{_UA,}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT


%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS LICENSE README
%attr(755,root,root) %{_bindir}/zathura
%dir %{_libdir}/zathura
%{_desktopdir}/zathura.desktop
%{_mandir}/man1/zathura.1*
%{_mandir}/man5/zathurarc.5*

%files devel
%defattr(644,root,root,755)
%{_includedir}/zathura
%{_pkgconfigdir}/zathura.pc

