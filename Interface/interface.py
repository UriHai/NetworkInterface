"""
This module contains the main logic for sending, receiving and handling frames
"""

from scapy.all import conf, get_if_hwaddr, get_if_addr
from time import time

from Interface.ARPCache.arp_cache import ARPCache
from Interface.Handlers.ethernet_handler import EthernetHandler
from Interface.Handlers.arp_handler import ARPHandler
from LinkLayer.Identifiers.mac_address import MACAddress
from NetworkLayer.Identifiers.ip_address import IPAddress


class Interface:
    def __init__(self, name: str) -> None:
        """
        Initialize network interface
        :param name: The interface name
        """
        self.sock: conf.L2socket = conf.L2socket(iface=name, promisc=True)
        self.mac: MACAddress = MACAddress(get_if_hwaddr(name))
        self.ip: IPAddress = IPAddress(get_if_addr(name))

        self.current_time: float = 0
        self.arp_cache: ARPCache = ARPCache()

        self.ethernet_handler: EthernetHandler = EthernetHandler(self)
        self.arp_handler: ARPHandler = ARPHandler(self)

    def start(self) -> None:
        """Receive and handle incoming frames"""
        self.current_time = time()
        self.arp_handler.send_gratuitous_arp()
        received_bytes: bytes
        while True:
            _, received_bytes, _ = self.sock.recv_raw()
            if received_bytes:
                self.ethernet_handler.handle(received_bytes)
            self.update_current_time()

    def update_current_time(self) -> None:
        """Update the current time and execute related actions"""
        current_time: float = time()
        self.arp_cache.update_entries_ages(current_time - self.current_time)
        self.current_time = current_time
