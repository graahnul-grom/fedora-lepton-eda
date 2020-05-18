fedora-lepton-eda
=================

Lepton EDA package for Fedora Linux


Download the source tarball:
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

Install the binary package just built from the RPMS/
directory by running `sudo dnf localinstall`.

