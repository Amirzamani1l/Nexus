import os

# leave empty to auto-detect your subnet, or set it manually like "192.168.1.0/24"
NETWORK_RANGE = os.getenv("NETWORK_RANGE", "")

SCAN_INTERVAL_SECONDS = 20

KNOWN_DEVICES_FILE = "known_devices.json"

TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN", "")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID", "")
