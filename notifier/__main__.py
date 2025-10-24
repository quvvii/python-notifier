import psutil
import telebot
import datetime, time
import requests

from notifier import config


last_alert = datetime.datetime.now() - datetime.timedelta(minutes=1)
bot = telebot.TeleBot(token=config.BOT_TOKEN, parse_mode="HTML")


def get_metrics():
    cpu = psutil.cpu_percent(interval=1)
    ram = psutil.virtual_memory().percent

    return [cpu, ram]


def get_ip():
    return requests.get("https://api.ipify.org").text


def format_message(message):
    return config.MESSAGE_BODY.format(
        ip=get_ip(),
        server_name=config.SERVER_NAME,
        message=message,
        timestamp=datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=3))).strftime("%d.%m.%Y %H:%M:%S")
    )


def send_notification(message):
    now = datetime.datetime.now()

    if (now - last_alert).total_seconds() < config.SEND_ALERT_TIME:
        return

    bot.send_message(
        chat_id=config.ADMIN_ID,
        text=format_message(message)
    )
    update_alert_time()


def update_alert_time():
    global last_alert

    last_alert = datetime.datetime.now()


def main():
    while True:
        metrics = get_metrics()
        message = ""

        if not isinstance(metrics[0], float) or not isinstance(metrics[1], float):
            send_notification(f"Can't get metrics. Metrics: {metrics}")
            continue

        if metrics[0] >= config.CPU_MAX_PERSENT:
            message += f"<b>CPU is overloaded:</b> <code>{metrics[0]}%</code>"

        if metrics[1] >= config.RAM_MAX_PERSENT:
            message += f"\n<b>RAM is overloaded:</b> <code>{metrics[1]}%</code>" \
                if message != "" else f"<b>RAM is overloaded:</b> <code>{metrics[1]}%</code>"

        send_notification(message)
        time.sleep(2)


if __name__ == "__main__":
    main()
