# which plugins to actually build and install
%global extdirs ext/faac

Summary:        GStreamer 1.0 streaming media framework "bad" non-free plug-ins
Name:           gstreamer1-plugins-bad-nonfree
Version:        1.18.4
Release:        7%{?dist}
License:        LGPLv2+
Group:          Applications/Multimedia
URL:            http://gstreamer.freedesktop.org/
Source0:        http://gstreamer.freedesktop.org/src/gst-plugins-bad/gst-plugins-bad-%{version}.tar.xz
BuildRequires:  gstreamer1-devel >= %{version}
BuildRequires:  gstreamer1-plugins-base-devel >= %{version}
BuildRequires:  check
BuildRequires:  gettext-devel
BuildRequires:  libXt-devel
BuildRequires:  gtk-doc
BuildRequires:  orc-devel
BuildRequires:  libdca-devel
BuildRequires:  faac-devel >= 1.30
BuildRequires:	gcc-c++
BuildRequires:	mesa-libGLES-devel
BuildRequires:	openssl-devel
BuildRequires:	meson
BuildRequires:	cmake
BuildRequires:	gobject-introspection-devel
BuildRequires:	opencv-devel
BuildRequires:  libdrm-devel
BuildRequires:	libltc-devel
BuildRequires:  lcms2-devel
BuildRequires:  pkgconfig(gudev-1.0)
BuildRequires:  pkgconfig(libusb-1.0)
BuildRequires:  pkgconfig(libva-drm)
BuildRequires:  pkgconfig(pangocairo)
BuildRequires:  pkgconfig(zvbi-0.2)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  libnice-devel
BuildRequires:  liblrdf-devel
BuildRequires:  lilv-devel
BuildRequires:  libdvdnav-devel

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

meson build --prefix=/usr --libdir=%{_libdir} --libexecdir=/usr/libexec --bindir=/usr/bin --sbindir=/usr/sbin --includedir=/usr/include --datadir=/usr/share --mandir=/usr/share/man --infodir=/usr/share/info --localedir=/usr/share/locale --sysconfdir=/etc  \
    -D package-name="gst-plugins-bad 1.0 unitedrpms rpm" \
    -D package-origin="https://unitedrpms.github.io" \
    -D doc=disabled -D faac=enabled -D msdk=disabled \
    -D dts=disabled -D faad=disabled -D bluez=disabled \
    -D libmms=disabled -D mpeg2enc=disabled -D mplex=disabled \
    -D neon=disabled -D rtmp=disabled -D rtmp2=disabled \
    -D flite=disabled -D sbc=disabled  \
    -D voamrwbenc=disabled -D x265=disabled -D opencv=disabled \
    -D dvbsuboverlay=disabled -D dvdspu=disabled -D siren=disabled \
    -D real=disabled -D opensles=disabled -D tinyalsa=disabled \
    -D wasapi=disabled -D wasapi2=disabled -D avtp=disabled \
    -D dc1394=disabled -D directfb=disabled -D iqa=disabled \
    -D libde265=disabled -D musepack=disabled -D openni2=disabled \
    -D sctp=disabled -D svthevcenc=disabled -D voaacenc=disabled \
    -D zxing=disabled -D wpe=disabled -D x11=disabled \
    -D openh264=disabled -D srt=disabled -D openmpt=disabled \
    -D lv2=disabled -D spandsp=disabled -D gobject-cast-checks=disabled \
    -D openal=disabled -D vdpau=disabled -D uvch264=disabled \
    -D ltc=disabled -D vulkan=disabled -D wayland=disabled \
    -D libdrm=disabled -D usb=disabled -D examples=disabled  \
    -D assrender=disabled -D bz2=disabled -D kate=disabled \
    -D magicleap=disabled -D aom=disabled -D bs2b=disabled \
    -D chromaprint=disabled -D curl=disabled -D fdkaac=disabled \
    -D fluidsynth=disabled -D gme=disabled -D gsm=disabled \
    -D lrdf=disabled -D ladspa=disabled -D microdns=disabled \
    -D modplug=disabled -D openjpeg=disabled -D sndfile=disabled \
    -D ofa=disabled -D openal=disabled -D openexr=disabled \
    -D openmpt=disabled -D opus=disabled -D rsvg=disabled \
    -D soundtouch=disabled -D spandsp=disabled -D srt=disabled \
    -D srtp=disabled -D wildmidi=disabled -D zbar=disabled \
    %if 0%{?fedora} <= 30
    -D va=disabled  
    %endif
    -D webrtc=disabled -D webrtcdsp=disabled -D webp=disabled 

%meson_build -C build

%install
%meson_install -C build


%files
%doc AUTHORS NEWS README RELEASE
%license 
# Plugins with external dependencies
%exclude %{_libdir}/
%exclude %{_datadir}/
%exclude %{_includedir}/
%exclude %{_bindir}/
%{_libdir}/gstreamer-1.0/libgstfaac.so


%changelog

* Mon Apr 19 2021 Unitedrpms Project <unitedrpms AT protonmail DOT com> 1.18.4-7
- Updated to 1.18.4

* Mon Jan 25 2021 Unitedrpms Project <unitedrpms AT protonmail DOT com> 1.18.3-7
- Updated to 1.18.3

* Mon Dec 07 2020 Unitedrpms Project <unitedrpms AT protonmail DOT com> 1.18.2-7
- Updated to 1.18.2

* Thu Oct 29 2020 Unitedrpms Project <unitedrpms AT protonmail DOT com> 1.18.1-7
- Updated to 1.18.1

* Mon Sep 28 2020 Unitedrpms Project <unitedrpms AT protonmail DOT com> 1.18.0-7
- Updated to 1.18.0

* Tue Aug 25 2020 Unitedrpms Project <unitedrpms AT protonmail DOT com> 1.17.90-7
- Updated to 1.17.90

* Fri Jul 10 2020 Unitedrpms Project <unitedrpms AT protonmail DOT com> 1.17.2-7
- Updated to 1.17.2

* Wed Dec 04 2019 Unitedrpms Project <unitedrpms AT protonmail DOT com> 1.16.2-7
- Updated to 1.16.2-7

* Fri Oct 18 2019 Unitedrpms Project <unitedrpms AT protonmail DOT com> 1.16.1-8
- Rebuilt for faac

* Wed Oct 02 2019 Unitedrpms Project <unitedrpms AT protonmail DOT com> 1.16.1-7
- Updated to 1.16.1-7

* Fri Apr 19 2019 Unitedrpms Project <unitedrpms AT protonmail DOT com> 1.16.0-7
- Updated to 1.16.0-7

* Wed Feb 27 2019 Unitedrpms Project <unitedrpms AT protonmail DOT com> 1.15.2-7
- Updated to 1.15.2-7

* Fri Jan 18 2019 Unitedrpms Project <unitedrpms AT protonmail DOT com> 1.15.1-7 
- Updated to 1.15.1-7

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
