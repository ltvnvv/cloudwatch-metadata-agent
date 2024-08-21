%global pkgname cloudwatch-agent
%define buildid @BUILDID@

Name:      %{pkgname}

Version:   0.1.0
Release:   ROCKIT1%{?buildid}%{?dist}
Summary:   Active CloudWatch agent for sending metric data via metadata API

License:   GPLv3
URL:       https://github.com/C2Devel/cloudwatch-metadata-agent.git
Source0:   %{pkgname}-%{version}.tar.gz
BuildArch: noarch
 
%description
Collects information about RAM load (in percentage) and sends data through the metadata service. 
 
Requires:  curl

%prep
%setup -q -n %{pkgname}-%{version}
  
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
