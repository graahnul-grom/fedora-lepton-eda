### [Lepton EDA](https://github.com/lepton-eda/lepton-eda) for Fedora Linux

This repository contains everything necessary to
build and install Lepton EDA RPM package on Fedora Linux.

Tested on Fedora 32 x86_64.

#### How to build and install

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

Download the source tarball. This script will download the latest
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
$ sudo dnf localinstall RPMS/x86_64/lepton-eda-1.9.10-1.fc32.x86_64.rpm
```
`x86_64` folder and `rpm` file may have different names,
depending on machine architecture and Fedora version.

