import ipaddress
import socket

from scapy.all import ARP, Ether, srp
from scapy.config import conf


def get_local_subnet():
    hostname = socket.gethostname()
    local_ip = socket.gethostbyname(hostname)
    network = ipaddress.ip_network(local_ip + "/24", strict=False)
    return str(network)


def scan(network_range=None):
    target = network_range or get_local_subnet()

    conf.verb = 0
    arp_request = ARP(pdst=target)
    broadcast = Ether(dst="ff:ff:ff:ff:ff:ff")
    packet = broadcast / arp_request

    answered, _ = srp(packet, timeout=3)

    devices = []
    for _, response in answered:
        devices.append({
            "ip": response.psrc,
            "mac": response.hwsrc.lower(),
        })

    return devices
