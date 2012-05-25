Name:		virtio-win
Version:	0.1
Release:	22.1%{?dist}
Summary:	Windows guest drivers
Group:		FIXME
License:	Unknown
URL:		http://www.linux-kvm.org/page/WindowsGuestDrivers
Source0:	http://alt.fedoraproject.org/pub/alt/virtio-win/latest/images/bin/%{name}-0.1-22.iso
BuildRoot:	%(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
BuildRequires:	xorriso
BuildArch:	noarch

%description
Windows guest drivers

%prep
mkdir -p %{_builddir}/%{name}-%{version}
xorriso -osirrox on -indev %{SOURCE0} -extract / %{_builddir}/%{name}-%{version}

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/virtio-win/drivers/amd64
mkdir -p %{buildroot}/usr/share/virtio-win/drivers/i386
cp -r %{_builddir}/%{name}-%{version}/XP/amd64   %{buildroot}/usr/share/virtio-win/drivers/amd64/Win2003
cp -r %{_builddir}/%{name}-%{version}/Win7/amd64 %{buildroot}/usr/share/virtio-win/drivers/amd64/Win2008
cp -r %{_builddir}/%{name}-%{version}/Win7/amd64 %{buildroot}/usr/share/virtio-win/drivers/amd64/Win7
cp -r %{_builddir}/%{name}-%{version}/XP/amd64   %{buildroot}/usr/share/virtio-win/drivers/amd64/WinXP
cp -r %{_builddir}/%{name}-%{version}/XP/x86     %{buildroot}/usr/share/virtio-win/drivers/i386/Win2003
cp -r %{_builddir}/%{name}-%{version}/Win7/x86   %{buildroot}/usr/share/virtio-win/drivers/i386/Win2008
cp -r %{_builddir}/%{name}-%{version}/Win7/x86   %{buildroot}/usr/share/virtio-win/drivers/i386/Win7
cp -r %{_builddir}/%{name}-%{version}/XP/x86     %{buildroot}/usr/share/virtio-win/drivers/i386/WinXP

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc
/usr/share/virtio-win

%changelog
* Fri May 25 2012 Harvard University FAS Research Computing <rchelp@fas.harvard.edu> - 0.1-22.1
- Initial package
