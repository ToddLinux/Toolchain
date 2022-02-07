# Todd Linux Toolchain
## Solution architecure
The toolchain required to build ToddLinux ISO and ToddLinux operating system should be hosted separetely. In order to speed up build process the toolchain should be easily accessible, prefferably in a form of an archive hosted by ToddLinux developers.

### Toolchain components
No package management should be performed at toolchain level. \
The single archive should contain:
- [GNU C compiler](https://gcc.gnu.org/)
- [GNU C library](https://www.gnu.org/software/libc/)
- [GNU coreutils](https://www.gnu.org/software/coreutils/)
- [GNU binutils](https://www.gnu.org/software/binutils/)
- [GNU M4](https://www.gnu.org/software/m4/)
- [GNU ncurses](https://www.gnu.org/software/ncurses/)
- [GNU diffutils](https://www.gnu.org/software/diffutils/)
- [GNU findutils](https://www.gnu.org/software/findutils/)
- [GNU gawk](https://www.gnu.org/software/gawk/)
- [GNU grep](https://www.gnu.org/software/grep/)
- [GNU make](https://www.gnu.org/software/make/)
- [GNU patch](https://www.gnu.org/software/patch)
- [GNU sed](https://www.gnu.org/software/sed/)
- [GNU tar](https://www.gnu.org/software/tar/)
- [GNU gzip](https://www.gnu.org/software/gzip)
- [GNU bash](https://www.gnu.org/software/bash)
- [GNU gettext](https://www.gnu.org/software/gettext)
- [GNU bison](https://www.gnu.org/software/bison)
- [GNU texinfo](https://www.gnu.org/software/texinfo)
- [GNU xorriso](https://www.gnu.org/software/xorriso/)
- [GNU wget](https://www.gnu.org/software/wget/)
- [GNU cpio](https://www.gnu.org/software/cpio/)
- [flex](https://github.com/westes/flex)
- [xz](https://tukaani.org/xz/)
- [Perl](https://www.perl.org/)
- [file](https://astron.com/pub/file/)
- [python 3](https://www.python.org/)
- [util-linux](https://mirrors.edge.kernel.org/pub/linux/utils/util-linux/)

Basically part 3 of LFS book with few additions

## Building 
### Requirements
Software packages with minimum versions:
- Bash 3.2
- Binutils 2.25
- Bison 2.7
- Bzip2 1.0.4
- Coreutils 6.9
- Diffutils 2.8.1
- Findutils 4.2.31
- Gawk 4.0.1
- GCC 6.2 including g++
- Glibc-2.11
- Grep 2.5.1a
- Gzip 1.3.12
- Linux Kernel 3.2
- M4 1.4.10
- Make 4.0
- Patch 2.5.4
- Perl 5.8.8
- Python 3.7
- Sed 4.1.5
- Tar 1.22
- Texinfo 4.7
- Xz 5.0.0

Other requirements:
- `/usr/bin/awk` should be a link to gawk
- `/usr/bin/yacc` should be a link to bison
- `/bin/sh` should be a symbolic or hard link to bash
