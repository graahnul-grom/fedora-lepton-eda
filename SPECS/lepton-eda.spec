Name:           lepton-eda
Version:        1.9.10
Release:        1%{?dist}
Summary:        Lepton Electronic Design Automation

License: GPLv2+
URL:     https://github.com/lepton-eda/lepton-eda
Source0: https://github.com/lepton-eda/lepton-eda/releases/download/1.9.10-20200319/lepton-eda-1.9.10.tar.gz

# fix guile-snarf detection on Fedora:
Patch0: 0-guile-snarf-m4-dmn.patch
# fix build with gcc 10: https://github.com/lepton-eda/lepton-eda/pull/607
Patch1: 1-607.patch
# fix bug in lepton-upcfg: https://github.com/lepton-eda/lepton-eda/pull/609
Patch2: 2-upcfg.patch
# add lepton-upcfg man page: https://github.com/lepton-eda/lepton-eda/pull/620
Patch3: 3-upcfg-man.patch


BuildRequires: gcc
BuildRequires: guile22-devel
BuildRequires: gettext-devel
BuildRequires: intltool
BuildRequires: groff
BuildRequires: flex
BuildRequires: gawk
BuildRequires: libtool
BuildRequires: autoconf
BuildRequires: automake
BuildRequires: desktop-file-utils
BuildRequires: pkgconfig(glib-2.0) >= 2.38.0
BuildRequires: pkgconfig(gtk+-2.0) >= 2.24.0
BuildRequires: pkgconfig(gdk-pixbuf-2.0) >= 2.21.0
BuildRequires: pkgconfig(cairo)
BuildRequires: pkgconfig(pango) >= 1.23.0
BuildRequires: pkgconfig(shared-mime-info)

Requires: guile22


%description
Lepton EDA is a suite of free software tools for designing
electronics. It provides schematic capture, netlisting into
over 30 netlist formats, and many other features.
It was forked from the gEDA/gaf suite in late 2016 by most
of its active developers at that time.
It's in active development and well supported.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1


%build
./autogen.sh
%configure \
    --disable-rpath \
    --disable-update-xdg-database
%make_build


%install
rm -rf $RPM_BUILD_ROOT
%make_install

find %{buildroot} -type f -name '*.la' -delete -print
rm -rf %{buildroot}%{_infodir}/dir


%find_lang liblepton
%find_lang lepton-schematic
%find_lang lepton-attrib
%find_lang lepton-cli
%find_lang lepton-netlist
%find_lang lepton-symcheck


%files -f liblepton.lang -f lepton-schematic.lang -f lepton-attrib.lang -f lepton-cli.lang -f lepton-netlist.lang -f lepton-symcheck.lang
%license COPYING COPYING.LGPL
%doc AUTHORS CONTRIBUTING.md
%{_bindir}/*
%{_includedir}/*
%{_libdir}/pkgconfig/*.pc
%{_libdir}/liblepton.so
%{_libdir}/liblepton.so.5
%{_libdir}/liblepton.so.5.0.0
%{_libdir}/libleptonrenderer.so
%{_libdir}/libleptonrenderer.so.2
%{_libdir}/libleptonrenderer.so.2.0.0
%{_datadir}/lepton-eda/*
%{_datadir}/icons/*
%{_datadir}/applications/*.desktop
%{_datadir}/mime/packages/liblepton.xml
%{_docdir}/lepton-eda/*
%{_mandir}/man1/*
%{_infodir}/*


%changelog
* Fri May 15 2020 dmn <graahnul.grom@gmail.com>
- Initial version of the package
