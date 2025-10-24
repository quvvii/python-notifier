import environs

env = environs.Env()
env.read_env()

BOT_TOKEN = env.str("TELEGRAM_BOT_TOKEN")
ADMIN_ID = env.int("TELEGRAM_ADMIN_ID")

CPU_MAX_PERSENT = 80.0
RAM_MAX_PERSENT = 80.0
SEND_ALERT_TIME = 20

MESSAGE_BODY = "{ip} - <b>{server_name}</b>\n\n<blockquote>{message}</blockquote>\n\n<i>{timestamp}</i>"
SERVER_NAME = "My server"
