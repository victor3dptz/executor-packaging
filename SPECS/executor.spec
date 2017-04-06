Summary:  The commercial version of Executor, a Macintosh environment for PCs
Name:  executor
Version: 1
Release:  1
License:  Commercial
Group: Applications/Emulators
Vendor: ARDI
Packager: Executor Packager
Requires: executor-aux >= 1

%description
Executor allows your Linux system to run many Macintosh applications.
Executor includes ARDI's reimplementation of a large percentage of the
core MacOS Classic routines.  This package contains the X version of
Executor for glibc based Linux distributions.  This package is only
available under license from ARDI and is not to be redistributed.

Documentation is available at http://www.ardi.com
%prep
%build

%install
mkdir -p %{buildroot}/usr/bin
mkdir -p %{buildroot}/opt/executor/bin
cp /opt/executor/bin/executor %{buildroot}/opt/executor/bin
cp /usr/bin/executor %{buildroot}/usr/bin
%files
/opt/executor/bin/executor
/usr/bin/executor
%post
/opt/executor/bin/executor
