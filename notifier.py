import requests

import config


class TelegramNotifier:
    def __init__(self):
        self.base_url = f"https://api.telegram.org/bot{config.TELEGRAM_BOT_TOKEN}"
        self.enabled = bool(config.TELEGRAM_BOT_TOKEN and config.TELEGRAM_CHAT_ID)

    def send(self, message):
        if not self.enabled:
            print("[notifier] telegram not configured, skipping alert")
            return False

        try:
            response = requests.post(
                f"{self.base_url}/sendMessage",
                data={"chat_id": config.TELEGRAM_CHAT_ID, "text": message},
                timeout=10,
            )
            return response.status_code == 200
        except requests.RequestException as e:
            print(f"[notifier] failed to send alert: {e}")
            return False
