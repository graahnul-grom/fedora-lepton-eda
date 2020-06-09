### Lepton EDA for Fedora Linux

This repository contains everything necessary to easily build and install
<br />
[Lepton EDA](https://github.com/lepton-eda/lepton-eda) RPM package on Fedora Linux.<br />
Current version: [1.9.11 release](https://github.com/lepton-eda/lepton-eda/releases/tag/1.9.11-20200604).
<br />
Tested on Fedora 32 x86_64.<br />

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
$ sudo dnf localinstall RPMS/x86_64/lepton-eda-1.9.11-1.fc32.x86_64.rpm
```
`x86_64` folder and `rpm` file may have different names,
depending on machine architecture and Fedora version.

