%global pkgname cloudwatch-agent
%define version @VERSION@
%define buildid @BUILDID@

Name:      %{pkgname}
Summary:   cloudwatch-metadata-agent
Version:   0.1.0
Release:   ROCKIT1%{?dist}
License:   GPLv3
Vendor:    ROCKIT
URL:       http://rockitsoft.ru
BuildArch: noarch
Source0:   %{pkgname}-%{?version}.tar.gz

Requires:  curl
 
%description
Collects information about RAM load (in percentage) and sends data through the metadata service. 
 

%prep
%setup -n %name -q
 
 
%install
mkdir -p %{buildroot}%{_sbindir}
mkdir -p %{buildroot}%{_unitdir}
install -m 0755 agent/cloudwatch-agent %{buildroot}%{_sbindir}/cloudwatch-agent
install -m 0644 agent/systemd/cloudwatch-agent.service %{buildroot}%{_unitdir}/cloudwatch-agent.service
install -m 0644 agent/systemd/cloudwatch-agent.timer %{buildroot}%{_unitdir}/cloudwatch-agent.timer
 
 
%files
%{_sbindir}/cloudwatch-agent
%{_unitdir}/cloudwatch-agent.service
%{_unitdir}/cloudwatch-agent.timer
 
 
%post
systemctl daemon-reload
systemctl enable cloudwatch-agent.timer
systemctl start cloudwatch-agent.timer

 
%preun
systemctl stop cloudwatch-agent.timer
systemctl disable cloudwatch-agent.timer