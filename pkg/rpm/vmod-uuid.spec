# -D MUST pass in _version and _release, and SHOULD pass in dist.

Summary: UUID module for Varnish Cache
Name: vmod-uuid
Version: %{_version}
Release: %{_release}%{?dist}
License: BSD
Group: System Environment/Daemons
URL: https://github.com/otto-de/libvmod-uuid
Source0: %{name}-%{version}.tar.gz

# varnish from varnish61 at packagecloud
# This is the Requires for VMOD ABI compatibility with VRT >= 8.0.
Requires: varnishd(vrt)%{?_isa} >= 8
Requires: uuid

BuildRequires: varnish-devel >= 6.1.0
BuildRequires: uuid-devel
BuildRequires: pkgconfig
BuildRequires: make
BuildRequires: gcc
BuildRequires: python-docutils >= 0.6

# git builds
#BuildRequires: automake
#BuildRequires: autoconf
#BuildRequires: autoconf-archive
#BuildRequires: libtool

Provides: vmod-uuid, vmod-uuid-debuginfo

%description
UUID Varnish vmod used to generate a uuid, including versions 1, 3, 4
and 5 as specified in RFC 4122. See the RFC for details about the
various versions.

%prep
%setup -q -n %{name}-%{version}

%build

# if this were a git build
# ./autogen.sh

%configure

make %{?_smp_mflags}

%check

make %{?_smp_mflags} check

%install

make install DESTDIR=%{buildroot}

# Only use the version-specific docdir created by %doc below
rm -rf %{buildroot}%{_docdir}

# None of these for fedora/epel
find %{buildroot}/%{_libdir}/ -name '*.la' -exec rm -f {} ';'
find %{buildroot}/%{_libdir}/ -name '*.a' -exec rm -f {} ';'

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{_libdir}/varnish*/vmods/
%{_mandir}/man3/*.3*
%doc README.rst COPYING LICENSE

%post
/sbin/ldconfig

%changelog
* Fri Nov 30 2018 Geoff Simmons <geoff[AT]uplex.de> - %{_version}-%{_release}
  Compatible with VRT 8 (Varnish 6.1 and libvarnishapi.so.2)

* Mon Apr 02 2018 Geoff Simmons <geoff[AT]uplex.de> - 1.5-1
- Compatible with VRT 7.0 and Varnish 6.0.0.

* Wed Dec 20 2017 Geoff Simmons <geoff[AT]uplex.de> - 1.4-1
- Compatible with VRT 6.1 and Varnish 5.2.1.
