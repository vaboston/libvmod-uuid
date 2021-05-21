# -D MUST pass in _version and _release, and SHOULD pass in dist.

Summary: UUID module for Varnish Cache
Name: vmod-uuid-maxwait
Version: %{_version}
Release: %{_release}%{?dist}
License: BSD
Group: System Environment/Daemons
URL: https://github.com/otto-de/libvmod-uuid
Source0: %{name}-%{version}.tar.gz

Requires: varnish-maxwait = 6.6.0
Requires: uuid

BuildRequires: varnish-maxwait-devel = 6.6.0
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

Provides: vmod-uuid-maxwait, vmod-uuid-maxwait-debuginfo

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
* Fri May 21 2021 Geoff Simmons <geoff@uplex.de> - %{_version}-%{_release}
- Compatibility with varnish-maxwait (6.6.0)

* Wed Apr 21 2021 Geoff Simmons <geoff[AT]uplex.de> - 1.10-1
  Compatible with VRT 13 (Varnish 6.6)

* Wed Jan 27 2021 Geoff Simmons <geoff[AT]uplex.de> - 1.9-1
  Compatible with VRT 12 (Varnish 6.5)

* Thu Apr 23 2020 Geoff Simmons <geoff[AT]uplex.de> - 1.8-1
  Compatible with VRT 10 (Varnish 6.3)

* Wed Aug 07 2019 Geoff Simmons <geoff[AT]uplex.de> - 1.7-1
  Compatible with VRT 9 (Varnish 6.2)

* Fri Nov 30 2018 Geoff Simmons <geoff[AT]uplex.de> - 1.6-1
  Compatible with VRT 8 (Varnish 6.1 and libvarnishapi.so.2)

* Mon Apr 02 2018 Geoff Simmons <geoff[AT]uplex.de> - 1.5-1
- Compatible with VRT 7.0 and Varnish 6.0.0.

* Wed Dec 20 2017 Geoff Simmons <geoff[AT]uplex.de> - 1.4-1
- Compatible with VRT 6.1 and Varnish 5.2.1.
