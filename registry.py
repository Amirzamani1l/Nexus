import json
import os
from datetime import datetime

import config


def load_known_devices():
    if not os.path.exists(config.KNOWN_DEVICES_FILE):
        return {}

    with open(config.KNOWN_DEVICES_FILE, "r") as f:
        return json.load(f)


def save_known_devices(devices):
    with open(config.KNOWN_DEVICES_FILE, "w") as f:
        json.dump(devices, f, indent=2)


def diff_devices(current_scan, known_devices):
    """returns (new_devices, updated_registry)"""
    new_devices = []
    now = datetime.now().isoformat(timespec="seconds")

    for device in current_scan:
        mac = device["mac"]

        if mac not in known_devices:
            new_devices.append(device)
            known_devices[mac] = {
                "ip": device["ip"],
                "first_seen": now,
                "last_seen": now,
                "label": "unnamed device",
            }
        else:
            known_devices[mac]["ip"] = device["ip"]
            known_devices[mac]["last_seen"] = now

    return new_devices, known_devices
