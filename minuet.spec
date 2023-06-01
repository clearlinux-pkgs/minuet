#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cmake
#
# Source0 file verified with key 0xBB463350D6EF31EF (heiko@shruuf.de)
#
Name     : minuet
Version  : 23.04.1
Release  : 33
URL      : https://download.kde.org/stable/release-service/23.04.1/src/minuet-23.04.1.tar.xz
Source0  : https://download.kde.org/stable/release-service/23.04.1/src/minuet-23.04.1.tar.xz
Source1  : https://download.kde.org/stable/release-service/23.04.1/src/minuet-23.04.1.tar.xz.sig
Summary  : No detailed summary available
Group    : Development/Tools
License  : GFDL-1.3 GPL-2.0
Requires: minuet-bin = %{version}-%{release}
Requires: minuet-data = %{version}-%{release}
Requires: minuet-lib = %{version}-%{release}
Requires: minuet-license = %{version}-%{release}
Requires: minuet-locales = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : extra-cmake-modules-data
BuildRequires : pkg-config
BuildRequires : pkgconfig(fluidsynth)
BuildRequires : qtbase-dev mesa-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
# About Minuet
Welcome to Minuet: the KDE software for music education. Minuet aims at supporting students and teachers in many aspects of music education, such as ear training, first-sight reading, solfa, scales, rhythm, harmony, and improvisation. Minuet makes extensive use of MIDI capabilities to provide a full-fledged set of features regarding volume, tempo, and pitch changes, which makes Minuet a valuable tool for both novice and experienced musicians.

%package bin
Summary: bin components for the minuet package.
Group: Binaries
Requires: minuet-data = %{version}-%{release}
Requires: minuet-license = %{version}-%{release}

%description bin
bin components for the minuet package.


%package data
Summary: data components for the minuet package.
Group: Data

%description data
data components for the minuet package.


%package dev
Summary: dev components for the minuet package.
Group: Development
Requires: minuet-lib = %{version}-%{release}
Requires: minuet-bin = %{version}-%{release}
Requires: minuet-data = %{version}-%{release}
Provides: minuet-devel = %{version}-%{release}
Requires: minuet = %{version}-%{release}

%description dev
dev components for the minuet package.


%package doc
Summary: doc components for the minuet package.
Group: Documentation

%description doc
doc components for the minuet package.


%package lib
Summary: lib components for the minuet package.
Group: Libraries
Requires: minuet-data = %{version}-%{release}
Requires: minuet-license = %{version}-%{release}

%description lib
lib components for the minuet package.


%package license
Summary: license components for the minuet package.
Group: Default

%description license
license components for the minuet package.


%package locales
Summary: locales components for the minuet package.
Group: Default

%description locales
locales components for the minuet package.


%prep
%setup -q -n minuet-23.04.1
cd %{_builddir}/minuet-23.04.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1685595121
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FCFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export CXXFLAGS="$CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
%cmake ..
make  %{?_smp_mflags}
popd
mkdir -p clr-build-avx2
pushd clr-build-avx2
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -Wl,-z,x86-64-v3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd -march=x86-64-v3 "
export FCFLAGS="$FFLAGS -O3 -Wl,-z,x86-64-v3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd -march=x86-64-v3 "
export FFLAGS="$FFLAGS -O3 -Wl,-z,x86-64-v3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd -march=x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -O3 -Wl,-z,x86-64-v3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd -march=x86-64-v3 "
export CFLAGS="$CFLAGS -march=x86-64-v3 -m64 -Wl,-z,x86-64-v3"
export CXXFLAGS="$CXXFLAGS -march=x86-64-v3 -m64 -Wl,-z,x86-64-v3"
export FFLAGS="$FFLAGS -march=x86-64-v3 -m64 -Wl,-z,x86-64-v3"
export FCFLAGS="$FCFLAGS -march=x86-64-v3 -m64 -Wl,-z,x86-64-v3"
%cmake ..
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1685595121
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/minuet
cp %{_builddir}/minuet-%{version}/COPYING %{buildroot}/usr/share/package-licenses/minuet/4cc77b90af91e615a64ae04893fdffa7939db84c || :
cp %{_builddir}/minuet-%{version}/COPYING.DOC %{buildroot}/usr/share/package-licenses/minuet/464c48ede3b2a4ea76b5f314f03213315f942c63 || :
pushd clr-build-avx2
%make_install_v3  || :
popd
pushd clr-build
%make_install
popd
%find_lang minuet
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/V3/usr/bin/minuet
/usr/bin/minuet

