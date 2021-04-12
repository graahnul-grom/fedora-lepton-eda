Name:           lepton-eda
Version:        1.9.14
Release:        1%{?dist}
Summary:        Lepton Electronic Design Automation

License: GPLv2+
URL:     https://github.com/lepton-eda/lepton-eda
Source0: https://github.com/lepton-eda/lepton-eda/releases/download/1.9.14-20210407/lepton-eda-1.9.14.tar.gz

# fix guile-snarf detection on Fedora
Patch0: detect-guile-snarf.patch


BuildRequires: gcc
BuildRequires: guile22-devel
BuildRequires: gettext-devel
BuildRequires: intltool
BuildRequires: groff
BuildRequires: texinfo
BuildRequires: flex
BuildRequires: gawk
BuildRequires: libtool
BuildRequires: autoconf
BuildRequires: automake
BuildRequires: desktop-file-utils
BuildRequires: libstroke-devel
BuildRequires: pkgconfig(glib-2.0) >= 2.38.0
BuildRequires: pkgconfig(gtk+-2.0) >= 2.24.0
BuildRequires: pkgconfig(gdk-pixbuf-2.0) >= 2.21.0
BuildRequires: pkgconfig(cairo)
BuildRequires: pkgconfig(pango) >= 1.23.0
BuildRequires: pkgconfig(shared-mime-info)

Requires: guile22
Requires: libstroke


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


%build
./autogen.sh
%configure \
    --disable-attrib \
    --disable-rpath \
    --disable-update-xdg-database
%make_build


%install
rm -rf $RPM_BUILD_ROOT
%make_install

find %{buildroot} -type f -name '*.la' -delete -print
rm -rf %{buildroot}%{_infodir}/dir


%find_lang liblepton
%find_lang libleptongui
%find_lang lepton-cli


%files -f liblepton.lang -f libleptongui.lang -f lepton-cli.lang
%license COPYING COPYING.LGPL
%doc AUTHORS CONTRIBUTING.md
%{_bindir}/*
%{_includedir}/*
%{_libdir}/pkgconfig/*.pc
%{_libdir}/liblepton.*
%{_libdir}/libleptongui.*
%{_datadir}/lepton-eda/*
%{_datadir}/icons/*
%{_datadir}/applications/*.desktop
%{_datadir}/mime/packages/liblepton.xml
%{_docdir}/lepton-eda/*
%{_mandir}/man1/*
%{_infodir}/*


%changelog
* Mon Dec 14 2020 dmn <graahnul.grom@gmail.com> 1.9.13-1
- Update to release 1.9.13
* Fri Jun 05 2020 dmn <graahnul.grom@gmail.com> 1.9.11-1
- Update to release 1.9.11
* Fri May 15 2020 dmn <graahnul.grom@gmail.com> 1.9.10-1
- Initial version of the package
