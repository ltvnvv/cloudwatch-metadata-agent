# cloudwatch-agent
Активный CloudWatch-агент. Собирает информацию о загрузке ОЗУ (в процентах) и отправляет данные через metadata-сервис. После этого будет записана соответствующая метрика CloudWatch.

Работает на systemd-таймере.

## Установка

RPM-based OS:
```sh
dnf install /path/to/cloudwatch-agent-0.1.0-ROCKIT1.el8.noarch.rpm
```

DEB-based OS:
```sh
dpkg -i /path/to/deb/cloudwatch-agent-0.1.0-ROCKIT.deb
```