Summary:	Document viewer
Name:		zathura
Version:	0.3.2
Release:	1
License:	BSD-like
Group:		Libraries
Source0:	https://pwmt.org/projects/zathura/download/%{name}-%{version}.tar.gz
# Source0-md5:	4ac91bfbb596decb43c7ef0dcbc3e361
BuildRequires:	check
BuildRequires:	girara3-devel
BuildRequires:	intltool
BuildRequires:	libmagic-devel
BuildRequires:	pkg-config
BuildRequires:	sqlite3-devel
BuildRequires:	zlib-devel
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
%{__sed} -i "s|^ZATHURA_GTK_VERSION.*|ZATHURA_GTK_VERSION ?= 3|" config.mk

%build
export CFLAGS="%{rpmcflags}"
export LDFLAGS="%{rpmldflags}"
%{__make} \
	QUIET=

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_libdir}/zathura

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT	\
	LIBDIR=%{_libdir}

# FIXME: wrong locale dir names
%{__mv} $RPM_BUILD_ROOT%{_localedir}/id{_ID,}
%{__mv} $RPM_BUILD_ROOT%{_localedir}/ta{_IN,}
%{__mv} $RPM_BUILD_ROOT%{_localedir}/uk{_UA,}
%{__mv} $RPM_BUILD_ROOT%{_localedir}/{no,nb}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT


%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS LICENSE README
%attr(755,root,root) %{_bindir}/zathura
%dir %{_libdir}/zathura
%{_datadir}/dbus-1/interfaces/org.pwmt.zathura.xml
%{_desktopdir}/zathura.desktop
%{_mandir}/man1/zathura.1*
%{_mandir}/man5/zathurarc.5*

%files devel
%defattr(644,root,root,755)
%{_includedir}/zathura
%{_pkgconfigdir}/zathura.pc

