%global  qt_version 6.7.2

Summary: Qt6 - QtImageFormats component
Name:    qt6-qtimageformats
Version: 6.7.2
Release: 0%{?dist}

License: LGPL-3.0-only OR GPL-3.0-only WITH Qt-GPL-exception-1.0
Url:     http://www.qt.io
Source0: %{name}-%{version}.tar.bz2

BuildRequires: cmake
BuildRequires: clang
BuildRequires: ninja
BuildRequires: qt6-qtbase-devel >= %{qt_version}
BuildRequires: qt6-qtbase-private-devel
%{?_qt6:Requires: %{_qt6}%{?_isa} = %{_qt6_version}}
BuildRequires: libtiff-devel
BuildRequires: jasper-devel
BuildRequires: pkgconfig(libmng)
BuildRequires: pkgconfig(libwebp)

# filter plugin provides
%global __provides_exclude_from ^%{_qt6_plugindir}/.*\\.so$

%description
The core Qt Gui library by default supports reading and writing image
files of the most common file formats: PNG, JPEG, BMP, GIF and a few more,
ref. Reading and Writing Image Files. The Qt Image Formats add-on module
provides optional support for other image file formats, including:
MNG, TGA, TIFF, WBMP.


%prep
%autosetup -n %{qt_module}-everywhere-src-%{qt_version}%{?unstable:-%{prerelease}} -p1

rm -rv src/3rdparty


%build
%cmake_qt6 -DQT_FEATURE_mng=ON \
    -DQT_BUILD_EXAMPLES:BOOL=OFF \
    -DQT_INSTALL_EXAMPLES_SOURCES=OFF

%cmake_build


%install
%cmake_install


%files
%license LICENSES/GPL*
%license LICENSES/LGPL*
%{_qt6_plugindir}/imageformats/libqmng.so
%{_qt6_plugindir}/imageformats/libqtga.so
%{_qt6_plugindir}/imageformats/libqtiff.so
%{_qt6_plugindir}/imageformats/libqwbmp.so
%{_qt6_plugindir}/imageformats/libqicns.so
%{_qt6_plugindir}/imageformats/libqjp2.so
%{_qt6_plugindir}/imageformats/libqwebp.so
%{_qt6_libdir}/cmake/Qt6/*.cmake
%{_qt6_libdir}/cmake/Qt6Gui/*.cmake
