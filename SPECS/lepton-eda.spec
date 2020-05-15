Name:           lepton-eda
Version:        1.9.10
Release:        1%{?dist}
Summary:        Lepton Electronic Design Automation

License: GPLv2+
URL:     https://github.com/lepton-eda/lepton-eda
Source0: https://github.com/lepton-eda/lepton-eda/releases/download/1.9.10-20200319/lepton-eda-1.9.10.tar.gz

BuildRequires:
Requires:

%description
Lepton EDA is a suite of free software tools for designing
electronics. It provides schematic capture, netlisting into
over 30 netlist formats, and many other features.
It was forked from the gEDA/gaf suite in late 2016 by most
of its active developers at that time.
It's in active development and well supported.

%prep
%autosetup


%build
%configure
%make_build


%install
rm -rf $RPM_BUILD_ROOT
%make_install


%files
%license add-license-file-here
%doc add-docs-here



%changelog
* Fri May 15 2020 dmn <graahnul.grom@gmail.com>
- Initial version of the package
