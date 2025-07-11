"""
This module contains a MACAddress class
"""
from __future__ import annotations

from typing import Union


class MACAddress:
    def __init__(self, mac: Union[str, bytes]) -> None:
        if isinstance(mac, bytes):
            self.mac = mac
        elif isinstance(mac, str):
            self.mac = self._convert_mac_string_to_bytes(mac)

    @staticmethod
    def _convert_mac_string_to_bytes(mac: str) -> bytes:
        """
        Convert string representation of a MAC address to bytes
        :param mac: String representation of the MAC address
        :return: Bytes representation of the MAC address
        """
        return bytes([int(byte, 16) for byte in mac.split(':')])

    def __eq__(self, other: MACAddress) -> bool:
        """
        Compare MAC addresses
        :param other: The MAC address to compare with
        :return: True if the MAC addresses are the same, False otherwise
        """
        return self.mac == other.mac
