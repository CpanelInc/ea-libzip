%define ns_prefix ea
%define pkg_base  libzip
%define pkg_name  %{ns_prefix}-%{pkg_base}
%define _prefix   /opt/cpanel/%{pkg_base}
%define prefix_dir /opt/cpanel/%{pkg_base}
%define prefix_lib %{prefix_dir}/%{_lib}
%define prefix_bin %{prefix_dir}/bin
%define prefix_inc %{prefix_dir}/include

Summary: A C library for reading, creating, and modifying zip and zip64 archives.
Name: %{pkg_name}
Version: 1.61.0
%define release_prefix 1
Release: %{release_prefix}%{?dist}.cpanel
License: Unknown
# https://github.com/nih-at/libzip/blob/master/LICENSE
Vendor: cPanel, Inc.
Group: Applications/Internet
Source: libzip-%{version}.tar.gz
URL: https://github.com/nih-at/libzip
BuildRoot: %{_tmppath}/%{pkg_name}-%{version}-%{release}-root

BuildRequires: cmake3

%description
This is libzip, a C library for reading, creating, and modifying zip and
zip64 archives. Files can be added from data buffers, files, or
compressed data copied directly from other zip archives. Changes made
without closing the archive can be reverted. Decryption and encryption
of Winzip AES and decryption of legacy PKware encrypted files is
supported. The API is documented by man pages.

%prep

%build
cmake3 .
make

%install
install -m 755 %{buildroot}/lib/libzip.so.5 %{_libdir}/libzip.so.5
install -m 755 %{buildroot}/lib/libzip.so.5.1 %{_libdir}/libzip.so.5.1

%files -n %{pkg_name}
%defattr(-,root,root,-)
%{_libdir}/libzip.so.5
%{_libdir}/libzip.so.5.1

%changelog
* Mon Feb 03 2020 Julian Brown <julian.brown@cpanel.net> - 1.61.0-1
- ZC-6083: Create ea-libzip package.

