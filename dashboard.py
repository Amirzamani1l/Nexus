from rich.console import Console
from rich.table import Table
from rich.live import Live
from rich.panel import Panel

console = Console()


def build_table(known_devices, last_scan_time):
    table = Table(title=f"Nexus — Network Guardian  (last scan: {last_scan_time})", expand=True)
    table.add_column("MAC Address", style="cyan")
    table.add_column("IP", style="green")
    table.add_column("Label", style="white")
    table.add_column("First Seen", style="dim")
    table.add_column("Last Seen", style="dim")

    for mac, info in sorted(known_devices.items(), key=lambda kv: kv[1]["last_seen"], reverse=True):
        table.add_row(mac, info["ip"], info["label"], info["first_seen"], info["last_seen"])

    return Panel(table, border_style="green")


def render_once(known_devices, last_scan_time):
    console.clear()
    console.print(build_table(known_devices, last_scan_time))
