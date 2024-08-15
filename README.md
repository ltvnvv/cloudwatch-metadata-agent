# cloudwatch-agent
Активный CloudWatch-агент. Собирает информацию о загрузке ОЗУ (в процентах) и отправляет данные через metadata-сервис. После этого будет записана соответствующая метрика CloudWatch.

Работает на systemd-таймере.

## Установка

RPM-based OS:
```sh
wget https://github.com/C2Devel/cloudwatch-metadata-agent/releases/download/0.1.0/cloudwatch-agent-<version>.rpm
dnf install ./cloudwatch-agent-<version>.rpm
```

DEB-based OS:
```sh
wget https://github.com/C2Devel/cloudwatch-metadata-agent/releases/download/0.1.0/cloudwatch-agent-<version>.deb
dpkg -i ./cloudwatch-agent-<version>.deb
```