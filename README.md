# python-notifier
![python](https://img.shields.io/badge/Python-3.8+-3776AB?logo=python&logoColor=fff)
![Docker](https://img.shields.io/badge/Docker-2496ED?logo=docker&logoColor=white)
![License](https://img.shields.io/badge/license-MIT-green)

A simple project that notifies you via a Telegram bot if the server's RAM or CPU are higher than necessary.

## Installation
1. Create `.env` file: 
```env 
TELEGRAM_BOT_TOKEN=
TELEGRAM_ADMIN_ID=
```

2. You can change some settings in the `notifier/config.py` file: 
- `CPU_MAX_PERSENT` - trigger limits for the CPU in percentage
- `RAM_MAX_PERSENT` - trigger limits for the RAM in percentage
- `SEND_ALERT_TIME` - the time interval between sending messages to Telegram
- `SERVER_NAME` - your server name
- `MESSAGE_BODY` - message that sends to Telegram
- `TIMEZONE` - your time relative to UTC (timestamp will be UTC + YOUR TIMEZONE hours)

3. Build the image: 
```bash
docker build -t python-notifier .
```

4. Start the container:
```bash
docker run -d \
--name notifier \
--env-file ./.env \
python-notifier
```

---

![Screenshot](https://i.ibb.co/ynmDT3PT/python-notifier.png)

## License
This project is licensed under the [MIT License](https://github.com/quvvii/python-notifier/blob/main/LICENSE).
