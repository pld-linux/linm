Summary:	LinM is a visual file manager
Summary(hu.UTF-8):	LinM egy vizuális fájlkezelő
Name:		linm
Version:	0.8.1
Release:	1
License:	GPL
Group:		Applications/Shells
Source0:	http://kldp.net/frs/download.php/4508/%{name}_%{version}-1.tar.gz
# Source0-md5:	10af8ec824b3e75d3602dad66d073655
URL:		http://kldp.net/projects/mls
# if you want to use samba
# BuildRequires:	samba-devel
BuildRequires:	ncurses-devel
BuildRequires:	openssl-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
LinM is a visaul file manager. It's a feature rich full-screen text
mode application that allows you to copy, move and delete files and
whole directory trees, search for files and run commands in the
subshell. LinM is best features are its ability to FTP, SFTP, view tar
and zip, alz files, and to poke into RPMs for specific files, and DEB
package.

%description -l hu.UTF-8
LinM egy vizuális fájlkezelő. Lehetőségek gazdag tárházát nyújtja ez a
teljes-képernyős, szöveges módú program, amellyel másolni, mozgatni és
törölni tudsz fájlokat és egész könyvtár-struktúrákat, kereshetsz
fájlokat és futtathatsz parancsokat egy alhéjban. LinM képes FTP-hez
és SFTP-hez csatlakozin, tar és zip fájlokba nézni, valamint RPM és
DEB csomagokba.

%prep
%setup -q


%build
%configure \
	--disable-static CPPFLAGS="-I/usr/include/ncursesw"
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_bindir}/*
%dir %{_sysconfdir}/linm
%{_desktopdir}/LinM.desktop
%{_pixmapsdir}/linm.xpm
%{_sysconfdir}/linm/*
%{_datadir}/locale/*
%{_libdir}/*
