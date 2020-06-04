Name:           lepton-eda
Version:        1.9.10
Release:        1%{?dist}
Summary:        Lepton Electronic Design Automation

License: GPLv2+
URL:     https://github.com/lepton-eda/lepton-eda
Source0: https://github.com/lepton-eda/lepton-eda/releases/download/1.9.10-20200319/lepton-eda-1.9.10.tar.gz

# fix guile-snarf detection on Fedora
Patch0: detect-guile-snarf.patch
# fix build with gcc 10: https://github.com/lepton-eda/lepton-eda/pull/607
Patch1: fix-gcc-10-build.patch
# fix bug in lepton-upcfg utility: https://github.com/lepton-eda/lepton-eda/pull/609
Patch2: fix-upcfg.patch
# add lepton-upcfg man page: https://github.com/lepton-eda/lepton-eda/pull/620
Patch3: add-upcfg-man-page.patch
# fix font rendering with pango 1.44 patches: https://github.com/lepton-eda/lepton-eda/pull/<PR number>
Patch4: fix-font-render-1-pr608.patch
Patch5: fix-font-render-2-pr615.patch
Patch6: fix-font-render-3-pr616.patch
Patch7: fix-font-render-4-pr623.patch
Patch8: fix-font-render-5-pr624.patch
Patch9: fix-font-render-6-pr629.patch
# fix memory leaks: https://github.com/lepton-eda/lepton-eda/pull/647
Patch10: fix-memleak-pr647.diff


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
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1
%patch10 -p1


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
%{_libdir}/liblepton.*
%{_libdir}/libleptonrenderer.*
%{_datadir}/lepton-eda/*
%{_datadir}/icons/*
%{_datadir}/applications/*.desktop
%{_datadir}/mime/packages/liblepton.xml
%{_docdir}/lepton-eda/*
%{_mandir}/man1/*
%{_infodir}/*


%changelog
* Fri May 15 2020 dmn <graahnul.grom@gmail.com> 1.9.10-1
- Initial version of the package
