%define ns_prefix ea
%define pkg_base  libzip
%define pkg_name  %{ns_prefix}-%{pkg_base}
%define _prefix   /opt/cpanel/%{ns_prefix}-%{pkg_base}
%define prefix_dir /opt/cpanel/%{ns_prefix}-%{pkg_base}
%define prefix_lib %{ns_prefix}-%{prefix_dir}/%{_lib}
%define prefix_bin %{ns_prefix}-%{prefix_dir}/bin
%define prefix_inc %{ns_prefix}-%{prefix_dir}/include

%if 0%{rhel} > 7
%global debug_package %{nil}
%endif

# I could not find any rhyme or reason for why the lib
# version is 5.1, while the libzip package is version 1.6.1
# so this may break in the future
# And, now with version 1.7.0, this changes to 5.3.

%define lib_major_version 5
%define lib_minor_version 3

Summary: A C library for reading, creating, and modifying zip and zip64 archives.
Name: %{pkg_name}
Version: 1.7.1
# Doing release_prefix this way for Release allows for OBS-proof versioning, See EA-4544 for more details
%define release_prefix 4
Release: %{release_prefix}%{?dist}.cpanel
License: https://github.com/nih-at/libzip/blob/master/LICENSE
Vendor: cPanel, Inc.
Group: Applications/Internet
Source: libzip-%{version}.tar.gz
URL: https://github.com/nih-at/libzip
BuildRoot: %{_tmppath}/%{pkg_name}-%{version}-%{release}-root

Patch1: 0001-Override-RPATH-for-zip-target.patch

Requires: bzip2-libs
Requires: zlib
%if 0%{rhel} > 7
# liblzma.so.5 is owned by this rpm
Requires: xz xz-libs
%else
Requires: lzma
%endif
Requires: ea-openssl11

BuildRequires: xz-devel
BuildRequires: ea-openssl11
BuildRequires: ea-openssl11-devel
BuildRequires: cmake3

%if 0%{rhel} > 7
# dependencry for cmake3
BuildRequires: brotli

# there is an unspecified requires: libcurl, that needs libnghttp2
BuildRequires: libcurl libnghttp2
%endif

%description
This is libzip, a C library for reading, creating, and modifying zip and
zip64 archives. Files can be added from data buffers, files, or
compressed data copied directly from other zip archives. Changes made
without closing the archive can be reverted. Decryption and encryption
of Winzip AES and decryption of legacy PKware encrypted files is
supported. The API is documented by man pages.

%package devel
Summary: Files for development of applications which will use ea-libzip
Group: Development/Libraries

%description devel
The files needed for developing applications with ea-libzip.

%prep
%setup -q -n libzip-%{version}
%patch1 -p1 -b .rpath

%build

export OPENSSL_ROOT_DIR=/opt/cpanel/ea-openssl11
export OPENSSL_LIBRARIES=/opt/cpanel/ea-openssl11/lib
export CPANEL_LIBZIP_RPATH=/opt/cpanel/ea-openssl11/lib
export CMAKE_COMMAND=cmake3
cmake3 .
make

%install
mkdir -p %{buildroot}%{_libdir}
mkdir -p %{buildroot}%{_libdir}/../include
install -m 755 zipconf.h %{buildroot}%{_libdir}/../include/zipconf.h
install -m 755 lib/zip.h %{buildroot}%{_libdir}/../include/zip.h

cd lib
install -m 755 libzip.so.%{lib_major_version}.%{lib_minor_version} %{buildroot}%{_libdir}/libzip.so.%{lib_major_version}.%{lib_minor_version}
ln -s libzip.so.%{lib_major_version}.%{lib_minor_version} %{buildroot}%{_libdir}/libzip.so.%{lib_major_version}
ln -s libzip.so.%{lib_major_version}.%{lib_minor_version} %{buildroot}%{_libdir}/libzip.so
cd ..

%files -n %{pkg_name}
%defattr(-,root,root,-)
%{_libdir}/libzip.so.%{lib_major_version}.%{lib_minor_version}
%{_libdir}/libzip.so.%{lib_major_version}
%{_libdir}/libzip.so

%files -n %{pkg_name}-devel
%defattr(-,root,root,-)
%{_prefix}/include/zipconf.h
%{_prefix}/include/zip.h

%changelog
* Thu Jul 23 2020 Tim Mullin <tim@cpanel.net> - 1.7.1-4
- EA-9181: Patch CMakeLists file so the RPATH does not end with a colon

* Fri Jul 17 2020 Tim Mullin <tim@cpanel.net> - 1.7.1-3
- EA-9178: Remove trailing colon from library's RPATH

* Mon Jun 29 2020 Julian Brown <julian.brown@cpanel.net> - 1.7.1-2
- ZC-6844: ea-libzip fix problems for CentOS 8

* Fri Jun 26 2020 Cory McIntire <cory@cpanel.net> - 1.7.1-1
- EA-9127: Update ea-libzip from v1.7.0 to v1.7.1

* Wed Jun 10 2020 Tim Mullin <tim@cpanel.net> - 1.7.0-1
- EA-9101: Update from upstream to 1.7.0

* Thu Mar 26 2020 Julian Brown <julian.brown@cpanel.net> - 1.6.1-3
- ZC-6449: Was not generating all the libzip.so variants.

* Tue Mar 17 2020 Julian Brown <julian.brown@cpanel.net> - 1.6.1-2
- ZC-6348: Remove jury rigged build system

* Wed Feb 05 2020 Julian Brown <julian.brown@cpanel.net> - 1.61.0-1
- ZC-6083: Create ea-libzip package.

