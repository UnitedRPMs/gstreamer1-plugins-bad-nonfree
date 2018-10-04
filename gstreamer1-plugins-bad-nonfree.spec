# which plugins to actually build and install
%global extdirs ext/faac

Summary:        GStreamer 1.0 streaming media framework "bad" non-free plug-ins
Name:           gstreamer1-plugins-bad-nonfree
Version:        1.14.4
Release:        7%{?dist}
License:        LGPLv2+
Group:          Applications/Multimedia
URL:            http://gstreamer.freedesktop.org/
Source0:        http://gstreamer.freedesktop.org/src/gst-plugins-bad/gst-plugins-bad-%{version}.tar.xz
BuildRequires:  gstreamer1-devel >= 1.4.0
BuildRequires:  gstreamer1-plugins-base-devel >= 1.4.0
BuildRequires:  check
BuildRequires:  gettext-devel
BuildRequires:  libXt-devel
BuildRequires:  gtk-doc
BuildRequires:  orc-devel
BuildRequires:  libdca-devel
BuildRequires:  faac-devel

%description
GStreamer is a streaming media framework, based on graphs of elements which
operate on media data.

This package contains plug-ins that depend on libraries which use a non-free
license.


%prep
%setup -q -n gst-plugins-bad-%{version}


%build
# Note we don't bother with disabling everything which is in Fedora, that
# is unmaintainable, instead we selectively run make in subdirs
%configure --disable-static \
    --with-package-name="gst-plugins-bad 1.0 unitedrpms rpm" \
    --with-package-origin="https://unitedrpms.github.io/" \
    --enable-debug \
    --enable-silent-rules \
    --enable-experimental
# Don't use rpath!
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
for i in %{extdirs}; do
    pushd $i
    make %{?_smp_mflags} V=0
    popd
done


%install
for i in %{extdirs}; do
    pushd $i 
    make install V=0 DESTDIR=$RPM_BUILD_ROOT
    popd
done
rm $RPM_BUILD_ROOT%{_libdir}/gstreamer-1.0/*.la


%files
%doc AUTHORS NEWS README RELEASE
%license COPYING.LIB
# Plugins with external dependencies
%{_libdir}/gstreamer-1.0/libgstfaac.so


%changelog

* Wed Oct 03 2018 Unitedrpms Project <unitedrpms AT protonmail DOT com> 1.14.4-7 
- Updated to 1.14.4-7

* Mon Sep 17 2018 Unitedrpms Project <unitedrpms AT protonmail DOT com> 1.14.3-7 
- Updated to 1.14.3-7

* Fri Jul 20 2018 Unitedrpms Project <unitedrpms AT protonmail DOT com> 1.14.2-7 
- Updated to 1.14.2-7

* Mon May 21 2018 Unitedrpms Project <unitedrpms AT protonmail DOT com> 1.14.1-7 
- Updated to 1.14.1-7

* Wed Mar 21 2018 Unitedrpms Project <unitedrpms AT protonmail DOT com> 1.14.0-7 
- Updated to 1.14.0-7

* Fri Mar 16 2018 Unitedrpms Project <unitedrpms AT protonmail DOT com> 1.13.91-7 
- Updated to 1.13.91-7

* Sun Mar 04 2018 Unitedrpms Project <unitedrpms AT protonmail DOT com> 1.13.90-7  
- Updated to 1.13.90-7

* Fri Dec 08 2017 Unitedrpms Project <unitedrpms AT protonmail DOT com> 1.12.4-7
- Updated to 1.12.4-7

* Fri Sep 22 2017 Unitedrpms Project <unitedrpms AT protonmail DOT com> 1.12.3-8  
- Automatic Mass Rebuild

* Mon Sep 18 2017 Unitedrpms Project <unitedrpms AT protonmail DOT com> - 1.12.3-7
- Updated to 1.12.3-7

* Thu Aug 03 2017 Unitedrpms Project <unitedrpms AT protonmail DOT com> 1.12.2-3  
- Automatic Mass Rebuild

* Thu Jul 20 2017 Unitedrpms Project <unitedrpms AT protonmail DOT com> - 1.12.2-2
- Updated to 1.12.2-2

* Sat Jun 24 2017 Unitedrpms Project <unitedrpms AT protonmail DOT com> - 1.12.1-2
- Updated to 1.12.1-2

* Thu May 25 2017 David Vásquez <davidva AT tutanota DOT com> 1.12.0-2
- Updated to 1.12.0-2

* Sat Apr 29 2017 David Vásquez <davidva AT tutanota DOT com> 1.11.91-2
- Updated to 1.11.91-2

* Thu Apr 20 2017 David Vásquez <davidva AT tutanota DOT com> 1.11.90-2
- Updated to 1.11.90-2

* Fri Feb 24 2017 David Vásquez <davidjeremias82 AT gmail DOT com> 1.11.2-1
- Updated to 1.11.2

* Fri Jan 27 2017 David Vásquez <davidjeremias82 AT gmail DOT com> 1.11.1-1
- Updated to 1.11.1

* Sat Dec 10 2016 Pavlo Rudyi <paulcarroty at riseup.net> - 1.10.2-1
- Update to 1.10.2

* Fri Nov 11 2016 Hans de Goede <j.w.r.degoede@gmail.com> - 1.10.0-1
- Update to 1.10.0

* Sat Jul  9 2016 Hans de Goede <j.w.r.degoede@gmail.com> - 1.8.2-1
- Update to 1.8.2

* Sat Jul  9 2016 Hans de Goede <j.w.r.degoede@gmail.com> - 1.6.4-1
- Update to 1.6.4

* Sat Aug 22 2015 Hans de Goede <j.w.r.degoede@gmail.com> - 1.4.5-1
- Initial gstreamer1-plugins-bad-nonfree rpmfusion package
