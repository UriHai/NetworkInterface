"""
This module contains the ARP cache class
"""

from typing import List, Union

from Interface.ARPCache.constants import MAX_ARP_ENTRY_AGE
from Interface.ARPCache.arp_entry import ARPEntry
from LinkLayer.Identifiers.mac_address import MACAddress
from NetworkLayer.Identifiers.ip_address import IPAddress


class ARPCache:
    def __init__(self) -> None:
        """Initialize ARP cache"""
        self.entries: List[ARPEntry] = []

    def update_arp_cache(self, ip: IPAddress, mac: MACAddress) -> None:
        """
        Add a new entry or update an existing one
        :param ip: IP address
        :param mac: MAC address
        """
        entry: ARPEntry
        for entry in self.entries:
            if entry.ip == ip:
                entry.mac = mac
                entry.age = 0
                return
        self.entries.append(ARPEntry(ip, mac))

    def get_mac_by_ip(self, ip: IPAddress) -> Union[MACAddress, None]:
        """
        Get the MAC address associated with an IP address in the ARP cache
        :param ip: IP address to get the MAC of
        :return: The MAC address linked to the IP address, None if the IP address is not listed in the ARP cache
        """
        entry: ARPEntry
        for entry in self.entries:
            if entry.ip == ip:
                return entry.mac
        return

    def update_entries_ages(self, time: float) -> None:
        """
        Remove entries that have reached the max age and increase the age of all remaining entries
        :param time: The time to increase the entries's ages by
        """
        entry: ARPEntry
        for entry in self.entries:
            if entry.age >= MAX_ARP_ENTRY_AGE:
                self.entries.remove(entry)
            else:
                entry.age += time
