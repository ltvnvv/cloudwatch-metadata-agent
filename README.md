# cloudwatch-ram-metadata-agent
Активный CloudWatch-агент. Собирает информацию о загрузке ОЗУ (в процентах) и отправляет данные через metadata-сервис. После этого будет записана соответствующая метрика CloudWatch.

Работает на systemd-таймере.

## Установка

Приложение пока не пакетируется.

При подготовке образа нужно довезти в него директорию `agent` и из-под рута выполнить следующее:

```sh
cp agent/cloudwatch-agent /usr/sbin/
chmod +x /usr/sbin/cloudwatch-agent

cp agent/systemd/* /usr/lib/systemd/system/

systemctl enable cloudwatch-agent.timer
```

