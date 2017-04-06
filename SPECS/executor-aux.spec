Summary:  Auxiliary files for Executor, a Macintosh environment for PCs
Name:  executor-aux
Version: 1
Release:  1
License:  Commercial
Group: Applications/Emulators
Vendor: ARDI
Packager: Executor Packager <questions@ardi.com>

%description
Executor allows your Linux system to run many Macintosh applications.
Executor includes ARDI's reimplementation of a large percentage of the
core MacOS Classic routines.  This package contains the auxiliary
files that Executor needs.

%prep
%build
%install

cp -r /root/rpmbuild/aux/etc %{buildroot}/etc
cp -r /root/rpmbuild/aux/home %{buildroot}/home
cp -r /root/rpmbuild/aux/opt %{buildroot}/opt
cp -r /root/rpmbuild/aux/usr %{buildroot}/usr
cp -r /root/rpmbuild/aux/var %{buildroot}/var

%post

# the following chmods are necessary because the permissions get messed up
# when we convert our .rpm to a .deb using alien

pushd /var/opt/executor > /dev/null
chmod -R go+w share/conf share/home/*"System Folder"
chmod go-w share/home/"System Folder"/*{Browser,Printer}
chmod go+w directory_map* printdef.ini share/home/*ware share/home share/home/Shareware/*Tex-Edit share/home/Shareware/Tex-Edit/*"Tex-Edit Prefs" share/home/Shareware/"speedometer3.23 Folder"
popd > /dev/null

%preun

if [ -e /etc/opt/executor/.xp ]; then
  mv /etc/opt/executor/.xp /etc/.temporary_deleteme_xp
fi
%postun
if [ -e /etc/.temporary_deleteme_xp ]; then
  if [ ! -e /etc/opt ]; then
    mkdir /etc/opt
  fi
  if [ ! -e /etc/opt/executor ]; then
    mkdir /etc/opt/executor
  fi
  mv /etc/.temporary_deleteme_xp /etc/opt/executor/.xp
fi

%files

%doc /opt/executor/man
%doc /usr/man/man1/executor.1.gz
%doc /usr/man/man5/ecf.5.gz
%doc /usr/man/man5/printers.ini.5.gz
%doc /usr/man/man5/hfv.5.gz
%doc /usr/man/man5/AppleDouble.5.gz
%doc /usr/man/man5/directory_map.5.gz
%doc /usr/man/man7/ExecutorVolume.7.gz


/opt/executor
/var/opt/executor
/etc/opt/executor
/home/executor
/usr/doc/executor
/usr/share/applications
