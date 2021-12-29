Lepton EDA for Fedora Linux
===========================

This repository contains everything necessary to easily build and install
<br />
[Lepton EDA](https://github.com/lepton-eda/lepton-eda) RPM package on Fedora Linux.
<br />
<br />
Current version: [1.9.17 release](https://github.com/lepton-eda/lepton-eda/releases/tag/1.9.17-20211219).
<br />
Tested on: Fedora 32 x86_64.
<br />
<br />
**Note:** Starting with Lepton EDA 1.9.13, RPM packages don't include `lepton-attrib`,
the batch attribute editor. It depends on the [gtkextra library](http://gtkextra.sourceforge.net),
version 3.0.0 or higher, but this [package in Fedora](https://src.fedoraproject.org/rpms/gtk+extra)
is extremely outdated (2.1.2, from 2010).
<br />
<br />
[Lepton EDA](https://github.com/lepton-eda/lepton-eda)
is a suite of free software tools for designing electronics,
an actively developed fork of the
[gEDA/gaf suite](http://wiki.geda-project.org/geda:gaf),
started in late 2016 by most of gEDA/gaf developers at that time.
It's backward compatible with its predecessor and
supports the same file format for symbols and schematics.


How to build and install
------------------------

Install required packages:
```
$ sudo dnf install git-core wget rpm-build
```

Clone the repository:
```
$ git clone https://github.com/graahnul-grom/fedora-lepton-eda.git
```

Go to the build directory:
```
$ cd fedora-lepton-eda/rpmbuild/
```

Download the source tarball: this script will download the latest
version of Lepton EDA source code tarball to the `SOURCES/` sub-directory:
```
$ ./download-source.sh
```

Install build dependencies:
```
$ sudo dnf builddep SPECS/lepton-eda.spec
```

Build source and binary RPM packages:
```
$ ./run-rpmbuild.sh
```

Install the binary package just built from the `RPMS/` sub-directory:
```
$ sudo dnf localinstall RPMS/x86_64/lepton-eda-1.9.17-1.fc32.x86_64.rpm
```
`x86_64` folder and `rpm` file may have different names,
depending on machine architecture and Fedora version.

