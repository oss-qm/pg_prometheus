# build config
%global pg_version_major	12

%global cmd_pg_config		%_bindir/pg_config-%pg_version_major

Summary:	PostgreSQL extension for Prometheus
Name:		pg_prometheus
Version:	0.2.2
Release:	1%{?dist}
License:	Apache License
Source0:	pg_prometheus-%version.tar.gz
URL:		http://www.postgis.net/

BuildRequires:	gcc
BuildRequires:	postgresql%pg_version_major-devel
BuildRequires:	cmake

Requires:	postgresql%pg_version_major

%description
PostgreSQL extension for Prometheus

%prep
%setup -q -n pg_prometheus-%version

%build
%__make %{?_smp_mflags}

%install
%__rm -rf %buildroot
%__make %{?_smp_mflags} DESTDIR=%buildroot install

%clean
%__rm -rf %buildroot

%files
%defattr(-,root,root)
%doc *.md
%license LICENSE

### global changelog
%changelog
* Mon Feb 17 2020 Enrio Weigelt, metux IT consult <info@metux.net> - 1.6.0
- Packaged version 3.0.1 for SLES
