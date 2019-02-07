Summary:  Old-school Macintosh Emulator
Name:  executor
Version: 2
Release:  1
License:  MIT
Group: Applications/Emulators
Packager: Victor3D <webmaster@victor3d.com.br>
Requires: nano qt5-qtbase boost
BuildRequires: git sed qt5-qtbase cmake>=3.10 SDL-devel boost-devel
URL:            http://wiki.victor3d.com.br
Source0:        https://github.com/victor3dptz/executor-packaging/raw/master/arch/executor.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root
BuildArch:     x86_64

%description
Executor allows your Linux system to run many Macintosh applications.
Executor includes ARDI's reimplementation of a large percentage of the
core MacOS Classic routines.

%prep
%setup -n %{name}
%build
git init
git remote add origin https://github.com/autc04/executor.git
git pull origin master
git submodule init
git submodule update
sed -i 's/SDL_keycode.h/SDL2\/SDL_keycode.h/g' src/config/front-ends/sdl2/keycode_map.h
sed -i 's/SDL.h/SDL2\/SDL.h/g' src/config/front-ends/sdl2/sdl2.cpp
sed -i 's/SDL.h/SDL2\/SDL.h/g' src/config/front-ends/sdl2/keycode_map.cpp
mkdir build
cd build
cmake ..
make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/bin
cp -vaR usr/ $RPM_BUILD_ROOT/usr/
install -pm 777 "build/executor" $RPM_BUILD_ROOT/usr/bin/

%files
%defattr(-,root,root,-)
/usr/*

%post

%clean
rm -rf $RPM_BUILD_ROOT

%changelog
* Thu Feb 07 2019 <webmaster@victor3d.com.br> - 2-1
- Executor 2000
