# executor-packaging
Modified spec-files to properly build rpm and deb packages of Executor emulator

Tested on CentOS 6.8 32bit

Use SPECS/executor.spec to build executor.rpm (contains binary)

Use SPECS/executor-aux.spec to build executor-aux.rpm (auxiliary files for the Executor *in aux directory*)

To build executor binary, visit https://github.com/ctm/executor

Check paths! 

To build deb, use alien on Deb-based distribution.

There are pre-built packages for CentOS 6.8 (32 bit) and Debian 8 Jessie (32 bit) in the "ready" directory.
Deb also has been tested on Linux Mint 18.1 (64 bit)

Arch Linux and Manjaro users use PKGBUILD