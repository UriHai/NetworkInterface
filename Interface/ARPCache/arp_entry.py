"""
This module contains the ARPEntry class that will be used by ARPCache
"""

from LinkLayer.Identifiers.mac_address import MACAddress
from NetworkLayer.Identifiers.ip_address import IPAddress


class ARPEntry:
    def __init__(self, ip: IPAddress, mac: MACAddress) -> None:
        """
        Initialize ARP entry
        :param ip: IP address
        :param mac: Mac address
        """
        self.ip: IPAddress = ip
        self.mac: MACAddress = mac
        self.age = 0
