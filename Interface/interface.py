"""
This module contains the main logic for sending, receiving and handling frames
"""
from scapy.all import conf, get_if_hwaddr


class Interface:
    def __init__(self, name: str) -> None:
        """
        Initialize network interface
        :param name: The interface name
        """
        self.mac: str = get_if_hwaddr(name)
        self.sock: conf.L2socket = conf.L2socket(iface=name, promisc=True)

    def start(self) -> None:
        """Receive and handle incoming frames"""
        # TODO: send gratuitous ARP
        received_bytes: bytes
        while True:
            _, received_bytes, _ = self.sock.recv_raw()
            if received_bytes:
                pass
