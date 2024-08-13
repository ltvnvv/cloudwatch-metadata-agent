Name:      cloudwatch-agent
Summary:   cloudwatch-ram-metadata-agent
Version:   1.6.2
Release:   CROC1%{?dist}
License:   GPLv3
Vendor:    CROC
URL:       http://cloud.croc.ru
BuildArch: noarch
Source0:   cloudwatch-agent.tar.gz

Requires:  curl
 
%description
Collects information about RAM load (in percentage) and sends data through the metadata service. 
 

%prep
%setup -n %name -q
 
 
%install
mkdir -p %{buildroot}%{_sbindir}
mkdir -p %{buildroot}%{_unitdir}
install -m 0755 cloudwatch-agent %{buildroot}%{_sbindir}/cloudwatch-agent
install -m 0644 cloudwatch-agent.service %{buildroot}%{_unitdir}/cloudwatch-agent.service
install -m 0644 cloudwatch-agent.timer %{buildroot}%{_unitdir}/cloudwatch-agent.timer
 
 
%files
%{_sbindir}/cloudwatch-agent
%{_unitdir}/cloudwatch-agent.service
%{_unitdir}/cloudwatch-agent.timer
 
 
%post
systemctl daemon-reload
systemctl enable cloudwatch-agent.service
systemctl start cloudwatch-agent.service
systemctl enable cloudwatch-agent.timer
systemctl start cloudwatch-agent.timer
 
 
%preun
systemctl stop cloudwatch-agent.service
systemctl disable cloudwatch-agent.service
systemctl stop cloudwatch-agent.timer
systemctl disable cloudwatch-agent.timer
 