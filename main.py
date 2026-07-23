import time
from datetime import datetime

import config
import dashboard
import registry
import scanner
from notifier import TelegramNotifier


def main():
    known_devices = registry.load_known_devices()
    notifier = TelegramNotifier()

    print("nexus is starting up, doing first scan...")
    print("(this needs admin/root privileges to send ARP packets)")

    while True:
        try:
            current_scan = scanner.scan(config.NETWORK_RANGE or None)
        except PermissionError:
            print("permission denied — run this with sudo/admin rights")
            return

        new_devices, known_devices = registry.diff_devices(current_scan, known_devices)
        registry.save_known_devices(known_devices)

        last_scan_time = datetime.now().strftime("%H:%M:%S")
        dashboard.render_once(known_devices, last_scan_time)

        for device in new_devices:
            message = (
                f"🚨 New device joined the network\n"
                f"IP: {device['ip']}\n"
                f"MAC: {device['mac']}\n"
                f"Time: {last_scan_time}"
            )
            print(f"[alert] {message}")
            notifier.send(message)

        time.sleep(config.SCAN_INTERVAL_SECONDS)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nnexus stopped.")