%files data
%defattr(-,root,root,-)
/usr/share/applications/org.kde.minuet.desktop
/usr/share/icons/hicolor/128x128/apps/minuet.png
/usr/share/icons/hicolor/128x128/apps/minuet.svg
/usr/share/icons/hicolor/16x16/actions/minuet-chords.svg
/usr/share/icons/hicolor/16x16/actions/minuet-intervals.svg
/usr/share/icons/hicolor/16x16/actions/minuet-rhythms.svg
/usr/share/icons/hicolor/16x16/actions/minuet-scales.svg
/usr/share/icons/hicolor/16x16/apps/minuet.png
/usr/share/icons/hicolor/16x16/apps/minuet.svg
/usr/share/icons/hicolor/22x22/actions/minuet-chords.svg
/usr/share/icons/hicolor/22x22/actions/minuet-intervals.svg
/usr/share/icons/hicolor/22x22/actions/minuet-rhythms.svg
/usr/share/icons/hicolor/22x22/actions/minuet-scales.svg
/usr/share/icons/hicolor/22x22/apps/minuet.png
/usr/share/icons/hicolor/22x22/apps/minuet.svg
/usr/share/icons/hicolor/32x32/apps/minuet.png
/usr/share/icons/hicolor/32x32/apps/minuet.svg
/usr/share/icons/hicolor/48x48/apps/minuet.png
/usr/share/icons/hicolor/48x48/apps/minuet.svg
/usr/share/icons/hicolor/64x64/apps/minuet.png
/usr/share/icons/hicolor/64x64/apps/minuet.svg
/usr/share/icons/hicolor/scalable/apps/minuet.svgz
/usr/share/metainfo/org.kde.minuet.appdata.xml
/usr/share/minuet/definitions/chords-root-position-definitions.json
/usr/share/minuet/definitions/intervals-ascending-melodic-harmonic-definitions.json
/usr/share/minuet/definitions/intervals-descending-melodic-definitions.json
/usr/share/minuet/definitions/rhythm-definitions.json
/usr/share/minuet/definitions/scales-bebop-definitions.json
/usr/share/minuet/definitions/scales-harmonic-major-and-its-modes-definitions.json
/usr/share/minuet/definitions/scales-harmonic-minor-and-its-modes-definitions.json
/usr/share/minuet/definitions/scales-major-and-its-modes-definitions.json
/usr/share/minuet/definitions/scales-pentatonic-major-and-its-modes-definitions.json
/usr/share/minuet/definitions/scales-simmetric-definitions.json
/usr/share/minuet/exercises/chords-root-position-exercises.json
/usr/share/minuet/exercises/intervals-ascending-melodic-exercises.json
/usr/share/minuet/exercises/intervals-descending-melodic-exercises.json
/usr/share/minuet/exercises/intervals-harmonic-exercises.json
/usr/share/minuet/exercises/rhythm-easy.json
/usr/share/minuet/exercises/rhythm-medium.json
/usr/share/minuet/exercises/scales-bebop-exercises.json
/usr/share/minuet/exercises/scales-harmonic-major-and-its-modes-exercises.json
/usr/share/minuet/exercises/scales-harmonic-minor-and-its-modes-exercises.json
/usr/share/minuet/exercises/scales-major-and-its-modes-exercises.json
/usr/share/minuet/exercises/scales-pentatonic-major-and-its-modes-exercises.json
/usr/share/minuet/exercises/scales-simmetric-exercises.json
/usr/share/minuet/soundfonts/GeneralUser-v1.47.sf2

%files dev
%defattr(-,root,root,-)
/usr/include/minuet/interfaces/icore.h
/usr/include/minuet/interfaces/iexercisecontroller.h
/usr/include/minuet/interfaces/iplugin.h
/usr/include/minuet/interfaces/iplugincontroller.h
/usr/include/minuet/interfaces/isoundcontroller.h
/usr/include/minuet/interfaces/iuicontroller.h
/usr/include/minuet/interfaces/minuetinterfacesexport.h
/usr/lib64/libminuetinterfaces.so

%files doc
%defattr(0644,root,root,0755)
/usr/share/doc/HTML/ca/minuet/index.cache.bz2
/usr/share/doc/HTML/ca/minuet/index.docbook
/usr/share/doc/HTML/ca/minuet/minuet-screenshot.png
/usr/share/doc/HTML/de/minuet/index.cache.bz2
/usr/share/doc/HTML/de/minuet/index.docbook
/usr/share/doc/HTML/en/minuet/index.cache.bz2
/usr/share/doc/HTML/en/minuet/index.docbook
/usr/share/doc/HTML/en/minuet/minuet-screenshot.png
/usr/share/doc/HTML/en/minuet/minuet-ui-components.png
/usr/share/doc/HTML/es/minuet/index.cache.bz2
/usr/share/doc/HTML/es/minuet/index.docbook
/usr/share/doc/HTML/it/minuet/index.cache.bz2
/usr/share/doc/HTML/it/minuet/index.docbook
/usr/share/doc/HTML/it/minuet/minuet-screenshot.png
/usr/share/doc/HTML/it/minuet/minuet-ui-components.png
/usr/share/doc/HTML/nl/minuet/index.cache.bz2
/usr/share/doc/HTML/nl/minuet/index.docbook
/usr/share/doc/HTML/pt/minuet/index.cache.bz2
/usr/share/doc/HTML/pt/minuet/index.docbook
/usr/share/doc/HTML/pt_BR/minuet/index.cache.bz2
/usr/share/doc/HTML/pt_BR/minuet/index.docbook
/usr/share/doc/HTML/ru/minuet/index.cache.bz2
/usr/share/doc/HTML/ru/minuet/index.docbook
/usr/share/doc/HTML/sv/minuet/index.cache.bz2
/usr/share/doc/HTML/sv/minuet/index.docbook
/usr/share/doc/HTML/uk/minuet/index.cache.bz2
/usr/share/doc/HTML/uk/minuet/index.docbook

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/libminuetinterfaces.so.0.3.0
/V3/usr/lib64/qt5/plugins/minuet/minuetfluidsynthsoundcontroller.so
/usr/lib64/libminuetinterfaces.so.0.3.0
/usr/lib64/qt5/plugins/minuet/minuetfluidsynthsoundcontroller.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/minuet/464c48ede3b2a4ea76b5f314f03213315f942c63
/usr/share/package-licenses/minuet/4cc77b90af91e615a64ae04893fdffa7939db84c

%files locales -f minuet.lang
%defattr(-,root,root,-)

